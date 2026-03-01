# MCP Transport Comparison: STDIO vs HTTP

This document explains the differences between STDIO and HTTP transports for MCP servers, and when to use each.

## 🔌 Transport Types

### STDIO Transport

**What it is:**
- Standard Input/Output communication
- Process-to-process communication
- Used by Claude Desktop

**How it works:**
```
Claude Desktop App
    ↓ (spawns process)
Python MCP Server Process
    ↓ (STDIO pipes)
JSON-RPC messages
```

**Configuration:**
```python
# run_mcp_stdio.py
mcp.run(transport="stdio")
```

**Pros:**
- ✅ Simple setup for local development
- ✅ No network configuration needed
- ✅ Secure (no network exposure)
- ✅ Perfect for Claude Desktop

**Cons:**
- ❌ Only works locally
- ❌ Can't be accessed remotely
- ❌ Requires process spawning
- ❌ Not suitable for web-based clients

---

### HTTP Transport (Streamable)

**What it is:**
- HTTP-based communication
- Network-accessible server
- Used by Mistral Le Chat, ALPIC.ai

**How it works:**
```
Mistral Le Chat (Web)
    ↓ (HTTP requests)
MCP Server (port 3000)
    ↓ (JSON-RPC over HTTP)
Blaxel Cloud
```

**Configuration:**
```python
# main.py
mcp: FastMCP = FastMCP(
    "BLAXEL_FLEET_MCP",
    port=3000,
    debug=True,
    stateless_http=True  # Required for Mistral
)

mcp.run(transport="streamable-http")
```

**Pros:**
- ✅ Works with web-based clients (Mistral Le Chat)
- ✅ Can be deployed to cloud (ALPIC.ai)
- ✅ Accessible remotely
- ✅ Stateless (better scalability)
- ✅ Multiple clients can connect

**Cons:**
- ❌ Requires network configuration
- ❌ Need to manage ports/firewalls
- ❌ More complex security considerations

---

## 📊 Comparison Table

| Feature | STDIO | HTTP (Streamable) |
|---------|-------|-------------------|
| **Client** | Claude Desktop | Mistral Le Chat, Web clients |
| **Network** | Local only | Remote accessible |
| **Setup** | Simple | Moderate |
| **Security** | Process isolation | Network security needed |
| **Scalability** | Single client | Multiple clients |
| **Deployment** | Local machine | Cloud platforms |
| **State** | Can be stateful | Stateless (recommended) |
| **Port** | N/A | 3000 (configurable) |

---

## 🎯 When to Use Each

### Use STDIO when:
- ✅ Using Claude Desktop
- ✅ Local development only
- ✅ No need for remote access
- ✅ Simple setup preferred
- ✅ Maximum security (no network exposure)

### Use HTTP when:
- ✅ Using Mistral Le Chat
- ✅ Deploying to ALPIC.ai or cloud
- ✅ Need remote access
- ✅ Multiple clients connecting
- ✅ Web-based MCP clients

---

## 🔧 Configuration Examples

### For Claude Desktop (STDIO)

**1. Create `run_mcp_stdio.py`:**
```python
from dotenv import load_dotenv
load_dotenv()

from src.server import mcp

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

**2. Configure Claude Desktop:**
```json
{
    "mcpServers": {
        "Blaxel Fleet Commander": {
            "command": "C:\\path\\to\\.venv\\Scripts\\python.exe",
            "args": ["C:\\path\\to\\run_mcp_stdio.py"]
        }
    }
}
```

---

### For Mistral Le Chat (HTTP)

**1. Use `main.py`:**
```python
from dotenv import load_dotenv
load_dotenv()

from src.server import mcp

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

**2. Start server:**
```bash
python main.py
# Server runs on http://localhost:3000
```

**3. Configure Le Chat:**
- Open chat.mistral.ai
- Settings → MCP Servers
- Add: `http://localhost:3000` (or your public URL)

---

## 🏗️ Server Configuration

Both transports use the same server instance defined in `src/server.py`:

```python
mcp: FastMCP = FastMCP(
    "BLAXEL_FLEET_MCP",
    port=3000,              # Only used for HTTP transport
    debug=True,             # Enable debug logging
    stateless_http=True     # Required for HTTP transport
)
```

**Key parameters:**

- `port=3000` — HTTP server port (ignored for STDIO)
- `debug=True` — Detailed logging for both transports
- `stateless_http=True` — Required for Mistral Le Chat compatibility

