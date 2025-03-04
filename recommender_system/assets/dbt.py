import dagster as dg
from dagster_dbt import dbt_assets, DbtCliResource, DbtProject
from dagster import EnvVar, AssetExecutionContext
from pathlib import Path

#DBT: https://github.com/dagster-io/dagster/blob/master/examples/assets_modern_data_stack/assets_modern_data_stack/assets/forecasting.py
#FIXME: update this path using an environment variable (using .env and EnvVar)
import os
DBT_PROJECT_PATH = os.getenv("DBT_PROJECT_PATH")
# DBT_PROJECT_DIR = Path("") #hardcoded path, works
# DBT_PROJECT_DIR = Path(EnvVar("DBT_PROJECT_PATH") ) #does not work
DBT_PROJECT_DIR = Path(DBT_PROJECT_PATH)
# DBT_PROFILES_DIR = Path(")
dbt_resource = DbtCliResource(project_dir=DBT_PROJECT_DIR)

dbt_project = DbtProject(project_dir=DBT_PROJECT_DIR)
dbt_project.prepare_if_dev()

#optional?
dbt_parse_invocation = dbt_resource.cli(["parse"]).wait()

# # Load dbt assets
# dbt_assets = load_assets_from_dbt_project(
#     project_dir=DBT_PROJECT_DIR,
#     profiles_dir=DBT_PROFILES_DIR
# )
from dagster import AssetKey
# from dagster_dbt import DagsterDbtTranslator
# class CustomizedDagsterDbtTranslator(DagsterDbtTranslator):
#     def get_asset_key(self, dbt_resource_props):
#         resource_type = dbt_resource_props["resource_type"]
#         name = dbt_resource_props["name"]
#         if resource_type == "source":
#             return AssetKey(f"{name}")
#         else:
#             return super().get_asset_key(dbt_resource_props)

# lee manifest.json extrae assets y los carga en el contexto (scores_movies_users, etc)
@dbt_assets(manifest=DBT_PROJECT_DIR/"target/manifest.json"
            ,
            # dagster_dbt_translator=CustomizedDagsterDbtTranslator(),
            name="dbt_elt"
    )
def dbt_models(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream() #works
    # yield from dbt.cli(["dev"] , context=context).stream() #does not work
    # yield from dbt.cli(["dev"]).stream()
    