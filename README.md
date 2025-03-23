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

To use it;

python_provider --proxy_url https://ethereum.blockpi.network/v1/rpc/public

╰─>$ python_provider --proxy_url https://ethereum.blockpi.network/v1/rpc/public
[03/23/25 19:41:30] INFO     2025-03-23 19:41:30,191 - async_websocket_client - INFO - Connecting to ws://127.0.0.1:8080/ws                              
                    INFO     2025-03-23 19:41:30,204 - async_websocket_client - INFO - Connected to ws://127.0.0.1:8080/ws, waiting for requests       
[03/23/25 19:41:33] INFO     2025-03-23 19:41:33,566 - async_websocket_client - INFO - Request 44bd7bb6-3193-4d3d-ae92-fe39607b3686 completed in 0.144s 
                    INFO     2025-03-23 19:41:33,631 - async_websocket_client - INFO - Request 08b93e17-1573-4b3e-b8d7-cb492020f3ee completed in 0.053s 
[03/23/25 19:41:34] INFO     2025-03-23 19:41:34,732 - async_websocket_client - INFO - Request 154a09e3-de1d-4843-a627-c5d839fdc1d0 completed in 0.053s 
                    INFO     2025-03-23 19:41:34,797 - async_websocket_client - INFO - Request f8a00f44-f8a3-467b-a481-66809d13a9b2 completed in 0.055s 
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
