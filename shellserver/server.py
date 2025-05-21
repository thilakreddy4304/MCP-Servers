from mcp.server.fastmcp import FastMCP
import asyncio
from typing import Dict, Any

# Create an MCP server
mcp = FastMCP("Terminal Server")

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
