# 🚀 Mistral Fleet Ops

> **Turn Mistral into a true deployment co-pilot.** From a simple prompt, you can provision sandboxes, deploy apps, or spin up entire fleets—instantly and in parallel. It works for both experts managing production environments and developers who hate DevOps. Your AI assistant understands your intent, executes in parallel, and keeps everything observable.

## What is Mistral Fleet Ops?

**Mistral Fleet Ops** transforms Mistral Le Chat into a true deployment co-pilot, solving one of the most persistent challenges in modern software delivery: the complexity barrier between human intent and live production URLs.

### The Problem We Solve

Whether you're a platform engineer managing hundreds of staging environments or a frontend developer who dreads anything beyond `npm start`, deployment has always been the same story: **tedious, error-prone, and time-consuming**.

You know what you want to achieve, but getting there means:
- Clicking through cloud consoles
- Managing SSH keys and credentials
- Writing YAML pipelines nobody understands
- Waiting for CI/CD queues
- Debugging cryptic build failures
- And worst of all—**doing everything sequentially, one environment at a time**

**What if you could simply describe what you want in natural language and have it deployed instantly across your entire fleet?**

### Our Solution

Mistral Fleet Ops is a **Model Context Protocol (MCP) server** that bridges the gap between natural language and cloud deployment. It transforms Mistral Le Chat into an actual operator for your infrastructure, enabling you to:

- **Provision cloud sandboxes** with simple prompts
- **Deploy any app** to any number of environments simultaneously
- **Get live URLs instantly**—preview tokens included, ready to share
- **Search deployment history** with natural language queries
- **Execute deployments in parallel**—spin up your entire fleet in seconds, not hours

### Key Innovation: Natural Language → Live Production URLs

The principle is beautifully simple:

1. **Configure** your Blaxel Cloud sandbox credentials once
2. **Describe** your deployment intent to Mistral Le Chat in natural language
3. **Mistral understands** and uses our MCP tools to execute
4. **Deployments run in parallel** across multiple sandboxes automatically
5. **Get live URLs** with preview tokens, ready to share with your team

### Built for Everyone

This isn't just for hardcore DevOps professionals. Thanks to our natural language interface, both seasoned infrastructure engineers and developers who prefer to avoid command lines can deploy apps with the same ease—**just by asking Mistral Le Chat**.

Mistral Fleet Ops makes cloud deployment dead-simple for Mistral Le Chat while keeping access control transparent and configuration-first, ensuring your infrastructure remains secure and manageable at scale.

---

## Highlights

- ⚡ **Parallel Deployment** — Deploy to N sandboxes simultaneously, not sequentially
- 🗣️ **Natural Language** — No YAML, no CLI, just describe what you want
- 🌐 **Instant Live URLs** — Automatic preview tokens, ready to share
- 🔍 **Semantic Search** — Find past deployments with natural language (LlamaIndex RAG)
- 📊 **Full Observability** — Tracing with Weave (Weights & Biases)
- 🛡️ **Graceful Degradation** — Logging failures never break deployments
- 🔧 **Zero Pipeline Config** — No CI/CD setup, no build scripts to maintain

---

## Quick Start

### MCP Client

Mistral Fleet Ops is built for:
- ✅ **Mistral Le Chat** (HTTP transport via ALPIC.ai)
- 🟣 [Mistral Le Chat Setup Guide](docs/setup/MISTRAL_SETUP.md)

---

### 1. Clone & Install

```bash
git clone https://github.com/Nsuccess/-Mistral-Fleet-Ops.git
cd mistral-fleet-ops

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -e .
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your API keys
```

**Required:**
```env
BL_API_KEY=your-blaxel-api-key
BL_WORKSPACE=your-workspace
```

**Optional (for RAG features):**
```env
MISTRAL_API_KEY=your-mistral-key
QDRANT_URL=your-qdrant-url
QDRANT_API_KEY=your-qdrant-key
```

### 4. Start Deploying!

**With Mistral Le Chat:**
See [MISTRAL_SETUP.md](docs/setup/MISTRAL_SETUP.md) for HTTP server setup, then open Mistral Le Chat and try:
> "Deploy https://github.com/user/my-react-app.git to 3 sandboxes"

---

**What happens next:**

Mistral Le Chat will:
1. ✅ Provision 3 Blaxel sandboxes in parallel
2. ✅ Clone your repository to each
3. ✅ Install dependencies (`npm ci`)
4. ✅ Build production bundles (`npm run build`)
5. ✅ Start servers on each sandbox
6. ✅ Return 3 live URLs with preview tokens

