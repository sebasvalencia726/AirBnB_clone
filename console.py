#!/usr/bin/python3
"""Console module
"""
import cmd
import sys
from models.base_model import *


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains the entry point
    of the command interpreter

    Args:
        cmd (instance): line-oriented interpreter framework
    """
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF implementation
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        raise SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
