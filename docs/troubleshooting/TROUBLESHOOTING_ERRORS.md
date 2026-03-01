# 🔧 Troubleshooting Common Errors

## ❌ Error Messages You Saw

### 1. "404 Not Found" Errors

```
INFO:     127.0.0.1:49171 - "GET /sse HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:49195 - "POST / HTTP/1.1" 404 Not Found
```

**Cause**: Testing wrong endpoints
**Solution**: Use `/mcp` endpoint, not `/sse` or `/`

**Correct endpoint**: `http://localhost:8000/mcp`

---

### 2. "406 Not Acceptable" Error

```
INFO:     127.0.0.1:49234 - "POST /mcp HTTP/1.1" 406 Not Acceptable
```

**Cause**: Missing required Accept headers
**Solution**: Include both content types in Accept header

**Required headers**:
```http
Content-Type: application/json
Accept: application/json, text/event-stream
```

**Why**: FastMCP's streamable-http needs to know the client accepts both JSON responses and Server-Sent Events (SSE) for streaming.

---

### 3. "421 Misdirected Request" - Invalid Host Header ⚠️ CRITICAL

```
[3/1/2026 1:17:32 PM] WARNING  Invalid Host header: folksy-productively-delaine.ngrok-free.dev
INFO:     197.215.26.122:0 - "POST /mcp HTTP/1.1" 421 Misdirected Request
```

**Cause**: FastMCP validates the Host header for security. ngrok sends its own domain (`folksy-productively-delaine.ngrok-free.dev`) but FastMCP expects `localhost:8000`.

**Solution**: Use ngrok's `--host-header` flag to rewrite the Host header

**WRONG**:
```bash
ngrok http 8000
```

**CORRECT**:
```bash
ngrok http 8000 --host-header="localhost:8000"
```

**Why this works**:
- ngrok receives requests with Host: `folksy-productively-delaine.ngrok-free.dev`
- `--host-header` flag rewrites it to Host: `localhost:8000`
- FastMCP accepts the request because it sees the expected host

---

## ✅ Verification Tests

### Test 1: Local Endpoint
```bash
curl http://localhost:8000/mcp -Method POST -Headers @{"Content-Type"="application/json";"Accept"="application/json, text/event-stream"} -Body '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}'
```

**Expected**: `200 OK` with MCP initialize response

### Test 2: ngrok Public Endpoint
```bash
curl https://folksy-productively-delaine.ngrok-free.dev/mcp -Method POST -Headers @{"Content-Type"="application/json";"Accept"="application/json, text/event-stream";"ngrok-skip-browser-warning"="true"} -Body '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}'
```

**Expected**: `200 OK` with MCP initialize response

---

## 🔍 Understanding FastMCP Security

### Host Header Validation

FastMCP validates the Host header to prevent **DNS rebinding attacks**. This is a security feature, not a bug.

**What is DNS rebinding?**
- Attacker tricks your browser into making requests to localhost
- Without Host validation, malicious sites could access your local MCP server
- FastMCP blocks requests with unexpected Host headers

**Why ngrok triggers this:**
- ngrok URL: `https://folksy-productively-delaine.ngrok-free.dev`
- Browser sends: `Host: folksy-productively-delaine.ngrok-free.dev`
- FastMCP expects: `Host: localhost:8000`
- Result: Request blocked

**The fix:**
```bash
ngrok http 8000 --host-header="localhost:8000"
```
This tells ngrok to rewrite the Host header before forwarding to your server.

---

## 🚨 Other Common Errors

### Port Already in Use
```
ERROR: [Errno 10048] error while attempting to bind on address ('127.0.0.1', 8000)
```

**Solution**:
```bash
# Find process using port 8000
netstat -ano | Select-String ":8000"

# Kill the process
Stop-Process -Id <PID> -Force

# Or change port in src/server.py
mcp = FastMCP("BLAXEL_FLEET_MCP", port=8001, ...)
```

---

### ngrok Connection Refused
```
ERROR: Failed to connect to localhost:8000
```

**Solution**:
1. Make sure MCP server is running first
2. Check server is on correct port
3. Test local endpoint before starting ngrok

---