---

## 🔐 Security Considerations

### STDIO Transport
- ✅ No network exposure
- ✅ Process-level isolation
- ✅ Credentials stay local
- ⚠️ Still need to protect `.env` file

### HTTP Transport
- ⚠️ Network-accessible (use firewall)
- ⚠️ Consider HTTPS for production
- ⚠️ Implement authentication if needed
- ⚠️ Protect API keys in environment variables
- ✅ `stateless_http=True` prevents session hijacking

**Recommendations:**
1. Use HTTPS in production (reverse proxy)
2. Implement API key authentication
3. Use firewall rules to restrict access
4. Never commit `.env` file to git
5. Rotate API keys regularly

---

## 🚀 Deployment Scenarios

### Local Development (STDIO)
```
Developer Machine
├── Claude Desktop
└── MCP Server (STDIO)
    └── Blaxel Cloud
```

### Cloud Deployment (HTTP)
```
Internet
├── Mistral Le Chat
└── ALPIC.ai / Cloud Server
    └── MCP Server (HTTP)
        └── Blaxel Cloud
```

### Hybrid Setup
```
Developer Machine
├── Claude Desktop (STDIO)
└── MCP Server (HTTP)
    ├── Mistral Le Chat (remote)
    └── Blaxel Cloud
```

---

## 📝 Environment Variables

Both transports use the same environment variables:

```env
# Required
BL_API_KEY=your-blaxel-api-key
BL_WORKSPACE=your-workspace

# Optional (RAG features)
MISTRAL_API_KEY=your-mistral-key
QDRANT_URL=your-qdrant-url
QDRANT_API_KEY=your-qdrant-key

# Optional (observability)
WANDB_API_KEY=your-wandb-key

# Optional (disable features)
WEAVE_DISABLED=true
WANDB_DISABLED=true
```

---

## 🔄 Switching Between Transports

You can easily switch between transports:

**From STDIO to HTTP:**
```bash
# Instead of:
python run_mcp_stdio.py

# Use:
python main.py
```

**From HTTP to STDIO:**
```bash
# Instead of:
python main.py

# Use:
python run_mcp_stdio.py
```

**Both at once:**
```bash
# Terminal 1: HTTP server for Mistral
python main.py

# Terminal 2: STDIO for Claude (if needed)
# Configure Claude Desktop to use run_mcp_stdio.py
```

---

## 🎓 Technical Details

### STDIO Communication
```
Client → stdin → MCP Server
MCP Server → stdout → Client
MCP Server → stderr → Logs
```

**Message format:**
```json
{"jsonrpc": "2.0", "method": "tools/list", "id": 1}
```

### HTTP Communication
```
Client → HTTP POST → MCP Server
MCP Server → HTTP Response → Client
```

**Request:**
```http
POST / HTTP/1.1
Content-Type: application/json

{"jsonrpc": "2.0", "method": "tools/list", "id": 1}
```

**Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{"jsonrpc": "2.0", "result": {...}, "id": 1}
```

---

## 🆘 Troubleshooting

### STDIO Issues

**Problem:** Claude Desktop can't find the server
- ✅ Check absolute paths in `claude_desktop_config.json`
- ✅ Verify virtual environment is activated
- ✅ Test manually: `python run_mcp_stdio.py`

**Problem:** Server crashes immediately
- ✅ Check `.env` file exists with valid keys
- ✅ Look at Claude Desktop logs
- ✅ Run with debug: `python run_mcp_stdio.py` in terminal

### HTTP Issues

**Problem:** Can't connect to server
- ✅ Verify server is running: `curl http://localhost:3000/healthz`
- ✅ Check firewall allows port 3000
- ✅ Ensure no other service using port 3000

**Problem:** Mistral Le Chat can't connect
- ✅ Use public URL (not localhost) for remote access
- ✅ Verify HTTPS if using secure connection
- ✅ Check CORS settings if needed

---

## 📚 Additional Resources

- [FastMCP Documentation](https://github.com/fastmcp/fastmcp)
- [MCP Protocol Specification](https://mcp.run)
- [Claude Desktop MCP Guide](https://docs.anthropic.com/claude/docs/mcp)
- [Mistral Le Chat Documentation](https://docs.mistral.ai)
- [ALPIC.ai Deployment Guide](https://alpic.ai/docs)

---

*Choose the transport that fits your use case!* 🚀
