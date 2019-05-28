s = input('input: ')

input = int(s)

def factorial(input):
    if input < 0:
        return false
    elif input == 1:
        return 1
    return input * factorial(input - 1)

# global count
def find_zero(n):
    count = 0
    rev_n = map(int, str(n))
    for i in reversed(rev_n):
        if i == 0:
            count += 1
        else:
            return count
            break

fact = factorial(input)
print find_zero(fact)


