-- models/marts/core/dim_customers.sql
{{ config(
    materialized='table'
) }}

SELECT
    customer_id,
    name,
    email,
    created_at
FROM {{ source('rawdata', 'customers') }}
