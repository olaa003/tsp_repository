def large_factorial(num):
    arr = [1]
    for i in range(2, num+1):
        carry = 0
        for j in range(len(arr)-1, -1, -1):
            mult = arr[j] * i + carry
            arr[j] = mult % 10
            carry = mult // 10
        while carry:
            arr.insert(0, carry % 10)
            carry //= 10
    return arr



    
