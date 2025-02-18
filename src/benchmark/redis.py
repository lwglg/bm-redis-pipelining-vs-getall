from redis import Redis


__all__ = [
    "get_redis_client",
]


def get_redis_client(hostname: str = "localhost", port: int = 6379) -> Redis:
    client = Redis(host=hostname, port=port, decode_responses=True)

    return client
