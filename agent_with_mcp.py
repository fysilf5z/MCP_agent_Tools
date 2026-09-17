import asyncio
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient

CHAT_MODEL = "qwen3:8b"
# Hosted remote MCP server we'll connect to over HTTP.
DEEPWIKI_MCP_URL = "https://mcp.deepwiki.com/mcp"

# System prompt that tells the model what tools it has and how to behave.
SYSTEM_PROMPT = (
    "You are a helpful assistant with access to tools for checking the current time, "
    "counting words, and looking up information about GitHub repositories. "
    "Use tools when the user's request needs information you don't already have. "
    "If a tool returns an error, tell the user plainly and do not retry with made-up arguments. "
    "If the question doesn't need a tool, just answer directly."
)

async def build_agent(client : MultiServerMCPClient):
    
    tools = await client.get_tools()
    for t in tools:
        print(f"tools are loaded{t.name}")
        
    model = ChatOllama(model = CHAT_MODEL , temperature=0)
    
    return create_agent(model=model , tools= tools , system_prompt= SYSTEM_PROMPT)

async def main():
    """Create a MCP server that connects two servers
    1."tools" is a local MCP server  started  as a subprocess over stdio. Langchain will launch `python mcp_server.py` for us.
    2. "deepwiki" is a hosted MCP server we connect to over Http. """
    
    client = MultiServerMCPClient({
        "tools" : {
            "command" : "python" ,
            "args" : ["mcp_server.py"],
            "transport" : "stdio"
            
        } , 
         "deepwiki" : {
             "url": DEEPWIKI_MCP_URL,
            "transport": "streamable_http",
         }
    })
    
    agent  =await build_agent(client)
    
    print("\nReady! Ask the agent something.")
    print("Type 'exit' to quit.\n")
    
    while True:
        question = input("You  :").strip()
        if not question or question.lower()   in("exit"  , "quit"):
            break
        
        result  = await agent.ainvoke({
            "messages": [{"role": "user", "content": question}],
        })
        
    
        #walk through  the retured messages  and print any tools calls
        
        for msg in result["messages"]:
            toolss= getattr(msg , "tool_calls", None)
            if toolss:
                for  d in toolss:
                    print(f"tool_calls {d['name']} {d["args"]}")
                    
          # The final message in the list is the agent's final answer.
        print(f"\nAnswer: {result['messages'][-1].content}\n")
        
        
if __name__ == "__main__":    
    # Run the async program.
    asyncio.run(main())    