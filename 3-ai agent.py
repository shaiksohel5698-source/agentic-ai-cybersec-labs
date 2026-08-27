

import os
from dotenv import load_dotenv
from google import genai

# 1. Environment variables load karo (.env file se)
load_dotenv()

# 2. Client initialize karo (direct key pass karke)
client = genai.Client(api_key="AQ.Ab8RN6J6u9Mop3efa8WelyjxET-EaL2vn7bfqXTIvac_v2lWiA")

# 3. AI Agent se response maango
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Tell me one sentence about why python is awesome for ai.",
)

# 4. Result print karo
print("🤖 AI Agent Response:")
print(response.text)
