# partitionEvenOdd
def partitionEvenOddIntegers(numbers):
    lastOddi = -1
    for i, num in enumerate(numbers):
        if num % 2:
            if lastOddi == -1:
                lastOddi = i
        else:
            # Swap
            if lastOddi != -1:
                numbers[lastOddi], numbers[i] = numbers[i], numbers[lastOddi]
                lastOddi += 1

def runTest(numbers):
    print('Input:', numbers)
    partitionEvenOddIntegers(numbers)
    print('Output:', numbers)

def start():
	runTest([7, 7, 4, 0, 9, 8, 2, 4, 1, 9])

start()
