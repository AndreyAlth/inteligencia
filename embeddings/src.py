from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def create_embeddings(data: str):
    translation = client.embeddings.create(
        model="text-embedding-3-small",
        input="Hola mi nombre es Gabriel",
        encoding_format="float"
    )
    return translation

st = create_embeddings("hla")
print(st.data[0].embedding)