# more variables 
# %s - string
# %d - signed decimal integer
#
name = "Chris"
age = 21 # a lie
height = 73 # inches
weight = 183 # lbs
eyes = 'Blue'
teeth = 'white'
hair = 'grey'

# conversion
metric_height = height * 2.54
metric_weight = weight * 0.453

print "Let's talk about %s." % name
print "He's %d inches tall, that's %d cm." % (height, metric_height)
print "He's %d pounds heavy, that's %d kg." % (weight, metric_weight)
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d and %d, I get %d." % ( age, height, weight, age + height + weight)
