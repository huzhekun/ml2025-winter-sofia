class MyList:
        numbers = []
        def append(self, num):
                self.numbers.append(num)

        def findNumber(self, number):
                index = -1
                for i in range(len(self.numbers)):
                        if number == self.numbers[i]:
                                index = i
                                break
                return index
