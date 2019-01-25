import argparse

from monosloth.singleton import MetaSingleton


class Parser(metaclass=MetaSingleton):

    def __init__(self):
        """Instantiate argument parser.
        """
        if not hasattr(self, 'parser'):
            self.parser = argparse.ArgumentParser()

    def attach(self, *args, **kwargs):
        """Bind command argument.

        :param *args: The arguments to bind.
        :param **kwargs: The keyword arguments to bind.

        """
        self.parser.add_argument(*args, **kwargs)

    def parse(self):
        args = self.parser.parse_args()
