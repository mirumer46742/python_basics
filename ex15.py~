from sys import argv

script = argv

filename=raw_input("Enter the name of file to open in read mode: ")
txt = open(filename)

print "Here's your file %r for reading:" % filename
print txt.read()

print "Type the filename again for writing in it:"
file_again = raw_input("> ")

txt_again = open(file_again,'a+')
text=raw_input("Enter text to write in file: ")
txt_again.write(text)
print("Here is the text of file you wrote to: \n")
print txt_again.read()

