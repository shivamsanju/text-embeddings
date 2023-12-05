import requests
import time
import concurrent.futures

# Replace with your server address
base_url = "http://20.204.210.96:80"
tei_base_url = "http://127.0.0.1:8081"

# Generate a string with 512 words (tokens)
input_data = "Lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


# # Test separate requests
# def test_separate_requests():
#     for _ in range(10000):
#         data = {"inputs": input_data}
#         response = requests.post(f"{base_url}/embed", json=data)
#         result = response.json()

# # Test batch request
# def test_batch_request():
#     data = {"inputs": [input_data] * 100}
#     response = requests.post(f"{base_url}/embed-batch", json=data)
#     result = response.json()


# # Test separate requests
# def test_separate_requests_tei():
#     for _ in range(100):
#         data = {"inputs": input_data}
#         response = requests.post(f"{tei_base_url}/embed", json=data)
#         result = response.json()

# # Measure time for separate requests
# separate_requests_time = timeit.timeit(test_separate_requests, number=1)
# print(f"Time taken for fastembed requests: {separate_requests_time:.4f} seconds")

# # Measure time for tei request
# batch_request_time = timeit.timeit(test_separate_requests_tei, number=1)
# print(f"Time taken for tei request: {batch_request_time:.4f} seconds")

# # Measure time for batch request
# batch_request_time = timeit.timeit(test_batch_request, number=1)
# print(f"Time taken for batch request: {batch_request_time:.4f} seconds")



def test_single_request():
    data = {"inputs": input_data}
    response = requests.post(f"{base_url}/embed", json=data)
    result = response.json()


with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the requests
    start = time.time()
    future_to_url = {executor.submit(test_single_request) for _ in range(10000)}

    # Wait for the requests to complete
    concurrent.futures.wait(future_to_url)
    print(f"Took {time.time() - start} s")