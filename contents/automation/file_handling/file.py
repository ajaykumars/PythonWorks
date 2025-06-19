file = open('inputFile.txt', 'r')
pass_file = open('passedList.txt', 'w')
fail_file = open('failedList.txt', 'w')

# print(file.read())

for line in file:
    if line.split()[2] == 'P':
        print(line)
        pass_file.write(line)
    else:
        fail_file.write(line)

file.close()
pass_file.close()
fail_file.close()
