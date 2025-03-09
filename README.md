# recommender_system

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

## Getting started

	$ conda env create -f environment.yml


## Define .env file

(in .gitignpore for security reasons)

DAGSTER_HOME=
MLFLOW_TRACKING_URI=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
MLFLOW_POSTGRES_DB=
MLFLOW_ARTIFACTS_PATH=
AIRBYTE_PASSWORD=
DBT_MANIFEST_PATH=
DBT_PROJECT_PATH=

## Dagster UI
Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `recommender_system/assets.py`. The assets are automatically loaded into the Dagster code location as you define them.

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `recommender_system_tests` directory and you can run tests using `pytest`:

```bash
pytest recommender_system_tests
```

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster Cloud

The easiest way to deploy your Dagster project is to use Dagster Cloud.

Check out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.


