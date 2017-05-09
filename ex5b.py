name = 'Mir Umer'
age = 25 # not a lie
height = 74.0 # inches

height_cms=height * 2.54

weight = 70.0 #kgs

weight_pound=weight * 2.20462

eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about '%s'." % name
print "He's %d inches tall." % height
print "He's %d centimeteres tall." % height_cms
print "He's %d kgs in weight." % weight
print "He's %d pounds in weight." % weight_pound
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)
