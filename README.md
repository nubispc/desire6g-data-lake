# DESIRE6G Data lake

This service acts as a wrapper for interactions with Harbor, MinIO, and
Prometheus APIs, providing a unified interface to work with container
registries, S3-compatible storage, and telemetry data, respectively.

## Requirements

- Python 3.x
- FastAPI
- Uvicorn
- Requests

## Setup

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/desire6g-data-lake.git
cd api-wrapper-service
pip install fastapi uvicorn requests
```

## Running the Server

Start the server with Uvicorn:

```bash
uvicorn app:app --reload
```

The server will start on `http://localhost:8000`.

## Usage
The service exposes the following endpoints:

- `GET /harbor/projects`: Lists projects in Harbor.
- `GET /minio/buckets`: Lists buckets in MinIO.
- `GET /prometheus/metrics`: Retrieves metrics from Prometheus.

## Example Requests

You can use any HTTP client to make requests to the endpoints. Here's an example using curl:

List Harbor projects:

```bash
curl http://localhost:8000/harbor/projects
```

List MinIO buckets:

```bash
curl http://localhost:8000/minio/buckets
```

Get Prometheus metrics:

```bash
curl http://localhost:8000/prometheus/metrics
```

In this version, the wrapper service provides endpoints for pulling Docker
images from Harbor (`/harbor/pull_image`), uploading files to MinIO
(`/minio/upload`), and querying metrics from Prometheus (`/prometheus/query`). You
can customize these endpoints further based on the functionality you need.



