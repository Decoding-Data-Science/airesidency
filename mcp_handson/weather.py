import mcp
from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Get the weather location."""
    return "It's always hot in Dubai"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
