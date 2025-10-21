import sys
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python logger.py <log_filename>")
    sys.exit(1)

filename = sys.argv[1]

while True:
    line = sys.stdin.readline().rstrip().split(" ", 1)

    action = line[0]
    message = line[1]
    if action == "QUIT":
        break

    with open(filename, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"{timestamp} [{action}] {message}\n")
