#!/usr/bin/python3
import argparse
import os
import sys

if __name__ == '__main__':
     # Read and validate arguments
    parser = argparse.ArgumentParser(description='Create dream journals.')
    parser.add_argument('journal_name', type=str, help='The path to the dream journal (without the file extension).')
    args = parser.parse_args()

    journal_name = args.journal_name

    # Make the directories if they don't exist
    dirname = os.path.dirname(journal_name)
    if dirname:
        os.makedirs(os.path.dirname(journal_name), exist_ok=True)

    # Check if the gpg file exists, if it does, decrypt it
    if os.path.exists(journal_name + ".gpg"):
        # decrypt gpg
        os.system('gpg --batch --yes ' + journal_name + ".gpg")
    else:
        # create journal file
        f = open(journal_name, 'w')
        f.close()

    # Open file for editing
    os.system('gedit -w ' + journal_name)

    # Encrypt file
    os.system('gpg -c --batch --yes ' + journal_name)

    # Delete the decrypted file
    os.remove(journal_name)
