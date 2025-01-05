# Databricks notebook source
dbutils.fs.mount( source = 'wasbs://bronzelayer@ipdheerenadls.blob.core.windows.net', 
                 mount_point= '/mnt/bronzelayer', extra_configs ={'fs.azure.sas.bronzelayer.ipdheerenadls.blob.core.windows.net':'sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2025-01-12T00:48:45Z&st=2024-12-29T16:48:45Z&spr=https&sig=SPLP9d8XjVDOxq%2BgKNMf9ssHrxjigoX26eiLyzFGNog%3D'})




# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/bronzelayer

# COMMAND ----------

dbutils.fs.mount( source = 'wasbs://processed@ipdheerenadls.blob.core.windows.net', 
                 mount_point= '/mnt/processed', extra_configs ={'fs.azure.sas.processed.ipdheerenadls.blob.core.windows.net':'sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2025-01-12T00:48:45Z&st=2024-12-29T16:48:45Z&spr=https&sig=SPLP9d8XjVDOxq%2BgKNMf9ssHrxjigoX26eiLyzFGNog%3D'})

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/processed

# COMMAND ----------

dbutils.fs.mount( source = 'wasbs://landing@ipdheerenadls.blob.core.windows.net', 
                 mount_point= '/mnt/landing', extra_configs ={'fs.azure.sas.landing.ipdheerenadls.blob.core.windows.net':'sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2025-01-12T00:48:45Z&st=2024-12-29T16:48:45Z&spr=https&sig=SPLP9d8XjVDOxq%2BgKNMf9ssHrxjigoX26eiLyzFGNog%3D'})

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/landing
