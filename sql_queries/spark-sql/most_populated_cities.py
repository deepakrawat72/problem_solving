from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import *
from pyspark.sql.types import LongType

data = """Warsaw,Poland,1 764 615
Cracow,Poland,769 498
Paris,France,2 206 488
Villeneuve-Loubet,France,15 020
Pittsburgh PA,United States,302 407
Chicago IL,United States,2 716 000
Milwaukee WI,United States,595 351
Vilnius,Lithuania,580 020
Stockholm,Sweden,972 647
Goteborg,Sweden,580 020"""

lines = data.split("\n")
data1 = list(map(lambda x : x.split(","), lines))

spark = SparkSession.builder.appName("populated_cities").master("local[*]").getOrCreate()

countryDf = spark.createDataFrame(data1, ["name", "country", "population"]) \
    .withColumn("population", replace(col("population"), lit(' '), lit('')).cast(LongType()))

window_by_country = Window.partitionBy("country").orderBy(desc("population"))
countryDf.withColumn("max_population", max("population").over(window_by_country)) \
    .filter(col("population") == col("max_population")) \
    .drop("max_population") \
    .show(truncate=False)

#countryDf.groupby("country").agg(max("population")).show(truncate=False)
