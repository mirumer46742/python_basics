def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % (cheese_count)
    print "You have %d boxes of crackers!" % (boxes_of_crackers)
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:" 
cheese_and_crackers(20, 30)

#This function call has been written by me myself
print "We can also ask the users to dynamically provide numbers:" 
x=int(raw_input("Enter First Number: "))
y=int(raw_input("Enter Second Number: "))
cheese_and_crackers(x, y)


print "OR, we can use variables from our script:"
cheese_count = 10
box_of_crackers = 50

cheese_and_crackers(cheese_count, box_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(cheese_count + 100, box_of_crackers + 1000)