### Mistral Le Chat Can't Connect
```
Connection failed: Unable to reach server
```

**Checklist**:
- [ ] MCP server running (`python main.py`)
- [ ] ngrok tunnel active with `--host-header` flag
- [ ] Test endpoint manually (see Verification Tests above)
- [ ] Check server logs for errors
- [ ] Verify URL includes `/mcp` at the end

---

## 📊 Expected Server Logs (Healthy)

```
wandb: Currently logged in as: successnwachukwu563
weave: View Weave data at https://wandb.ai/...
INFO:     Using local config at config.yaml
INFO:     Started server process [1648]
INFO:     StreamableHTTP session manager started
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     127.0.0.1:49245 - "POST /mcp HTTP/1.1" 200 OK  ✅
```

**Good signs**:
- ✅ `200 OK` responses
- ✅ No "Invalid Host header" warnings
- ✅ No "404 Not Found" errors
- ✅ No "406 Not Acceptable" errors

---

## 🛠️ Debug Commands

### Check Server Status
```bash
# Test local endpoint
curl http://localhost:8000/mcp

# Check if server is listening
netstat -ano | Select-String ":8000"

# View server logs
# (Check Terminal 18 or wherever python main.py is running)
```

### Check ngrok Status
```bash
# View ngrok web interface
start http://127.0.0.1:4040

# Check ngrok API
curl http://127.0.0.1:4040/api/tunnels | ConvertFrom-Json

# View ngrok logs
# (Check Terminal 19 or wherever ngrok is running)
```

### Test MCP Protocol
```bash
# Initialize request (should return server capabilities)
curl http://localhost:8000/mcp -Method POST `
  -Headers @{"Content-Type"="application/json";"Accept"="application/json, text/event-stream"} `
  -Body '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}'

# List tools request (should return available tools)
curl http://localhost:8000/mcp -Method POST `
  -Headers @{"Content-Type"="application/json";"Accept"="application/json, text/event-stream"} `
  -Body '{"jsonrpc":"2.0","method":"tools/list","params":{},"id":2}'
```

---

## 🔄 Restart Everything (Clean Slate)

```bash
# 1. Stop everything
.\STOP_DEMO.bat

# 2. Wait 5 seconds
timeout /t 5

# 3. Start with correct configuration
# Terminal 1: Start MCP Server
python main.py

# Terminal 2: Start ngrok with host header fix
ngrok http 8000 --host-header="localhost:8000"

# 4. Test local endpoint
curl http://localhost:8000/mcp

# 5. Test public endpoint
curl https://your-ngrok-url.ngrok-free.dev/mcp
```

---

## 📚 Related Documentation

- `NGROK_COMMANDS.md` - ngrok command reference
- `QUICK_REFERENCE.md` - Quick troubleshooting guide
- `MISTRAL_LECHAT_CONNECTION_GUIDE.md` - Connection instructions
- `CONNECTION_INFO.txt` - Current connection details

---

## ✅ Success Indicators

You know everything is working when:

1. **Local test passes**:
   ```
   curl http://localhost:8000/mcp
   → 200 OK with MCP response
   ```

2. **Public test passes**:
   ```
   curl https://your-url.ngrok-free.dev/mcp
   → 200 OK with MCP response
   ```

3. **Server logs show**:
   ```
   INFO: 127.0.0.1:XXXXX - "POST /mcp HTTP/1.1" 200 OK
   ```

4. **No error messages**:
   - ❌ No "Invalid Host header"
   - ❌ No "404 Not Found"
   - ❌ No "406 Not Acceptable"
   - ❌ No "421 Misdirected Request"

5. **Mistral Le Chat connects successfully**

---

## 🎯 Quick Fix Summary

**Problem**: "Invalid Host header" error with ngrok
**Solution**: Add `--host-header="localhost:8000"` flag

**Before**:
```bash
ngrok http 8000  ❌
```

**After**:
```bash
ngrok http 8000 --host-header="localhost:8000"  ✅
```

**That's it!** This single flag fixes the 421 Misdirected Request error.

---

**Last Updated**: March 1, 2026
**Status**: All errors resolved ✅
**ngrok Command**: `ngrok http 8000 --host-header="localhost:8000"`
