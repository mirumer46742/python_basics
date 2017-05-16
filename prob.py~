mylist=[56700,777,1151,222,121,666,119,152,78111]
length_list=[]
small_list=[]
rem_list=[]
count_list=[]
final_list=[]
last_list=[]
dictionary={}

print '-'*70
print "Actual list:", mylist

#Inserting length of each value in length_list
for num in mylist:
    length_list.append(len(str(num)))
    
#print list with less no. of digits
for num in mylist:
    if min(length_list)==len(str(num)):
        small_list.append(num) 
print '-'*70+"\n"
print "The list with least no. of digits:", small_list
print "\n"+'-'*70


for num in small_list:
    #break numbers in digits and make their remainder list
    while num!=0:        
        rem=num%10
        rem_list.append(rem)
        num=num/10
    #Count the occurances of each digit in number and take their max
    for n in rem_list:
        count_list.append(rem_list.count(n))
    final_list.append(max(count_list))
    #reset count and remainder list after each iteration
    count_list=[]
    rem_list=[]
#print "The List of occurances are:", final_list


#zip() takes corresponding values from two lists
#dict() makes the value pairs a a dictionary
dictionary = dict(zip(small_list, final_list))

#append keys from dictionary to a list which has got max() values
for key,val in dictionary.items():
    if val == max(dictionary.values()):
        last_list.append(key)
                
print "\nThe list of numbers with max. no. of same digits:",last_list
print "\n"+'-'*70

print "The Smallest one:",min(last_list)
print '-'*70
