-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   },
-- META   "dependencies": {
-- META     "lakehouse": {
-- META       "default_lakehouse": "d1e02103-b302-434c-989c-0c63e9f193e1",
-- META       "default_lakehouse_name": "lh_dp700",
-- META       "default_lakehouse_workspace_id": "3e2204cc-b967-485c-bf55-8dfa0134abad",
-- META       "known_lakehouses": [
-- META         {
-- META           "id": "d1e02103-b302-434c-989c-0c63e9f193e1"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

-- Create schema if not exists
CREATE SCHEMA IF NOT EXISTS dp700_e013;

-- Create the employees table
CREATE TABLE IF NOT EXISTS dp700_e013.employees (
    employee_id INT,
    name STRING,
    department_id INT,
    hire_date DATE,
    salary DECIMAL(10, 2)
);

INSERT INTO dp700_e013.employees VALUES
    (10, 'Lily Morgan', 104, '2024-12-10', 71000.00),
    (11, 'Noah Carter', 103, '2025-02-05', 69000.00);

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
