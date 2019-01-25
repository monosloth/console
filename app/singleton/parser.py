import argparse

from monosloth.singleton import MetaSingleton


class Parser(metaclass=MetaSingleton):

    def __init__(self):
        """Instantiate argument parser.
        """
        if not hasattr(self, 'parser'):
            self.parser = argparse.ArgumentParser()

    def set_commands(self, commands):
        self.commands = commands

    def attach(self, *args, **kwargs):
        """Bind command argument.

        :param *args: The arguments to bind.
        :param **kwargs: The keyword arguments to bind.

        """
        self.parser.add_argument(*args, **kwargs)

    def parse(self):
        """Invoke the relevant command after parsing the arguments.
        """
        args = vars(self.parser.parse_args())

        for key, value in self.commands.items():
            if value['name'] in args or value['alias'] in args:
                command = resolve(value['module'])
                command.invoke(args)
