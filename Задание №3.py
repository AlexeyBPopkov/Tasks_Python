numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def oddQ(n):
    if n % 2 != 0 and n > 50: return True
    return False

print(list(filter(oddQ, numbers)))