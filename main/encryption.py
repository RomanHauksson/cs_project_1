import sys
from typing import Final

# maybe use do while loop for this?

alphabet: Final[str] = "abcdefghijklmnopqrstuvwxyz"

# TODO: handle lowercase testing


def encrypt(input: str):
    output = ""
    for i, letter in enumerate(input):
        index = alphabet.find(letter)
        offset = alphabet.find(passkey[i % len(passkey)])
        output += alphabet[(index + offset) % 26]
    return output


def decrypt(input: str):
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
        print("ERROR Must specify an argument.")
        continue
    if len(line) > 2:
        print("ERROR Cannot supply more than one argument.")
        continue
    [command, argument] = line
    match command:
        case "PASS":
            passkey = argument
        case "ENCRYPT":
            if passkey is None:
                print("ERROR The passkey is not set.")
            else:
                print("RESULT " + encrypt(argument))
        case "DECRYPT":
            if passkey is None:
                print("ERROR The passkey is not set.")
            else:
                print("RESULT " + decrypt(argument))
        case "QUIT":
            break
        case _:
            print(f'ERROR Invalid command "{command}".')