**All in under 60 seconds.**



---

## MCP Tools

### Deployment Tools

| Tool | Description |
|------|-------------|
| `fleet_provision_sandbox` | Create a new Blaxel cloud sandbox |
| `fleet_check_latency` | Measure network latency to a sandbox |
| `fleet_clone_repo` | Clone a GitHub repository to a sandbox |
| `fleet_install_deps` | Install npm dependencies |
| `fleet_build_app` | Build production bundle |
| `fleet_start_server` | Start server and get live URL |
| `fleet_deploy_game` | All-in-one: deploy to N sandboxes in parallel |
| `fleet_list_sandboxes` | List all available sandboxes with status |
| `fleet_verify_live` | Verify URLs are responding (health check) |

### RAG Tools (Semantic Search)

| Tool | Description |
|------|-------------|
| `fleet_search_logs` | Search deployment history with natural language |
| `fleet_suggest_fix` | Get AI-powered fix suggestions from successful deployments |

---

## Usage Examples

### Deploy to Multiple Environments

```
User: I want to deploy https://github.com/Nsuccess/mcp-leap.git to 2 VMs. Please do it step by step:
1. Provision 2 sandboxes
2. Check latency on each
3. Clone repo and install dependencies on each
4. Build the app on each
5. Start the server on each and give me the URLs
6. Verify the URLs are live with 200 OK

Show me each step as you do it.

Mistral: I'll deploy your app to 2 Blaxel sandboxes in parallel...

🚀 Provisioning sandboxes...
📦 Cloning repository...
📚 Installing dependencies...
🔨 Building production bundles...
🌐 Starting servers...

✅ Deployment complete! Here are your live URLs:
• VM 1: https://fleet-abc123.blaxel.app?token=...
• VM 2: https://fleet-def456.blaxel.app?token=...

All 2 deployments completed in 47 seconds.
```

### Search Deployment History

```
User: Find deployments that failed with npm errors in the last 24 hours

Mistral: [Uses fleet_search_logs with semantic search]

Found 3 matching deployments:
1. fleet-xyz (2 hours ago)
   Error: "npm ERR! peer dep missing: react@^18.0.0"
2. fleet-abc (6 hours ago)
   Error: "npm ERR! ERESOLVE unable to resolve dependency tree"
3. fleet-def (yesterday)
   Error: "npm ERR! code ENOENT"
```

### Get Fix Suggestions

```
User: How do I fix the ERESOLVE dependency error?

Mistral: [Uses fleet_suggest_fix powered by RAG]

Based on 12 successful deployments with similar issues, here are fixes:
1. Use legacy peer deps: `npm install --legacy-peer-deps`
2. Update package.json to use compatible versions
3. Delete package-lock.json and reinstall

The most successful approach (89% success rate) was option 1.
```

### Quick Health Check

```
User: Are all my deployments still running?

Mistral: [Uses fleet_verify_live]

Checking 3 URLs...
✅ fleet-abc123: 200 OK (latency: 45ms)
✅ fleet-def456: 200 OK (latency: 52ms)
❌ fleet-ghi789: 502 Bad Gateway

1 deployment needs attention. Would you like me to redeploy fleet-ghi789?
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Mistral Le Chat                           │
│                    (MCP Client)                             │
│                                                             │
│   "Deploy my app to 5 sandboxes"                           │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP / JSON-RPC
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Mistral Fleet Ops                              │
│                  (MCP Server)                               │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Deployment │  │    RAG      │  │    Observability    │  │
│  │    Tools    │  │   Tools     │  │      (Weave)        │  │
│  │             │  │             │  │                     │  │
│  │ • Provision │  │ • Search    │  │ • Trace all calls   │  │
│  │ • Clone     │  │ • Suggest   │  │ • Log deployments   │  │
│  │ • Build     │  │             │  │                     │  │
│  │ • Serve     │  │             │  │                     │  │
│  └──────┬──────┘  └──────┬──────┘  └─────────────────────┘  │
└─────────┼────────────────┼──────────────────────────────────┘
          │                │
          ▼                ▼
┌─────────────────┐  ┌─────────────────────────────────────────┐
│  Blaxel Cloud   │  │           LlamaIndex RAG                │
│   Sandboxes     │  │                                         │
│                 │  │  ┌─────────────┐  ┌─────────────────┐   │
│  Parallel       │  │  │   Mistral   │  │     Qdrant      │   │
│  Provisioning   │  │  │  Embeddings │  │   Vector DB     │   │
│  & Deployment   │  │  │  (1024 dim) │  │                 │   │
│                 │  │  └─────────────┘  └─────────────────┘   │
└─────────────────┘  └─────────────────────────────────────────┘
```

