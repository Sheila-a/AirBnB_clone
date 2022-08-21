#!/usr/bin/env python3
"""program that contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class for interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Enter Ctrl+D to exit the program
        """
        print()
        return True

    def emptyline(self):
        """do nothing if ENTER is pressed"""
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if self.verify_arg(arg, False):
            base = ''
            if 'User' in arg:
                base = User()
            elif 'Place' in arg:
                base = Place()
            elif 'State' in arg:
                base = State()
            elif 'City' in arg:
                base = City()
            elif 'Amenity' in arg:
                base = Amenity()
            elif 'Review' in arg:
                base = Review()
            else:
                base = BaseModel()
            base.save()
            print(base.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        if self.verify_arg(arg, True):
            word = arg.split(' ')
            val = f"{word[0]}.{word[1]}"
            print(storage.all()[val])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if self.verify_arg(arg, True):
            word = arg.split(' ')
            val = f"{word[0]}.{word[1]}"
            del storage.all()[val]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation
        of all instances based or not on the class name
        """
        if arg == '' or self.verify_arg(arg, False):
            lis_str = []
            for key in storage.all().keys():
                if arg == '' or key.startswith(arg):
                    lis_str.append(str(storage.all()[key]))
            print(lis_str)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute (save the change
        into the JSON file). Ex: $ update
        BaseModel 1234-1234-1234 email 'aibnb@mail.com'
        """
        if self.verify_arg(arg, True):
            word = arg.split(' ')
            if len(word) < 3:
                print('** attribute name missing **')
            elif len(word) < 4:
                print('** value missing **')
            else:
                val = f"{word[0]}.{word[1]}"
                obj = storage.all()[val]
                attr = word[2]
                if attr not in ['id', 'created_at',
                                'updated_at']:
                    value = word[3]
                    if value.startswith('"'):
                        x = 3
                        for i in range(x, len(word)):
                            if word[i].endswith('"'):
                                x = i + 1
                                break
                        value = ' '.join(word[3:x])
                        value = value[1:-1]
                    if attr in type(obj).__dict__:
                        try:
                            typ = type(type(obj).__dict__[attr])
                            value = typ(value)
                            obj.__dict__[attr] = value
                            storage.save()
                        except Exception:
                            return False

    def verify_arg(self, arg, idCheck):
        """Checks that arg to a command is correct"""
        if arg == "":
            print("** class name missing **")
            return False
        word = arg.split(' ')
        if word[0] not in ['BaseModel', 'User', 'Place', 'State', 'City',
                           'Amenity', 'Review']:
            print("** class doesn't exist **")
            return False
        if idCheck:
            if len(word) < 2:
                print("** instance id missing **")
                return False
            val = f"{word[0]}.{word[1]}"
            if val not in storage.all():
                print("** no instance found **")
                return False
        return True

    def default(self, line):
        """Method called to handle inputs that are not explicit
        commands"""
        if line.startswith('User.'):
            self.handle_model(line, 'User')
        elif line.startswith('BaseModel.'):
            self.handle_model(line, 'BaseModel')
        elif line.startswith('Place.'):
            self.handle_model(line, 'Place')
        elif line.startswith('Amenity.'):
            self.handle_model(line, 'Amenity')
        elif line.startswith('State.'):
            self.handle_model(line, 'State')
        elif line.startswith('City.'):
            self.handle_model(line, 'City')
        elif line.startswith('Review.'):
            self.handle_model(line, 'Review')

    def handle_model(self, line, modelName):
        """This will handle model commands"""
        spt = line.split('.')
        mtd = spt[1]
        if mtd == 'all()':
            self.do_all(modelName)
        elif mtd == 'count()':
            count = 0
            for key in storage.all().keys():
                if key.startswith(modelName):
                    count += 1
            print(count)
        elif mtd.startswith('show("') and mtd.endswith('")'):
            id = mtd[6:-2]
            arg = f'{modelName} {id}'
            self.do_show(arg)
        elif mtd.startswith('destroy("') and mtd.endswith('")'):
            id = mtd[9:-2]
            arg = f'{modelName} {id}'
            self.do_destroy(arg)
        elif mtd.startswith('update("') and mtd.endswith('")'):
            args = mtd[8:-2].split('"')
            arg = modelName
            for i in args:
                if not i.startswith(','):
                    arg += ' ' + i
            self.do_update(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
