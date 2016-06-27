# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def get_every_second(basic_list):
        if type(basic_list) is list:
            selected_numbers = list()
            for i in range(len(basic_list)):
                if i % 2 != 0:
                    selected_numbers.append(basic_list[i])
            return selected_numbers
        else:
            return 'Give me list'

my_list = [1, 2, 3, 4, 5]
print(get_every_second(my_list))
