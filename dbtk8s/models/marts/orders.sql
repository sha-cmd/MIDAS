-- models/marts/core/fct_orders.sql
{{ config(
    materialized='table'
) }}

SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.status,
    o.amount
    FROM {{ source('rawdata', 'orders') }} o
