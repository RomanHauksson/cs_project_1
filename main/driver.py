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
                encryption.stdin.flush()
                logger.stdin.write(f"PASS Password has been set to {password}")
                logger.stdin.flush()
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
                encryption.stdout.flush()
                logger.stdin.write(f'ENCRYPT The string "{string}" has been encrypted')
                logger.stdin.flush()
                encrypted_string = encryption.stdout.read()
                logger.stdin.write(
                    f'ENCRYPT "{string}" encrypted is "{encrypted_string}"'
                )
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
                encryption.stdin.flush()
                logger.stdin.write(f'DECRYPT The string "{string}" has been dycrypted')
                logger.stdin.flush()
                decrypted_string = encryption.stdout.read()
                encryption.stdout.flush()
                logger.stdin.write(
                    f'DECRYPT "{string}" decrypted is "{decrypted_string}"'
                )
                logger.stdin.flush()
                string_history.append(decrypted_string)
                print(decrypted_string)
            case "history":
                logger.stdin.write("HISTORY The user requested to see the history")
                logger.stdin.flush()
                print(string_history)
                logger.stdin.write(
                    f"HISTORY The current history is {', '.join(string_history)}"
                )
                logger.stdin.flush()
            case "quit":
                encryption.stdin.write("QUIT")
                encryption.stdin.flush()
                logger.stdin.write("QUIT The user quit the program")
                logger.stdin.flush()
                break

    encryption.wait()
    logger.wait()


if __name__ == "__main__":
    main()
