#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
import cmd
import shlex

classes = ["BaseModel", "User", "State", "City",
           "Amenity", "Place" "Review"]

json_file= "file.json"


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    
    air_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
    
    def do_create(self, line):

        if line is None or line == "":
            print(" class name missing ")
        elif line not in HBNBCommand.air_classes:
            print(" class doesn't exist ")
        else:
            instance = HBNBCommand.air_classes[line]()
            instance.save()
            print(instance.id)
            storage.save()
        
    def do_show(self, line):
        """ Prints a representation of an instance.
            """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        file_dict = storage.all()
        key_to_search = "{}.{}".format(args[0], args[1])
        if key_to_search in file_dict.keys():
            print(file_dict[key_to_search])
        else:
            print("** no instance found **")
    
    def do_destroy(self, line):
        """ Deletes an instance.
            """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        file_dict = storage.all()
        key_to_search = "{}.{}".format(args[0], args[1])
        if key_to_search in file_dict.keys():
            file_dict.pop(key_to_search)
            storage.save()
        else:
            print("** no instance found **")
            return
    
    def do_all(self, arg):
        """
        prints all string representation
        """
        if not arg:
            new_list = [str(value) for key, value in storage.all().items()]
            if len(new_list) != 0:
                print(new_list)
        elif arg not in self.air_classes:
            print(" class doesn't exist ")
            return
        else:
            new_list = [str(value) for key,
                        value in storage.all().items() if arg in key]
            if len(new_list) != 0:
                print(new_list)
    
    def do_update(self, line):
        """
        Is a command to update
        """
        if line is None or line == "":
            print(" class name missing ")
        elif line.split(" ")[0] not in HBNBCommand.air_classes:
            print(" class doesn't exist ")
        elif len(line.split(" ")) < 2:
            print(" instance id missing ")
        elif len(line.split(" ")) < 3:
            print(" attribute name missing ")
        elif len(line.split(" ")) < 4:
            print(" value missing ")
        else:
            key = "{}.{}".format(line.split(" ")[0], line.split(" ")[1])
            if key not in storage.all():
                print(" no instance found ")
            else:
                obj_upt = line.split()[2]
                value = line.split()[3]
                setattr(storage.all()[key], obj_upt, value)
                storage.save()
    
    def do_count(self, arg):
        """retrieve the number of instances of a
        class: <class name>.count()."""
        counter = 0
        instances = storage.all()
        for key, obj in instances.items():
            if arg in obj.str():
                counter += 1
        print(counter)
        
    def do_EOF(self, line):
        print()
        return True
    
    def do_quit(self, line):
        return True
    
    def emptyline(self):
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
