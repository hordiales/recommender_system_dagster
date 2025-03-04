import dagster as dg
from dagster_dbt import dbt_assets, DbtCliResource, DbtProject
from dagster import EnvVar, AssetExecutionContext
from pathlib import Path

#DBT: https://github.com/dagster-io/dagster/blob/master/examples/assets_modern_data_stack/assets_modern_data_stack/assets/forecasting.py
#FIXME: update this path using an environment variable (using .env and EnvVar)
DBT_PROJECT_DIR = Path("/Users/hordia/dev/MLOps-itba/dbt_mlops")
# DBT_PROFILES_DIR = Path("/Users/hordia/dev/MLOps-itba/dbt_mlops")
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

# lee manifest.json extrae assets y los carga en el contexto (scores_movies_users, etc)
@dbt_assets(manifest=DBT_PROJECT_DIR/"target/manifest.json")
def dbt_models(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream() #works
    # yield from dbt.cli(["dev"] , context=context).stream() #does not work
    # yield from dbt.cli(["dev"]).stream()
    