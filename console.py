#!/usr/bin/python3
"""This file is our HBNB Project console. It's used to make new entries and 
interact with our site."""
import cmd
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The command line interface for our project. You should be able to make
    new instances from here."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing if line is empty"""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return (True)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return (True)

    def postcmd(self, stop, line):
        """creates newline after a command is entered"""
        if line and line not in {'quit', 'EOF'}:
            print()
        return (stop)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
         and prints the id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.__dict__:
            print("** class doesn't exist **")
        else:
            new_instance = models.__dict__[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
         name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.__dict__:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.__dict__:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
         the class name"""
        args = arg.split()
        if len(args) > 0 and args[0] not in models.__dict__:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if len(args) == 0 or args[0] == key.split(".")[0]:
                    print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
         updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.__dict__:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                instance = models.storage.all()[key]
                if args[2] in instance.__dict__:
                    attr_type = type(getattr(instance, args[2]))
                    args[3] = attr_type(args[3])
                setattr(instance, args[2], args[3])
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
