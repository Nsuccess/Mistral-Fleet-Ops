# 🚀 ALPIC.ai Deployment Guide

## Why ALPIC.ai? (Learned from Hackathon Winners)

Winning projects from Mistral-MCP-Hackathon-2025 used ALPIC.ai as their primary deployment platform. Here's why:

### Benefits
- ✅ **Persistent URLs** - No more changing URLs on restart
- ✅ **One-Click Deploy** - Connect GitHub and deploy in minutes
- ✅ **Auto-Deploy** - Pushes to your branch automatically deploy
- ✅ **Built-in Auth** - Handles OAuth and API key authentication
- ✅ **Monitoring** - Built-in logs and performance tracking
- ✅ **Transport Agnostic** - Converts stdio to SSE/HTTP automatically
- ✅ **Production Ready** - SSL, custom domains, and more

---

## 🎯 Quick Start (5 Minutes)

### Step 1: Sign Up
1. Go to https://app.alpic.ai
2. Sign in with your GitHub account
3. Create a Team (or join existing)

### Step 2: Connect Repository
1. Add ALPIC.ai app to your GitHub organization
2. Select organization: `your-github-username`
3. Choose repository: `Blaxel-Fleet-Commander-MCP-Server`
4. Grant necessary permissions

### Step 3: Configure Deployment
1. **Branch**: Select `main` (or your production branch)
2. **Environment Variables**: Add from your `.env` file:
   ```
   BLAXEL_API_KEY=your_key_here
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_key
   MISTRAL_API_KEY=your_mistral_key
   WANDB_API_KEY=your_wandb_key
   CONFIG=config.yaml
   ```

3. **Build Commands**: ALPIC auto-detects, but verify:
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Start command
   python main.py
   ```

### Step 4: Deploy
1. Click "Deploy" button
2. Wait for build to complete (usually 1-2 minutes)
3. Check build logs for any errors

### Step 5: Get Your URL
1. Go to project page
2. Copy your MCP server URL (format: `https://your-project.alpic.app/mcp`)
3. This URL is persistent and won't change!

---

## 🔧 Configuration Details

### Supported Languages
- ✅ Python (what we use)
- ✅ TypeScript/JavaScript
- 🔜 More coming soon

### Supported Frameworks
- ✅ FastMCP (what we use)
- ✅ MCP SDK
- ✅ Custom implementations

### Transport Handling
ALPIC automatically converts:
- `stdio` → SSE + HTTP streaming
- Keeps compatibility with new MCP transports
- No code changes needed!

---

## 🌍 Multiple Environments

ALPIC supports multiple deployment environments:

### Development
- Branch: `dev`
- URL: `https://your-project-dev.alpic.app/mcp`
- Auto-deploys on push to `dev`

### Staging
- Branch: `staging`
- URL: `https://your-project-staging.alpic.app/mcp`
- Auto-deploys on push to `staging`

### Production
- Branch: `main`
- URL: `https://your-project.alpic.app/mcp`
- Auto-deploys on push to `main`

---

## 🔐 Authentication

### Auto-Detection
ALPIC automatically detects your auth method:
- None (open access)
- API Key (Bearer token)
- OAuth 2.1 (user login)

### Configuration
Set in your MCP server code:
```python
# In src/server.py
mcp = FastMCP(
    "BLAXEL_FLEET_MCP",
    port=8000,
    debug=True,
    stateless_http=True,
    # Add auth config here if needed
)
```

ALPIC handles the rest!

---

## 📊 Monitoring & Logs

### Build Logs
- Real-time build output
- Error messages and warnings
- Deployment status

### Runtime Logs
- Server startup logs
- Request/response logs
- Error tracking
- Performance metrics

### Access Logs
- View from project dashboard
- Filter by time range
- Search for specific errors
- Export for analysis

---

## 🌐 Custom Domains

### Setup
1. Go to project settings
2. Click "Custom Domain"
3. Add your domain: `mcp.yourdomain.com`
4. Update DNS records as instructed
5. ALPIC handles SSL certificate automatically

### DNS Configuration
```
Type: CNAME
Name: mcp
Value: your-project.alpic.app
TTL: 3600
```

---

## 🔄 Deployment Workflow

### Automatic Deployment
```bash
# Make changes locally
git add .
git commit -m "Update Blaxel tools"
git push origin main

# ALPIC automatically:
# 1. Detects push to main branch
# 2. Pulls latest code
# 3. Runs build commands
# 4. Deploys new version
# 5. Updates live server (zero downtime)
```

