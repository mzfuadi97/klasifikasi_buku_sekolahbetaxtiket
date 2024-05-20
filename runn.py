import mlflow

model = mlflow.pyfunc.load_model("runs:/7dc5ad42e7344ff6b2f7d5477507ec22/model")
model.serve(port=5000)
