#!/usr/bin/python3
"""Makes the console for the AirBnB clone Project"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """The command line interface"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Does nothing if line is empty"""
        pass

    def do_quit(self, arg):
        """Quit command to exit program"""
        return (True)

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return (True)

    def help_quit(self):
        """Desired output messange and a new line"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """Desired output messange and a new line"""
        print("EOF signal to exit the program\n")

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if args is None or args == []:
            print("** class name missing **")
            return ()
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return ()
        else:
            new_i = eval("{}()".format(args[0]))
            new_i.save()
            print(new_i.id)

    def do_show(self, arg):
        """Prints the instance by id"""
        args = arg.split()
        if args is None or args == []:
            print("** class name missing **")
            return ()
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return ()
        elif len(args) < 2:
            print("** instance id missing **")
            return ()
        else:
            for key, value in models.storage.all().items():
                if key == "{}.{}".format(args[0], args[1]):
                    print(value)
                    return ()
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance by id"""
        args = arg.split()
        if args is None or args == []:
            print("** class name missing **")
            return ()
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return ()
        elif len(args) < 2:
            print("** instance id missing **")
            return ()
        else:
            for key in models.storage.all().keys():
                if key == "{}.{}".format(args[0], args[1]):
                    del models.storage.all()[key]
                    models.storage.save()
                    return ()
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all str representations of all instances"""
        args = arg.split()
        if args is None or args == []:
            output = list(map(str, models.storage.all().values()))
            print(output)
        else:
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
                return ()
            else:
                output = []
                for key in models.storage.all():
                    if args[0] in key:
                        output.append("{}".format(models.storage.all()[key]))
                print(output)

    def do_update(self, arg):
        """Adds or updates attibute by class id and name"""
        args = arg.split()
        if args is None or args == []:
            print("** class name missing **")
            return ()
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return ()
        elif len(args) < 2:
            print("** instance id missing **")
            return ()
        elif len(args) < 3:
            print("** attribute name missing **")
            return ()
        elif len(args) < 4:
            print("** value missing **")
            return ()
        else:
            for key in models.storage.all():
                if key == "{}.{}".format(args[0], args[1]):
                    if isinstance(arg[3], float):
                        setattr(models.storage.all()[key], args[2],
                                float(args[3]))
                        models.storage.save()
                        return ()
                    elif isinstance(arg[3], int):
                        setattr(models.storage.all()[key], args[2],
                                int(args[3]))
                        models.storage.save()
                        return ()
                    elif isinstance(arg[3], str):
                        setattr(models.storage.all()[key], args[2],
                                str(args[3]))
                        models.storage.save()
                        return ()
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
