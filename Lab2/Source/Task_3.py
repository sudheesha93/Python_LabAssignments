#Library Management System

class Library():      # CLASS 1
    def __init__(self):     #_init_ constructor
        pass

    def lib(self):
        libName = "MNLC_UMKC"   # Private data member
        print("Library name is",libName)

class Membership():      #CLASS 2
    fee="$200"
    def __init__(self):         #_init_ constructor
       print("Membership fee: $200")

class MemFee(Membership):      #CLASS 3 inheriting the class 2

    def __init__(self):     #_init_ constructor
        Membership.__init__(self)

    def mFee(self,f):
        self.isPaid=f
        if (self.f=="true"):
            print(self.fee," Membership fee has been paid")
        else:
            print(self.fee, " Membership fee has not been paid")

class SDetails(): #CLASS 4
    def __init__(self): #_init_ constructor
        pass

    def studentInfo(self, sName,sID):
        self.sName = sName
        self.sID = sID
        print(self.sName," with student ID is",self.sID)

class BDetails():    #CLASS 5
    def __init__(self): #_init_ constructor
        pass

    def book(self,bName,bID,bAuthor):
        self.bName=bName
        self.bID=bID
        self.bAuthor=bAuthor
        print("Book "+self.bName+" with ID: "+self.bID+"/ Author: "+self.bAuthor)

class SBDetails(SDetails,BDetails):   # multiple inheritance (#CLASS 6)
    def __init__(self):     #_init_ constructor
        super().__init__()  # use of super keyword

    def bookDates(self,borrowDate,returnDate):
        self.borrowDate = borrowDate
        self.returnDate = returnDate
        print("The book was borrowed on "+self.borrowDate+" and has to be returned on "+self.returnDate)
        print("------------------------------------------------------------------------------")

#instances of classes
l1=Library()
l1.lib()
s1=SDetails()
s1.studentInfo("Sudheesha",19)
fee1=MemFee()
fee1.mFee("true")
b1=SBDetails()
b1.book("Python","20000","Rashmi")
b1.bookDates("09-20-2017","09-29-2017")

l2=Library()
l2.lib()
s2=SDetails()
s2.studentInfo("Sindhu",18)
fee2=MemFee()
fee2.mFee("false")
b2=SBDetails()
b2.book("Deep Learning","20002","VijayaKumari")
b2.bookDates("07-15-2017","07-25-2017")
