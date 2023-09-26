# Azure Function App for Text Processing

This README provides a step-by-step guide to setting up and running the Azure Function App for text processing locally. The function accepts HTML text, processes it, and returns a JSON object containing processed sentences.

## Prerequisites

Before you can run the Azure Function App, you'll need to install the following:

1. **Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Node.js**: Download and install Node.js from [nodejs.org](https://nodejs.org/).
3. **Azure Functions Core Tools**: Install it using npm by running the following command:
    ```bash
    npm install -g azure-functions-core-tools@3 --unsafe-perm true
    ```
4. **Azurite**: Install Azurite, the Azure Storage emulator, using npm:
    ```bash
    npm install -g azurite
    ```
5. **Git**: Download and install Git from [git-scm.com](https://git-scm.com/).
6. **VS Code**: Download and install Visual Studio Code from [Visual Studio Code](https://code.visualstudio.com/).

## Setup

### Clone the Repository

Clone the repository containing the Azure Function App to your local machine.

```bash
git clone <repository_url>
```

Navigate to the project directory.

```bash
cd <project_directory>
```

### Create a venv and activate it

```
python -m .venv venv
./venv/Scripts/activate
```


### Install Python Dependencies

Install the Python dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Run Locally

### Start Azurite

Before running the function app, start the Azurite emulator:

```bash
azurite --silent --location <path_to_azurite_data> --debug <path_to_azurite_debug_log>
```

Replace `<path_to_azurite_data>` and `<path_to_azurite_debug_log>` with the paths where you want Azurite to store its data and log files, respectively.

### Run Function App

#### Using Command Line

To run the function app locally, navigate to the project directory in your terminal and run:

```bash
func start
```

This will start the Azure Functions runtime and your function will be available for triggering.

#### Using VS Code

1. Open the project directory in VS Code.
2. Install the Azure Functions extension for VS Code if you haven't already.
3. Press `F5` to start debugging. This will automatically start the Azure Functions runtime.

## Test the Function

To test the function, you can use tools like Postman or `curl` to send a POST request to the function's endpoint, which will be displayed in the terminal when the function starts (usually `http://localhost:7071/api/function`).

### Using curl

```bash
curl -X POST http://localhost:7071/api/function -d '{"html_body":"<div>your HTML content here</div>"}'
```

Replace `<function_name>` with the name of your function.

## Troubleshooting

If you encounter the error "No job functions found," ensure that:

- Your function signature matches what Azure Functions expects.
- Your `function.json` is correctly configured.
- You've installed all the prerequisites.

For detailed output, run:

```bash
func start --verbose
```

## Conclusion

You should now have your Azure Function App running locally and accessible for testing. Feel free to modify the code in `__init__.py` to suit your specific needs.