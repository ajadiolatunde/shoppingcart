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
dc= cP2.__dict__

print (dc)
def df(street="ola",name="ade"):
    print (street)

df(**dc)

class C:
    dangerous = 2
c1 = C()
c2 = C()

print (c1.dangerous)
c1.dangerous = 3
print (c1.dangerous)
print (c2.dangerous)
del c1.dangerous
print (c1.dangerous)
C.dangerous = 3
print (c2.dangerous)
print (C.__dict__)
print (dir(C))