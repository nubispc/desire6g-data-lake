from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

HARBOR_URL = 'http://localhost:8000/harbor'
MINIO_URL = 'http://localhost:9000/minio'
PROMETHEUS_URL = 'http://localhost:9090/prometheus'


@app.get("/harbor/pull_image")
def pull_image_from_harbor(image_name: str):
    response = requests.get(f"{HARBOR_URL}/pull_image/{image_name}")
    if response.status_code == 200:
        return {"message": f"Image '{image_name}' pulled successfully from Harbor"}
    else:
        raise HTTPException(status_code=response.status_code, detail="Error pulling image from Harbor")


@app.post("/minio/upload")
def upload_file_to_minio(file_name: str, file_content: bytes):
    files = {'file': (file_name, file_content)}
    response = requests.post(f"{MINIO_URL}/upload", files=files)
    if response.status_code == 200:
        return {"message": f"File '{file_name}' uploaded successfully to MinIO"}
    else:
        raise HTTPException(status_code=response.status_code, detail="Error uploading file to MinIO")


@app.get("/prometheus/query")
def query_prometheus_metric(metric_name: str):
    response = requests.get(f"{PROMETHEUS_URL}/query", params={"metric": metric_name})
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error querying metric from Prometheus")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
