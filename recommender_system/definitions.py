from dagster import Definitions, load_assets_from_modules, define_asset_job, AssetSelection
from recommender_system.configs import job_data_config, job_training_config

from recommender_system.assets import (
    core_assets, recommender_assets#, airbyte_assets
)
from recommender_system.assets.airbyte import airbyte_assets, airbyte_resource

# from recommender_system.assets.core import core_assets
# from recommender_system.assets.recommender import recommender_assets
from recommender_system.assets.dbt import dbt_models, dbt_resource, dbt_assets

from dagster import EnvVar
from dagster_airbyte import AirbyteResource, load_assets_from_airbyte_instance

# from recommender_system.assets.recommender.train_model import sql_training_data #ya es un recommender asset
all_assets = [*core_assets, *recommender_assets, *airbyte_assets, dbt_models]

mlflow_resources = {
    'mlflow': {
        'config': {
            'experiment_name': 'recommender_system',
        }            
    },
}

# previous config for data origin
data_job = define_asset_job(
    name='get_data',
    selection=['pre_movies', 'pre_users', 'pre_scores', 'training_data'],
    config=job_data_config
)

#ya es un recommender asset
# sql_data_job = define_asset_job(
#     name='sql_get_data',
#     selection=['sql_training_data'],
#     config=job_data_config
# )

# from dagster import fs_io_manager

airbye_job = define_asset_job(
    name="airbye_job",
    selection=AssetSelection.assets(*airbyte_assets),
    # selection=AssetSelection.groups('airbyte'),
    # config=job_airbyte_config
)

dbt_job = define_asset_job(
    name="dbt_job",
    selection=AssetSelection.assets(dbt_models),
)

# from dagster import graph, job

# @graph
# def airbyte_dbt_pipeline():
#     airbye_job()
#     dbt_job()

# airbyte_dbt_job = airbyte_dbt_pipeline.to_job()

recommender_job = define_asset_job(
    name="only_training",
    # selection=['sql_training_data','preprocessed_training_data', 'user2Idx', 'movie2Idx'],
    selection=AssetSelection.groups('recommender'),
    config=job_training_config
)

defs = Definitions(
    assets=all_assets,
    jobs=[
        data_job,
        # sql_data_job, #ya es un recommender asset
        recommender_job,
        airbye_job,
        dbt_job
        # airbyte_dbt_job #pipeline test
    ],
    resources={  
        # "airbyte": airbyte_resource, 
        # "io_manager": fs_io_manager,
        "dbt": dbt_resource,
        # "db_io_manager": DbIOManager(**POSTGRES_CONFIG),
        # **job_data_config["resources"], #no agregar esto para no duplicar key
    }
)