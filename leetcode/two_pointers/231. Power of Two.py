def isPowerOfTwo(n: int) -> bool:
    
    if n == 1: return True
    if n == 0 or n % 3 != 0: return False
    return isPowerOfTwo(n/3)


print(isPowerOfTwo(27))
