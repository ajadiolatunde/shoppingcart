class PostalAddress:
    pass

cP1 = PostalAddress()
# Create an Instance for person ABC
cP1.name = "ABC"
cP1.street = "Central Street - 1"

# Create an Instance for person DEF
cP2 = PostalAddress()
cP2.name = "DEF"
cP2.street = "Central Street - 2"

print (cP2.__dict__)