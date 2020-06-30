#!/usr/bin/python3
""" this module contends a console in cmd module, is for
    manage of data
"""
import cmd
import json
import shlex
from datetime import datetime
from models import storage
# from models import classes
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """console to data engine of HBNB."""

    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_EOF(self, line):
        """ implement exit command whit EOF"""
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (
            to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        if arg == '':
            print('** class name missing **')
        elif arg in self.classes.keys():
            new_class = self.classes[arg]()
            new_class.save()
            print('{}'.format(new_class.id))
        else:
            print('** class doesn\'t exist **')

    def do_show(self, line):
        """
            Prints the string representation of an instance based on the class
            name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        arg = line.split()
        if len(arg) == 0:
            print('** class name missing **')
        elif arg[0] not in self.classes.keys():
            print('** class doesn\'t exist **')
        elif len(arg) == 1 and arg[0] in self.classes.keys():
            print('** instance id missing **')
        elif len(arg) == 2 and arg[0] in self.classes.keys():
            key = arg[0] + '.' + arg[1]
            list_obj = storage.all()
            id_counter = 0
            for obj in list_obj.keys():
                if obj == key:
                    obj_class = list_obj[obj]
                    new_class = self.classes[arg[0]](**obj_class)
                    print(new_class)
                    id_counter += 1
            if id_counter == 0:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (
            save the change into the JSON file). Ex: $ destroy
            BaseModel 1234-1234-1234.
        """
        arg = line.split()
        if len(arg) == 0:
            print('** class name missing **')
        elif arg[0] not in self.classes.keys():
            print('** class doesn\'t exist **')
        elif len(arg) == 1 and arg[0] in self.classes.keys():
            print('** instance id missing **')
        elif len(arg) == 2 and arg[0] in self.classes.keys():
            key = arg[0] + '.' + arg[1]
            list_obj = storage.all()
            id_counter = 0
            for obj in list_obj.keys():
                if obj == key:
                    id_counter += 1
            if id_counter > 0:
                del list_obj[key]
                storage.save()
            if id_counter == 0:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances
            based or not on the class name. Ex: $ all BaseModel or $ all
        """
        arg = line.split()
        list_instances = []
        if len(arg) == 0 or (len(arg) > 0 and arg[0] in self.classes.keys()):

            list_obj = storage.all()
            for obj in list_obj.keys():
                obj_class = list_obj[obj]
                find_class = obj_class['__class__']
                new_class = eval(find_class + '(**list_obj[obj])')
                # my_new_model = BaseModel(**list_obj[obj])
                list_instances.append(str(new_class))
            print(list_instances)
        else:
            print('** class doesn\'t exist **')

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email
        "aibnb@holbertonschool.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        A string argument with a space must be between double quote
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        objects = storage.all()
        if args[0] in self.classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                base = ["id", "created_at", "updated_at"]
                if obj:
                    arg = shlex.split(line)
                    if len(arg) < 3:
                        print("** attribute name mising **")
                    elif len(arg) < 4:
                        print("** value missing **")
                    elif arg[2] not in base:
                        obj[arg[2]] = arg[3]
                        # obj["updated_at"] = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
