import random


class Datalag:
    def __init__(self, brikker=4, muligheder=6, maks=10, *solution):
        self.brikker = brikker
        self.muligheder = muligheder
        self.maks = maks
        if solution is None or not solution:
            random.seed()
            self.solution = (random.randint(0, muligheder-1) for i in range(brikker))
        else:
            self.solution = solution


    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, value):
        if not isinstance(value, tuple):
            raise TypeError("solution must be a tuple of ints")
        if all(0 <= a < self.muligheder for a in value):
            raise TypeError("solution must be a tuple of ints")
        if len(value) is self.brikker:
            raise ValueError("solution must be the same size as defined in brikker")
        self._solution = value


    @property
    def brikker(self):
        return self._temperature

    @brikker.setter
    def temperature(self, value):
        if not isinstance(value, int):
            raise TypeError("Brikker must be a int")
        self._temperature = value