import time

def timer(func):
    def wrapper():
        start_time = time.time()
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' took {duration:.6f} seconds to execute.")
        return result
    return wrapper

@timer
def example_function():
    time.sleep(4)
    print("Function executed.")

example_function()
