from mcp.server.fastmcp import FastMCP
import subprocess
from typing import Dict, Any

# Create an MCP server
mcp = FastMCP("Terminal Server")

# Add a terminal command execution tool
@mcp.tool()
def execute_command(command: str) -> Dict[str, Any]:
    """
    Execute a terminal command
    
    Args:
        command: The terminal command to execute
        
    Returns:
        A dictionary containing the command output and exit code
    """
    try:
        # Execute the command and capture output
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            capture_output=True,
            text=True
        )
        
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
            "success": result.returncode == 0
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
    import asyncio
    
    async def main():
        await mcp.run()
    
    asyncio.run(main())
