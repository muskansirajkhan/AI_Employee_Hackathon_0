from pathlib import Path
from Watchers.gmail_watcher import GmailWatcher
from Watchers.slack_watcher import SlackWatcher
import logging
from datetime import datetime


def main():
    vault_path = Path(__file__).parent

    # Setup Logging
    log_file = vault_path / "Logs" / "activity.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("===== AI Employee Started =====")

    # Gmail watcher (simulation mode, credentials optional)
    gmail_watcher = GmailWatcher(str(vault_path))

    # Slack watcher (simulation mode)
    slack_watcher = SlackWatcher(str(vault_path))

    # Gmail updates
    gmail_updates = gmail_watcher.check_for_updates()
    for msg in gmail_updates:
        gmail_watcher.create_action_file(msg)

    # Slack updates
    slack_updates = slack_watcher.check_for_updates()
    for msg in slack_updates:
        slack_watcher.create_action_file(msg)

    print("Simulation check complete, updates found:")
    print(f"Gmail: {len(gmail_updates)} messages")
    print(f"Slack: {len(slack_updates)} messages")

    logging.info("Simulation check complete")
    logging.info(f"Gmail messages: {len(gmail_updates)}")
    logging.info(f"Slack messages: {len(slack_updates)}")


if __name__ == "__main__":
    main()