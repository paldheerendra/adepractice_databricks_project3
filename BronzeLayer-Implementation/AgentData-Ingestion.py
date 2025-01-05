# Databricks notebook source
from pyspark.sql.functions import *
schema = "agent_id integer, agent_name string, agent_name string, agent_phone string, branch_id integer, create_timestamp timestamp"

df = spark.read.parquet("/mnt/landing/AgentData/*.parquet")
df_with_flag = df.withColumn("merge_flag", lit(False))
df_with_flag.write.option("path", "/mnt/bronzelayer/Agent").mode("append").saveAsTable("bronzelayer.Agent")



# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/bronzelayer

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   *
# MAGIC FROM
# MAGIC   system.information_schema.tables
# MAGIC WHERE
# MAGIC   table_catalog = 'ipdheerendatabricks'
