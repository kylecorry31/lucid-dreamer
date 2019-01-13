#!/usr/bin/python3
import argparse
import os
import sys
import getpass

if __name__ == '__main__':
     # Read and validate arguments
    parser = argparse.ArgumentParser(description='Create dream journals.')
    parser.add_argument('journal_name', type=str, help='The path to the dream journal (without the file extension).')
    parser.add_argument('--editor', type=str, help='The command to open the file in the editor (ensure your editor command runs in wait mode).')
    args = parser.parse_args()

    journal_name = args.journal_name
    editor_cmd = args.editor if args.editor else "gedit -w"

    encryption_password = getpass.getpass()

    # Make the directories if they don't exist
    dirname = os.path.dirname(journal_name)
    if dirname:
        os.makedirs(os.path.dirname(journal_name), exist_ok=True)

    # Check if the gpg file exists, if it does, decrypt it
    if os.path.exists(journal_name + ".gpg"):
        # decrypt gpg
        ret = os.system('echo "' + encryption_password + '" | gpg --batch --yes --passphrase-fd 0 ' + journal_name + ".gpg")
        if ret:
            print("Error decrypting dream journal")
            exit(1)
    else:
        # create journal file
        f = open(journal_name, 'w')
        f.close()

    # Open file for editing
    os.system(editor_cmd + ' ' + journal_name)

    # Encrypt file
    os.system('echo "' + encryption_password + '" | gpg -c --batch --yes --passphrase-fd 0 ' + journal_name)

    # Delete the decrypted file
    os.system('shred -u ' + journal_name)
