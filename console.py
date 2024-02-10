#!/usr/bin/env python3
"""
console.py
"""
import re
import cmd
from models.base_model import BaseModel
import shlex
from models import storage
from models.user import User
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
import sys
import json
import ast


class HBNBCommand(cmd.Cmd):
    """
    hbnbcommand
    """

    completekey = "tab"
    prompt = "(hbnb) "
    CC = ["BaseModel", "User", "Amenity", "Place", "Review", "State", "City"]

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        empty line
        """
        pass

    def do_create(self, arg):
        """
        CREATE.
        """
        if not arg:
            print("** class name missing **")
        else:
            if arg not in self.CC:
                print("** class doesn't exist **")
            else:
                SP = shlex.split(arg)
                N = SP[0]
                yues = eval(N)().id
                print(yues)
                storage.save()

    def do_show(self, arg):
        """
        Show
        """
        SP = shlex.split(arg)
        if len(SP) == 0 or len(SP) < 1:
            print("** class name missing **")
        else:
            if SP[0] not in self.CC:
                print("** class doesn't exist **")
            elif len(SP) < 2 or len(SP) == 1:
                print("** instance id missing **")
            else:
                K = "{}.{}".format(SP[0], SP[1])
                if K in storage.all():
                    print(storage.all()[K])
                else:
                    print("** no instance found **")
        return

    def do_destroy(self, arg):
        """destroy"""
        SP = shlex.split(arg)
        D = storage.all()

        if len(SP) == 0 or SP == "" or SP is None:
            print("** class name missing **")
            return
        else:
            if SP[0] not in self.CC:
                print("** class doesn't exist **")
                return
            elif len(SP) == 1 or len(SP) < 2:
                print("** instance id missing **")
                return
            else:
                key = SP[0] + "." + SP[1]
                if key in D:
                    del D[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        ALL
        """
        D = storage.all()

        SP = shlex.split(arg)

        if len(SP) == 0:
            for key, value in D.items():
                print([str(value)])

        elif SP[0] not in self.CC:
            print("** class doesn't exist **")

        else:
            for key, value in D.items():
                if key.split(".")[0] == SP[0]:
                    print([str(value)])

    def do_update(self, arg):
        """
        Updates
        """
        XX = shlex.split(arg)

        if len(XX) == 0:
            print("** class name missing **")
        elif XX[0] not in self.CC:
            print("** class doesn't exist **")
        elif len(XX) < 2:
            print("** instance id missing **")
        else:
            MYclassname, MYinstanceId, MYattributeName, MYname = XX[:4]
            K = f"{MYclassname}.{MYinstanceId}"
            DI = storage.all()
            ineU = DI.get(K)
            if ineU is None:
                print("** no instance found **")
            elif len(XX) < 3:
                print("** attribute name missing **")
            elif len(XX) < 4:
                print("** value missing **")
            else:
                try:
                    AT = type(getattr(ineU, MYattributeName))
                    MYname = AT(MYname)
                except AttributeError:
                    pass
                setattr(ineU, MYattributeName, MYname)
                storage.save()

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""

        TT = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count,
        }
        match = re.search(r"\.", arg)
        if bool(match):
            arg_list = arg.split(".")
            clsS = arg_list[0]
            start, end = match.span()
            arGl = [arg[:start], arg[end:]]

            match = re.search(r"\((.*?)\)", arGl[1])
            if bool(match):
                start, end = match.span()
                command = arg_list[1].split("(")
                cmet = command[0]
                e_arg = command[1].split(")")[0]
                al = e_arg.split(",")
                cotext = arGl[1][:start]
                coarg = match.group()[1:-1]
                command = [cotext, coarg]

                if cmet in TT.keys():
                    if cmet != "update":
                        call = f"{arGl[0]} {e_arg}"
                        return TT[cmet](call)
                    elif len(al) >= 2 and re.search(r"\{.*?\}", e_arg):
                        ob = al[0]
                        ana = al[1:]
                        ana[0] = ana[0].lstrip()
                        for i in range(1, len(ana)):
                            ana[i] = "," + ana[i]
                        jostr = "".join(ana)
                        result_dict = ast.literal_eval(jostr)
                        for k, v in result_dict.items():
                            TT[cmet]("{} {} {} {}".format(clsS, ob, k, v))
                        return ""

                    elif len(al) == 3:
                        ob = al[0]
                        ana = al[1:]
                        for i in range(0, len(ana)):
                            ana[i] = ana[i].lstrip()
                            TT[cmet](
                                "{} {} {} {}".format(clsS, ob, ana[0], ana[1])
                            )
                        return ""

        print(f"*** Unknown syntax: {arg}")

        return False

    def do_count(self, arg):
        """count()"""

        ar = shlex.split(arg)
        if not ar:
            print("** class name missing **")
        elif ar[0] not in self.CC:
            print("** class doesn't exist **")
        else:

            count = sum(1 for x in storage.all().values()
                        if ar[0] == x.__class__.__name__)
            print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
