
export REPO_FOLDER=$PWD/../mlops-ecosystem
export postgres_data_folder=$REPO_FOLDER/dbs/data/postgres
export mongo_data_folder=$REPO_FOLDER/dbs/data/mongo
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=mysecretpassword
export POSTGRES_HOST=localhost:5432
export MLFLOW_POSTGRES_DB=mlflow_db

export MLFLOW_ARTIFACTS_PATH=$PWD/mlflow_data
export MLFLOW_TRACKING_URI=http://localhost:8002

#mlflow server --backend-store-uri postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST/$MLFLOW_POSTGRES_DB --default-artifact-root $MLFLOW_ARTIFACTS_PATH -h 0.0.0.0 -p 8002
mlflow server --default-artifact-root $MLFLOW_ARTIFACTS_PATH -h 0.0.0.0 -p 8002
