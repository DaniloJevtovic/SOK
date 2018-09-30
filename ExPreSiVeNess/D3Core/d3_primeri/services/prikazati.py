import  abc


class PrikazatiService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def naziv(self):
        pass

    @abc.abstractmethod
    def identifier(self):
        pass

    @abc.abstractmethod
    def prikazati(self):
        pass