
def factorial(x:int) -> int:
    n = 1
    for i in range(1, x+1):
        n *= i
    return n

def euler(iter_count:int) -> float:
    result = 0
    for i in range(iter_count):
        result += 1/factorial(i)
    return result

print(euler(30))



