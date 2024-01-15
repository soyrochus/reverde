# Reverde

LLM based, multimodal, conversion tool; transformation of the old to the new

This is a proof of concept (PoC) on how to create an extendible LLM based conversion tool. The PoC uses the OpenAI. As long as the original data is representable to text or supported as a binary format by OpenAI (i.e. images) 

![The Lotus (genus 'Nelumbo') is the symbol of rebirth in many cultures](image/reverde.png)

The Lotus (genus *Nelumbo*) is the symbol of rebirth in many cultures.

## Installation

Clone the repository. Use the dependency and package manager [Poetry](https://python-poetry.org/) to install all the dependencies of Reverde.

```bash
poetry install
```

## Configuration for usage with OpenAI

Create a text file _"openai_api_key.env"_ in the root of the project. This will contain the "OPENAI_API_KEY" environment variable used by the application to obtain the token associated to a valid OpenAI account when calling the API.

```bash
OPENAI_API_KEY=sk-A_seCR_et_key_GENERATED_foryou_by_OPENAI
```
The key is loaded into the execution context of the application when run from the command line or run in the debugger.

## Configuration by environment variables

If the file _"openai_api_key.env"_ is not present, then 'reverde' will look for the environment variable "OPENAI_API_KEY". 

An optional environment variable is "REVERDE_PLUGINS_PATH" which is used by the application to automatically discover and load user created conversion types (Python modules with a specific interface).

For development you can create a text file _"dev.env"_ in the root of the project. This should have the "REVERDE_PLUGINS_PATH" variable with the right value if so needed:

```bash
REVERDE_PLUGINS_PATH="./plugins/"
```

The environment variables are loaded into the execution context of the application when run in the debugger if as such specified in the file _"launch.json"_. An example launch configuration shows how:

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Module",
            "type": "python",
            "request": "launch",
            "module": "reverde",
            "justMyCode": true,
            "args":["-d","pascal"],
            "envFile": "${workspaceFolder}/dev.env"
        }
    ]
}
```

## Usage

Reverde is a relatively simple command-line tool, but supporting various different conversion types. Details of the workings of each conversion_type/conversor may differ. Each converstion_type can display its specific documentation by calling the command with the _--doc_ parameter. 

By providing the _--help_ parameter, the following help screen will be shown, showing all possible command line arguments:

```bash
❯ reverde --help
usage: reverde [-h] [-p PROMPT] [-c CONVERSION_TYPE] [-i [INPUT_FILES_PATH_SPEC ...]] [-o [OUTPUT_FILES ...]] [-d DOC]

Reverde - LLM based, multimodal, conversion tool

options:
  -h, --help            show this help message and exit
  -p PROMPT, --prompt PROMPT
                        Optional prompt
  -c CONVERSION_TYPE, --conversion_type CONVERSION_TYPE
                        Conversion type (processor name)
  -i [INPUT_FILES_PATH_SPEC ...], --input_files_path_spec [INPUT_FILES_PATH_SPEC ...]
                        Input files path specification
  -o [OUTPUT_FILES ...], --output_files [OUTPUT_FILES ...]
                        Output files path specification
  -d DOC, --doc DOC     Show conversion_type documentation
```

## Development
[Activate the Python virtual environment](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment) with

```bash
poetry shell
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Copyright and license

Copyright © 2024 Iwan van der Kleijn

Licensed under the MIT License 
[MIT](https://choosealicense.com/licenses/mit/)