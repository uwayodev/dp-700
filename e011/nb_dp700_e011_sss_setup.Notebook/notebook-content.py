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

# #!/usr/bin/env python
# #coding: utf-8
# 
# ### nb_dp700_e011_sss_setup
# # 
# #New notebook

# CELL ********************

import json
import os
import uuid
import random
import time
from datetime import datetime

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Settings
output_folder = "/lakehouse/default/Files/dp700_e011/source"
schema_name   = "dp700_e011"
num_files     = 10
wait_seconds  = 5

# Make sure that source folder and destination schema exist
os.makedirs(output_folder, exist_ok=True)
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

for i in range(num_files):
    now = datetime.utcnow()
    timestamp_str = now.strftime("%Y%m%dT%H%M%SZ")

    # Simulate one temperature reading
    record = {
        "id": str(uuid.uuid4()),
        "temperature": round(random.uniform(18.0, 30.0), 2),
        "timestamp": now.isoformat()
    }

    # Build file path with name like temperature_20250404T101010Z.json
    filename = f"temperature_{timestamp_str}.json"
    filepath = os.path.join(output_folder, filename)

    # Write the JSON file
    with open(filepath, "w") as f:
        json.dump(record, f)

    print(f"✅ [{i+1}/{num_files}] Wrote: {filename}")
    time.sleep(wait_seconds)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
