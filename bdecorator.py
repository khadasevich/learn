import os
from datetime import datetime
def statistic(func1):
    """First decorator"""
    def wrap():
        print "Username"
        func1()
        print "Final"
    return wrap
    

@statistic
def username(f = os.getlogin(), d = datetime.today()):
   print f," local date and time: ", d

print username()


