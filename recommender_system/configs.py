mlflow_resources = {
    'mlflow': {
        'config': {
            'experiment_name': 'recommender_system',
        }            
    },
}

data_ops_config = {
    'pre_movies': {
        'config': {
            'uri': 'https://raw.githubusercontent.com/mlops-itba/Datos-RS/main/data/peliculas_0.csv'
            }
    },
    'pre_scores': {
        'config': {
            'uri': 'https://raw.githubusercontent.com/mlops-itba/Datos-RS/main/data/scores_0.csv'
            }
    },
    'pre_users': {
        'config': {
            'uri': 'https://raw.githubusercontent.com/mlops-itba/Datos-RS/main/data/usuarios_0.csv'
            }
    }
}

# 'ops': configuración de los assets
# ** contenido de los dicts (key/value)
# data_ops_config
job_data_config = {
    'resources': {
        **mlflow_resources
        #,
        # **airbyte_resources,  # Agregar Airbyte como recurso
    },
    'ops': { 
        **data_ops_config,
    }
}

training_config = {
    'model_trained': {
        'config': {
            'batch_size': 128,
            'epochs': 10,
            'learning_rate': 1e-3,
            'embeddings_dim': 5
        }
    }
}

#training_config 
job_training_config = {
    'resources': {
        **mlflow_resources
    },
    'ops': {
        **training_config
    }
}