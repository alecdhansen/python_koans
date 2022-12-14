#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This is very different to AboutModules in Ruby Koans
# Our AboutMultipleInheritance class is a little more comparable
#

from runner.koan import *

from .another_local_module import *
from .local_module_with_all_defined import *


# https://docs.python.org/3/library/sys.html?highlight=modules#sys.modules


class AboutModules(Koan):
    def test_importing_other_python_scripts_as_modules(self):
        from . import local_module  # local_module.py

        duck = local_module.Duck()
        self.assertEqual("Daffy", duck.name)

    def test_importing_attributes_from_classes_using_from_keyword(self):
        from .local_module import Duck

        duck = Duck()  # no module qualifier needed this time
        self.assertEqual("Daffy", duck.name)

    def test_we_can_import_multiple_items_at_once(self):
        from . import jims, joes

        jims_dog = jims.Dog()
        joes_dog = joes.Dog()
        self.assertEqual("jims dog", jims_dog.identify())
        self.assertEqual("joes dog", joes_dog.identify())

    def test_importing_all_module_attributes_at_once(self):
        # NOTE Using this module level import declared at the top of this script:
        #   from .another_local_module import *
        #
        # Import wildcard cannot be used from within classes or functions

        goose = Goose()
        hamster = Hamster()

        self.assertEqual("Mr Stabby", goose.name)
        self.assertEqual("Phil", hamster.name)

    def test_modules_hide_attributes_prefixed_by_underscores(self):
        with self.assertRaises(NameError):
            private_squirrel = _SecretSquirrel()

    def test_private_attributes_are_still_accessible_in_modules(self):
        from .local_module import Duck  # local_module.py

        duck = Duck()
        self.assertEqual("password", duck._password)
        # module level attribute hiding doesn't affect class attributes
        # (unless the class itself is hidden).

    def test_a_module_can_choose_which_attributes_are_available_to_wildcards(self):
        # NOTE Using this module level import declared at the top of this script:
        #   from .local_module_with_all_defined import *

        # 'Goat' is on the __ALL__ list
        goat = Goat()
        self.assertEqual("George", goat.name)

        # How about velociraptors?
        lizard = _Velociraptor()
        self.assertEqual("Cuddles", lizard.name)

        # SecretDuck? Never heard of her!
        with self.assertRaises(NameError):
            duck = SecretDuck()
