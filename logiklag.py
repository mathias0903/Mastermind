import datalag as dl


class LogikLag:
    def __init__(self, brikker=4, muligheder=6, maks=10, *solution):
        self.data = dl.Datalag(brikker=brikker, muligheder=muligheder, maks=maks, *solution)
        self.running = True


    def gæt(self, *gæt):
        if len(gæt) is self.data.getBrikker():
            if all(0 <= value < self.data.getMuligheder() for value in gæt):
                solution = self.data.getSolution()
                for value in range(0, self.data.getMuligheder()):
                    a = gæt.count(value)
                    if a > solution.count(value):
                        a = solution.count(value)
                b = 0
                for value in range(0, self.data.getBrikker()-1):
                    if gæt[value] is solution[value]:
                        b += 1
                return a, b
        return False