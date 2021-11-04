class MyCalendar(object):

    def __init__(self):
        self.cals = []

    def book(self, start, end):
        if not self.cals:
            self.cals.append((start, end))
            return True

        for i in range(len(self.cals)):
            if end <= self.cals[i][0]:
                if i > 0 and self.cals[i-1][1] <= start:
                    self.cals = self.cals[0:i] + [(start, end)] + self.cals[i:]
                    return True
                elif i == 0:
                    self.cals = [(start, end)] + self.cals
                    return True
                return False
        if self.cals[-1][1] > start:
            return False
        self.cals = self.cals + [(start, end)]
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


def solution(inputs):
    obj = MyCalendar()
    for input in inputs:
        print("current", obj.cals, input)
        print(obj.book(*input))


solution([[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]])
