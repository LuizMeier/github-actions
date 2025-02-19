import json
from api_client import APIClient
from data_processor import DataProcessor


def main():
    base_url = "https://dogapi.dog/api/v2"  # Define the base URL for the Dog API
    api_client = APIClient(base_url)  # Pass the base URL to the APIClient
    data_processor = DataProcessor()

    # Fetch data from the Dog API
    raw_data = api_client.fetch_data("breeds")  # Pass the endpoint to fetch_data

    # Process the fetched data
    filtered_data = data_processor.filter_data(raw_data)

    transformed_data = data_processor.transform_data(filtered_data)

    # Getting which is the biggest dog
    max = 0
    for breed in filtered_data:
        if breed['attributes']['male_weight']['max'] > max:
            max = breed['attributes']['male_weight']['max']
            name = breed['attributes']['name']

    # Print the results
    print(json.dumps(transformed_data, indent=2))

    # Print the biggest dog
    print(f"You woud say: {name} is the biggest dog. It weights {max} kg")


if __name__ == "__main__":
    main()
