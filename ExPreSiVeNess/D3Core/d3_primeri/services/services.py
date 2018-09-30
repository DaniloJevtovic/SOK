import abc

class UcitatiService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def naziv(self):
        pass

    @abc.abstractmethod
    def identifier(self):
        pass

    @abc.abstractmethod
    def ucitati(self):
        pass

class Servis(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def naziv(self):
        pass

    @abc.abstractmethod
    def identifier(self):
        pass


class UcitatiServis(Servis):
    @abc.abstractmethod
    def ucitati(self):
        pass


class PrikazatiServis(Servis):
    @abc.abstractmethod
    def prikazati(self):
        pass