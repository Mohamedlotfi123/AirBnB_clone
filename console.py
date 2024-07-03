#!/usr/bin/python3
""" Console that contain the entry point of command interpreter """
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter.
    """
    prompt = "(hbnb) "
    Classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
            }

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

    def do_create(self, class_name):
        """
        Creates a new instance of Class
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.Classes.keys():
            print("** class doesn't exist **")
        else:
            for key, Class in self.Classes.items():
                if class_name == key:
                    instance = Class()
            #if class_name == "BaseModel":
             #   instance = BaseModel()
            #else:
            #    instance = Class()
            models.storage.new(instance)
            models.storage.save()
            print(instance.id)

    def do_show(self, Args):
        """
        prints the string representation of an instance.
        """
        arg_list = Args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.Classes.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            class_id = f"{arg_list[0]}.{arg_list[1]}"
            all_objs = models.storage.all()
            keys_list = list(all_objs.keys())
            if class_id not in keys_list:
                print("** no instance found **")
            else:
                print(all_objs[class_id])

    def do_destroy(self, Args):
        """
        Destory command deletes an instance
        """
        arg_list = Args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.Classes.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            class_id = f"{arg_list[0]}.{arg_list[1]}"
            all_objs = models.storage.all()
            keys_list = list(all_objs.keys())
            if class_id not in keys_list:
                print("** no instance found **")
            else:
                all_objs.pop(class_id)

    def do_all(self, Args):
        """
        All command prints string representation of all instaces.
        """
        if Args and Args not in self.Classes.keys():
            print("** class doesn't exist **")
        else:
            all_objs = models.storage.all()
            values = [str(obj) for obj in all_objs.values()]
            print(values)

    def do_update(self, Args):
        """
        Update command update instance
        """
        arg_list = Args.split()
        list_len = len(arg_list)
        if list_len == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.Classes.keys():
            print("** class doesn't exist **")
        elif list_len == 1:
            print("** instance id missing **")
        elif list_len == 2:
            print("** attribute name missing **")
        elif list_len == 3:
            print("** value missing **")
        else:
            Format = "%Y-%m-%dT%H:%M:%S.%f"
            class_id = f"{arg_list[0]}.{arg_list[1]}"
            all_objs = models.storage.all()
            keys_list = list(all_objs.keys())
            if class_id not in keys_list:
                print("** no instance found **")
            else:
                if arg_list[2] in ["created_at", "updated_at"]:
                    arg_list[3] = datetime.strptime(arg_list[3], Format)
                elif arg_list[2] == "my_number":
                    arg_list[3] = int(arg_list[3])
                setattr(all_objs[class_id], arg_list[2], arg_list[3])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
