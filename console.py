#!/usr/bin/python3
""" Console that contain the entry point of command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self):
        """
        exit the program.
        """
        return True

    def emptyline(self):
        """
        do nothing
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
