from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")
# from mcp.server.mcpserver import MCPServer

# mcp = MCPServer("Demo")

@mcp.tool()
def add(a : int  , b: int):
    """Addition two numbers a  and b"""
    return a+ b

@mcp.resource("greeting://{name}")
def greeting(name : str)-> str:
    "Return professionall greeting"
    return f"Hello {name}"

@mcp.prompt()
def greet_user(name : str  , style : str = "friendly")->str:
    "Greeting prompt"
    styles = {
        "friendly": "Please write a warm  freiendly greeting",
        "formal" :"Please write a professional greeting",
        "causal": "Please write a causal greeting   "        
    }
    return f" {styles.get(style , styles['friendly'])} name is {name}"