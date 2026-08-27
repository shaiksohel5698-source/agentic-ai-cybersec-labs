import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Real Tool Function
def check_port_status(port: int) -> str:
    """Checks if a given network port is open or closed."""
    common_ports = {80: "Open (HTTP)", 443: "Open (HTTPS)", 22: "Open (SSH)"}
    return common_ports.get(int(port), f"Port {port} is Closed/Filtered")

# 2. Correct Model Name: gemini-3.6-flash
model = genai.GenerativeModel(
    model_name="gemini-3.6-flash",
    tools=[check_port_status]
)

# 3. Automatic Function Calling Enabled
chat = model.start_chat(enable_automatic_function_calling=True)

# 4. User Query
response = chat.send_message("Can you check if port 443 and port 8080 are open?")

print("\n🤖 Agent Output:")
print(response.text)