class myclass:
    def __init__(self, fullname):
        self.FullName = fullname
        
    def getfullname(self):
        return self.FullName

a= myclass(fullname= 'ABC')
print(a.getfullname())