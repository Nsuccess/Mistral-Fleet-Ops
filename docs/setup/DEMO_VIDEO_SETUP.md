# 🎬 Demo Video Setup Guide

Complete step-by-step guide to record your Blaxel Fleet Commander demo with Mistral Le Chat using ngrok.

## ✅ Prerequisites Checklist

- [x] ngrok installed (you just did this!)
- [ ] .env file configured with Blaxel credentials
- [ ] Virtual environment activated
- [ ] Dependencies installed

---

## 🚀 Quick Setup (5 Minutes)

### Step 1: Verify Your Environment

```powershell
# Navigate to your project
cd "C:\Users\NewUserName\Desktop\Blaxel Fleet Commander MCP Server"

# Activate virtual environment
.venv\Scripts\activate

# Verify .env file exists and has required variables
type .env
```

**Required in .env:**
```env
BL_API_KEY=your-blaxel-api-key
BL_WORKSPACE=your-workspace-name
```

---

### Step 2: Sign Up for ngrok (Optional but Recommended)

**Why?** Removes banner, gives you better limits, and allows reconnection.

1. Go to [ngrok.com/signup](https://ngrok.com/signup)
2. Sign up (free account)
3. Copy your authtoken from dashboard
4. Run in PowerShell (admin):

```powershell
ngrok config add-authtoken YOUR_TOKEN_HERE
```

**Skip this if you want to start immediately** - ngrok works without signup too!

---

### Step 3: Start Your MCP Server

**Terminal 1 (PowerShell - Regular):**

```powershell
# Navigate to project
cd "C:\Users\NewUserName\Desktop\Blaxel Fleet Commander MCP Server"

# Activate virtual environment
.venv\Scripts\activate

# Start the MCP server
python main.py
```

**Expected output:**
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:3000 (Press CTRL+C to quit)
```

✅ **Leave this terminal running!**

---

### Step 4: Expose with ngrok

**Terminal 2 (PowerShell - Admin):**

```powershell
# Start ngrok tunnel
ngrok http 3000
```

**Expected output:**
```
ngrok                                                                    

Session Status                online
Account                       your-email@example.com (Plan: Free)
Version                       3.36.1
Region                        United States (us)
Latency                       45ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123.ngrok.io -> http://localhost:3000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

🎯 **Copy the HTTPS URL** (e.g., `https://abc123.ngrok.io`)

✅ **Leave this terminal running too!**

---

### Step 5: Configure Mistral Le Chat

1. Open [chat.mistral.ai](https://chat.mistral.ai) in your browser
2. Click **Settings** (gear icon, top right)
3. Go to **"MCP Servers"** section
4. Click **"Add Server"**
5. Fill in:
   - **Name:** `Blaxel Fleet Commander`
   - **URL:** Paste your ngrok URL (e.g., `https://abc123.ngrok.io`)
6. Click **"Save"**
7. Refresh the page

---

### Step 6: Verify Connection

In Le Chat, type:
```
List my available tools
```

**Expected response:**
Le Chat should show all your MCP tools:
- fleet_deploy_game
- fleet_list_sandboxes
- fleet_verify_live
- etc.

✅ **If you see the tools, you're ready to record!**

---

## 🎥 Demo Video Script

### Scene 1: Introduction (30 seconds)

**Show on screen:**
- Your project folder
- README.md open

**Say:**
> "Hi! I'm going to show you Blaxel Fleet Commander - an MCP server that lets you deploy apps to cloud sandboxes using natural language with Mistral Le Chat."

---

### Scene 2: Show the Setup (30 seconds)

**Show Terminal 1:**
```powershell
python main.py
# Server running on port 3000
```

**Show Terminal 2:**
```powershell
ngrok http 3000
# Highlight the public URL
```

**Say:**
> "I've started the MCP server locally and exposed it with ngrok. Now I can connect Mistral Le Chat to this public URL."

---

### Scene 3: Configure Le Chat (30 seconds)

**Screen record:**
1. Open chat.mistral.ai
2. Settings → MCP Servers
3. Add server with ngrok URL
4. Show tools appearing

**Say:**
> "I'll add the server to Mistral Le Chat. Once connected, Le Chat can see all the deployment tools."

---

### Scene 4: Deploy an App (2 minutes)

**In Le Chat, type:**
```
Deploy https://github.com/Mistral-MCP-Hackathon-2025/mistral-jump.git to 2 Blaxel sandboxes
```

**Show:**
- Le Chat understanding the request
- Parallel deployment happening
- Progress updates
- Live URLs with preview tokens returned

**Say:**
> "Watch as Le Chat deploys the Mistral Jump game to 2 sandboxes in parallel. It clones the repo, installs dependencies, builds the app, and starts the servers - all automatically."

---

### Scene 5: Verify Deployments (1 minute)

**In Le Chat, type:**
```
Verify all my deployment URLs are live
```

**Show:**
- Health check running
- Status codes (200 OK)
- Latency measurements

**Then click one of the URLs to show the live app**

**Say:**
> "Let's verify the deployments are working. Both sandboxes are live and responding. Here's the actual deployed game running in the cloud."

---

### Scene 6: Show Parallel Power (1 minute)

**In Le Chat, type:**
```
List all my sandboxes with their latency
```

**Show:**
- Multiple sandboxes listed
- Latency measurements
- Status information

**Say:**
> "The real power is parallel deployment. I can deploy to multiple environments simultaneously, not one at a time like traditional CI/CD."

---

### Scene 7: Conclusion (30 seconds)

**Show:**
- Both terminals still running
- Le Chat with successful deployments
- Live URLs

**Say:**
> "That's Blaxel Fleet Commander - natural language deployment to cloud sandboxes via MCP. No YAML, no pipelines, just describe what you want and it happens. Thanks for watching!"

---

## 📋 Pre-Recording Checklist

### Before You Start Recording:

- [ ] Both terminals running (MCP server + ngrok)
- [ ] ngrok URL copied
- [ ] Le Chat configured and showing tools
- [ ] Test deployment works (do a practice run!)
- [ ] Close unnecessary browser tabs
- [ ] Close unnecessary applications
- [ ] Set Windows to "Do Not Disturb" mode
- [ ] Prepare a test repository URL
- [ ] Have your script/talking points ready

### Screen Recording Settings:

- [ ] Use OBS Studio or Windows Game Bar (Win+G)
- [ ] Record at 1920x1080 (1080p)
- [ ] 30 FPS is fine
- [ ] Include system audio if you're narrating
- [ ] Test recording 10 seconds first

---

## 🎯 Demo Commands to Use

### Command 1: Basic Deployment
```
Deploy https://github.com/Mistral-MCP-Hackathon-2025/mistral-jump.git to 2 sandboxes
```

### Command 2: List Sandboxes
```
List all my Blaxel sandboxes with their status and latency
```

### Command 3: Verify URLs
```
Verify these URLs are live: [paste URLs from deployment]
```

### Command 4: Show Tools
```
What deployment tools do you have access to?
```

---

## 🐛 Troubleshooting During Demo

### If MCP Server Crashes:
```powershell
# Terminal 1: Restart server
python main.py
```
ngrok URL stays the same, no need to reconfigure Le Chat!

### If ngrok Disconnects:
```powershell
# Terminal 2: Restart ngrok
ngrok http 3000
```
You'll get a NEW URL - need to update Le Chat settings.

### If Le Chat Doesn't Show Tools:
1. Refresh the browser page
2. Remove and re-add the server
3. Check both terminals are running
4. Verify ngrok URL is correct

### If Deployment Fails:
- Check .env has valid BL_API_KEY and BL_WORKSPACE
- Verify Blaxel account has credits
- Try a different repository (use Mistral Jump as backup)

---

## 💡 Pro Tips for Great Demo

### 1. Practice First!
Run through the entire demo 2-3 times before recording.

### 2. Keep It Simple
Don't try to show every feature - focus on the core value:
- Natural language → Parallel deployment → Live URLs

### 3. Show Real Results
Actually click the deployed URLs to show the apps working.

### 4. Explain the Value
Emphasize:
- No YAML pipelines
- No CI/CD setup
- Parallel execution
- Instant results

### 5. Have a Backup Plan
If something fails:
- Have a pre-deployed URL ready to show
- Can show the code/architecture instead
- Explain what should happen

---

## 🎬 Recording Tools

### Option 1: OBS Studio (Recommended)
- Free and professional
- Download: [obsproject.com](https://obsproject.com)
- Best quality and control

### Option 2: Windows Game Bar
- Built into Windows 10/11
- Press `Win + G` to start
- Quick and easy

### Option 3: Screen Recording Software
- Camtasia (paid)
- Bandicam (paid)
- ShareX (free)

---

## 📤 After Recording

### 1. Edit Your Video
- Trim dead space at start/end
- Add title card (optional)
- Add captions (optional)
- Speed up slow parts (optional)

### 2. Export Settings
- Format: MP4
- Resolution: 1920x1080
- Bitrate: 5-10 Mbps
- Frame rate: 30 FPS

### 3. Upload
- YouTube (unlisted or public)
- Vimeo
- Loom
- Direct file for submission

---

## 🔄 Quick Reset Between Takes

If you need to record multiple takes:

```powershell
# Keep both terminals running!
# Just refresh Le Chat and start over
# ngrok URL stays the same
```

No need to restart anything unless something crashes.

---

## ✅ Final Checklist Before Recording

- [ ] MCP server running (Terminal 1)
- [ ] ngrok running (Terminal 2)
- [ ] Le Chat configured and showing tools
- [ ] Test deployment successful
- [ ] Screen recording software ready
- [ ] Microphone tested (if narrating)
- [ ] Script/talking points prepared
- [ ] Notifications disabled
- [ ] Clean desktop/browser
- [ ] Good lighting (if showing face)

---

## 🎉 You're Ready!

**Current Status:**
- ✅ ngrok installed
- ✅ MCP server code ready
- ✅ Setup guide complete

**Next Steps:**
1. Configure your .env file
2. Start both terminals
3. Configure Le Chat
4. Practice once
5. Record!

**Estimated Time:**
- Setup: 5 minutes
- Practice: 10 minutes
- Recording: 5-10 minutes
- Total: ~25 minutes

---

## 🆘 Need Help?

**Check these if something goes wrong:**

1. **Server won't start:**
   - Verify .env file exists
   - Check BL_API_KEY is valid
   - Ensure port 3000 is free

2. **ngrok won't connect:**
   - Run as administrator
   - Check internet connection
   - Try different port: `ngrok http 8000`

3. **Le Chat can't connect:**
   - Verify ngrok URL is HTTPS
   - Check both terminals running
   - Try removing and re-adding server

4. **Deployment fails:**
   - Check Blaxel credentials
   - Verify repository is public
   - Try Mistral Jump repo as backup

---

**Good luck with your demo! 🚀**

*Remember: The best demos are simple, clear, and show real value. You've got this!*