### Manual Deployment
1. Go to project dashboard
2. Click "Deploy" button
3. Select branch to deploy
4. Confirm deployment

---

## 📱 Distribution

### MCP Install Instructions Generator
ALPIC provides a tool to generate installation instructions:

1. Go to https://alpic.ai/install-instructions
2. Enter your ALPIC URL
3. Get complete tutorial with:
   - Step-by-step instructions
   - Screenshots
   - One-click install links
   - Support for popular MCP clients

### Example Output
```markdown
# Install Blaxel Fleet Commander

## For Mistral Le Chat
1. Open https://chat.mistral.ai
2. Go to Intelligence → Connectors
3. Click "+ Add Connector"
4. Use URL: https://your-project.alpic.app/mcp

## For Claude Desktop
Add to config:
{
  "mcpServers": {
    "blaxel": {
      "url": "https://your-project.alpic.app/mcp"
    }
  }
}
```

---

## 💰 Pricing

Check current pricing at: https://alpic.ai/pricing

### Free Tier (if available)
- Limited deployments
- Basic monitoring
- Community support

### Paid Plans
- Unlimited deployments
- Advanced monitoring
- Priority support
- Custom domains
- Team collaboration

---

## 🆚 ALPIC vs ngrok

| Feature | ngrok | ALPIC.ai |
|---------|-------|----------|
| Setup | 2 min | 5 min |
| URL Persistence | ❌ | ✅ |
| Auto-Deploy | ❌ | ✅ |
| Authentication | Manual | ✅ Auto |
| Monitoring | Basic | ✅ Full |
| Custom Domain | 💰 Paid | ✅ Yes |
| Production | ❌ No | ✅ Yes |
| Best For | Testing | Production |

---

## 🎯 Recommended Strategy

### For Hackathon Demo
1. **Keep ngrok for local testing** - Fast iteration
2. **Deploy to ALPIC for submission** - Persistent URL
3. **Provide both in README** - Flexibility for judges

### For Production
1. **Use ALPIC exclusively** - Reliable and scalable
2. **Set up custom domain** - Professional appearance
3. **Enable monitoring** - Track usage and errors
4. **Configure authentication** - Secure access

---

## 🚀 Deploy Now!

### Quick Deploy Command
```bash
# 1. Commit your latest changes
git add .
git commit -m "Ready for ALPIC deployment"
git push origin main

# 2. Go to ALPIC
open https://app.alpic.ai

# 3. Follow the steps above
# 4. Get your persistent URL
# 5. Update Mistral Le Chat connector
```

---

## 📚 Resources

### Official Links
- **Platform**: https://app.alpic.ai
- **Documentation**: https://docs.alpic.ai
- **Blog**: https://alpic.ai/blog
- **Install Generator**: https://alpic.ai/install-instructions

### Support
- **Discord**: Join ALPIC community
- **Email**: support@alpic.ai
- **GitHub**: Report issues

### Examples
- **Mistral MCP Hackathon Winners**: https://github.com/Mistral-MCP-Hackathon-2025
- **Deploy Badge**: `[![Deploy on ALPIC.ai](https://img.shields.io/badge/Deploy-ALPIC.ai-ff69b4)](https://alpic.ai/deploy?repo=YOUR_REPO)`

---

## ✅ Deployment Checklist

Before deploying to ALPIC:

- [ ] Code is committed to GitHub
- [ ] `.env.example` file exists with all required variables
- [ ] `requirements.txt` or `package.json` is up to date
- [ ] `main.py` uses `streamable-http` transport
- [ ] Server runs successfully locally
- [ ] All tests pass
- [ ] Documentation is complete
- [ ] README has installation instructions

After deploying:

- [ ] Build completed successfully
- [ ] Server is running (check logs)
- [ ] MCP endpoint responds: `https://your-project.alpic.app/mcp`
- [ ] Tested connection from Mistral Le Chat
- [ ] Updated README with ALPIC URL
- [ ] Added deploy badge to README

---

## 🎉 Success!

Once deployed to ALPIC, you'll have:
- ✅ Persistent, production-ready MCP server
- ✅ Automatic deployments on git push
- ✅ Built-in monitoring and logs
- ✅ Professional URL for your project
- ✅ Easy distribution to users

**Your Blaxel Fleet Commander is now ready for the world!** 🚀

---

**Last Updated**: March 1, 2026
**Status**: Ready to deploy
**Recommended**: Deploy to ALPIC for hackathon submission
