# ⚡ QUICK REFERENCE CARD

## 🎯 Current Status
- ✅ MCP Server: RUNNING (port 8000)
- ✅ ngrok Tunnel: ACTIVE
- ✅ Public URL: https://folksy-productively-delaine.ngrok-free.dev/mcp
- ✅ Ready for Mistral Le Chat

---

## 🔌 Connect to Mistral Le Chat (30 seconds)

1. Go to https://chat.mistral.ai
2. Sidebar → Intelligence → Connectors
3. "+ Add Connector" → "Custom MCP Connector"
4. Fill in:
   - Name: `Blaxel Fleet Commander`
   - URL: `https://folksy-productively-delaine.ngrok-free.dev/mcp`
5. Click "Connect"
6. Enable in chat → Click "Tools" → Check the box
7. Test: "List my available tools"

---

## 🛠️ Available Tools

### Blaxel Management
- `blaxel_list_sessions` - List all sandboxes
- `blaxel_create_session` - Create new sandbox
- `blaxel_delete_session` - Delete sandbox
- `blaxel_get_session_info` - Get sandbox details

### Deployment
- `blaxel_deploy_repo` - Deploy Git repo
- `blaxel_run_command` - Execute commands
- `blaxel_verify_deployment` - Check deployment

### Qdrant (Placeholder)
- `qdrant_search` - Semantic search
- `qdrant_upsert` - Add vectors

---

## 🚀 Quick Commands

### Start Everything (CORRECT WAY)
```bash
# Terminal 1: Start MCP Server
python main.py

# Terminal 2: Start ngrok with host header fix
ngrok http 8000 --host-header="localhost:8000"
```

**CRITICAL**: Always use `--host-header="localhost:8000"` with ngrok!
Without it, FastMCP will reject requests with "421 Misdirected Request"

### Stop Everything
```bash
.\STOP_DEMO.bat
```

### Check Server Status
```bash
curl http://localhost:8000/mcp
```

### Check ngrok Status
```bash
curl https://folksy-productively-delaine.ngrok-free.dev/mcp
```

---

## 📊 Monitoring

### ngrok Web Interface
http://127.0.0.1:4040

### Weave Dashboard
https://wandb.ai/successnwachukwu563-bvc/blaxel-fleet-commander/weave

### Server Logs
Check Terminal 18 (MCP Server)

### Tunnel Logs
Check Terminal 15 (ngrok)

---

## 🎯 Demo Commands for Mistral Le Chat

```
"List all my Blaxel sandboxes"

"Create 2 new Blaxel sessions"

"Deploy https://github.com/Mistral-MCP-Hackathon-2025/mistral-jump.git to a sandbox"

"Show me information about my active sessions"

"Run 'npm install' in all my sandboxes"

"Verify all my deployment URLs are live"

"Delete inactive sandbox sessions"
```

---

## 📚 Documentation Files

### Connection Guides
- `MISTRAL_LECHAT_CONNECTION_GUIDE.md` - Complete guide
- `CONNECTION_INFO.txt` - Quick reference
- `MISTRAL_CONNECTION_VERIFIED.md` - Verification

### Deployment Options
- `DEPLOYMENT_OPTIONS_SUMMARY.md` - ngrok vs ALPIC
- `ALPIC_DEPLOYMENT_GUIDE.md` - ALPIC instructions
- `NGROK_COMMANDS.md` - ngrok reference

### Setup Guides
- `MISTRAL_SETUP.md` - Initial setup
- `QUICK_START_MISTRAL.md` - Quick start
- `DEMO_VIDEO_SETUP.md` - Demo prep
- `QDRANT_SETUP.md` - Qdrant config

---

## 🔧 Troubleshooting

### Server Not Responding
```bash
# Check if running
netstat -ano | Select-String ":8000"

# Restart server
.\STOP_DEMO.bat
.\START_DEMO.bat
```

### ngrok Tunnel Down
```bash
# Check status
curl http://127.0.0.1:4040/api/tunnels

# Restart ngrok
ngrok http 8000
```

### Connection Failed in Mistral Le Chat
1. Verify server is running
2. Check ngrok tunnel is active
3. Test endpoint: `curl https://your-url.ngrok-free.dev/mcp`
4. Check server logs for errors

---

## 🎓 Key Learnings from Hackathon Winners

1. ✅ Use `streamable-http` transport for Mistral
2. ✅ MCP endpoint is at `/mcp` (not root)
3. ✅ ngrok works great for testing
4. ✅ ALPIC.ai recommended for production
5. ✅ Document both deployment options

---

## 🚀 Next Steps

### Immediate
- [ ] Test connection in Mistral Le Chat
- [ ] Verify all tools work
- [ ] Try demo commands

### Short-term
- [ ] Deploy to ALPIC.ai (optional)
- [ ] Record demo video
- [ ] Prepare submission

### Long-term
- [ ] Add authentication
- [ ] Implement RAG tools
- [ ] Submit to registries

---

## 📞 Quick Links

- **Mistral Le Chat**: https://chat.mistral.ai
- **ngrok Dashboard**: http://127.0.0.1:4040
- **Weave Tracing**: https://wandb.ai/successnwachukwu563-bvc/blaxel-fleet-commander/weave
- **ALPIC.ai**: https://app.alpic.ai
- **GitHub Repo**: (your repo URL)

---

## ✅ Pre-Flight Checklist

Before connecting to Mistral Le Chat:
- [x] MCP server running
- [x] ngrok tunnel active
- [x] Public URL accessible
- [x] Tools registered
- [x] Documentation complete
- [ ] Tested in Mistral Le Chat

---

**Last Updated**: March 1, 2026
**Status**: ✅ READY
**Public URL**: https://folksy-productively-delaine.ngrok-free.dev/mcp
**Action**: Connect to Mistral Le Chat and test!
