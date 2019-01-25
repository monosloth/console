from abc import ABCMeta, abstractmethod

class AbstractCommand(metaclass=ABCMeta):

    @abstractmethod
    def invoke(self, args):
        pass
