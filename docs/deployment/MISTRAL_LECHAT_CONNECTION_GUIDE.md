# 🎯 COMPLETE GUIDE: Connecting to Mistral Le Chat

## 📚 Based on Research from Mistral MCP Hackathon Winners & Official Docs

This guide combines insights from the Mistral-MCP-Hackathon-2025 winning projects and official Mistral documentation.

---

## 🔍 What We Learned from Hackathon Winners

### Their Setup
- **Primary Deployment**: ALPIC.ai (one-click deploy platform)
- **Alternative**: ngrok for local testing (found in mistral-jump config)
- **Transport**: `streamable-http` (explicitly for "Alpic compatibility")
- **Port**: 3000 (we use 8000 to avoid conflicts)
- **MCP Endpoint**: `/mcp` (standard FastMCP endpoint)

### ngrok Evidence
Found in `cloned/mistral-jump/vite.config.ts`:
```typescript
allowedHosts: ["5bfd7ddf4949.ngrok-free.app", "52.58.159.118", "*"]
```
This confirms they used ngrok for development/testing!

---

## 🚀 TWO DEPLOYMENT OPTIONS

### Option 1: ngrok (What We're Using - FREE)

**Pros:**
- ✅ Free tier available
- ✅ Instant setup (no account needed for basic)
- ✅ Works immediately for testing
- ✅ Perfect for demos and development

**Cons:**
- ❌ URL changes on restart (not persistent)
- ❌ 40 connections/minute limit
- ❌ Shows ngrok warning page on first visit
- ❌ Not suitable for production

**Our Setup:**
```
Local Server: http://localhost:8000/mcp
Public URL: https://folksy-productively-delaine.ngrok-free.dev/mcp
```

### Option 2: ALPIC.ai (Production - Recommended by Hackathon Winners)

**Pros:**
- ✅ One-click deployment from GitHub
- ✅ Persistent URLs
- ✅ Automatic SSL/HTTPS
- ✅ Handles authentication
- ✅ Auto-deploys on git push
- ✅ Supports multiple environments
- ✅ Built-in monitoring and logs
- ✅ Automatic transport layer handling (stdio → SSE/HTTP)

**Cons:**
- ❌ Requires GitHub account
- ❌ May have usage limits (check their pricing)
- ❌ Less control over infrastructure

**How ALPIC.ai Works:**
1. Sign in with GitHub
2. Connect your repository
3. Choose branch to deploy
4. Set environment variables
5. Click deploy
6. Get persistent MCP server URL

**ALPIC.ai Features:**
- Automatically detects MCP framework
- Handles build commands
- Provides remote URL for testing
- Supports custom domains
- Auto-updates on git push
- Handles authentication layer
- Keeps server compatible with new MCP transports

---

## 🔌 HOW TO CONNECT TO MISTRAL LE CHAT

### Official Steps (from Mistral Help Center)

#### 1. Open Le Chat Sidebar
- Go to https://chat.mistral.ai
- Click the toggle panel button to reveal sidebar (if hidden)

#### 2. Navigate to Connectors
- Expand "Intelligence" menu
- Click "Connectors"

#### 3. Add Custom Connector
- Click "+ Add Connector" button (right side)
- This opens the MCP Connectors directory

#### 4. Configure Custom MCP Connector
- Click "Custom MCP Connector" tab at the top
- Fill in the form:

**For ngrok (our current setup):**
```
Connector Name: Blaxel Fleet Commander
Connector Server: https://folksy-productively-delaine.ngrok-free.dev/mcp
Description: Manage Blaxel cloud sandboxes and deployments
Authentication Method: None (or as configured)
```

**For ALPIC.ai (if you deploy there):**
```
Connector Name: Blaxel Fleet Commander
Connector Server: https://your-project.alpic.app/mcp
Description: Manage Blaxel cloud sandboxes and deployments
Authentication Method: (auto-detected by ALPIC)
```

#### 5. Connect
- Click "Connect" button
- Platform will attempt to connect to your server
- If authentication is required, follow the OAuth flow

#### 6. Verify Connection
- Your connector should appear in the connections list
- Status should show as "Connected"

#### 7. Enable in Chat
- Go back to main Le Chat screen
- Click "Tools" button (below chat input)
- Check the box next to "Blaxel Fleet Commander"
- Alternatively, type `/Blaxel Fleet Commander` in chat

#### 8. Test It!
Try these commands:
```
"List my available tools"
"Show me all my Blaxel sandboxes"
"What can you do with Blaxel Fleet Commander?"
```

---

## 🔐 AUTHENTICATION METHODS SUPPORTED

Mistral Le Chat auto-detects these authentication types:

1. **None** (what we're using for demo)
2. **API Key** (Bearer token)
3. **OAuth 2.1** (user login flow)

### Per-Function Permissions
Users can control whether Le Chat:
- Asks permission every time before using a function
- Always allows function execution without asking

Configure this in the Connector's detail page.

---

## 🛠️ TECHNICAL DETAILS

### MCP Protocol Version
- **Supported**: MCP 2024-11-05 and later
- **Transport**: streamable-http (single endpoint)
- **Endpoint**: `/mcp` (standard)

### Required Headers (for testing)
```http
Content-Type: application/json
Accept: application/json, text/event-stream
```

### Example Initialize Request
```json
{
  "jsonrpc": "2.0",
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {
      "name": "Mistral Le Chat",
      "version": "1.0"
    }
  },
  "id": 1
}
```

### Server Response Format
```
event: message
data: {"jsonrpc":"2.0","id":1,"result":{...}}
```

---

## 📊 COMPARISON: ngrok vs ALPIC.ai

| Feature | ngrok (Current) | ALPIC.ai (Recommended) |
|---------|----------------|------------------------|
| Setup Time | 2 minutes | 5 minutes |
| Cost | Free tier | Check pricing |
| URL Persistence | ❌ Changes on restart | ✅ Persistent |
| SSL/HTTPS | ✅ Automatic | ✅ Automatic |
| Authentication | Manual setup | ✅ Auto-handled |
| Monitoring | Basic (web UI) | ✅ Full dashboard |
| Auto-deploy | ❌ Manual | ✅ On git push |
| Custom Domain | ❌ Paid only | ✅ Supported |
| Production Ready | ❌ No | ✅ Yes |
| Best For | Testing/Demo | Production |

---

## 🎯 RECOMMENDED WORKFLOW

### For Development/Testing (Current)
1. ✅ Use ngrok for quick testing
2. ✅ Keep MCP server running locally
3. ✅ Test with Mistral Le Chat
4. ✅ Iterate quickly

### For Production/Demo Video
1. Deploy to ALPIC.ai
2. Get persistent URL
3. Configure in Mistral Le Chat
4. Record demo with stable connection

### For Hackathon Submission
1. Keep both options documented
2. Provide ngrok setup for judges to test locally
3. Provide ALPIC.ai URL for live demo
4. Show both deployment methods in README

---

## 🚨 CURRENT LIMITATIONS

### Mistral Le Chat MCP Support
According to official docs, these features are NOT YET supported:
- ❌ Prompts (MCP prompts feature)
- ❌ Resources (MCP resources feature)
- ❌ Sampling (MCP sampling feature)

### What IS Supported
- ✅ Tools (function calling)
- ✅ Custom connectors
- ✅ OAuth 2.1 authentication
- ✅ API Key authentication
- ✅ Per-function permissions
- ✅ streamable-http transport

---

## 🔧 TROUBLESHOOTING

### Connection Failed
1. Check server is running: `curl http://localhost:8000/mcp`
2. Check ngrok tunnel: `curl https://your-url.ngrok-free.dev/mcp`
3. Verify MCP endpoint responds to initialize request
4. Check server logs for errors

### ngrok "Invalid Host" Error
- This is normal for free tier
- Mistral Le Chat should handle it automatically
- If not, try restarting ngrok tunnel

### Tools Not Appearing
1. Verify connector is "Connected" status
2. Enable tools in chat (click Tools button)
3. Try typing `/Blaxel Fleet Commander` to invoke
4. Check server logs for incoming requests

### Authentication Errors
1. Verify authentication method matches server config
2. Check API keys are correct
3. For OAuth, ensure redirect URLs are configured
4. Test with "None" authentication first

---

## 📱 MOBILE SUPPORT

According to research:
- ✅ Mistral Le Chat mobile app supports MCP connectors
- ✅ All custom connectors sync across devices
- ✅ Same functionality as web version
- ✅ Tools available on iOS and Android

---

## 🎓 LEARNING FROM HACKATHON WINNERS

### What They Did Right
1. **Used ALPIC.ai for production** - Persistent, reliable URLs
2. **Kept ngrok for development** - Fast iteration
3. **Clear documentation** - Easy for judges to test
4. **Multiple deployment options** - Flexibility for users
5. **Proper authentication** - Production-ready security

### What We Can Improve
1. Deploy to ALPIC.ai for persistent demo URL
2. Add authentication layer (API key or OAuth)
3. Implement proper error handling
4. Add monitoring and logging
5. Create one-click install instructions

---

## 🚀 NEXT STEPS

### Immediate (For Demo)
- [x] ngrok tunnel running
- [x] MCP server responding
- [x] Documentation complete
- [ ] Test connection in Mistral Le Chat
- [ ] Record demo video

### Short-term (For Production)
- [ ] Deploy to ALPIC.ai
- [ ] Add API key authentication
- [ ] Implement proper error messages
- [ ] Add usage monitoring
- [ ] Create install instructions generator

### Long-term (For Distribution)
- [ ] Submit to MCP registries
- [ ] Create one-click install links
- [ ] Add custom domain
- [ ] Implement OAuth 2.1
- [ ] Add rate limiting

---

## 📚 REFERENCES

### Official Documentation
- [Mistral Le Chat Custom Connectors](https://help.mistral.ai/en/articles/393572-configuring-a-custom-connector)
- [Using MCP Connectors with Le Chat](https://help.mistral.ai/en/articles/393511-using-my-mcp-connectors-with-le-chat)
- [Mistral MCP Documentation](https://docs.mistral.ai/agents/tools/mcp)

### ALPIC.ai Resources
- [One-Click Deploy Guide](https://alpic.ai/blog/introducing-one-click-deploy)
- [ALPIC.ai Platform](https://app.alpic.ai)
- [MCP Install Instructions Generator](https://alpic.ai/install-instructions)

### Community Resources
- [MCP with Le Chat Tutorial](https://remotebrowser.substack.com/p/mcp-with-le-chat-from-mistral)
- [Mistral MCP Hackathon Projects](https://github.com/Mistral-MCP-Hackathon-2025)
- [FastMCP Documentation](https://gofastmcp.com)

---

## ✅ VERIFICATION CHECKLIST

Before connecting to Mistral Le Chat:

- [x] MCP server running locally
- [x] Server responds to `/mcp` endpoint
- [x] Initialize request returns valid response
- [x] ngrok tunnel active and forwarding
- [x] Public URL accessible
- [x] Tools properly registered
- [x] Documentation complete
- [ ] Tested in Mistral Le Chat
- [ ] Demo video recorded

---

**Last Updated**: March 1, 2026
**Status**: Ready for Mistral Le Chat connection
**Current URL**: https://folksy-productively-delaine.ngrok-free.dev/mcp
**Recommended Next Step**: Deploy to ALPIC.ai for persistent URL
