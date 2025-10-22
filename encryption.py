import sys
from typing import Final

# maybe use do while loop for this?

alphabet: Final[str] = "abcdefghijklmnopqrstuvwxyz"

# TODO: handle lowercase testing


def encrypt(input: str):
    input = input.lower()
    output = ""
    for i, letter in enumerate(input):
        index = alphabet.find(letter)
        offset = alphabet.find(passkey[i % len(passkey)])
        output += alphabet[(index + offset) % 26]
    return output


def decrypt(input: str):
    input = input.lower()
    output = ""
    for i, letter in enumerate(input):
        index = alphabet.find(letter)
        offset = alphabet.find(passkey[i % len(passkey)])
        output += alphabet[(index - offset) % 26]
    return output


passkey = None

while True:
    line = sys.stdin.readline().rstrip().split()
    if len(line) == 0:
        break
    if len(line) == 1:
        if line[0] == "QUIT":
            break
        else:
            raise ValueError(f"Invalid command: {line[0]}")
    if len(line) > 2:
        print("ERROR Cannot supply more than one argument.")
        continue
    [command, argument] = line
    match command:
        case "PASS":
            passkey = argument.lower()
        case "ENCRYPT":
            if passkey is None:
                print("ERROR The passkey is not set.")
            else:
                print("RESULT " + encrypt(argument))
            sys.stdout.flush()
        case "DECRYPT":
            if passkey is None:
                print("ERROR The passkey is not set.")
            else:
                print("RESULT " + decrypt(argument))
            sys.stdout.flush()
        case _:
            print(f'ERROR Invalid command "{command}".')
