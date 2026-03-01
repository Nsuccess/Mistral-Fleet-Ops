# 🎯 Mistral Le Chat Setup Guide

This guide shows you how to use Blaxel Fleet Commander with **Mistral Le Chat** instead of Claude Desktop.

## 🌐 Deployment Options

### Option 1: Deploy to ALPIC.ai (Recommended)

ALPIC.ai provides one-click deployment for MCP servers that work with Mistral Le Chat.

**Steps:**

1. **Fork this repository** to your GitHub account

2. **Click the deploy button:**
   
   [![Deploy on ALPIC.ai](https://img.shields.io/badge/Deploy-ALPIC.ai-ff69b4?style=for-the-badge&logo=alpic&logoColor=white)](https://alpic.ai/deploy?repo=https://github.com/YOUR_USERNAME/blaxel-fleet-commander)
   
   *(Replace `YOUR_USERNAME` with your GitHub username)*

3. **Configure environment variables** in ALPIC dashboard:
   ```
   BL_API_KEY=your-blaxel-api-key
   BL_WORKSPACE=your-workspace-name
   MISTRAL_API_KEY=your-mistral-key (optional, for RAG)
   QDRANT_URL=your-qdrant-url (optional, for RAG)
   QDRANT_API_KEY=your-qdrant-key (optional, for RAG)
   WANDB_API_KEY=your-wandb-key (optional, for tracing)
   ```

4. **Deploy** and get your MCP server URL

5. **Connect to Le Chat:**
   - Open [chat.mistral.ai](https://chat.mistral.ai)
   - Go to Settings → MCP Servers
   - Add your ALPIC deployment URL
   - Start chatting!

---

### Option 2: Self-Hosted HTTP Server

Run the MCP server locally or on your own infrastructure.

**1. Install dependencies:**

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/blaxel-fleet-commander.git
cd blaxel-fleet-commander

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -e .
```

**2. Configure environment:**

```bash
cp .env.example .env
# Edit .env with your API keys
```

**3. Run the HTTP server:**

```bash
python main.py
```

The server will start on `http://localhost:3000` by default.

**4. Configure Le Chat:**

- Open [chat.mistral.ai](https://chat.mistral.ai)
- Go to Settings → MCP Servers
- Add server URL: `http://localhost:3000` (or your public URL)
- Start using the tools!

---

### Option 3: Use with Claude Desktop (STDIO)

If you still want to use Claude Desktop, use the STDIO transport:

**1. Create `run_mcp_stdio.py`:**

```python
"""STDIO entrypoint for Claude Desktop."""
from dotenv import load_dotenv
load_dotenv()

from src.server import mcp

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

**2. Configure Claude Desktop:**

Add to `claude_desktop_config.json`:

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

## 🔧 Configuration Differences

### Transport Modes

| Transport | Use Case | Configuration |
|-----------|----------|---------------|
| **streamable-http** | Mistral Le Chat, ALPIC.ai | `python main.py` |
| **stdio** | Claude Desktop | `python run_mcp_stdio.py` |
| **http** | Custom MCP clients | Set `MCP_TRANSPORT=http` |

### Server Configuration

The server is configured in `src/server.py`:

```python
mcp: FastMCP = FastMCP(
    "BLAXEL_FLEET_MCP", 
    port=3000,              # HTTP port
    debug=True,             # Enable debug logging
    stateless_http=True     # Required for Mistral/ALPIC
)
```

**Key settings:**
- `stateless_http=True` — Required for Mistral Le Chat compatibility
- `port=3000` — Default HTTP port (configurable via env vars)
- `debug=True` — Detailed logging for troubleshooting

---

## 🎯 Using with Mistral Le Chat

Once connected, you can use natural language commands:

### Example Prompts

**Deploy an app:**
```
Deploy https://github.com/user/my-react-app.git to 3 Blaxel sandboxes
```

**Check sandbox status:**
```
List all my Blaxel sandboxes and show their latency
```

**Verify deployments:**
```
Check if all my deployment URLs are still live
```

**Search deployment history:**
```
Find deployments that failed with npm errors in the last 24 hours
```

**Get fix suggestions:**
```
How do I fix the ERESOLVE dependency error?
```

---

## 🔍 Troubleshooting

### Server won't start

1. Check `.env` file has valid `BL_API_KEY` and `BL_WORKSPACE`
2. Ensure port 3000 is not already in use
3. Verify all dependencies installed: `pip install -e .`

### Le Chat can't connect

1. Verify server is running: `curl http://localhost:3000/healthz`
2. Check firewall allows connections on port 3000
3. For ALPIC deployment, verify environment variables are set

### Tools not appearing in Le Chat

1. Restart the MCP server
2. Refresh Le Chat browser tab
3. Check server logs for errors: `python main.py` (watch console output)

### RAG features not working

1. Add optional environment variables:
   ```
   MISTRAL_API_KEY=your-key
   QDRANT_URL=your-url
   QDRANT_API_KEY=your-key
   ```
2. Deployment tools work without RAG—it's completely optional

---

## 📊 Architecture: Mistral vs Claude

### Mistral Le Chat (HTTP Transport)

```
┌─────────────────────────────────────────┐
│         Mistral Le Chat                 │
│      (chat.mistral.ai)                  │
│                                         │
│   "Deploy my app to 5 sandboxes"       │
└─────────────────┬───────────────────────┘
                  │ HTTP / JSON-RPC
                  ▼
┌─────────────────────────────────────────┐
│    Blaxel Fleet Commander               │
│    (HTTP Server on port 3000)           │
│                                         │
│    transport="streamable-http"          │
│    stateless_http=True                  │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│         Blaxel Cloud Sandboxes          │
│      (Parallel Deployment)              │
└─────────────────────────────────────────┘
```

### Claude Desktop (STDIO Transport)

```
┌─────────────────────────────────────────┐
│         Claude Desktop                  │
│      (Local Application)                │
│                                         │
│   "Deploy my app to 5 sandboxes"       │
└─────────────────┬───────────────────────┘
                  │ STDIO / JSON-RPC
                  ▼
┌─────────────────────────────────────────┐
│    Blaxel Fleet Commander               │
│    (Python Process)                     │
│                                         │
│    transport="stdio"                    │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│         Blaxel Cloud Sandboxes          │
│      (Parallel Deployment)              │
└─────────────────────────────────────────┘
```

---

## 🚀 Quick Start Commands

### For Mistral Le Chat (HTTP)

```bash
# Start HTTP server
python main.py

# Or with custom port
PORT=8000 python main.py
```

### For Claude Desktop (STDIO)

```bash
# Create STDIO runner
cat > run_mcp_stdio.py << 'EOF'
from dotenv import load_dotenv
load_dotenv()
from src.server import mcp
if __name__ == "__main__":
    mcp.run(transport="stdio")
EOF

# Configure Claude Desktop with path to run_mcp_stdio.py
```

---

## 🎉 Benefits of Mistral Le Chat

| Feature | Benefit |
|---------|---------|
| **Web-based** | No desktop app installation required |
| **Mistral Models** | Access to Mistral's latest AI models |
| **HTTP Transport** | Easy deployment to cloud platforms |
| **ALPIC Integration** | One-click deployment |
| **Stateless** | Better scalability for production |

---

## 📚 Additional Resources

- [Mistral Le Chat](https://chat.mistral.ai)
- [ALPIC.ai Documentation](https://alpic.ai/docs)
- [FastMCP Documentation](https://github.com/fastmcp/fastmcp)
- [Blaxel Documentation](https://blaxel.ai/docs)

---

## 🤝 Support

Having issues? 

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review server logs: `python main.py` (watch console)
3. Open an issue on GitHub

---

*Built for both Claude Desktop and Mistral Le Chat* 🚀
