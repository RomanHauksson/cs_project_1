#!/usr/bin/env python

import sys
from subprocess import PIPE, Popen

from simple_term_menu import TerminalMenu

log_filename = sys.argv[1]

logger = Popen(
    ["python3.13", "logger.py", log_filename], stdout=PIPE, stdin=PIPE, encoding="utf8"
)

encryption = Popen(
    ["python3.13", "encryption.py"], stdout=PIPE, stdin=PIPE, encoding="utf8"
)

logger.stdin.write("START")

while True:
    print("Menu")


logger.stdin.write("EXIT")
