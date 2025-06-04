from smolagents import ToolCallingAgent, ToolCollection, LiteLLMModel
from mcp import StdioServerParameters


model = LiteLLMModel(
        model_id="ollama_chat/qwen2.5:14b",
        num_ctx=8192) 

# Outline STDIO stuff to get to MCP Tools
server_parameters = StdioServerParameters(
    command="uv",
    args=["run", "server.py"],
    env=None,
)

# Run the agent using the MCP tools 
with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tool_collection:
    agent = ToolCallingAgent(tools=[*tool_collection.tools], model=model)
    agent.run("what is the current price of nvda?")
    