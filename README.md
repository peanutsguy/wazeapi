# PyWaze REST API

This project leverages **PyWaze** and **FastAPI** to create a REST API for calculating distance and travel time between locations. The API is designed to be lightweight, efficient, and easy to deploy.

## Features

- Calculate distance and travel time using PyWaze.
- Expose functionality via a FastAPI-based REST API.
- Containerized for seamless deployment using Docker.

## Requirements

- Docker installed on your system.

## Usage

1. Pull the image:
    ```bash
    docker pull ghcr.io/peanutsguy/wazeapi
    ```

2. Start the container, exposing port 3000:
    ```bash
    docker run -p 3000:3000 --name=wazeapi ghcr.io/peanutsguy/wazeapi
    ```

## API Endpoints

- **POST /travel-time**: Calculate the estimated travel time and distance between two locations.

### Request Structure

The **POST /travel-time** endpoint expects a JSON payload with the following structure:

```json
{
    "start": {
        "lat": float,
        "lon": float
    },
    "end": {
        "lat": float,
        "lon": float
    }
}
```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [PyWaze](https://github.com/eifinger/pywaze) for route calculations.
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- Docker for containerization.
- Community contributions and support.