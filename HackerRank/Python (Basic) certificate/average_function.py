import os

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    def avg(num1, *nums):
        numbers_count = len(nums) + 1
        whole_sum = sum([x for x in nums]) + num1
        average = whole_sum / numbers_count
        print(f"{average:.2f}")


    nums = list(map(int, input().split()))
    res = avg(*nums)

    # fptr.write('%.2f' % res + '\n')
    #
    # fptr.close()
