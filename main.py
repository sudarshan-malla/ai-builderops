# from fastapi import FastAPI, Request
# import json

# app = FastAPI()

# @app.post("/webhook")
# async def webhook_listener(request: Request):
#     payload = await request.json()
#     with open("latest_error.json", "w") as f:
#         json.dump(payload, f, indent=4)
#     return {"status": "received"}
from fastapi import FastAPI, Request
import os
import openai
from pydantic import BaseModel

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class GitHubPayload(BaseModel):
    action: str
    repository: dict
    workflow: str
    conclusion: str
    head_commit: dict

@app.post("/webhook")
async def github_webhook(payload: GitHubPayload):
    if payload.conclusion == "failure":
        prompt = f"CI/CD pipeline failed. Commit message: {payload.head_commit['message']}. Suggest a fix."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return {"ai_suggestion": response['choices'][0]['message']['content']}
    return {"status": "success"}
