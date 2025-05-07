from openai import OpenAI
import os, json

def diagnose_ci_error(error_log_path):
    with open(error_log_path) as f:
        payload = json.load(f)
    error_summary = payload['workflow_job']['conclusion']
    
    OpenAI.api_key = os.getenv("sk-...RJIA")
    prompt = f"""Diagnose this CI/CD job result: {error_summary}.
    Suggest what the problem might be and how to fix the YAML."""
    
    response = OpenAI.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
