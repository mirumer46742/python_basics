def binary(n):
    count_list=[]
    rem_list=[]
    count=0
    while n!=0:        
        rem=int(n)%2
        rem_list.append(rem)
        n=int(n)/2
    #Reverses the binary equivalent    
    rem_list.reverse()
    print "The binary equal of number is:",rem_list

    for num in rem_list:
        if num==0:
            count=count+1 
        if num==1:
            count_list.append(count)
            count=0                   
    print "The maximum gap is: ",max(count_list)
    


number=raw_input("Enter any number:")
binary(number)

