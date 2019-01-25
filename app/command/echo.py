from app.command import OptionalCommand


class EchoCommand(OptionalCommand):

	def __init__(self, settings):
		super().__init__(settings, 'echo', 'echo')

	def action(self, a):
		print('Hello, world!')
