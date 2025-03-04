from dagster import asset, Output, String, AssetIn, FreshnessPolicy, MetadataValue
from dagster_mlflow import mlflow_tracking
import pandas as pd


# Configurar los assets desde Airbyte
from dagster_airbyte import build_airbyte_assets
from dagster import AssetExecutionContext

#### 
# dbt
###
# from pathlib import Path

# from dagster import AssetExecutionContext
# from dagster_dbt import DbtCliResource, dbt_assets

# DBT_PROJECT_DIR = file_relative_path(__file__, "../../dbt_project")
# DBT_PROJECT_DIR = "/Users/hordia/dev/MLOps-itba/dbt_mlops/"
# dbt_resource = DbtCliResource(project_dir=DBT_PROJECT_DIR)
# dbt_parse_invocation = dbt_resource.cli(["parse"]).wait()
# DBT_MANIFEST_PATH = dbt_parse_invocation.target_path.joinpath("manifest.json")
# @dbt_assets(
#     manifest=DBT_MANIFEST_PATH,
#     # io_manager_key="db_io_manager",
# )
# def dbt_project_assets(context: AssetExecutionContext, dbt: DbtCliResource):
#     yield from dbt.cli(["dev"], context=context).stream()
#     #yield from dbt.cli(["build"], context=context).stream()
# ########

# # Replace with the actual connection IDs from Airbyte
airbyte_movies = build_airbyte_assets(
    connection_id="99411b7e-ddec-495c-ae57-9849ec67875e",
    destination_tables=["airbyte_movies"],
    # auto_materialize_policy="eager"  
)

# test ids
# movies / connection_id="99411b7e-ddec-495c-ae57-9849ec67875e",

#alt ids
#movies = 1d4fd1c5-33eb-4b1f-bbaa-41b3870ff51e

# Define Airbyte asset
# @asset
# def airbyte_movies(context):
#     assets = build_airbyte_assets(
#         connection_id="99411b7e-ddec-495c-ae57-9849ec67875e",
#         destination_tables=["airbyte_movies"]
#         #,
#         #auto_materialize_policy="eager"  # 
#     )

#     #Return an Output object for tracking
#     return Output(
#         #value=assets,  # This holds the Airbyte assets
#         value=None,  # This holds the Airbyte assets
#         metadata={"description": "Movies data synced from Airbyte"}
#     )


airbyte_users = build_airbyte_assets(
    connection_id="e66616fb-8642-4e3a-9102-f6a67b088e32",
    destination_tables=["airbyte_users"]
)

# Ejecutado asi, ejecuta en airbyte, recibe data del proceso pero falta el Output y falla el STEP
airbyte_scores = build_airbyte_assets(
    connection_id="b149a0f1-d8ea-44da-9320-0a971a1e7f99",
    destination_tables=["airbyte_scores"]
)

# from dagster_airbyte import airbyte_sync_op

# @asset
# def airbyte_scores(context):
#     """Trigger Airbyte sync and return metadata but no binary output."""

#     # Trigger the Airbyte sync
#     airbyte_result = airbyte_sync_op(context, connection_id="b149a0f1-d8ea-44da-9320-0a971a1e7f99")

#     # Extract metadata from the Airbyte sync result
#     sync_status = airbyte_result.get("status", "Unknown")
#     sync_id = airbyte_result.get("job_info", {}).get("job", {}).get("id")

#     context.log.info(f"Airbyte sync triggered: Status = {sync_status}, Job ID = {sync_id}")

#     return Output(
#         value=None,  # No binary output
#         metadata={
#             "airbyte_sync_status": sync_status,
#             "airbyte_job_id": sync_id
#         }
#     )

# Group all Airbyte assets
# Agrupa los assets de Airbyte para usarlos en Dagster
# airbyte_assets = [airbyte_movies, airbyte_users, airbyte_scores]