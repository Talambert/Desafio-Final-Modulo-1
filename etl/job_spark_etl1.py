from pyspark.sql.functions import mean, max, min, col, count, lit
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciceSpark")
    .getOrCreate()
)

#leitura
enem = (
    spark
    .read
    .format("CSV")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load("s3://datalake-tancredo-dfinal1-edc-producao-421168935276/raw-data/")
)


#Transformação em parquet
(
 enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("NU_ANO_CENSO")
    .save("s3://datalake-tancredo-dfinal1-edc-producao-421168935276/staging-zone/")
)
