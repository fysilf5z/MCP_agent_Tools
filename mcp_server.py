from datetime import datetime
# from mcp.server.mcpserver import MCPServer

# mcp = MCPServer("mcpdemo")

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")
@mcp.tool()
def current_time():
    """this function return current date and time
    This tool use when user asked about current time """
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time
    

@mcp.tool()
def word_count(text: str) -> int:
    """Count the number of words in a piece of text.
    Use this when the user asks how long a piece of writing is
    or asks you to count the words in something they've shared.
    Returns the word count as an integer.
    """
    return len(text.split())

if __name__ == "__main__":
    # Run the MCP server over stdio.
    mcp.run()
    
