export DAGSTER_HOME=$PWD/dagster_home

#DAGSTER_HOME=$REPO_FOLDER/dagster_home
MLFLOW_TRACKING_URI=http://localhost:8002
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_HOST=localhost:5432
MLFLOW_POSTGRES_DB=mlflow_db
#MLFLOW_ARTIFACTS_PATH=$REPO_FOLDER/mlflow_data
export AMLFLOW_ARTIFACTS_PATH=$PWD/mlflow_data
export AIRBYTE_PASSWORD=1TY8gsvfOToqLwxowQovdNdtteEPkAxj
export DBT_MANIFEST_PATH=$PWD/../dbt_mlops/dbt_project.yml


dagster dev
