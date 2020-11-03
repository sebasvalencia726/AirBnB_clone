#!/usr/bin/python3
"""Console module
"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains the entry point
    of the command interpreter

    Args:
        cmd (instance): line-oriented interpreter framework
    """
    def __init__(self):
        """Constructor that display the prompt (hbnb)
        """
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF implementation
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if len(args) == 0:
            print('** class name missing **')
        elif args != 'BaseModel':
            print("** class doesn't exist **")
        else:
            BaseModel().save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
