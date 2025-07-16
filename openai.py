import openai
from fastapi import FastAPI, Request

openai.api_key = "YOUR_AZURE_OPENAI_KEY"
openai.api_base = "https://trialai1.openai.azure.com/"
openai.api_type = "azure"
openai.api_version = "2023-05-15"

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )
    return {"response": response['choices'][0]['message']['content']}
