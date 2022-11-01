from abc import ABC, abstractmethod


class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def h(self):
        pass


f = Father()
