# File: filesystem_watcher.py
# Folder: watchers

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import shutil
import time
import openai
import os

# 🔐 Secure API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Folder paths
VAULT_PATH = Path("C:/Users/Texon/Desktop/AI_Employee/Vault")
INBOX = VAULT_PATH / "Inbox"
NEEDS_ACTION = VAULT_PATH / "Needs_Action"

class DropFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        # Step 1: Copy file to Needs_Action
        source = Path(event.src_path)
        dest = NEEDS_ACTION / f"FILE_{source.name}"
        shutil.copy2(source, dest)

        # Step 2: Create .md metadata file
        md_path = dest.with_suffix(".md")
        md_content = f"""---
type: file_drop
original_name: {source.name}
size: {source.stat().st_size}
---

New file dropped for processing.
"""
        md_path.write_text(md_content)

        print(f"Processed {source.name} -> {md_path.name}")

        # Step 3: AI processing
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Process this file metadata:\n{md_content}"}
                ]
            )
            ai_text = response.choices[0].message.content
        except Exception as e:
            ai_text = f"[AI processing failed: {e}]"

        # Step 4: Append AI response
        md_path.write_text(md_content + f"\n\n---\nAI Response:\n{ai_text}\n---\n")
        print(f"AI processing done for {md_path.name}")

# Run watcher
observer = Observer()
observer.schedule(DropFolderHandler(), path=str(INBOX), recursive=False)
observer.start()

print("File System Watcher running... (drop a file in Inbox to test)")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()