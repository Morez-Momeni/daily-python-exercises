"""
Problem #64: Extract Process Name and ID from System Logs
Date: 2026-09-30

A regex pattern tested against real system logs to extract:
- Process name  (letters, dashes, dots)
- Process ID    (digits)

In Python, the flags (gmu) are passed to re.compile() instead.
"""

import re

# The pattern (Python-compatible: flags passed separately)
PATTERN = re.compile(
    r"^(?:[0-9\-\:\.\+T]+)\s"
    r"(?:[a-zA-Z0-9_\-]+)\s"
    r"(?P<PsName>[a-zA-Z\-.]+)"
    r"\[(?P<PsId>[0-9]+)\]",
    re.MULTILINE | re.UNICODE
)

# Sample log lines (typical systemd / syslog format)
SAMPLE_LOG = """\
2026-09-30T14:22:01.123456+00:00 myhost systemd[1]: Started Daily apt download activities.
2026-09-30T14:22:02.234567+00:00 myhost sshd[1234]: Accepted password for morez from 192.168.1.5
2026-09-30T14:22:03.345678+00:00 myhost NetworkManager[890]: <info> device wlan0 activated
2026-09-30T14:22:04.456789+00:00 myhost kernel: some random line without process bracket
2026-09-30T14:22:05.567890+00:00 myhost cron[4567]: (root) CMD (run-parts /etc/cron.hourly)
"""


def extract_processes(log_text: str):
    """Return a list of (process_name, process_id) tuples."""
    results = []
    for match in PATTERN.finditer(log_text):
        results.append((match.group("PsName"), match.group("PsId")))
    return results


if __name__ == "__main__":
    processes = extract_processes(SAMPLE_LOG)
    print(f"Found {len(processes)} processes:\n")
    for name, pid in processes:
        print(f"  Process: {name:<20} PID: {pid}")