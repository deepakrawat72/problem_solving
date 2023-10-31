"""
Write a structured query that “merges” two rows of the same id (to replace nulls).
+---+-----+----+--------+
| id| name| age|    city|
+---+-----+----+--------+
|100| John|  35|    null|
|100| John|null| Georgia|
|101| Mike|  25|    null|
|101| Mike|null|New York|
|103| Mary|  22|    null|
|103| Mary|null|   Texas|
|104|Smith|  25|    null|
|105| Jake|null| Florida|
+---+-----+----+--------+

output :
+---+-----+----+--------+
|id |name |age |city    |
+---+-----+----+--------+
|100|John |35  |Georgia |
|101|Mike |25  |New York|
|103|Mary |22  |Texas   |
|104|Smith|25  |null    |
|105|Jake |null|Florida |
+---+-----+----+--------+
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("merge_two_row").master("local[*]").getOrCreate()

inputDf = spark.createDataFrame([
    ("100", "John", 35, None),
    ("100", "John", None, "Georgia"),
    ("101", "Mike", 25, None),
    ("101", "Mike", None, "New York"),
    ("103", "Mary", 22, None),
    ("103", "Mary", None, "Texas"),
    ("104", "Smith", 25, None),
    ("105", "Jake", None, "Florida")], ["id", "name", "age", "city"])

inputDf.show()

cityDf = inputDf.filter(expr("age IS NULL")).select("id", "name", "city")
ageDf = inputDf.filter(expr("city IS NULL")).select("id", "name", "age")
#
cityDf.show()
ageDf.show()

merged_rows = cityDf.alias("city").join(ageDf.alias("age"), col("city.id") == col("age.id"), "outer")
merged_rows.select(
    coalesce(col("city.id"), col("age.id")).alias("id"), coalesce(col("city.name"), col("age.name")).alias("name"), "age", "city"
).show(truncate=False)
