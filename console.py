#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = '(hbnb) '
        
    def do_EOF(self, line):
        """ implement exit command whit EOF"""
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
        elif arg == 'BaseModel':
            new_BaseModel = BaseModel()
            new_BaseModel.save()
            print('{}'.format(new_BaseModel.id))
        else:
            print('** class doesn\'t exist **')
    
    def do_show(self, *args):
        """
            Prints the string representation of an instance based on the class
            name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        if len(args) < 1:
            print('** class name missing **')
        elif args[1] != 'BaseModel':
            print('** class doesn\'t exist **')
        if len(args) == 2 and args[1] == 'BaseModel':
            print('** instance id missing **')
        
        
        else:
            print('** class doesn\'t exist **')

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()