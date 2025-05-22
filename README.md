# MCP Servers Collection

![MCP Tool Call Demo](/static/mcp-tool-call.gif)

This repository contains a collection of Model Context Protocol (MCP) servers for different purposes. Each subdirectory is a separate MCP server implementation that can be used with Claude Desktop, the MCP CLI, or any other MCP-compatible client.

## Available Servers

### Shell Server

A server that provides terminal command execution capabilities through the MCP protocol. Located in the `shellserver` directory.

- **Features**: Execute terminal commands and get structured output
- **Usage**: See the [Shell Server README](./shellserver/README.md) for details

### Resource Server (Example)

A basic server demonstrating the use of resources in MCP. Located in the `quickstart-resources` directory.

## Getting Started

Each server can be run independently:

```bash
# Navigate to the server directory
cd shellserver

# Run the server directly
python server.py

# Or use the MCP development tools
mcp dev server.py

# Install in Claude Desktop
mcp install server.py
```

## Installation Requirements

- Python 3.9+
- MCP Python SDK

Install the MCP SDK with pip:

```bash
pip install "mcp[cli]"
```

## Adding New Servers

To add a new MCP server to this collection:

1. Create a new directory for your server
2. Implement your server following the MCP protocol
3. Add a README.md with usage instructions
4. Update this root README.md to include your new server

## License

MIT
