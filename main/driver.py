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

    def log(message: str):
        logger.stdin.write(message)
        logger.stdin.flush()

    def get_string(
        history_message: str, new_string_message: str, add_to_history: bool = True
    ):
        selected_option = TerminalMenu([history_message, new_string_message]).show()
        if selected_option == 0:
            if len(string_history) == 0:
                print("No strings in history")
                return None
            history_index = TerminalMenu(string_history).show()
            return string_history[history_index]
        else:
            print("Enter a string: ")
            string = sys.stdin.readline().rstrip()
            if not string.isalpha():
                raise ValueError("Input must contain only letters.")
            if add_to_history:
                string_history.append(string)
            return string

    while True:
        option_main = menu_main.show()
        match options_main[option_main]:
            case "password":
                password = get_string(
                    "Set the password to a string from the history",
                    "Set the password to a new string",
                    add_to_history=False,
                )
                if password is None:
                    continue
                encryption.stdin.write(f"PASS {password}\n")
                encryption.stdin.flush()
                log(f"PASS Password has been set to {password}\n")
                print(f"Password has been set to {password}")
            case "encrypt":
                string = get_string(
                    "Encrypt a string from your history",
                    "Encrypt a new string",
                )
                if string is None:
                    continue
                log(f'ENCRYPT The string "{string}" is being encrypted\n')
                encryption.stdin.write(f"ENCRYPT {string}\n")
                encryption.stdin.flush()
                response = encryption.stdout.readline().rstrip()
                if response.startswith("RESULT "):
                    encrypted_string = response[7:]
                else:
                    print(response)
                    continue
                log(f'ENCRYPT "{string}" encrypted is "{encrypted_string}"\n')
                string_history.append(encrypted_string)
                print(f'"{string}" encrypted is "{encrypted_string}"')
            case "decrypt":
                string = get_string(
                    "Decrypt a string from your history",
                    "Decrypt a new string",
                )
                if string is None:
                    continue
                log(f'DECRYPT The string "{string}" is being decrypted\n')
                encryption.stdin.write(f"DECRYPT {string}\n")
                encryption.stdin.flush()
                response = encryption.stdout.readline().rstrip()
                if response.startswith("RESULT "):
                    decrypted_string = response[7:]
                else:
                    print(response)
                    continue
                log(f'DECRYPT "{string}" decrypted is "{decrypted_string}"\n')
                string_history.append(decrypted_string)
                print(f'"{string}" decrypted is "{decrypted_string}"')
            case "history":
                log("HISTORY The user requested to see the history\n")
                if len(string_history) == 0:
                    print("No strings in history")
                else:
                    print("String history: ")
                    for string in string_history:
                        print(f"- {string}")
                log(f"HISTORY The current history is {', '.join(string_history)}\n")
            case "quit":
                print("Quitting...")
                encryption.stdin.write("QUIT\n")
                encryption.stdin.flush()
                log("QUIT The user quit the program\n")
                break

    encryption.wait()
    logger.wait()


if __name__ == "__main__":
    main()