---

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `BL_API_KEY` | ✅ | Blaxel API key for sandbox provisioning |
| `BL_WORKSPACE` | ✅ | Blaxel workspace name |
| `MISTRAL_API_KEY` | ❌ | Mistral AI key for embeddings (RAG) |
| `QDRANT_URL` | ❌ | Qdrant endpoint for vector storage (RAG) |
| `QDRANT_API_KEY` | ❌ | Qdrant API key (RAG) |
| `WANDB_API_KEY` | ❌ | Weights & Biases key for tracing |
| `GITHUB_TOKEN` | ❌ | GitHub token for private repositories |

### Notes

- If RAG variables are missing, deployment tools still work perfectly
- Logging failures never break deployments (graceful degradation)
- All credentials are stored in `.env` (never committed to git)

---

## Project Structure

```
├── src/
│   ├── blaxel/                 # Blaxel cloud integration (deployment tools)
│   │   ├── tools.py            # fleet_deploy_game, fleet_list_sandboxes
│   │   ├── granular_tools.py   # Step-by-step deployment tools
│   │   └── types.py            # Type definitions
│   ├── qdrant/                 # LlamaIndex RAG system
│   │   ├── llamaindex_manager.py   # Production RAG pipeline
│   │   └── llamaindex_tools.py     # fleet_search_logs, fleet_suggest_fix
│   ├── config/                 # Configuration management
│   │   ├── manager.py          # YAML config loader
│   │   └── permissions.py      # Access control
│   └── server.py               # MCP server (HTTP transport)
│
├── main.py                     # Mistral Le Chat entry point
├── config.yaml                 # Blaxel sandbox configuration
├── .env.example                # Environment template
├── pyproject.toml              # Dependencies
└── README.md
```

---

## Troubleshooting

### MCP Server Not Connecting

1. Verify your HTTP server is running and accessible via ngrok
2. Ensure virtual environment has all dependencies: `pip install -e .`
3. Check `.env` file exists with valid `BL_API_KEY` and `BL_WORKSPACE`
4. See [MISTRAL_SETUP.md](docs/setup/MISTRAL_SETUP.md) for detailed connection guide

### Deployment Failures

1. Verify your Blaxel API key is valid and not expired
2. Check that the GitHub repository is public (or provide `GITHUB_TOKEN`)
3. Ensure the repo has a valid `package.json` with `build` script

### RAG Features Not Working

1. Add `MISTRAL_API_KEY`, `QDRANT_URL`, and `QDRANT_API_KEY` to `.env`
2. Deployments still work without RAG—it's completely optional
3. Check Qdrant instance is accessible from your network

### Slow Startup

1. First run downloads LlamaIndex models—subsequent runs are faster
2. Set `WEAVE_DISABLED=true` in `.env` to skip observability setup

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| MCP Server | FastMCP | Tool registration & transport |
| Cloud Sandboxes | Blaxel | Instant VM provisioning |
| RAG Framework | LlamaIndex | Semantic search pipeline |
| Embeddings | Mistral AI | 1024-dimensional vectors |
| Vector Database | Qdrant | Fast similarity search |
| Observability | Weave (W&B) | Tracing & debugging |

---

## Why Mistral Fleet Ops?

| Traditional Deployment | Mistral Fleet Ops |
|------------------------|-----------------|
| Write YAML pipelines | Just ask Mistral |
| Click through consoles | Natural language |
| Deploy one at a time | Parallel execution |
| Wait for CI/CD queues | Instant provisioning |
| Debug cryptic errors | AI-powered suggestions |
| Manage SSH keys | Zero credential management |

---

## License

MIT

---

## Acknowledgments

Built with ❤️ for the **Mistral MCP Hackathon** 🎂

### Technologies 
- [Blaxel](https://blaxel.ai) — Cloud sandbox infrastructure 
- [Mistral AI](https://mistral.ai) — Embeddings & AI
- [LlamaIndex](https://llamaindex.ai) — Production RAG framework
- [Qdrant](https://qdrant.tech) — Vector database
- [Weights & Biases](https://wandb.ai) — Observability platform

### Team
- **[Nsuccess](https://github.com/Nsuccess)** — Solo developer

---

