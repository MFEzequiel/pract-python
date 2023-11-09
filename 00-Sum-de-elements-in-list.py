"Hobligatorio"

my_list = [1, 2, 3, 4, 5, 7, 8]

def my_def(lst):
    sum = 0

    for num in lst:
        sum += num
        
    return sum

r = my_def(my_list)
print(r)