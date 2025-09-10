class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        # for i in range(len(self.__elements) - 1):
        #     for j in range(i + 1, len(self.__elements)):
        #         difference = abs(self.__elements[i] - self.__elements[j])
        #         if difference > self.maximumDifference:
        #             self.maximumDifference = difference
        self.maximumDifference = max(self.__elements) - min(self.__elements)


# _ = input()
# a = [int(e) for e in input().split(' ')]
#
# d = Difference(a)
# d.computeDifference()
#
# print(d.maximumDifference)
