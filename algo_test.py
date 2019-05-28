s = input('input: ')
# if not isinstance(s, (int, float)):
#     raise TypeError('bad operand type')
input = list(s)
new_list = []
zero_list = []

def my_abs(input):

    for x in input:
        if x == 0:
            zero_list.append(0)

        else:
            new_list.append(x)

    new_list.extend(zero_list)
    print new_list

my_abs(input)