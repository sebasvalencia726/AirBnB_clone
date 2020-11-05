#!/usr/bin/python3
""" Console class """

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ Principal class """
    prompt = "(hbnb) "

    classes = [
        "BaseModel",
        "User",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State"
    ]

    def emptyline(self):
        """When you use ENTER after a command it doesn't print anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program \n"""
        return True

    def do_EOF(self, line):
        """End of file, use to exit the program \n"""
        return True

    def de_create(self, line):
        """Create a new instance of BaseModel"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval('{}()'.format(args[0]))
            models.storage.save()
            print(new_inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in objects.keys():
                print(objects[key])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in objects.keys():
                objects.pop(key, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = line.split()
        objects = models.storage.all()
        n_list = []

        if len(args) == 0:
            for obj in objects.values():
                n_list.append(obj.__str__())
            print(n_list)

        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    n_list.append(obj.__str__())
            print(n_list)

    def do_update(self, line):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        elif len(args) == 2:
            print("** attribute name missing **")

        elif len(args) == 3:
            print("** value missing **")

        elif "{" not in line and "}" not in line:
            key = args[0] + '.' + args[1]
            object2 = objects.get(key, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(object2, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

        else:
            key = args[0] + '.' + args[1]
            object2 = objects.get(key)
            kwargs = eval("{" + line.split("{")[1].split("}")[0] + "}")
            if object2 is None:
                print("** no instance found **")
                return
            for key[val] in kwargs.items():
                setattr(object2, key, val)
            models.storage.save()


if __name__ == '__main__':
    interprete = HBNBCommand()
    interprete.cmdloop()
