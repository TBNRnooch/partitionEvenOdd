# partitionEvenOdd
def partitionEvenOddIntegers(numbers):
while i<j: 
    # iterate till non-odd (even)
    while (i<j and a[i]%2 !=0):	
    	i+=1
    # iterate till non-even (odd)
    while (i<j and a[j]%2 ==0):	
    	j-=1
    if i != j:
        # swap even with odd
        a[i], a[j] = a[j], a[i]


def runTest(numbers):
    print('Input:', numbers)
    partitionEvenOddIntegers(numbers)
    print('Output:', numbers)


def start():
	runTest([7, 7, 4, 0, 9, 8, 2, 4, 1, 9])

start()
