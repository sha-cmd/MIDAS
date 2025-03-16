-- models/marts/core/dim_customers.sql
{{ config(
    materialized='table'
) }}

SELECT
    id AS customer_id,
    name,
    email,
    created_at
FROM {{ source('raw_data', 'customers') }}
