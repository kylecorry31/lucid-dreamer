# Lucid Dreamer
A program to create encrypted dream journals on Linux.

## Getting started

### Dependencies
- python3
- gpg
- gedit
- make

```shell
sudo apt -y install python3 gpg gedit make
```

### Install
To install, ensure you have the required dependencies above, then run the following command:
```shell
make install
```

### Usage
Once the CLI is installed, you can run the following command from the terminal.

```shell
usage: lucid-dreamer.py [-h] journal_name

positional arguments:
  journal_name  The path to the dream journal (without the file extension).

optional arguments:
  -h, --help    show this help message and exit
```

After writing your dream in gedit, save and close the gedit window. This will prompt your for a password to encrypt the dream journal with.

The program may prompt for a password to decrypt the journal, use the same password you used to encrypt it when it was first created.

## Contributing
Please fork this repo and submit a pull request to contribute. I will review all changes and respond if they are accepted or rejected (as well as reasons, so it will be accepted).

### Issues
If you are submitting a bug, please describe the bug in detail and how to replicate if possible. Logs are also very useful.

If you are submitting a feature idea, please describe it in detail and document the potential use cases of that feature if it isn't clear.

## Credits
- [@kylecorry31](https://github.com/kylecorry31) - Initial work

## License
You are free to copy, modify, and distribute lucid-dreamer with attribution under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
