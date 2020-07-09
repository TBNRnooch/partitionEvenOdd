# partitionEvenOdd
def partitionEvenOddIntegers(numbers):

    for n in numbers:
        if n & 1 == 1:
            numbers.remove(n)
            numbers.append(n)
            
def runTest(numbers):
    print('Input:', numbers)

    partitionEvenOddIntegers(numbers)

    print('Output:', numbers)


def start():
    runTest([7, 7, 4, 0, 9, 8, 2, 4, 1, 9])

start()
