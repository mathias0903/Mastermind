import datalag as dl


class LogikLag:
    def __init__(self, brikker=4, muligheder=6, maks=10, solution=None):
        self.data = dl.Datalag(brikker=brikker, muligheder=muligheder, maks=maks, solution=solution)
        self.running = True


    def gæt(self, *gæt):
        if len(gæt) is self.data.brikker:
            if all(0 <= value < self.data.muligheder for value in gæt):
                solution = self.data.solution
                total_color = 0
                for value in range(0, self.data.muligheder):
                    a = gæt.count(value)
                    if a > solution.count(value):
                        a = solution.count(value)
                    total_color += a
                total_correct = 0
                for value in range(0, self.data.brikker):
                    if gæt[value] is solution[value]:
                        total_correct += 1
                if total_correct==4:
                    return "you owned the libtards"
                return total_color, total_correct
        return False
