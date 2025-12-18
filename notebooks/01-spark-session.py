# Databricks notebook source
# MAGIC %md
# MAGIC ####1. How to create Spark Session

# COMMAND ----------

from pyspark.sql import SparkSession

spark_session = SparkSession.builder.getOrCreate()

spark_session.version

# COMMAND ----------

# MAGIC %md
# MAGIC ####2. What is pre-created Spark Session

# COMMAND ----------

spark.version

# COMMAND ----------

# MAGIC %md
# MAGIC ####3. How to use SparkSession to read table data?

# COMMAND ----------

df = spark.table("dev.spark_db.diamonds")
df.display()