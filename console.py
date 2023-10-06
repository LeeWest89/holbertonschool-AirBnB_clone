#!/usr/bin/python3
"""Creates HBNB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The command line"""
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
        """creates newline after a commad is entered"""
        if line and line not in {'quit', 'EOF'}:
            print()
        return (stop)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
