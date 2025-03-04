from dagster import asset, Output, String, AssetIn, FreshnessPolicy, MetadataValue
from dagster_mlflow import mlflow_tracking
import pandas as pd

# Configurar los assets desde Airbyte
from dagster_airbyte import build_airbyte_assets
from dagster import with_resources

# https://docs.dagster.io/api/python-api/libraries/dagster-airbyte
# # Replace with the actual connection IDs from Airbyte
# airbyte_movies = build_airbyte_assets(
#     connection_id="1d4fd1c5-33eb-4b1f-bbaa-41b3870ff51e",
#     destination_tables=["airbyte_movies"],
#     # auto_materialize_policy="eager"  
# )


from dagster import EnvVar
from dagster_airbyte import AirbyteResource, load_assets_from_airbyte_instance


# Definir el recurso de Airbyte
airbyte_resource = AirbyteResource(
    host="localhost",
    port="8000",
    username="hordiales@gmail.com",
    password=EnvVar("AIRBYTE_PASSWORD")
)

airbyte_movies = with_resources(
    build_airbyte_assets(
        connection_id="1d4fd1c5-33eb-4b1f-bbaa-41b3870ff51e",
        destination_tables=["airbyte_movies"],
        # destination_database="mlflow_db",
        # destination_schema="source",
        # asset_key_prefix=["airbyte"],
    ),
    {"airbyte": airbyte_resource},
)

# Define Airbyte asset
# @asset
# # def airbyte_movies(context):
# def airbyte_movies():
#     assets = build_airbyte_assets(
#         connection_id="1d4fd1c5-33eb-4b1f-bbaa-41b3870ff51e",
#         destination_tables=["airbyte_movies"],
#         auto_materialize_policy="eager"  # 
#     )

#     #Return an Output object for tracking
#     return Output(
#         #value=assets,  # This holds the Airbyte assets
#         value=None,  # This holds the Airbyte assets
#         metadata={"description": "Movies data synced from Airbyte"}
#     )

@asset
def airbyte_users(context):
    assets = build_airbyte_assets(
        connection_id="c9a7844f-758a-4e75-8e58-55347a46f9c2",
        destination_tables=["airbyte_movies"],
        auto_materialize_policy="eager"  # 
    )

    #Return an Output object for tracking
    return Output(
        #value=assets,  # This holds the Airbyte assets
        value=None,  # This holds the Airbyte assets
        metadata={"description": "Movies data synced from Airbyte"}
    )
# airbyte_users = build_airbyte_assets(
#     connection_id="c9a7844f-758a-4e75-8e58-55347a46f9c2",
#     destination_tables=["airbyte_users"]
# )

@asset
def airbyte_scores(context):
    assets = build_airbyte_assets(
        connection_id="ab4c34e7-00e6-4fc3-9c66-04bb04004db0",
        destination_tables=["airbyte_movies"],
        auto_materialize_policy="eager"  # 
    )

    #Return an Output object for tracking
    return Output(
        #value=assets,  # This holds the Airbyte assets
        value=None,  # This holds the Airbyte assets
        metadata={"description": "Movies data synced from Airbyte"}
    )

# Ejecutado asi, ejecuta en airbyte, recibe data del proceso pero falta el Output y falla el STEP
# airbyte_scores = build_airbyte_assets(
#     connection_id="ab4c34e7-00e6-4fc3-9c66-04bb04004db0",
#     destination_tables=["airbyte_scores"]
# )

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
airbyte_assets = [airbyte_movies, airbyte_users, airbyte_scores]