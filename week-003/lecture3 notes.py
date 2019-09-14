# open: a file by using open(filename, mode)
# some_file_object.close()
# modes:    r - read
#           w - write
#           a - append
#           b - binary 

# Watch out for loading the entire file into memory
# instead, read it line by line and do what you want at each line
input_file = open(input_file_name)
for line in input_file:
    print(len(line))

