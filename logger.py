import sys
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python logger.py <log_filename>")
    sys.exit(1)

filename = sys.argv[1]


def log(action: str, message: str):
    with open(filename, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"{timestamp} [{action}] {message}\n")


log("START", "Logging started")

while True:
    line = sys.stdin.readline().rstrip().split(" ", 1)

    action = line[0]
    if action == "QUIT":
        break

    message = "" if len(line) == 1 else line[1]
    log(action, message)

log("STOP", "Logging stopped")
