import sys

from src.benchmark import get_redis_client, perform_data_fetching
from src.shared import Logger


def main():
    limit = 100000
    redis_client = get_redis_client()
    base_message = f"\nIncrementing from 1 to {limit} and retrieving the data using"
    
    Logger.log("Redis Benchmarking - Pipelining vs All", bold=True)
    Logger.log(f"{base_message} pipeline...", bold=True)
    
    data = perform_data_fetching(redis_client, with_pipelining=True, limit=limit)
    
    Logger.success(f"Retrieved data: {data}", bold=True)
    Logger.log(f"{base_message} get...", bold=True)
    
    data = perform_data_fetching(redis_client, with_pipelining=False, limit=limit)
    
    Logger.success(f"Retrieved data: {data}", bold=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"{exc.__class__.__name__}: {str(exc)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("SIGINT received. Quitting application...")
        sys.exit(2)
