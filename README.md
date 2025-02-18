# bm-redis-pipelining-vs-getall

Comparison, in terms of time complexity, between the mechanisms of pipelining and fetching all data at once.

## Requisites
- Python v3.12;
- Docker v27.5.1. How to install it in [here](https://docs.docker.com/engine/install/ubuntu/);
- Docker Compose v2.32.4. How to install it in [here](https://docs.docker.com/compose/install/linux/); 
- UV Package Manager. How to install it in [here](https://docs.astral.sh/uv/getting-started/installation/).

## Getting started

At the project's root, execute the following commands:

- Run the Redis server via Docker Compose, and show the execution logs:
```bash
docker compose up -d redis && docker compose logs redis --follow
```


- In a different terminal, installing the correct version of Python for this project:
```bash
uv python install 3.12
```

- Installing project dependencies:
```bash
uv pip install -r pyproject.toml
```

- Activating the local environment (optional):
```bash
source .venv/bin/activate
```

- Running the application:
```bash
uv run python -m src 
```
