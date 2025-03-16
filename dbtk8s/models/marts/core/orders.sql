-- models/marts/core/fct_orders.sql
{{ config(
    materialized='table'
) }}

SELECT
    o.id AS order_id,
    o.customer_id,
    o.order_date,
    o.status,
    o.amount
FROM {{ source('raw_data', 'orders') }} o
