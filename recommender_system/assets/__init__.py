from dagster import load_assets_from_package_module
from . import core
from . import recommender
# from . import airbyte

core_assets = load_assets_from_package_module(
    package_module=core, group_name='core',
    
)
recommender_assets = load_assets_from_package_module(
    package_module=recommender, group_name='recommender'
)

# airbyte_assets = load_assets_from_airbyte_instance(airbyte_resource)

# airbyte_assets = load_assets_from_package_module(
#     package_module=airbyte, group_name='airbyte'
# )
# from airbyte import airbyte_assets