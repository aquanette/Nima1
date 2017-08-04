import os

##########   WRITING FILE OUT   ##########
#open file to write
#open file to read/write
#to_write_file_pointer = open('to_read.txt', 'w')
to_write_file_pointer = open('read_write.txt','w+')
#FOR: number in range from 1 to 10, write the number and a new line to our file
for number in range(1, 10):
    #write number to file (with a new line)
    to_write_file_pointer.write("{0}\n".format(number))
#create a list of letters to output to our file
letters = ['a', 'b', 'c', 'd', 'e']
#FOR: letter in letters from a to e, write letter and a new line to our file
for letter in letters:
    #write letter to file (with a new line)
    to_write_file_pointer.write("{0}\n".format(letter))
#close file
#to_write_file_pointer.close()
to_write_file_pointer.seek(0)
##########   READING FILE IN   ##########
#open file to read
#to_read_file_pointer = open('to_read.txt', 'r')
#open file to write
to_write_file_pointer2 = open('output.txt','w')
#FOR: line in to_read_file_pointer, read and print each line
#for line in to_read_file_pointer:
for line in to_write_file_pointer:
    #print line
    #print("Line: {0}".format(line))
    to_write_file_pointer2.write("Line: {0}".format(line))
#close file
#to_read_file_pointer.close()
to_write_file_pointer.close()
to_write_file_pointer2.close()
#uncomment line below to remove file after reading
#os.remove('to_read.txt')
#ALL DONE!

