MCP with Local Tools Langchain will  work with LLM .

Using Langchain and ::Langchain MCP adapters Local Ollama
Installed MCP Cli

Python — application development
Ollama — runs the LLM locally
Qwen3.5 — local language model
LangChain — creates and manages the AI agent
MCP — connects the agent to external tools
DeepWiki MCP — provides GitHub repository information
AsyncIO — handles asynchronous MCP/tool operations
uv — manages the Python environment and dependencies


User question
      ↓
   Ollama
      ↓
Does it need a tool?
      ↓
     Yes
      ↓
MCP Tool
      ↓
DeepWiki / other MCP server
      ↓
   Tool result
      ↓
   Ollama
      ↓
Final answer