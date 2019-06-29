

def countMoves(numbers):
    
    numlist = []
    for i in range(1,numbers[0]+1):
        numlist.append(numbers[i])
    for i in range(numbers[0]-1):
        if numbers[i] == min(numbers):
            numbers[i] = numbers[i] + 1 
    
    print(min(numlist))
    return numlist

print(countMoves([5,5,6,8,8,5]))

