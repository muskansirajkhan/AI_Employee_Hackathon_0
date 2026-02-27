# File: process_md.py
# Folder: watchers

from pathlib import Path
import openai
import os

# 🔑 Set OpenAI API key from environment variable (safe for Git)
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_file(md_path: Path):
    """
    Reads a markdown file, sends its content to OpenAI, 
    and appends the AI response safely.
    """
    if not md_path.exists():
        print(f"File {md_path} not found!")
        return
    
    content = md_path.read_text()
    
    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Process this file metadata:\n{content}"}
            ]
        )
        ai_text = response.choices[0].message.content
    except Exception as e:
        ai_text = f"[AI processing failed: {e}]"
    
    # Append AI response to the markdown file
    md_path.write_text(content + f"\n\n---\nAI Response:\n{ai_text}\n---\n")
    
    print(f"AI processing done for {md_path.name}")