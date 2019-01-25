from app.command import AbstractCommand


class EchoCommand(AbstractCommand):

	def invoke(self, args):
		print('Hello, world!')
