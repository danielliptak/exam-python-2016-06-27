# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

try:
    def note_my_word(file_name, note):
            f = open(file_name, 'a')
            f.write(3 * note)
            f.close()
    note_my_word('note.txt', 'bananaaaa')
except:
    print('Please try again')
