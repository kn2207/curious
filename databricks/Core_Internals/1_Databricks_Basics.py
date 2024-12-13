# Databricks notebook source
print("Hello Dear World - Hope you are doing well")

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

filelist = dbutils.fs.ls('/databricks-datasets')
display(filelist)
