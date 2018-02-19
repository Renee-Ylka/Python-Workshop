money = input ("How much money do you have? (Should be greater than 50000) ")
x = money / 50000
if money < 50000 : print "You cannot buy an iPhone. :("
else:
    print "You can buy", x, "iPhone(s). :)"
    y = money%50000
    Wii = 20000
    z = Wii - y
    print "You need an additional", z, "to buy a Wii."


