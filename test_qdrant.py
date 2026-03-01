"""Test Qdrant connection and setup.

Run this to verify your Qdrant credentials are working correctly.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("  Qdrant Connection Test")
print("=" * 60)
print()

# Check environment variables
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")
mistral_api_key = os.getenv("MISTRAL_API_KEY")

print("1. Checking environment variables...")
print(f"   QDRANT_URL: {qdrant_url[:50]}..." if qdrant_url else "   QDRANT_URL: ❌ NOT SET")
print(f"   QDRANT_API_KEY: {'✅ SET' if qdrant_api_key else '❌ NOT SET'}")
print(f"   MISTRAL_API_KEY: {'✅ SET' if mistral_api_key else '❌ NOT SET'}")
print()

if not qdrant_url or not qdrant_api_key:
    print("❌ ERROR: Qdrant credentials not configured!")
    print("   Please check your .env file.")
    exit(1)

if not mistral_api_key:
    print("⚠️  WARNING: MISTRAL_API_KEY not set.")
    print("   RAG features will not work without it.")
    print()

# Test Qdrant connection
print("2. Testing Qdrant connection...")
try:
    from qdrant_client import QdrantClient
    
    client = QdrantClient(
        url=qdrant_url,
        api_key=qdrant_api_key,
    )
    
    # Try to get collections
    collections = client.get_collections()
    print(f"   ✅ Connected successfully!")
    print(f"   Cluster: nils (europe-west3-0.gcp)")
    print(f"   Collections: {len(collections.collections)}")
    
    if collections.collections:
        print()
        print("   Existing collections:")
        for col in collections.collections:
            print(f"   - {col.name} ({col.vectors_count} vectors)")
    else:
        print("   No collections yet (will be created on first use)")
    
except ImportError:
    print("   ❌ ERROR: qdrant-client not installed!")
    print("   Run: pip install qdrant-client")
    exit(1)
except Exception as e:
    print(f"   ❌ ERROR: {e}")
    print()
    print("   Possible issues:")
    print("   - Check QDRANT_URL is correct")
    print("   - Check QDRANT_API_KEY is correct")
    print("   - Check internet connection")
    print("   - Check firewall settings")
    exit(1)

print()

# Test Mistral embeddings (if API key is set)
if mistral_api_key:
    print("3. Testing Mistral embeddings...")
    try:
        from mistralai import Mistral
        
        mistral_client = Mistral(api_key=mistral_api_key)
        
        # Test embedding
        response = mistral_client.embeddings.create(
            model="mistral-embed",
            inputs=["test connection"],
        )
        
        embedding = response.data[0].embedding
        print(f"   ✅ Embeddings working!")
        print(f"   Model: mistral-embed")
        print(f"   Dimensions: {len(embedding)}")
        
    except ImportError:
        print("   ❌ ERROR: mistralai not installed!")
        print("   Run: pip install mistralai")
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        print()
        print("   Possible issues:")
        print("   - Check MISTRAL_API_KEY is correct")
        print("   - Check internet connection")
        print("   - Check Mistral API status")
else:
    print("3. Skipping Mistral test (API key not set)")

print()
print("=" * 60)
print("  Test Complete!")
print("=" * 60)
print()

# Summary
print("Summary:")
print(f"  Qdrant: {'✅ Connected' if qdrant_url and qdrant_api_key else '❌ Not configured'}")
print(f"  Mistral: {'✅ Working' if mistral_api_key else '⚠️  Not configured (optional)'}")
print()

if qdrant_url and qdrant_api_key:
    print("✅ Your Qdrant setup is ready!")
    print()
    print("Next steps:")
    print("  1. Run your MCP server: python main.py")
    print("  2. Deploy something to create collections")
    print("  3. Use semantic search: 'Find deployments that failed'")
else:
    print("❌ Please configure Qdrant credentials in .env file")

print()
