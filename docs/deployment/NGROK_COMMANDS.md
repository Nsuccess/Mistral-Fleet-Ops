# 🌐 ngrok Quick Reference

Essential ngrok commands for your demo.

## 🚀 Basic Commands

### Start Tunnel (Most Common)
```powershell
ngrok http 3000
```
Creates a public HTTPS URL pointing to your local port 3000.

### With Custom Subdomain (Paid Plan Only)
```powershell
ngrok http 3000 --domain=your-name.ngrok.app
```

### With Region Selection
```powershell
ngrok http 3000 --region=us
# Options: us, eu, ap, au, sa, jp, in
```

---

## 🔧 Setup Commands

### Add Auth Token (One-Time Setup)
```powershell
ngrok config add-authtoken YOUR_TOKEN_HERE
```
Get your token from: https://dashboard.ngrok.com/get-started/your-authtoken

### Check Configuration
```powershell
ngrok config check
```

### View Current Config
```powershell
type %USERPROFILE%\.ngrok2\ngrok.yml
```

---

## 📊 Monitoring

### Web Interface
While ngrok is running, open: http://localhost:4040

**Features:**
- See all requests in real-time
- Inspect request/response details
- Replay requests
- View connection stats

### Status Check
```powershell
ngrok api tunnels list
```

---

## 🎯 Demo-Specific Commands

### Start for Demo (Recommended)
```powershell
# Simple and clean
ngrok http 3000
```

### Start with Custom Label
```powershell
ngrok http 3000 --log=stdout --log-level=info
```

### Start in Background (Advanced)
```powershell
start /B ngrok http 3000
```

---

## 🛑 Stop Commands

### Stop ngrok
Press `Ctrl+C` in the ngrok terminal

### Force Kill (If Frozen)
```powershell
taskkill /IM ngrok.exe /F
```

---

## 🔍 Troubleshooting Commands

### Check if Port is in Use
```powershell
netstat -ano | findstr :3000
```

### Kill Process on Port 3000
```powershell
# Find PID from netstat output, then:
taskkill /PID <PID> /F
```

### Test Local Server
```powershell
curl http://localhost:3000/healthz
```

### Test ngrok URL
```powershell
curl https://your-url.ngrok.io/healthz
```

---

## 📝 Common Issues & Fixes

### Issue: "Failed to listen on port 3000"
**Solution:**
```powershell
# Your MCP server isn't running
# Start it first:
python main.py
```

### Issue: "Account limit exceeded"
**Solution:**
- Free tier: 1 tunnel at a time
- Close other ngrok instances
- Or upgrade to paid plan

### Issue: "Invalid authtoken"
**Solution:**
```powershell
# Re-add your token
ngrok config add-authtoken YOUR_NEW_TOKEN
```

### Issue: "Connection refused"
**Solution:**
```powershell
# Check if MCP server is running
curl http://localhost:3000/healthz

# If not, start it:
python main.py
```

---

## 🎬 Demo Day Workflow

### Before Demo:
```powershell
# Terminal 1: Start MCP server
python main.py

# Terminal 2: Start ngrok
ngrok http 3000

# Copy the HTTPS URL from ngrok output
```

### During Demo:
- Keep both terminals visible (optional)
- Use the ngrok URL in Le Chat
- Monitor requests at http://localhost:4040

### After Demo:
```powershell
# Stop both (Ctrl+C in each terminal)
# Or use STOP_DEMO.bat
```

---

## 💡 Pro Tips

### 1. Keep URL Stable
Free tier gives you a new URL each time. To keep the same URL:
- Sign up for paid plan ($8/month)
- Or keep ngrok running during entire demo session

### 2. Monitor Traffic
Open http://localhost:4040 in browser to see:
- All requests from Le Chat
- Response times
- Any errors

### 3. Test Before Recording
```powershell
# Test the full flow:
curl https://your-ngrok-url.ngrok.io/healthz
# Should return: {"status": "ok"}
```

### 4. Backup Plan
If ngrok fails during demo:
- Have a pre-recorded video ready
- Or use localhost and explain the concept
- Or deploy to a real server beforehand

---

## 🔐 Security Notes

### Free Tier Security:
- ✅ HTTPS encryption
- ✅ Random subdomain (hard to guess)
- ⚠️ URL changes each restart
- ⚠️ Anyone with URL can access

### For Production:
- Use authentication
- Use paid plan with custom domain
- Implement rate limiting
- Monitor access logs

### For Demo:
- Free tier is fine
- Don't share URL publicly
- Stop ngrok after demo
- Don't use production credentials

---

## 📊 ngrok Free Tier Limits

| Feature | Limit |
|---------|-------|
| **Tunnels** | 1 at a time |
| **Connections** | Unlimited |
| **Requests/min** | 4,000 |
| **Duration** | No time limit |
| **HTTPS** | ✅ Included |
| **Custom Domain** | ❌ Paid only |
| **Reserved URLs** | ❌ Paid only |

**Perfect for demos!** ✅

---

## 🆘 Emergency Commands

### If Everything Breaks:
```powershell
# 1. Kill all ngrok processes
taskkill /IM ngrok.exe /F

# 2. Kill Python processes
taskkill /IM python.exe /F

# 3. Wait 5 seconds
timeout /t 5

# 4. Restart everything
python main.py
# (in new terminal)
ngrok http 3000
```

### If Port is Stuck:
```powershell
# Find what's using port 3000
netstat -ano | findstr :3000

# Kill that process
taskkill /PID <PID_NUMBER> /F

# Restart
python main.py
```

---

## 📚 Additional Resources

- **ngrok Dashboard:** https://dashboard.ngrok.com
- **Documentation:** https://ngrok.com/docs
- **Status Page:** https://status.ngrok.com
- **Community:** https://ngrok.com/slack

---

## ✅ Quick Checklist

Before starting your demo:

- [ ] ngrok installed
- [ ] Auth token added (optional but recommended)
- [ ] MCP server running on port 3000
- [ ] ngrok tunnel active
- [ ] HTTPS URL copied
- [ ] Le Chat configured
- [ ] Test deployment successful
- [ ] Web interface open (http://localhost:4040)

**You're ready to record!** 🎬

---

*Keep this file open during your demo for quick reference!*
