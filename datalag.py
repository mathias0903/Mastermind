import random


class Datalag:
    def __init__(self, brikker=4, muligheder=6, maks=10, solution=None):
        self.brikker = brikker
        self.muligheder = muligheder
        self.maks = maks
        if solution is None:
            random.seed()
            self.solution = tuple(random.randint(0, muligheder-1) for i in range(brikker))
        else:
            self.solution = solution


    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, value):
        if not isinstance(value, tuple):
            raise TypeError("solution must be a tuple of ints")
        if not all(0 <= a <= self.muligheder for a in value):
            raise TypeError("values of solution must be between 0 and muligheder: "+str(self.muligheder))
        if not len(value) is self.brikker:
            raise ValueError("solution must be the same size as defined in brikker")
        self._solution = value


    @property
    def brikker(self):
        return self._brikker

    @brikker.setter
    def brikker(self, value):
        if not isinstance(value, int):
            raise TypeError("Brikker must be a int")
        self._brikker = value

    @property
    def muligheder(self):
        return self._muligheder

    @muligheder.setter
    def muligheder(self, value):
        if not isinstance(value, int):
            raise TypeError("muligheder must be a int")
        self._muligheder = value

    @property
    def maks(self):
        return self._maks

    @maks.setter
    def maks(self, value):
        if not isinstance(value, int):
            raise TypeError("maks must be a int")
        self._maks = value