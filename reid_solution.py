
def solution(i):
    prime_string = makePrimeString()
    minion_ID = prime_string[i:i+5]
    return minion_ID

def makePrimeString():
    s=''
    prime = 2
    
    while len(s) < 10005:
        s += str(prime)
        prime += 1
        while not is_prime(prime):
            prime += 1
    return s

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(solution(10000))
