from dagster import asset, Output, String, AssetIn, FreshnessPolicy, MetadataValue
from dagster_mlflow import mlflow_tracking
import pandas as pd


# Configurar los assets desde Airbyte
from dagster_airbyte import build_airbyte_assets
from dagster import AssetExecutionContext


# Replace with the actual connection IDs from Airbyte
airbyte_movies = build_airbyte_assets(
    connection_id="99411b7e-ddec-495c-ae57-9849ec67875e",
    destination_tables=["airbyte_movies"]
)

airbyte_users = build_airbyte_assets(
    connection_id="e66616fb-8642-4e3a-9102-f6a67b088e32",
    destination_tables=["airbyte_users"]
)

airbyte_scores = build_airbyte_assets(
    connection_id="b149a0f1-d8ea-44da-9320-0a971a1e7f99",
    destination_tables=["airbyte_scores"]
)

# Group all Airbyte assets
# Agrupa los assets de Airbyte para usarlos en Dagster
# airbyte_assets = [airbyte_movies, airbyte_users, airbyte_scores]