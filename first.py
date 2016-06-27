# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def get_every_second(basic_list):
        if type(basic_list) is list:
            selected_numbers = list()
            for i in range(len(basic_list)-1):
                if i % 2 == 0:
                    selected_numbers.append(basic_list[i+1])
            return selected_numbers
        else:
            return 'Give me list'

print(get_every_second([2, 3, 5, 6, 7, 9, 6, 8, 7, 7, 8]))
