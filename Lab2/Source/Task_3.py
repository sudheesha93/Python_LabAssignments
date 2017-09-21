#Library Management System

class Library():      # CLASS 1
    def __init__(self):     #_init_ constructor
        pass

    def lib(self):
        libName = "MNLC_UMKC"   # Private data member
        print("Library name is",libName)

class LibraryMembership():      #CLASS 2
    fee="$200"
    def __init__(self):         #_init_ constructor
       print("Membership fee: $200")

class MembershipFee(LibraryMembership):      #CLASS 3 inheriting the class 2

    def __init__(self):     #_init_ constructor
        LibraryMembership.__init__(self)

    def membershipFee(self,isPaid):
        self.isPaid=isPaid
        if (self.isPaid=="true"):
            print("Membership amount of",self.fee,"has been paid")
        else:
            print("Membership amount of", self.fee, "has not been paid")

class StudentDetails(): #CLASS 4
    def __init__(self): #_init_ constructor
        pass

    def studentInfo(self, sName,sID):
        self.sName = sName
        self.sID = sID
        print(self.sName," with student ID is",self.sID)

class BookDetails():    #CLASS 5
    def __init__(self): #_init_ constructor
        pass

    def book(self,bName,bID,bAuthor):
        self.bName=bName
        self.bID=bID
        self.bAuthor=bAuthor
        print("Book "+self.bName+" with ID: "+self.bID+"/ Author: "+self.bAuthor)

class StudentBookDetails(StudentDetails,BookDetails):   # multiple inheritance (#CLASS 6)
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

s1=StudentDetails()
s1.studentInfo("Sudheesha",19)

fee1=MembershipFee()
fee1.membershipFee("true")

b1=StudentBookDetails()
b1.book("Python","20000","Rashmi")
b1.bookDates("09-20-2017","09-29-2017")

l2=Library()
l2.lib()
s2=StudentDetails()
s2.studentInfo("Sindhu",18)
fee2=MembershipFee()
fee2.membershipFee("false")
b2=StudentBookDetails()
b2.book("Deep Learning","20002","VijayaKumari")
b2.bookDates("07-15-2017","07-25-2017")
