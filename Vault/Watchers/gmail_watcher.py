from base_watcher import BaseWatcher
from datetime import datetime
from pathlib import Path

class GmailWatcher(BaseWatcher):
    def __init__(self, vault_path: str, credentials_path: str = None):
        super().__init__(vault_path)  # BaseWatcher ka simple init
        self.processed_ids = set()
        self.creds = None
        self.service = None

        # Hackathon / simulation mode
        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            if credentials_path:
                try:
                    self.creds = Credentials.from_authorized_user_file(credentials_path)
                    self.service = build('gmail', 'v1', credentials=self.creds)
                except Exception as e:
                    print(f"⚠️ Credentials invalid ya missing: {e}")
                    self.creds = None
                    self.service = None
        except ImportError:
            # Google modules installed nahi → simulation mode
            pass

    def check_for_updates(self) -> list:
        if not self.service:
            print("⚠️ Simulation mode: Gmail service not available")
            return []
        results = self.service.users().messages().list(
            userId='me', q='is:unread is:important'
        ).execute()
        messages = results.get('messages', [])
        return [m for m in messages if m['id'] not in self.processed_ids]

    def create_action_file(self, message) -> Path:
        # Simulation ke liye unique filename
        filepath = Path(self.vault_path) / 'Needs_Action' / f'EMAIL_{datetime.now().timestamp()}.md'
        filepath.write_text(f"# Simulated Email Action for message {message}")
        return filepath