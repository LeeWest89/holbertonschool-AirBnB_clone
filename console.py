#!/usr/bin/python3
"""The interactive and non-interactive console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """The command line"""
    prompt = "(hbnb) "

    def empty_line(self):
        """Do nothing if line is empty"""
        pass

    def do_EOF(self, arg):
        """If command is EOF exit the program"""
        return (True)

    def do_quit(self, arg):
        """if quit is the input exit the program"""
        return (True)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
