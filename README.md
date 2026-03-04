# 🤖 AI Employee Vault 📂

AI-Powered File Organizer & Processor ✨ – now with **Silver Tier automation**  

This project helps you:

📝 Drop files in the **Inbox** folder  

📂 Automatically move them to **Needs_Action**  

🤖 Process metadata using **OpenAI GPT**  

📄 Create `.md` files with AI responses  

📧 **Gmail watcher** – detects unread/important emails (simulation or real mode)  

💬 **Slack watcher** – detects messages in Slack channels (simulation or real mode)  

---

### Folders included:

- `Vault/Inbox` – Place new files here  
- `Vault/Needs_Action` – Files copied here for action  
- `Vault/Done` – Completed files (optional)  

---

### Watchers & Scripts:

- `Watchers/filesystem_watcher.py` – Monitors Inbox & triggers AI  
- `Watchers/process_md.py` – Helper script for processing `.md` files  
- `Watchers/gmail_watcher.py` – Handles Gmail messages  
- `Watchers/slack_watcher.py` – Handles Slack messages  
- `replacements.txt` – Example file for replacements  

---

### 💡 Usage:

1. Set your **OpenAI API key** in `.env` (DO NOT push this!)  
2. Run `main.py` to check **Inbox, Gmail & Slack** (simulation mode supported)  
3. Drop a file in Inbox → watch AI work magic!  

---

### ⚠️ Note:

- Keep `.env` and `venv/` out of GitHub  
- Silver Tier watchers support **simulation mode** if credentials are not provided  
