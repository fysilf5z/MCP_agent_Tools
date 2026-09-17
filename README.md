Project 1 :MCP with Local Tools Langchain will  work with LLM .

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


Project 2: 
Project Brief: Dev.to Blog Publisher MCP Server

This project creates a custom MCP (Model Context Protocol) server that allows an AI agent to publish blog posts directly to Dev.to using the Dev.to API.

Flow
AI Agent
   ↓
MCP Client
   ↓
Dev.to Blog Publisher MCP Server
   ↓
publish_blog_to_devto()
   ↓
Dev.to REST API
   ↓
Blog Published / Draft Created
Main technologies
Python — application development
FastMCP — creates the MCP server and exposes tools
Requests — sends HTTP requests to the Dev.to API
dotenv — loads the Dev.to API key from .env
Logging — tracks publishing operations and errors
Dev.to API — creates and publishes articles
stdio transport — allows an MCP client to communicate with the server locally