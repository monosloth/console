from app.commands import AbstractCommand


class PositionalCommand(AbstractCommand):

	def __init__(self, settings, name, alias, type):
		super().__init__(settings)
		self.name = name
		self.alias = alias
		self.type = type

	def attach(self, parser):
		parser.add_argument(
			"-{}".format(self.alias),
			"--{}".format(self.name),
			action='store',
			type=self.type
        )
