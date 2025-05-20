# MCP Terminal Server

A simple Model Context Protocol (MCP) server that provides a terminal command execution tool. This server allows LLM applications to execute terminal commands on your system through a standardized API.

## Features

- Execute arbitrary terminal commands
- Get structured responses with stdout, stderr, and exit codes
- Simple interface for LLM applications

## Installation

### Prerequisites

- Python 3.9 or higher
- MCP Python SDK

### Setup

1. Install the MCP SDK:

```bash
pip install "mcp[cli]"
```

2. Clone this repository or download the server.py file.

## Usage

### Running the Server

Run the server directly with Python:

```bash
python server.py
```

Or use the MCP development tools to test it:

```bash
mcp dev server.py
```

### Installing in Claude Desktop

You can install this server directly in Claude Desktop with:

```bash
mcp install server.py
```

### Available Tools

#### execute_command

Executes a terminal command and returns the output.

**Input:**

- `command` (string): The terminal command to execute

**Output:**

- `stdout` (string): Standard output of the command
- `stderr` (string): Standard error output of the command
- `exit_code` (number): Exit code of the command (0 means success)
- `success` (boolean): Whether the command succeeded

## Example Usage

When connected to Claude or another LLM that supports MCP:

```
User: What files are in my current directory?

Claude: I can check that for you. Let me run the 'ls' command to see what files are in your current directory.

[Claude uses the execute_command tool with "ls -la"]

Based on the output, I can see the following files in your current directory:
...
```

## Security Considerations

⚠️ **Warning**: This server allows execution of arbitrary terminal commands. Only use it in trusted environments and be cautious about who has access to your MCP-enabled LLM.

Consider adding additional validation or restricting commands if deploying in shared environments.

## License

MIT
