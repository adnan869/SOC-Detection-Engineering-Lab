import sys
import json
import subprocess
import os
from datetime import datetime

LOG_FILE = r"C:\Program Files (x86)\ossec-agent\active-response\active-responses.log"

def log(message):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} disable-soc-test: {message}\n")
    except Exception:
        pass

def main():
    try:
        # Read Wazuh JSON input
        input_data = sys.stdin.readline()

        if not input_data:
            log("No input received.")
            return

        message = json.loads(input_data)

        # Accept only the add command
        if message.get("command") != "add":
            log("Ignored: command is not add.")
            return

        alert = message.get("parameters", {}).get("alert", {})

        # Verify triggering rule
        rule_id = str(alert.get("rule", {}).get("id", ""))

        if rule_id != "100101":
            log(f"Ignored unexpected rule ID: {rule_id}")
            return

        # Verify Windows agent
        agent_id = str(alert.get("agent", {}).get("id", ""))

        if agent_id != "002":
            log(f"Ignored unexpected agent ID: {agent_id}")
            return

        # Verify target account
        username = (
            alert.get("data", {})
            .get("win", {})
            .get("eventdata", {})
            .get("targetUserName", "")
        )

        if username != "SOC Test":
            log(f"Ignored unexpected account: {username}")
            return

        # Disable only SOC Test
        result = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy", "Bypass",
                "-Command",
                "Disable-LocalUser -Name 'SOC Test'"
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            log("SUCCESS: SOC Test account disabled.")
        else:
            log(f"ERROR: {result.stderr}")

    except Exception as error:
        log(f"ERROR: {error}")

if __name__ == "__main__":
    main()
