# python_provider

## Table of Contents

- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Setup for Development](#setup-for-development)
- [Usage](#usage)
- [Commands](#commands)
  - [Testing](#testing)
  - [Linting](#linting)
  - [Formatting](#formatting)
  - [Releasing](#releasing)
- [License](#license)

## Getting Started

### Installation

Install `python_provider` with pip:

```shell
pip install -e .
```

### Setup for Development

If you're looking to contribute or develop with `python_provider`, get the source code and set up the environment:

```shell
git clone git@github.com:8ball030/vs_python_client.git
cd python_provider
poetry install && poetry shell
```

## Usage

With `python_provider` installed, you have access to a command line tool.

```python
╰─>$ python_provider --help
                                                                                                                                                                                
 Usage: python_provider [OPTIONS]                                                                                                                                               
                                                                                                                                                                                
 WebSocket client for handling asynchronous blockchain RPC requests.                                                                                                            
                                                                                                                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --proxy_url    TEXT                                 URL of the proxy server                                                                                                  │
│ --host         TEXT                                 WebSocket server host                                                                                                    │
│ --port         INTEGER                              WebSocket server port                                                                                                    │
│ --path         TEXT                                 WebSocket endpoint path                                                                                                  │
│ --log-level    [DEBUG|INFO|WARNING|ERROR|CRITICAL]  Set the logging level                                                                                                    │
│ --help                                              Show this message and exit.                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


```

## Commands

Here are common commands you might need while working with the project:

### Formatting

```shell
make fmt
```

### Linting

```shell
make lint
```

### Testing

```shell
make test
```

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
