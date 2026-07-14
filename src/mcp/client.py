import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def _call_tool_async(
    tool_name: str,
    params: dict,
):
    """
    Connect to the Semantic Scholar MCP Server
    and execute an MCP tool.

    Parameters
    ----------
    tool_name : str
        Name of the MCP tool.

    params : dict
        Parameters expected by the tool.

    Returns
    -------
    CallToolResult
        Response returned by the MCP Server.
    """

    

    server = StdioServerParameters(
         command="npx",
    args=[
        "-y",
        "openalex-research-mcp",
    ]
    
    )


    async with stdio_client(server) as (read, write):

      

        async with ClientSession(read, write) as session:

        
            await session.initialize()


            result = await session.call_tool(
                tool_name,
                params,
            )

            return result


def call_tool(
    tool_name: str,
    params: dict,
):
    """
    Public function used by the application.

    Converts synchronous Python code into an
    asynchronous MCP request.
    """

    return asyncio.run(
        _call_tool_async(
            tool_name,
            params,
        )
    )