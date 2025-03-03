Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


# Conda env

```bash
conda create -n mlops-dbt python=3.9
conda activate mlops-dbt
pip install dbt-postgres

dbt --version
```

Con el siguiente comando se crea el repo y se configura la db

```bash
dbt init db_postgres
```

```
En el archivo de configuración `~/.dbt/profiles.yml` se debe configurar la base de datos
```yaml
dbt_elt:
  outputs:
    dev:
      type: postgres
      threads: 1
      host: localhost
      port: 5432
      user: postgres
      pass: mysecretpassword
      dbname: mlops
      schema: target
```

### Testear conexión
```bash
dbt debug

dbt run
