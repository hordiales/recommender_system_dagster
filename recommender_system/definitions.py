from dagster import Definitions, load_assets_from_modules, define_asset_job, AssetSelection
from recommender_system.configs import job_data_config, job_training_config
from recommender_system.assets import (
    core_assets, recommender_assets, airbyte_assets
#, dbt_transformations
)

from dagster import EnvVar
from dagster_airbyte import AirbyteResource, load_assets_from_airbyte_instance
# Definir el recurso de Airbyte
airbyte_resource = AirbyteResource(
    host="localhost",
    port="8000",
    username="hordiales@gmail.com",
    password=EnvVar("AIRBYTE_PASSWORD")
)

# airbyte_assets = load_assets_from_airbyte_instance(airbyte_resource)

# all_assets = load_assets_from_modules([movies_users])
# all_assets = [*core_assets, *recommender_assets]
all_assets = [*core_assets, *recommender_assets, *airbyte_assets]


mlflow_resources = {
    'mlflow': {
        'config': {
            'experiment_name': 'recommender_system',
        }            
    },
}


data_job = define_asset_job(
    name='get_data',
    selection=['movies', 'users', 'scores', 'training_data'],
    config=job_data_config
)


from dagster import fs_io_manager
# job_airbyte_config = {
#     'resources': {
#         "airbyte": airbyte_resource,
#         "io_manager": fs_io_manager, 
#         # **mlflow_resources
#         #,
#         # **airbyte_resources,  # Agregar Airbyte como recurso
#     },
#     'ops': { 
#         # "airbyte": airbyte_resource,
#         # "io_manager": fs_io_manager, 
#     }
# }

airbye_job = define_asset_job(
    name="airbye_job",
    selection=AssetSelection.groups('airbyte'),
    # config=job_airbyte_config
)

recommender_job = define_asset_job(
    name="only_training",
    # selection=['preprocessed_training_data', 'user2Idx', 'movie2Idx'],
    selection=AssetSelection.groups('recommender'),
    config=job_training_config
)

# defs = Definitions(
#     assets=[*airbyte_assets],  # ✅ Ensure assets are properly loaded
#     resources={  
#         "airbyte": airbyte_resource,  # ✅ Airbyte Resource
#         "io_manager": fs_io_manager,  # ✅ Fix missing io_manager
#         **job_data_config["resources"],  # ✅ Other resources (e.g., MLflow)
#     },
# )
defs = Definitions(
    assets=all_assets,
    jobs=[
        data_job,
        recommender_job
        ,
        airbye_job
    ],
    resources={  
        "airbyte": airbyte_resource, 
        "io_manager": fs_io_manager, 
        # **job_data_config["resources"], #no agregar esto para no duplicar key
    }
)

# defs = Definitions(
#     assets=[*airbyte_assets],  # Agregar los assets de Airbyte
#     resources={
#         "airbyte": airbyte_resource,  # Incluir el recurso de Airbyte
#         **job_data_config["resources"]
#     },
# )
