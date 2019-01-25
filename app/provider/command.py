import yaml

from monosloth.provider import AbstractProvider
from app.singleton import Parser


class CommandProvider(AbstractProvider):

    def register(self):
        """Register all commands with an argument parser.
        """
        parser = Parser()

        with open('./config/commands.yaml') as stream:
            commands = yaml.load(stream)

            for name, data in commands.items():
                args = self.__get_args(data)
                kwargs = self.__get_kwargs(data)

                parser.attach(*args, **kwargs)


    def __get_args(self, data):
        """Build command arguments.

        :param data: The data to extract args from.

        :return: A tuple of args.

        """
        args = ()

        if 'name' in data:
            args += (data['name'],)

        if 'alias' in data:
            args += ('--{}'.format(data['alias']),)

        return args

    def __get_kwargs(self, data):
        """Build command keyword arguments.

        :param data: The data to extract kwargs from.

        :return: A dict of kwargs.

        """
        kwargs = {}

        if 'action' in data:
            kwargs['action'] = data['action']

        if 'type' in data:
            kwargs['type'] = data['type']

        return kwargs
