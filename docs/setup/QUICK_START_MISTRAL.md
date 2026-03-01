# 🚀 Quick Start: Mistral Le Chat

Get Blaxel Fleet Commander running with Mistral Le Chat in 5 minutes!

## ⚡ Fastest Path: Local Testing

### Step 1: Start the Server

```bash
# Make sure you're in the project directory
cd blaxel-fleet-commander

# Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Start HTTP server
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:3000
```

### Step 2: Configure Mistral Le Chat

1. Open [chat.mistral.ai](https://chat.mistral.ai)
2. Click Settings (gear icon)
3. Go to "MCP Servers" section
4. Click "Add Server"
5. Enter:
   - **Name:** Blaxel Fleet Commander
   - **URL:** `http://localhost:3000`
6. Click "Save"

### Step 3: Test It!

In Le Chat, try:

```
List my Blaxel sandboxes
```

or

```
Deploy https://github.com/Mistral-MCP-Hackathon-2025/mistral-jump.git to 2 sandboxes
```

**That's it!** 🎉

---

## 🌐 For Remote Access (ALPIC.ai)

### Step 1: Fork Repository

1. Go to your GitHub repository
2. Click "Fork" button
3. Fork to your account

### Step 2: Deploy to ALPIC.ai

1. Click this button (update with your username):
   
   [![Deploy on ALPIC.ai](https://img.shields.io/badge/Deploy-ALPIC.ai-ff69b4?style=for-the-badge)](https://alpic.ai/deploy?repo=https://github.com/YOUR_USERNAME/blaxel-fleet-commander)

2. Sign in to ALPIC.ai

3. Configure environment variables:
   ```
   BL_API_KEY=your-blaxel-api-key
   BL_WORKSPACE=your-workspace-name
   ```

4. Click "Deploy"

5. Wait for deployment (2-3 minutes)

6. Copy your public URL (e.g., `https://your-app.alpic.ai`)

### Step 3: Connect Le Chat

1. Open [chat.mistral.ai](https://chat.mistral.ai)
2. Settings → MCP Servers → Add Server
3. Enter:
   - **Name:** Blaxel Fleet Commander
   - **URL:** Your ALPIC.ai URL
4. Save and start using!

---

## 🎯 Example Commands

Once connected, try these in Le Chat:

### Basic Commands

```
List all my sandboxes
```

```
Check the latency to my sandboxes
```

### Deployment

```
Deploy https://github.com/user/my-app.git to 3 sandboxes
```

```
Deploy the Mistral Jump game to 2 sandboxes and give me the URLs
```

### Verification

```
Verify all my deployment URLs are still live
```

```
Check if https://my-sandbox.blaxel.app is responding
```

### Search (if RAG configured)

```
Find deployments that failed in the last 24 hours
```

```
Show me successful deployments from yesterday
```

---

## 🔧 Troubleshooting

### Server won't start

**Error:** `Address already in use`
```bash
# Port 3000 is taken, use different port
PORT=8000 python main.py
```

**Error:** `BL_API_KEY not found`
```bash
# Check .env file exists
cat .env  # macOS/Linux
type .env  # Windows

# Should contain:
BL_API_KEY=your-key
BL_WORKSPACE=your-workspace
```

### Le Chat can't connect

**Problem:** "Connection refused"
- ✅ Verify server is running: `curl http://localhost:3000/healthz`
- ✅ Check firewall allows port 3000
- ✅ For remote access, use public IP or domain

**Problem:** "Server not responding"
- ✅ Check server logs in terminal
- ✅ Restart server: `Ctrl+C` then `python main.py`
- ✅ Verify `.env` has valid credentials

### Tools not appearing

**Problem:** Le Chat doesn't show tools
- ✅ Refresh Le Chat browser tab
- ✅ Remove and re-add server in settings
- ✅ Check server logs for errors

---

## 📝 Environment Variables

### Required

```env
BL_API_KEY=your-blaxel-api-key
BL_WORKSPACE=your-workspace-name
```

Get these from [blaxel.ai](https://blaxel.ai)

### Optional (RAG Features)

```env
MISTRAL_API_KEY=your-mistral-key
QDRANT_URL=your-qdrant-url
QDRANT_API_KEY=your-qdrant-key
```

Without these, deployment tools still work perfectly!

### Optional (Observability)

```env
WANDB_API_KEY=your-wandb-key
```

Or disable:
```env
WEAVE_DISABLED=true
WANDB_DISABLED=true
```

---

## 🎓 Next Steps

### 1. Read Full Documentation

- [MISTRAL_SETUP.md](MISTRAL_SETUP.md) - Complete setup guide
- [TRANSPORT_COMPARISON.md](TRANSPORT_COMPARISON.md) - Technical details
- [README.md](README.md) - Full project documentation

### 2. Configure RAG (Optional)

Add semantic search capabilities:
```env
MISTRAL_API_KEY=your-key
QDRANT_URL=your-qdrant-url
QDRANT_API_KEY=your-key
```

Then try:
```
Find deployments that failed with npm errors
```

### 3. Deploy to Production

- Use ALPIC.ai for easy cloud deployment
- Or deploy to your own server
- Configure HTTPS for security
- Set up monitoring

---

## 💡 Tips

### Performance

- First deployment takes longer (downloads dependencies)
- Subsequent deployments are much faster
- Use parallel deployment for multiple sandboxes

### Security

- Never commit `.env` file
- Use firewall rules for HTTP server
- Rotate API keys regularly
- Use HTTPS in production

### Best Practices

- Test locally before deploying to cloud
- Monitor server logs for errors
- Keep dependencies updated
- Use semantic search to learn from past deployments

---

## 🆘 Need Help?

1. **Check logs:** Watch terminal output when running `python main.py`
2. **Test health:** `curl http://localhost:3000/healthz`
3. **Verify config:** Check `.env` file has all required variables
4. **Read docs:** See [MISTRAL_SETUP.md](MISTRAL_SETUP.md) for detailed troubleshooting

---

## 🎉 Success Checklist

- [ ] Server starts without errors
- [ ] Health check returns `{"status": "ok"}`
- [ ] Le Chat shows "Blaxel Fleet Commander" in MCP servers
- [ ] Can list sandboxes
- [ ] Can deploy an app
- [ ] Get live URLs with preview tokens

**All checked?** You're ready to deploy! 🚀

---

*Get started in 5 minutes, master it in an hour!*
