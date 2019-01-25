from app import Settings


class AbstractCommand:

    def __init__(self, settings):
        self.settings = settings

    def action(self, arg):
        pass

    def attach(self, parser):
        pass
