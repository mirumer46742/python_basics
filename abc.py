filename=raw_input("Enter the name of the file: ")
fileheader=open(filename)

dictionary = {}

for one_line in fileheader:
    words_list = one_line.split()
    
    for word in words_list:
      if word not in dictionary:
        dictionary[word] = 1
      else:
        dictionary[word] = dictionary[word] + 1

print "The distinct words and their occurances are:" + "\n" + '.'*50

for  [word , occur]  in dictionary.items(): 
  print [word , occur]
