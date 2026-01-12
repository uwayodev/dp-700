# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d1e02103-b302-434c-989c-0c63e9f193e1",
# META       "default_lakehouse_name": "lh_dp700",
# META       "default_lakehouse_workspace_id": "3e2204cc-b967-485c-bf55-8dfa0134abad",
# META       "known_lakehouses": [
# META         {
# META           "id": "d1e02103-b302-434c-989c-0c63e9f193e1"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ## DP-700 Examp Prep Episode 009: Notebooks
# 
# ### 🔹 Parameters

# PARAMETERS CELL ********************

dataset = "movies"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### 🔹 Reading data from a file in Lakehouse

# CELL ********************

df = spark.read.format("csv").option("header","true").load(f"Files/dp700_e009/{dataset}.csv")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### 🔹 Displaying data

# CELL ********************

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### 🔹 Using Spark SQL

# CELL ********************

df.createOrReplaceTempView("df_view")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT
# MAGIC  *
# MAGIC ,now() AS ts
# MAGIC  FROM df_view

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_ts = spark.sql('''
    SELECT
    *
    ,now() AS ts
    FROM df_view
''')
display(df_ts)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### 🔹 Writing data to a table in Lakehouse

# CELL ********************

spark.sql('''
CREATE SCHEMA IF NOT EXISTS dp700_e009
''')

df_ts.write.mode("overwrite").format("delta").saveAsTable(f"dp700_e009.{dataset}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### 🔹 Reading data from a table in Lakehouse

# CELL ********************

df_table = spark.sql(f"SELECT * FROM lh_dp700.dp700_e009.{dataset}")
display(df_table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### 🔹 Using NotebooUtils to set an exit value for the notebook

# CELL ********************

notebookutils.notebook.exit(f"Dataset {dataset} was processed ok!")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
