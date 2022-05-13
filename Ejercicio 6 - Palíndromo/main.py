
def isPal(num):
    numString = str(num)
    for i in range(0,int(len(numString)/2+1)):
        if (numString[i] != numString[-i-1]):
            return False
    return True

maxProduct = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        result = i * j
        if isPal(result):
            if result > maxProduct:
                maxProduct = result

print(maxProduct)