#!/usr/bin/python3
"""Console module
"""
import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains the entry point
    of the command interpreter

    Args:
        cmd (instance): line-oriented interpreter framework
    """
    def __init__(self, *args):
        """Constructor that display the prompt (hbnb)
        """
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'
        self.args = args

    def do_EOF(self, arg):
        """EOF implementation
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if len(line) == 0:
            print('** class name missing **')
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id

        Args:
            args (str): class name and id of the instance.
        """
        all_objs = storage.all()
        args = args.split(' ')
        if args == ['']:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] != 'BaseModel':
            print("class doesn't exist")
        elif args[1]:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if obj.id == args[1]:
                    print(obj)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and
        id and save the change into the JSON file.

        Args:
            args (str): class name and id to delete.
        """
        all_objs = storage.all()
        args = args.split(' ')
        if args == ['']:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] != 'BaseModel':
            print("class doesn't exist")
        elif args[1]:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if obj.id == args[1]:
                    del(all_objs[obj_id])
                    obj.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name.

        Args:
            args (class): class objects to print.
        """
        list = []
        all_objs = storage.all()
        args = args.split(' ')
        if args != [''] and args[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            for key, value in all_objs.items():
                dictionary = value.__str__()
                list.append(dictionary)
                print(list)

    def do_update(self, args):
        """Updates an instance based on the class name and
        id by adding or updating attribute and save the change
        into the JSON file.

        Args:
            args (str): Usage: update <class name>
                           <id> <attribute name> "<attribute value>"
        """
        all_objs = storage.all()
        args = args.split(' ')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = sys.argv
        args = args.split(separator=' ')
    else:
        HBNBCommand().cmdloop()
