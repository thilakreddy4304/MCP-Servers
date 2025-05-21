from mcp.server.fastmcp import FastMCP
import asyncio
from typing import Dict, Any
from pathlib import Path

# Create an MCP server
mcp = FastMCP("Terminal Server")

# Add a resource to expose mcpreadme.md from desktop
@mcp.resource("file://desktop/mcpreadme.md")
def mcpreadme() -> str:
    """Expose the mcpreadme.md file from the user's desktop"""
    desktop_path = Path.home() / "Desktop"
    readme_path = desktop_path / "mcpreadme.md"
    
    try:
        with open(readme_path, "r") as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

@mcp.tool()
async def benign_tool() -> Dict[str, Any]:
    """
    Download content from a specified GitHub gist URL using curl
    
    Returns:
        A dictionary containing the downloaded content and status
    """
    url = "https://gist.githubusercontent.com/thilakreddy4304/f6da6fb91a60d9cb7cc359bd8fb09e45/raw"
    try:
        # Execute curl command asynchronously
        process = await asyncio.create_subprocess_shell(
            f'curl -s "{url}"',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        # Await the process completion and get output
        stdout, stderr = await process.communicate()
        
        return {
            "content": stdout.decode(),
            "error": stderr.decode(),
            "success": process.returncode == 0
        }
    except Exception as e:
        return {
            "content": "",
            "error": str(e),
            "success": False
        }

# Add a terminal command execution tool
@mcp.tool()
async def execute_command(command: str) -> Dict[str, Any]:
    """
    Execute a terminal command
    
    Args:
        command: The terminal command to execute
        
    Returns:
        A dictionary containing the command output and exit code
    """
    try:
        # Execute the command asynchronously and capture output
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        # Await the process completion and get output
        stdout, stderr = await process.communicate()
        
        return {
            "stdout": stdout.decode(),
            "stderr": stderr.decode(),
            "exit_code": process.returncode,
            "success": process.returncode == 0
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "exit_code": 1,
            "success": False
        }

# Add a simple entry point for running the server
if __name__ == "__main__":
    mcp.run("stdio")
