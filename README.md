# My Python API Project

This project fetches data from the Dog API "https://api.thedogapi.com/v2/breeds", processes the data, and demonstrates the use of GitHub Actions.

## Project Structure

```
my-python-api-project
├── src
│   ├── __init__.py
│   ├── api_client.py
│   ├── data_processor.py
│   └── main.py
├── .github
│   └── workflows
│       └── ci.yml
├── requirements.txt
└── README.md
```

## How to Run

1. Install the dependencies:
   ```sh
   pip install -r requirements.txt
    ```

2. Run the main script:
    ```python
    python src/main.py
    ```

## GitHub Actions

* Checks out the code
* Sets up Python
* Installs dependencies
* Runs tests using `pytest`
* Lints the code using `flake8`
* Executes the `main.py` script to show the result


With these updates, the project now fetches and processes data from the Dog API's breeds endpoint, and the GitHub Actions pipeline will execute the `main.py` script to show the result.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.