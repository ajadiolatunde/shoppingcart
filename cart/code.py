from datetime import datetime
def QuestionsMarks(str):
    count_q = 0
    qs = False
    first = ""
    last = ""
    res = False
    for i in str:
        last = i
        if count_q == 3 and i.isdigit() and int(first) + int(last) == 10:
            res = True
            break
        if qs == False:
            if i.isdigit():
                qs = True
                first = i
        else:
            if i == "?":
                count_q += 1
            else:
                if i.isdigit():
                    qs = False
    return res

    # code goes here
    return str


# keep this function call here
file = open("res","r")
data  = file
days = {'Mon-Thu':['Mon','Tues','Thurs'],'Mon-Fri':['Mon','Tues','Thurs']}

for i in data.readlines():
    
    l = i.split(',')
    for j in l[1:]:
        if "Mon" in j:
            print (len(l),l[1:])
            break

file.close()
# from django.utils import timezone
import datetime
time =  datetime.timedelta(days=30)
print (time)

class Me(object):
    count = 0
    all = 0
    def __init__(self):
        setattr(self,"name","tunde")
        self.all += 1
        self.name = "change"

        Me.count += 1
    def findMe(self):
        pass



f = Me()
d = Me()
print (f.__getattribute__('name'))