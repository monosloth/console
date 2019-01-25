from app.commands import AbstractCommand


class OptionalCommand(AbstractCommand):

	def __init__(self, settings, name, alias):
		super().__init__(settings)
		self.name = name
		self.alias = alias

	def attach(self, parser):
		parser.add_argument(
			"-{}".format(self.alias),
			"--{}".format(self.name),
			action='store_true'
        )
