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

    logger.stdin.write("START\n")
    logger.stdin.flush()

    options_main = ["password", "encrypt", "decrypt", "history", "quit"]
    menu_main = TerminalMenu(options_main)
    string_history = []
    while True:
        option_main = menu_main.show()
        match options_main[option_main]:
            case "password":
                option_password = TerminalMenu(
                    [
                        "Set the password to a string from your history",
                        "Set the password to a new string",
                    ]
                ).show()
                match option_password:
                    case 0:
                        if len(string_history) == 0:
                            print("No strings in history")
                            continue
                        option_password_history = TerminalMenu(string_history).show()
                        password = string_history[option_password_history]
                    case 1:
                        print("Enter a string: ")
                        password = sys.stdin.readline().rstrip()
                encryption.stdin.write(f"PASS {password}\n")
                encryption.stdin.flush()
                logger.stdin.write(f"PASS Password has been set to {password}\n")
                logger.stdin.flush()
            case "encrypt":
                option_encrypt = TerminalMenu(
                    [
                        "Encrypt a string from your history",
                        "Encrypt a new string",
                    ]
                ).show()
                match option_encrypt:
                    case 0:
                        if len(string_history) == 0:
                            print("No strings in history")
                            continue
                        option_encrypt_history = TerminalMenu(string_history).show()
                        string = string_history[option_encrypt_history]
                    case 1:
                        print("Enter a string: ")
                        string = sys.stdin.readline().rstrip()
                        string_history.append(string)
                encryption.stdin.write(f"ENCRYPT {string}\n")
                encryption.stdin.flush()
                logger.stdin.write(
                    f'ENCRYPT The string "{string}" has been encrypted\n'
                )
                logger.stdin.flush()
                response = encryption.stdout.readline().rstrip()
                if response.startswith("RESULT "):
                    encrypted_string = response[7:]
                else:
                    encrypted_string = response
                logger.stdin.write(
                    f'ENCRYPT "{string}" encrypted is "{encrypted_string}"\n'
                )
                logger.stdin.flush()
                string_history.append(encrypted_string)
                print("Encrypted string: " + encrypted_string)
            case "decrypt":
                option_decrypt = TerminalMenu(
                    [
                        "Decrypt a string from your history",
                        "Decrypt a new string",
                    ]
                ).show()
                match option_decrypt:
                    case 0:
                        if len(string_history) == 0:
                            print("No strings in history")
                            continue
                        option_decrypt_history = TerminalMenu(string_history).show()
                        string = string_history[option_decrypt_history]
                    case 1:
                        print("Enter a string: ")
                        string = sys.stdin.readline().rstrip()
                        string_history.append(string)
                encryption.stdin.write(f"DECRYPT {string}\n")
                encryption.stdin.flush()
                logger.stdin.write(
                    f'DECRYPT The string "{string}" has been decrypted\n'
                )
                logger.stdin.flush()
                response = encryption.stdout.readline().rstrip()
                if response.startswith("RESULT "):
                    decrypted_string = response[7:]
                else:
                    decrypted_string = response
                logger.stdin.write(
                    f'DECRYPT "{string}" decrypted is "{decrypted_string}"\n'
                )
                logger.stdin.flush()
                string_history.append(decrypted_string)
                print(decrypted_string)
            case "history":
                logger.stdin.write("HISTORY The user requested to see the history\n")
                logger.stdin.flush()
                if len(string_history) == 0:
                    print("No strings in history")
                else:
                    print("String history: ")
                    for string in string_history:
                        print(f"- {string}")
                logger.stdin.write(
                    f"HISTORY The current history is {', '.join(string_history)}\n"
                )
                logger.stdin.flush()
            case "quit":
                print("Quitting...")
                encryption.stdin.write("QUIT\n")
                encryption.stdin.flush()
                logger.stdin.write("QUIT The user quit the program\n")
                logger.stdin.flush()
                break

    encryption.wait()
    logger.wait()


if __name__ == "__main__":
    main()
