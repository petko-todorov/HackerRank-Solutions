import math
import os
import random
import sys


def transformSentence(sentence):
    words = sentence.split(" ")

    result = []
    for s in words:
        if len(s) == 1:
            result.append(s)
            continue

        word = f'{s[0]}'
        for i in range(len(s) - 1):
            x = ord(s[i].lower())
            y = ord(s[i + 1].lower())
            if x < y:
                word += s[i + 1].upper()
            elif x > y:
                word += s[i + 1].lower()
            else:
                word += s[i + 1]

        result.append(word)

    print(" ".join(result))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    # fptr.write(result + '\n')

    # fptr.close()
