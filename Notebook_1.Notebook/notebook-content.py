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

# CELL ********************

df = spark.sql("OPTIMIZE lh_dp700.dp700_e011.temperature_stream")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("VACUUM lh_dp700.dp700_e011.temperature_stream")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("VACUUM lh_dp700.dp700_e011.temperature_stream RETAIN 200 HOURS ")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
