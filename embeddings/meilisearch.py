# In the command line:
# pip3 install meilisearch

# In your .py file:
import meilisearch
import json
import os
from dotenv import load_dotenv

load_dotenv()
meilisearch_host = os.getenv('MEILISEARCH_HOST')
meilisearch_key = os.getenv('MEILISEARCH_MASTER_KEY')

client = meilisearch.Client(meilisearch_host, meilisearch_key)

async def create_index(file_url: str, index_name: str):
    if not file_url:
        raise ValueError("file_url is required")
    json_file = open(file_url, encoding='utf-8')
    document = json.load(json_file)
    res = client.index(index_name).add_documents(document)
    return res

