mylist=[56700,121,1151,222,122,115,666,119,152,156,78111]
length_list=[]
small_list=[]
test_list=[]
rem_list=[]
rem_list2=[]
count_list=[]
count_list2=[]
maximum_list=[]
final_list=[]
index_list=[]
index_list2=[]

print '-'*60+"\n"
print "Actual list is:", mylist

#Inserting length of each value in digit_list
for num in mylist:
    length_list.append(len(str(num)))
    
#print keylist with less digits
for num in mylist:
    if min(length_list)==len(str(num)):
        small_list.append(num) 
print '-'*60+"\n"
print "List of least no. of digits:", small_list
print "\n"+'-'*60

count=0
for num in small_list:
    while num!=0:        
        rem=num%10
        rem_list.append(rem)
        num=num/10 
    #print "Rem List is:",rem_list
    rem_list2.append(rem_list)
    
    for n in rem_list:
        count_list.append(rem_list.count(n))
    #print "Count List is:",count_list
    count_list2.append(count_list)
    index=count_list2.index(max(count_list2))
     
    
    count_list=[]
    rem_list=[]

#for n in count_list2:
#    index_list2.append(max(count_list2))
#   index=count_list2.index(max(count_list2))
    
print "The smallest number with minimum unique numbers:",small_list[index]
print '-'*60
#print "Index List is: ", index_list2
#print "\n Count LIst 2 is:",count_list2 
#print "Rem LIst 2 is:",rem_list2
