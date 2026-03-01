# 🗄️ Qdrant Setup Guide

Your Qdrant cluster is now configured! This guide explains what it does and how to use it.

## ✅ Current Configuration

**Cluster Name:** nils  
**Region:** europe-west3-0 (GCP - Belgium)  
**Endpoint:** `https://990b02e3-be8f-4c36-afb1-6d529ab3b7c9.europe-west3-0.gcp.cloud.qdrant.io`  
**Status:** ✅ Configured in `.env`

---

## 🎯 What Qdrant Does

Qdrant is a **vector database** that powers the RAG (Retrieval-Augmented Generation) features in Blaxel Fleet Commander.

### Features Enabled:

1. **Semantic Search** - Find deployments using natural language
   ```
   "Find deployments that failed with npm errors"
   "Show me successful deployments from yesterday"
   ```

2. **AI-Powered Suggestions** - Get fix recommendations
   ```
   "How do I fix the ERESOLVE dependency error?"
   "Suggest solutions for build failures"
   ```

3. **Deployment Analytics** - Track patterns and insights
   - Success/failure rates
   - Common errors
   - Performance metrics

---

## 📊 How It Works

```
Deployment happens
    ↓
Logs captured (command, stdout, stderr)
    ↓
Mistral creates embeddings (1024 dimensions)
    ↓
Stored in Qdrant (3 collections)
    ↓
Searchable with natural language
```

### Collections Created:

1. **`ssh_commands`** - Commands executed
2. **`ssh_stdout`** - Command outputs
3. **`ssh_stderr`** - Error messages

*Note: Collections are created automatically on first deployment*

---

## 🧪 Test Your Setup

### Quick Test:

```bash
# Activate virtual environment
.venv\Scripts\activate

# Run test script
python test_qdrant.py
```

**Expected output:**
```
✅ Connected successfully!
Cluster: nils (europe-west3-0.gcp)
Collections: 0
No collections yet (will be created on first use)
```

### Manual Test:

```python
from qdrant_client import QdrantClient
import os

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

# Check connection
collections = client.get_collections()
print(f"Connected! Collections: {len(collections.collections)}")
```

---

## 🚀 Using RAG Features

### After Your First Deployment:

Once you deploy an app, logs are automatically indexed. Then you can:

**1. Search Deployment History:**
```
In Le Chat: "Find all deployments from the last 24 hours"
```

**2. Find Errors:**
```
In Le Chat: "Show me deployments that failed with build errors"
```

**3. Get Suggestions:**
```
In Le Chat: "How do I fix npm dependency conflicts?"
```

**4. Analyze Patterns:**
```
In Le Chat: "What are the most common deployment errors?"
```

---

## 📈 Monitoring Your Cluster

### Qdrant Cloud Dashboard:

1. Go to [cloud.qdrant.io](https://cloud.qdrant.io)
2. Sign in
3. Select cluster "nils"
4. View:
   - Storage usage
   - Request metrics
   - Collection details
   - API usage

### Check Collections:

```python
from qdrant_client import QdrantClient
import os

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

# List all collections
collections = client.get_collections()
for col in collections.collections:
    print(f"{col.name}: {col.vectors_count} vectors")
```

---

## 🔧 Configuration Details

### Environment Variables:

```env
# Qdrant Cloud (cluster: nils)
QDRANT_URL=https://990b02e3-be8f-4c36-afb1-6d529ab3b7c9.europe-west3-0.gcp.cloud.qdrant.io
QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.eM3MFtGG0o9suC1eHdFm5Ojhxiu2AOwfM8Hq2W9iOro

# Mistral (for embeddings)
MISTRAL_API_KEY=your-mistral-key
```

### Collection Schema:

**ssh_commands:**
- Vector size: 1024 (Mistral embeddings)
- Distance: Cosine similarity
- Payload: job_id, host, user, command, timestamp, return_code

**ssh_stdout:**
- Vector size: 1024
- Payload: job_id, host, user, command, stdout, timestamp, return_code

**ssh_stderr:**
- Vector size: 1024
- Payload: job_id, host, user, command, stderr, timestamp, return_code

---

## 💡 Pro Tips

### 1. Graceful Degradation
If Qdrant is down, deployments still work! Logging failures never break deployments.

### 2. Search Optimization
More deployments = better search results. The system learns from your patterns.

### 3. Cost Management
Qdrant free tier includes:
- 1 GB storage
- Unlimited requests
- Perfect for demos and small projects

### 4. Data Privacy
Your deployment logs stay in your Qdrant cluster. Not shared with anyone.

---

## 🐛 Troubleshooting

### Connection Failed

**Error:** `Connection refused` or `Timeout`

**Solutions:**
1. Check internet connection
2. Verify QDRANT_URL is correct (no trailing slash)
3. Check firewall settings
4. Verify API key is correct

**Test:**
```bash
curl https://990b02e3-be8f-4c36-afb1-6d529ab3b7c9.europe-west3-0.gcp.cloud.qdrant.io
```

### Authentication Failed

**Error:** `Unauthorized` or `Invalid API key`

**Solutions:**
1. Check QDRANT_API_KEY in .env
2. Verify no extra spaces in API key
3. Regenerate API key in Qdrant dashboard if needed

### Collections Not Created

**Issue:** No collections after deployment

**Solutions:**
1. Check MISTRAL_API_KEY is set (needed for embeddings)
2. Verify deployment completed successfully
3. Check server logs for errors
4. Run `python test_qdrant.py` to verify connection

### Embeddings Failed

**Error:** `Mistral API error`

**Solutions:**
1. Check MISTRAL_API_KEY is valid
2. Verify Mistral API quota
3. Check internet connection
4. See Mistral API status page

---

## 🔐 Security Notes

### API Key Security:
- ✅ Stored in .env (git-ignored)
- ✅ Never commit to repository
- ✅ Rotate regularly
- ✅ Use separate keys for dev/prod

### Access Control:
- Your API key has full access to cluster "nils"
- Don't share API key publicly
- Regenerate if compromised

### Data Privacy:
- Deployment logs stored in your cluster
- Not accessible to others
- Encrypted in transit (HTTPS)
- Encrypted at rest (Qdrant Cloud)

---

## 📊 Usage Examples

### Example 1: Find Failed Deployments

```python
# In Le Chat:
"Find all deployments that failed in the last 6 hours"

# Behind the scenes:
# 1. Query converted to embedding
# 2. Semantic search in ssh_stderr collection
# 3. Results ranked by relevance
# 4. Returned with context
```

### Example 2: Get Fix Suggestions

```python
# In Le Chat:
"How do I fix npm ERESOLVE errors?"

# Behind the scenes:
# 1. Search for similar successful deployments
# 2. Find patterns in solutions
# 3. Generate suggestions based on history
# 4. Return ranked recommendations
```

### Example 3: Deployment Analytics

```python
# In Le Chat:
"Show me deployment statistics for the last week"

# Behind the scenes:
# 1. Query all collections
# 2. Aggregate by time period
# 3. Calculate success/failure rates
# 4. Identify common patterns
```

---

## 🎓 Learning Resources

- **Qdrant Docs:** https://qdrant.tech/documentation/
- **Mistral Embeddings:** https://docs.mistral.ai/capabilities/embeddings/
- **Vector Search Guide:** https://qdrant.tech/articles/what-is-a-vector-database/
- **RAG Explained:** https://www.llamaindex.ai/blog/what-is-rag

---

## ✅ Quick Checklist

Setup complete when:

- [ ] QDRANT_URL in .env
- [ ] QDRANT_API_KEY in .env
- [ ] MISTRAL_API_KEY in .env
- [ ] `python test_qdrant.py` passes
- [ ] First deployment successful
- [ ] Collections created automatically
- [ ] Semantic search works in Le Chat

---

## 🎉 You're All Set!

Your Qdrant cluster "nils" is ready to power semantic search and AI-powered suggestions!

**Next steps:**
1. Run a deployment to create collections
2. Try semantic search in Le Chat
3. Explore deployment analytics
4. Get AI-powered fix suggestions

**Remember:** RAG features are optional. Deployments work perfectly without them!

---

*Your deployment logs are now searchable with natural language!* 🚀
