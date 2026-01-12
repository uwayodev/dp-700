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

assignments = spark.sql("SELECT * FROM lh_dp700.dp700_e004.assignments")
departments = spark.sql("SELECT * FROM lh_dp700.dp700_e004.departments")
employees = spark.sql("SELECT * FROM lh_dp700.dp700_e004.employees")
projects = spark.sql("SELECT * FROM lh_dp700.dp700_e004.projects")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(assignments)
display(departments)
display(employees)
display(projects)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pyspark.sql.functions as F

display( \
    employees \
    .filter(F.col("salary") >= 75000) \
    .select(
        F.col("name"),
        F.col("salary"),
        F.concat(F.lit("$ "), F.col("salary")).alias("salary_string")
    )
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display( \
    employees \
    .filter("salary >= 75000") \
    .selectExpr(
        "name",
        "salary",
        "'$ ' || salary AS salary_string"
    ) \
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display( \
    employees \
    .join(departments, employees["department_id"] == departments["department_id"], "left") \
    .select(
        employees["name"],
        employees["department_id"],
        departments["department_name"]
    ) \
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pyspark.sql.functions as F

e = employees.alias("e")
d = departments.alias("d")

display( \
    e.join(d, F.col("e.department_id") == F.col("d.department_id"), "left") \
    .select(
        F.col("e.name").alias("employee_name"),
        F.col("e.department_id"),
        F.col("d.department_name")
 ) \
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display( \
    employees \
    .join(departments, employees["department_id"] == departments["department_id"], "left") \
    .groupBy("department_name") \
    .count() \
    .withColumnRenamed("count", "number_of_employees") \
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pyspark.sql.functions as F

e = employees.alias("e")
d = departments.alias("d")

display( \
    e.join(d, F.col("e.department_id") == F.col("d.department_id"), "left") \
    .groupBy(F.col("d.department_name")) \
    .count() \
    .withColumnRenamed("count", "number_of_employees") \
)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
