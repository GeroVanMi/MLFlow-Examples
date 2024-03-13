import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

mlflow.set_experiment("/tracking_server_tutorial")

with mlflow.start_run():
    mlflow.log_metric("foo", 1)
    mlflow.log_metric("bar", 2)
