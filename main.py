"""
Main entry point of application

This module contains code calling setup, processing and tear down operations.
"""

import sys
from typing import Optional, List

MAIN_USAGE_TEXT: str = """Usage: python main.py

        PubSub Telegram Bot Comments

        Starts the application without any command-line arguments. This program manages comments using a PubSub architecture on Telegram.

        Before starting, ensure you have the following information ready:
        - Telegram group chat link where conversations will occur.
        - Phone numbers of group members who can receive OTPs for login (ensure these numbers can receive text messages).
        """


def main(system_argument: List[Optional[str]]):
    """
    Main entry point of program. This is usually gotten from sys.argv.
    Due to testing requirements at the moment until something more elegant is implemented,
    the system_arguments will not have default value, and it will be required to pass sys.argv to
    the function. Again, this is just to note that ideally,  system_argument is supplied from command line
    arguments executing this module.

    :param system_argument: List of program execution command line arguments (usually sys.argv)
    :return: None
    """
    if len(system_argument) > 1:
        print(MAIN_USAGE_TEXT)

    else:
        print("Enter comma separated list of telegram phone numbers:")


if __name__ == '__main__':
    main(sys.argv)