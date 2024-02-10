#!/usr/bin/python3
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_show_missing_class(self):
        correct = "** class name missing **"
        commands = ["show", ".show()", ]
        for command in commands:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())

    def test_create_missing_class(self):
        correct = "** class name missing **"
        commands = ["create", "destroy"]
        for command in commands:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())
    def test_destroy_missing_class(self):
        correct = "** class name missing **"
        commands = ["destroy", ".destroy()"]
        for command in commands:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())
                


    
if __name__ == "__main__":
    unittest.main()
