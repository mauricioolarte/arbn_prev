#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = '(hbnb) '
    # intro = '\n'
    
    # def do_prompt(self, line):
    #     "Change the interactive prompt"
    #     self.prompt = line + ': '

    def do_EOF(self, line):
        """ implement exit command whit EOF"""
        return True
    
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()