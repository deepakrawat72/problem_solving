"""
Description: You are given a time series data, which is a clickstream of user activity. Perform Sessionization on the data (as per the session definition given below) and generate session ids.

Expected Steps:

•    Read the input data file into your program (datafile.txt already present in solution explorer).
•    Use spark batch (PySpark/Spark-Scala) to add a column with name session_id and generate the session ids based on the following logic:
        -> Session expires after inactivity of 30 minutes; because of inactivity, no clickstream record will be generated.
        -> Session remains active for a maximum duration of 2 hours (i.e., after every two hours a new session starts)
•    Save the resultant data (original data, enriched with Session IDs) in a Parquet file format.

Given Dataset:

Timestamp    User_id
2021-05-01T11:00:00Z    u1
2021-05-01T13:13:00Z    u1
2021-05-01T15:00:00Z    u2
2021-05-01T11:25:00Z    u1
2021-05-01T15:15:00Z    u2
2021-05-01T02:13:00Z    u3
2021-05-03T02:15:00Z    u4
2021-05-02T11:45:00Z    u1
2021-05-02T11:00:00Z    u3
2021-05-03T12:15:00Z    u3
2021-05-03T11:00:00Z    u4
2021-05-03T21:00:00Z    u4
2021-05-04T19:00:00Z    u2
2021-05-04T09:00:00Z    u3
2021-05-04T08:15:00Z    u1
"""

from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("Time series analysis").getOrCreate()

user_session_data_df = spark.read.option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", "|") \
    .csv("../spark-sql/user_session_data.csv")

window_by_user_id = Window.partitionBy("User_id").orderBy("Timestamp")

session_expiry_time = 30 * 60
session_inactivity_time = 2 * 60 * 60


def createSessionList(timestamp, time_diff):
    curr_session_id = None
    session_ids = []

    for diff in time_diff:
        if curr_session_id is None:
            curr_session_id = 1
        else:
            if diff >= session_expiry_time or diff >= session_inactivity_time:
                curr_session_id += 1

        session_ids.append(curr_session_id)

    return zip(timestamp, session_ids)


schema = ArrayType(StructType([
    StructField("timestamp", TimestampType(), False),
    StructField("session_id", StringType(), False)
]))

session_id_generator = udf(lambda z, y: createSessionList(z, y), schema)

user_session_data_df.select("User_id", "Timestamp").orderBy("User_id") \
    .withColumn("time_diff",
                coalesce(unix_timestamp(col("Timestamp")) - unix_timestamp(lag("Timestamp", 1).over(window_by_user_id)),
                         lit(0))) \
    .groupby("User_id").agg(collect_list("Timestamp").alias("timestamp"), collect_list("time_diff").alias("time_diff")) \
    .withColumn("generated_session_ids", session_id_generator(col("timestamp"), col("time_diff"))) \
    .drop("timestamp", "time_diff") \
    .select(col("User_id"), explode(col("generated_session_ids"))) \
    .withColumn("timestamp", col("col.timestamp")) \
    .withColumn("session_id", concat(col("User_id"), lit("_s"), col("col.session_id"))) \
    .drop("col") \
    .show(truncate=False)
