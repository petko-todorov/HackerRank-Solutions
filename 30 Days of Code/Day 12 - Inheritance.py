class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        results = {
            lambda x: x >= 90: 'O',
            lambda x: x >= 80: 'E',
            lambda x: x >= 70: 'A',
            lambda x: x >= 55: 'P',
            lambda x: x >= 40: 'D',
            lambda x: x < 40: 'T',
        }
        avg_scores = sum(self.scores) / len(self.scores)

        return next(v for k, v in results.items() if k(avg_scores))

# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input())  # not needed for Python
# scores = list(map(int, input().split()))
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade:", s.calculate())
