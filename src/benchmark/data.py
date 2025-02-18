import redis

from .timing import timing


__all__ = [
    "perform_data_fetching",
]


@timing
def run_pipeline(redis_client: redis.Redis, limit: int) -> redis.typing.ResponseT:
    pipe = redis_client.pipeline()
    
    for _ in range(limit):
        pipe.incr("incr_key")
    
    pipe.get("incr_key")

    return pipe.execute()[-1]


@timing
def run_getall(redis_client: redis.Redis, limit: int) -> redis.typing.ResponseT:
    for _ in range(limit):
        redis_client.incr("incr_key")

    return redis_client.get("incr_key")


def perform_data_fetching(
    redis_client: redis.Redis,
    with_pipelining: bool,
    limit: int = 100000,
) -> redis.typing.ResponseT:
    redis_client.set("incr_key", "0")
    
    if with_pipelining:
        return run_pipeline(redis_client, limit)
    
    return run_getall(redis_client, limit)
