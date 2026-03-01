"""CLI entrypoint to run the MCP server for Mistral (Le Chat).

Loads environment variables via python-dotenv, imports the configured MCP
server instance, and starts it using the streamable HTTP transport.

This transport is compatible with:
- Mistral Le Chat (via ALPIC.ai deployment)
- Any MCP client that supports HTTP transport
- Claude Desktop (with HTTP configuration)
"""

from dotenv import load_dotenv

load_dotenv()

# ruff: noqa: E402
from src.server import mcp  # noqa: F401

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )  # Use "streamable-http" for Mistral Le Chat / ALPIC compatibility
