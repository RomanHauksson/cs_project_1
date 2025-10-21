#!/usr/bin/env python

import sys
from subprocess import PIPE, Popen

from simple_term_menu import TerminalMenu


def main():
    log_filename = sys.argv[1]

    logger = Popen(
        ["python3.13", "logger.py", log_filename],
        stdout=PIPE,
        stdin=PIPE,
        encoding="utf8",
    )

    encryption = Popen(
        ["python3.13", "encryption.py"], stdout=PIPE, stdin=PIPE, encoding="utf8"
    )

    logger.stdin.write("START")

    options_main = ["password", "encrypt", "decrypt", "history", "quit"]
    menu_main = TerminalMenu(options_main)
    string_history = []
    while True:
        option_main = menu_main.show()
        match options_main[option_main]:
            case "password":
                options_password = [
                    "Set the password to a string from your history",
                    "Set the password to a new string",
                ]
                option_password = TerminalMenu(options_password).show()
                match options_password[option_password]:
                    case "Set the password to a string from your history":
                        option_password_history = TerminalMenu(string_history).show()
                        password = string_history[option_password_history]
                    case "Set the password to a new string":
                        print("Enter a string: ")
                        password = sys.stdin.readline().rstrip()
                encryption.stdin.write(f"PASS {password}")
            case "encrypt":
                options_encrypt = [
                    "Encrypt a string from your history",
                    "Encrypt a new string",
                ]
                option_encrypt = TerminalMenu(options_encrypt).show()
                match options_encrypt[option_encrypt]:
                    case "Encrypt a string from your history":
                        option_encrypt_history = TerminalMenu(string_history).show()
                        string = string_history[option_encrypt_history]
                    case "Encrypt a new string":
                        print("Enter a string: ")
                        string = sys.stdin.readline().rstrip()
                        string_history.append(string)
                encryption.stdin.write(f"ENCRYPT {string}")
                encrypted_string = encryption.stdout.read()
                string_history.append(encrypted_string)
                print(encrypted_string)
            case "decrypt":
                options_decrypt = [
                    "Decrypt a string from your history",
                    "Decrypt a new string",
                ]
                option_decrypt = TerminalMenu(options_decrypt).show()
                match options_decrypt[option_decrypt]:
                    case "Decrypt a string from your history":
                        option_decrypt_history = TerminalMenu(string_history).show()
                        string = string_history[option_decrypt_history]
                    case "Decrypt a new string":
                        print("Enter a string: ")
                        string = sys.stdin.readline().rstrip()
                        string_history.append(string)
                encryption.stdin.write(f"DECRYPT {string}")
                decrypted_string = encryption.stdout.read()
                string_history.append(decrypted_string)
                print(decrypted_string)
            case "history":
                print(string_history)
            case "quit":
                encryption.stdin.write("QUIT")
                logger.stdin.write("QUIT")
                break


if __name__ == "__main__":
    main()
