#!/usr/bin/python3
"""
The cmd module is mainly useful for building custom shells
that let a user work with a program interactively.
console.py is the entry point command line interpreter for Airbnb project
"""
from ast import arg
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = "(hbnb) "

    air_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_EOF(self, line):
        """EOF to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """method called when an empty line is entered in
        response to the prompt.
        onecmd(str): Interpret the argument as though it had been
        typed in response to the prompt.
        onecmd help us to implement an empty line + ENTER
        should not execute anything
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Args:
            arg(str): given class in the command line interpreter
        If the class name is missing, print ** class name missing **
        If the class name doesn't exist, print ** class doesn't exist **
        """
        if line is None or line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.air_classes[line]()
            instance.save()
            print(instance.id)
            storage.save()

    def do_show(self, line):
        """
        String representation of a id instance
        """
        if line is None or line == "":
            print("** class name missing **")
        elif line.split(" ")[0] not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        elif len(line.split(" ")) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line.split(" ")[0], line.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """
        Is a command to destroy a instance
        """
        if line is None or line == "":
            print("** class name missing **")
        elif line.split(" ")[0] not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        elif len(line.split(" ")) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line.split(" ")[0], line.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """
        prints all string representation
        """
        if not arg:
            new_list = [str(value) for key, value in storage.all().items()]
            if len(new_list) != 0:
                print(new_list)
        elif arg not in self.air_classes:
            print("** class doesn't exist **")
            return
        else:
            new_list = [
                str(value) for key, value in storage.all().items() if arg in key
            ]
            if len(new_list) != 0:
                print(new_list)

    def do_update(self, line):
        """
        Is a command to update
        """
        if line is None or line == "":
            print("** class name missing **")
        elif line.split(" ")[0] not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        elif len(line.split(" ")) < 2:
            print("** instance id missing **")
        elif len(line.split(" ")) < 3:
            print("** attribute name missing **")
        elif len(line.split(" ")) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(line.split(" ")[0], line.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj_upt = line.split()[2]
                value = line.split()[3]
                setattr(storage.all()[key], obj_upt, value)
                storage.save()

    def do_count(self, args):
        """retrieve the number of instances of a
        class: <class name>.count()."""
        counter = 0
        instances = storage.all()
        for key, obj in instances.items():
            if arg in obj.__str__():
                counter += 1
        print(counter)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
