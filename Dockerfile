FROM python:3.9-slim
LABEL authors="romain.boyrie"

WORKDIR /app

RUN pip install --upgrade pip && pip install dbt-core==1.7.18 dbt-bigquery==1.7.9

COPY . /app

ENV DBT_PROFILES_DIR=/app

ENTRYPOINT ["dbt"]

CMD ["run"]