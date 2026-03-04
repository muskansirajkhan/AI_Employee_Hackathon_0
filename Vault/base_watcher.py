# Vault/Watchers/base_watcher.py
class BaseWatcher:
    def __init__(self, vault_path):
        self.vault_path = vault_path

    def watch(self):
        raise NotImplementedError("Subclasses must implement this method")

    def run(self):
        print("Watcher running... (simulation)")