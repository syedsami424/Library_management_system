from tabulate import tabulate
import mysql.connector
import datetime
import math

#CREATING THE DATABASE
def create_database():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',charset="utf8",passwd='1234')
    mycursor=mydb.cursor()
    mycursor.execute('create database library')
    mydb.commit()

#CREATING THE TABLES
def create_table_member():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',charset="utf8",database='library')
    mycursor=mydb.cursor()
    com="create table member(MID int(5) primary key,Mname varchar(25),telno int(8),Address varchar(75),DR int(4),BH varchar(1000),DOB date,Gender char(1),DOR date,MS varchar(20),pass char(5))"
    mycursor.execute(com)
def create_table_books():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',charset="utf8",database='library')
    mycursor=mydb.cursor()
    com="create table books(bookid int(5) primary key,bookname varchar(50),genre varchar(50),BS int(2),author varchar(30),price decimal(4,2),plot varchar(10000))"
    mycursor.execute(com)

def create_table_popular_author():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',charset="utf8",database='library')
    mycursor=mydb.cursor()
    com="create table popular_author(author varchar(75) NOT NULL,genre varchar(50))"
    mycursor.execute(com)


#MAIN MENU
def main_menu():
    while True:
        print("======================================================================================================================================================================")
        print('\t\t***\t***\t***\t***\t***\t*******     WELCOME TO VK PUBLIC LIBRARY    *******\t***\t***\t***\t***\t***')
        print('\t\t\t\t\t\t================================*MAIN MENU*===================================')
        print()

        print('\t\t\t\t\t\t\t\t        1. ENTER AS AN EMPLOYEE')
        print('\t\t\t\t\t\t\t\t        2. ENTER AS A MEMBER')
        print('\t\t\t\t\t\t\t\t        3. ENTER AS A GUEST')
        print('\t\t\t\t\t\t\t\t        4. TERMS AND CONDITIONS')
        print()
        print('\t\t\t\t\t\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print()
        c=int(input('ENTER YOUR CHOICE: '))
        print("======================================================================================================================================================================")
        if c==1:
            main_menu_emp()
        elif c==2:
            main_menu_mem()
        elif c==3:
            main_menu_guest()
        elif c==4:
            terms_and_conditions()
        else:
            print()
            print("Oops!, You have entered an invalid key")
            print()
            p=input("Enter any key to start Again")
            main_menu()



#SEARCH FOR A BOOK
from tabulate import tabulate
import mysql.connector
def search_everything_mem():
    def show_plot(bookname,bookid):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select plot from books where bookid='{}'".format(bookid))
            result=mycursor.fetchall()
            print()
            print("=>",bookname)
            print()
            print(result[0][0])
            print()
            print()
            p=input("Enter any key to continue")
            print("**********************************************************************************************************************************************************************")


    def search_bookname1(id):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookname from books where bookid={}".format(id))
        result=mycursor.fetchall()
        return result[0][0]
    def search_bookid(bookname):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid from books where bookname='{}'".format(bookname))
        result=mycursor.fetchall()
        return result[0][0]
    def search_BookID(id):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where bookid={}".format(id))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
        print()
        show_plot(search_bookname1(id),id)

    def search_bookname(name):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select bookid,bookname,author from books where bookname='{}'".format(name))
            result=mycursor.fetchall()
            print()
            if result:
                print("**********************************************************************************************************************************************************************")
                print()
                print()
                print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
                print()
                print()
                print("**********************************************************************************************************************************************************************")
                show_plot(name,search_bookid(name))
            else:
                print("**********************************************************************************************************************************************************************")
                print()
                print()
                print("Sorry, No Book with this Name is in our Records")
                print()
                print()
                print("******************************************************************************************************************************************************************** *")

            print()

    def search_authorname(add):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select bookid,bookname,author from books where author='{}'".format(add))
            result=mycursor.fetchall()
            print("***********************************************************************************************************************************************************************")
            print()
            print()
            print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
            print()
            print()
            print("**********************************************************************************************************************************************************************")
            bookid=int(input("Enter the Book ID of the book for which you would like to see the plot"))
            show_plot(search_bookname1(bookid),bookid)
    def search_genre(gen):
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
           mycursor=mydb.cursor()
           mycursor.execute("select bookid,bookname,genre from books where Genre='{}' order by bookname".format(gen))
           result=mycursor.fetchall()
           print("*********************************************************************************************************************************************************************")
           print()
           print()
           print(tabulate(result,headers=["Book ID","Book Name","Genre"],tablefmt="fancy_grid"))
           print()
           print()
           print("*********************************************************************************************************************************************************************")
           bookid=input("Enter the Book ID of the Book for which you want to View the Plot: ")
           print()
           show_plot(search_bookname1(bookid),bookid)
           print()


    while True:
        print("\n","\n","1.Search the ID of the book","\n","2.Search the Name of the book","\n","3.Search an Author","\n","4.Search a genre","\n","5.Exit to Member Menu","\n","\n")
        print()
        option=int(input("Enter the number that corresponds to the option you want to choose: "))
        if option==1:
            mid=int(input("Enter the Book ID: "))
            search_BookID(mid)
        elif option==2:
            name=input("Enter the name of the book to be searched: ")
            name=name.upper()
            search_bookname(name)
        elif option==3:
            add=input("Enter the name of the author to be searched: ")
            add=add.upper()
            search_authorname(add)
        elif option==4:
            genre=input("Enter The Genre: ")
            genre=genre.upper()
            search_genre(genre)
        elif option==5:
            main_menu_mem()
        else:
            print("Oops!, It look like you have entered an invalid option")
            p=input("Enter any key to coninue")
            print()
            search_everything_mem()

#UPDATE MEMBER DETAILS
def update_everything_mem(MID):
    import mysql.connector
    from tabulate import tabulate
    def UpdateMembername(MID,name):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()
        print()
        print()

        print("**********************************************************************************************************************************************************************************")

        print(tabulate(result,headers=['MID','MName','telno','Address','DR','BH','DOB','Gender'],tablefmt='fancy_grid'))
        print()
        print()

        print("**********************************************************************************************************************************************************************************")



        M=input("Do you want to change the member name(yes-y or no-n)")
        if M in "Yy":
            query="update member set Mname='{}' where MID={}".format(name,MID)
            mycursor.execute(query)
            mydb.commit()
        if M in "Nn":
           print("Ok, nothing was changed.")
        else:
            print("You may try later")
            return
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()
        print()
        print()

        print("**********************************************************************************************************************************************************************************")

        print(tabulate(result,headers=['MID','MName','telno','Address','DR','BH','DOB','Gender'],tablefmt='fancy_grid'))
        print()
        print()

        print("**********************************************************************************************************************************************************************************")


    def UpdateMembertel(MID,telno):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()

        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()
        print("YOUR EXISTING DETAILS ARE.....")
        print()
        print(tabulate(result,headers=['MID','MName','telno','Address','DR','BH','DOB','Gender'],tablefmt='fancy_grid'))


        M=input("Do you want to change the telephone number(Yes or No)")
        M=M.upper()
        if M in "Y":
            query="update member set telno={} where MID={}".format(telno,MID)
            mycursor.execute(query)
            mydb.commit()
        elif M in "N":
            print("Ok, nothing was changed")
        else:
            print("you may try later")
            return
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()

        print("**********************************************************************************************************************************************************************")

        print()
        print()
        print("YOUR NEW DETAILS ARE.......")
        print()
        print(tabulate(result,headers=['MID','MName','telno','Address','DR','BH','DOB','Gender'],tablefmt='fancy_grid'))
        print()
        print()

        print("**********************************************************************************************************************************************************************")



    def UpdateMemberadd(MID,add):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()

        print("**********************************************************************************************************************************************************************************")

        print()
        print()

        print(tabulate(result,headers=['MID','MName','telno','Address','DR','BH','DOB','Gender'],tablefmt='fancy_grid'))
        print()
        print()

        print("**********************************************************************************************************************************************************************************")



        M=input("do you want to change the address(y or n)")
        if M in "Yy":
            query="update member set Address='{}' where MID={}".format(add,MID)
            mycursor.execute(query)
            mydb.commit()
        elif M in "Nn":
            print("Ok, nothing was changed")
        else:
            print("you may try later")
            return
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()
        print(tabulate(result,headers=['MID','MName','telno','Address','DR','BH','DOB','Gender'],tablefmt='fancy_grid'))

    while True:
        print("\t\t\t\t\t\t\t\t        UPDATE MEMBER DETAILS")
        print("*********************************************************************************************************************************************************************")

        print("\n","1.Update the name of a customer","\n","2.Update the Telephone No. of a customer","\n","3.Update the Address of a customer","\n","4.Exit to Member Menu")
        print()
        option=int(input("Enter the number that corresponds to the option you want to choose: "))
        if option==1:
            name=(input("Enter the new Member Name: "))
            name=name.upper()
            UpdateMembername(mid,name)
        elif option==2:
            telno=input("Enter the new Telephone No. of the customer: ")
            UpdateMembertel(mid,telno)
        elif option==3:
            add=input("Enter the new address of customer: ")
            add=add.upper()
            UpdateMemberadd(mid,add)
        elif option==4:
            main_menu_mem()
        else:
            break


#CANCEL A MEMBERSHIP
def cancelMID(MID):
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='library')
        mycursor=mydb.cursor()
        mycursor.execute('select*from member where MID={}'.format(MID))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        print()
        M=input('Are you sure you want to cancel this membership(Yes or No): ')
        M=M.upper()
        if M=="YES":
            query="update member set MS='DEACTIVATED' where MID={}".format(MID)
            mycursor.execute(query)
            mydb.commit()
            print()
            print()
            print("This Record has been successfully Deleted")
            print()
            print()
        else:
            print('Please try later.')
            print()
            return


        print("**********************************************************************************************************************************************************************")




#DISPLAY DUES REMAINING
def show_duesremaining(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("select DR from member where MID='{}' order by Mname".format(MID))
    result=mycursor.fetchall()
    print("**********************************************************************************************************************************************************************")
    print()
    print("Your Currect Dues Remaining is BHD: ",result[0][0])
    print()
    if result[0][0]>=40:
        print("Please Note that your membership will automatially be suspended if your dues exceed BHD 50")
    print()
    print("**********************************************************************************************************************************************************************")



#BORROW A BOOK
def borrow_book(MID):
    from tabulate import tabulate
    def search_MID(id):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender,DOR,MS from member where MID='{}' order by Mname".format(id))
        result=mycursor.fetchall()

        print("**********************************************************************************************************************************************************************")

        print()
        print()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        print()
        print()

        print("***********************************************************************************************************************************************************************")



    def check_return(mid):

        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="select DOR from member where MID={}".format(mid)
        mycursor.execute(query)
        result=mycursor.fetchall()
        if result[0][0]:
            return False
        else:
            return True



    import datetime
    def date_diff(a,b,c,d):
        p=d-a
        if p>7:
            a=a+7
            return (a,b,c)
        elif p<7 and b==12:
            c+=1
            b=1
            a=7-p
            return (a,b,c)
        elif p<7:
            b=b+1
            a=7-p
            return(a,b,c)



    def leap_year(D,year):
        if year%4==0 and year%100!=0 or year%400==0:
            for k in D:
                if k==2:
                    D[k]=29

    def doret():
        tdate=datetime.date.today()
        print("THE DATE OF BORROWING: ",tdate)
        D={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        c=tdate.year
        leap_year(D,c)
        a=tdate.day
        b=tdate.month
        for k in D:
            if b==k:
                x=date_diff(a,b,c,D[k])
                p=str(x[0])
                q=str(x[1])
                r=str(x[2])
                if len(q)!=2:
                     q="0"+q
                if len(p)!=2:
                    p="0"+p
                date="{}-{}-{}".format(r,q,p)
                print("THE DATE OF RETURNING: ",date)
                return date
                break

    import mysql.connector
    def borrow_book4(MID):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="select Mname from member where MID={}".format(MID)
        mycursor.execute(query)
        result=mycursor.fetchall()
        return result[0][0]

    def borrow_book2(book,MID):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        Mname=borrow_book4(MID)
        query="update member set BH='{}' where MID={}".format(book,MID)
        mycursor.execute(query)
        mydb.commit()

    def borrow_book3(book):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="update books set BS=BS-1 where bookname='{}'".format(book)
        mycursor.execute(query)
        mydb.commit()
        print()

    def borrow_book5(MID):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        date=doret()
        query="update member set DOR='{}' where MID={}".format(date,MID)
        mycursor.execute(query)
        mydb.commit()


    def borrow_book1(MID):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        if check_return(MID):
            book=input("Enter Book you wish to borrow: ")
            book=book.upper()
            query="select BS from books where bookname='{}'".format(book)
            mycursor.execute(query)
            result=mycursor.fetchall()
            if result[0][0]!=0:
                borrow_book2(book,MID)
                borrow_book3(book)
                borrow_book5(MID)
                search_MID(MID)
            else:
                print("Please wait until this book is returned.")
        else:
            print("Please return the previous book that you borrowed.")
    def borrow_book_plot(MID,bookname):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        if check_return(MID):
            query="select BS from books where bookname='{}'".format(bookname)
            mycursor.execute(query)
            result=mycursor.fetchall()
            if result[0][0]!=0:
                borrow_book2(bookname,MID)
                borrow_book3(bookname)
                borrow_book5(MID)
                search_MID(MID)
            else:
                print("Please wait until this book is returned.")
        else:
            print("Please return the previous book that you borrowed.")
    def search_everything_mem():
        def show_plot(bookname,bookid):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select plot from books where bookid='{}'".format(bookid))
            result=mycursor.fetchall()
            if result[0]:
                print()
                print("=>",bookname)
                print()
                print(result[0][0])
                print()
                choice=input("Do you want to borrow this book? (Yes/No): ")
                choice=choice.upper()
                if choice=="YES":
                    borrow_book_plot(MID,bookname)
            else:
                print("Sorry, The plot for this book is unavailable")
            print()
            p=input("Enter any key to continue")

        def search_bookname1(id):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select bookname from books where bookid={}".format(id))
            result=mycursor.fetchall()
            return result[0][0]
        def search_bookname(name):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select bookid,bookname,author from books where bookname='{}'".format(name))
            result=mycursor.fetchall()
            print()
            if result:
                print("********************************************************************************************************************************************************************************************")
                print()
                print()
                print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
                print()
                print()
                print("********************************************************************************************************************************************************************************************")
            else:
                print("********************************************************************************************************************************************************************************************")
                print()
                print()
                print("Sorry, No Book with this Name is in our Records")
                print()
                print()
                print("********************************************************************************************************************************************************************************************")

            print()

            p=input("Enter any key to continue")
        def search_authorname(add):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select bookid,bookname,author from books where author='{}'".format(add))
            result=mycursor.fetchall()
            print("********************************************************************************************************************************************************************************************")
            print()
            print()
            print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
            print()
            print()
            print("********************************************************************************************************************************************************************************************")
            bookid=input("Enter the Book ID of the Book for which you want to View the Plot: ")
            k=search_bookname1(bookid)
            print(k)
            show_plot(search_bookname1(bookid),bookid)


        def search_genre(genre):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select bookid,bookname,genre from books where genre='{}'".format(genre))
            result=mycursor.fetchall()
            print("**********************************************************************************************************************************************************************")
            print()
            print()
            print(tabulate(result,headers=["Book ID","Book Name","Genre"],tablefmt="fancy_grid"))
            print()
            print()
            print("**********************************************************************************************************************************************************************")
            print()
            k=input("Do you want to see the plot of any book(Yes/No): ")
            k=k.upper()
            print()
            if k=="YES":
                bookid=input("Enter the Book ID of the Book for which you want to View the Plot: ")
                show_plot(search_bookname1(bookid),bookid)
            else:
                print("Okay, please proceed to borrowing...")
                print()
        def show_all_genres():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            query="select distinct genre from books"
            mycursor.execute(query)
            result=mycursor.fetchall()
            if result:
                print("**********************************************************************************************************************************************************************")
                print()
                print()
                print(tabulate(result,headers=["Available Genres"],tablefmt="fancy_grid"))
                print()
                print()
                print("**********************************************************************************************************************************************************************")
            else:
                print("******************************************************************************************************************************************************************************************")
                print()
                print()
                print("Enter any key to continue")
                print()
                print()
                print("******************************************************************************************************************************************************************************************")
        def show_all_authors():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            print("**************************************************************************************************************************************************************************")
            print()
            print()
            print("This is a list of some popular Authors that you might be of your interest")
            print()
            print()
            print("**************************************************************************************************************************************************************************")
            query="select author,genre from popular_author"
            mycursor.execute(query)
            result=mycursor.fetchall()
            print("**********************************************************************************************************************************************************************************************")
            print()
            print()
            print(tabulate(result,headers=["Author Name","Genre"],tablefmt="fancy_grid"))
            print()
            print()
            print("**********************************************************************************************************************************************************************************************")
            p=input("Enter any key to continue")
        while True:
            print("\n","1.Search the Name of the book that you want to Borrow","\n","2.Search based on the Genre of the Book","\n","3.Search Based on The Author of the Book","\n","4.Proceed to Borrowing your Book","\n","5.Go back to to Member menu","\n","6.Exit to Log-in screen")
            print()
            print()
            option=int(input("Enter the number that corresponds to the option you want to choose"))
            if option==1:
                name=input("Enter the name of the book to be searched: ")
                name=name.upper()
                search_bookname(name)
            elif option==2:
                show_all_genres()
                genre=input("Enter The Genre: ")
                genre=genre.upper()
                search_genre(genre)
            elif option==3:
                show_all_authors()
                add=input("Enter the name of the author to be searched: ")
                add=add.upper()
                search_authorname(add)
            elif option==4:
                borrow_book1(MID)
            elif option==5:
                main_menu_mem()
            elif option==6:
                main_menu()
            else:
                print("********************************************************************************************************************************************************************************************")
                print()
                print()
                print("Oops!, It seems Like you have entered an invalid key, Please try again later")
                p=input("Enter any key to continue: ")
                print()
                print()
                print("********************************************************************************************************************************************************************************************")
    search_everything_mem()














#RETURN A BOOK
import mysql.connector
from tabulate import tabulate

def return_book_set_null(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    query="update member set DOR=NULL where MID='{}'".format(MID)
    mycursor.execute(query)
    mydb.commit()

def show_BH(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    query="select Mname from member where MID={}".format(MID)
    mycursor.execute(query)
    result=mycursor.fetchall()
    return result[0][0]
    print("**********************************************************************************************************************************************************************")
    print()
    print("Your Currect Dues Remaining is BHD:",result[0][0])
    print()
    print("**********************************************************************************************************************************************************************")



def return_book(MID):
    def find_record(MID):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="select MID,Mname,telno,BH,DOR from member where MID={}".format(MID)
        mycursor.execute(query)
        result=mycursor.fetchall()
        return [result[0][3],result[0][4]]

    def show_record(MID):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="select MID,Mname,telno,BH,DOR from member where MID={}".format(MID)
        mycursor.execute(query)
        result=mycursor.fetchall()
        print("**********************************************************************************************************************************************************************")
        print()
        print()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Book To be returned","Expected Date of Return"],tablefmt="fancy_grid"))
        print()
        print()
        print("**********************************************************************************************************************************************************************")
        print()


    def find_BID(bookname):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="select bookid from books where bookname='{}'".format(bookname)
        mycursor.execute(query)
        result=mycursor.fetchall()
        return result[0][0]


    def add(MID,cost):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="update member set DR=DR+{} where MID={}".format(cost,MID)
        mycursor.execute(query)
        mydb.commit()

    def return_bookID(MID,bookid): #return book by entering bookid
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        choice=input("Are you sure you want to return this book?(yes or no): ")
        choice=choice.upper()
        if choice=="YES":
            return_book_set_null(MID)
            query="update books set BS=BS+1 where bookid={}".format(bookid)
            mycursor.execute(query)
            mydb.commit()
            print()
            print("Book was successfully returned")
            print()
            p=input("Enter any Key to return to the Main Menu")
            main_menu_mem()
        elif choice=="NO":
            print("Ok, nothing was changed.")
        else:
            print("Please Try Again Later….")
            return_book(MID)

    def check_number(x):
        if x<0:
            x=math.fabs(x)
            x=int(x)
        return x


    def check_BNAME(a,b):
        if a!=b:
            return False
        else:
            return True

    def return_bookName(MID,Bname): #return book by entering bookname
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        choice=input("Are you sure you want to return this book?(yes or no): ")
        choice=choice.upper()
        if choice=="YES":
            return_book_set_null(MID)
            query="update books set BS=BS+1 where bookname='{}'".format(Bname)
            mycursor.execute(query)
            mydb.commit()
            print()
            print("Book was successfully returned")
            print()
            p=input("Enter any Key to return to the Main Menu")
            main_menu_mem()
        elif choice=="NO":
            print("Ok, nothing was changed")
        else:
            print("Please Try Again Later")
            return_book(MID)


    while True:
        date=datetime.date.today()
        tdate_day=date.day      #Todays Day
        tdate_month=date.month  # Month
        tdate_year=date.year    # Year
        BNAME=find_record(MID)
        BID=find_BID(BNAME[0])
        RDATE_day=BNAME[1].day  #Day of return
        RDATE_month=BNAME[1].month
        RDATE_year=BNAME[1].year
        print()
        if BNAME[1]:
            show_record(MID)
            print("\n","1.Return The Book using its Book ID","\n","2.Return The Book using the Book Name","\n","3.Exit to Member Menu","\n","4.Exit to Main Menu","\n")
            print()
            days=tdate_day-RDATE_day
            months=tdate_month-RDATE_month
            years=tdate_year-RDATE_year

            days=check_number(days)
            months=check_number(months)
            years=check_number(years)
            if days>=1 or months>=1 or years>=1:
                cost=days*0.2 + months*2 + years*20
                print("An Amount of BHD",cost," has been credited to your account as late submission fee")
                print()
                add(MID,cost)
            A=int(input("Enter your choice: "))
            if A==1:
                bookid=int(input("Enter your Book Id: "))
                print()
                if bookid==BID:
                    return_bookID(MID,bookid)
                else:
                    print("Oops!, This isn't the same bookid of the book that you have borrowed")
                    print()
                    p=input("Enter any key to Try Again")
                    print()
                    return_book(MID)
            elif A==2:
                bookname=input("Enter the borrowed book's name: ")
                bookname=bookname.upper()
                print()
                if bookname==str(BNAME[0]):
                    return_bookName(MID,bookname)
                else:
                    print("Oops!, This isn't the same Book Name of the book that you have borrowed")
                    print()
                    p=input("Enter any key to Try Again")
                    print()
                    return_book(MID)
            elif A==3:
                main_menu_mem()
            elif A==4:
                main_menu()
            else:
                print("Oops!, it looks like you have entered an invalid key")
                i=input("Enter any key to continue")
                return_book(MID)
        else:
            print("You Have not borrowed a book yet")
            print()
            print("Please Enyer Option 4 to borrow a book when you are in the Member Menu")
            print()
            p=input("Enter any key to return to the Main Menu")
            main_menu_mem()



def show_latestbook(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    query="select BH,DOR from member where MID={}".format(MID)
    mycursor.execute(query)
    result=mycursor.fetchall()
    print("**********************************************************************************************************************************************************************")
    print()
    print("The Latest Book that you borrowed is: ",result[0][0])
    if result[0][1]:
        print()
        print("To be returned on :",result[0][1])
    print()
    print("**********************************************************************************************************************************************************************")




def check_MS(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("select MS from member where MID={}".format(MID))
    result=mycursor.fetchall()
    if result[0][0] in ["DEACTIVATED","SUSPENDED"]:
        print("Oops!, it looks like this record isn't a Member of this Library Anymore")
        print("Please Contact the Front Desk for Further Info on this matter")
        print()
        p=input("Enter any key to Exit to Login Screen")
        main_menu()
    else:
        return True

def greeting(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("select Mname,Gender from member where MID={}".format(MID))
    result=mycursor.fetchall()
    if result[0][1]=="M":
        return "Welcome Mr.",result[0][0]
    elif result[0][1]=="F":
        return "Welcome Ms.",result[0][0]
    else:
        return "Welcome",result[0][0]


def password(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("select pass from member where MID={}".format(MID))
    result=mycursor.fetchall()
    password=input("Enter Your Password: ")
    if password==result[0][0]:
        return True
    else:
        print("Incorrect Password")
        print("Please re-login and try again")
        print()
        p=input("Enter any key to continue")
        main_menu()
def suspend_now(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("update member set MS='SUSPENDED' where MID={}".format(MID))
    mydb.commit()

def auto_suspend(MID):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("select DR,MS from member where MID={}".format(MID))
    result=mycursor.fetchall()
    if result[0][0]>50 and result[0][1]!="DEACTIVATED":
        suspend_now(MID)
        print("Oops!, it looks like this record isn't a Member of this Library Anymore")
        print("Please Contact the Front Desk for Further Info on this matter")
        print()
        p=input("Enter any key to Exit to Login Screen")
        main_menu()
    else:
        return True


#MAIN MENU MEM(FINAL)
def main_menu_mem():
    while True:
        print("                                                                    GREETINGS...HOPE YOU ARE DOING GOOD!")
        print("*********************************************************************************************************************************************************************")
        print()
        print()
        MID=int(input("ENTER YOUR 5-DIGIT MEMBER ID: "))
        if auto_suspend(MID):
            if check_MS(MID):
                if password(MID):
                    print()
                    print()
                    print("**********************************************************************************************************************************************************************")
                    print("**********************************************************************************************************************************************************************")
                    print("**********************************************************************************************************************************************************************")
                    print("\t\t\t\t\t\t\t\t\t",greeting(MID)[0],greeting(MID)[1])
                    print()
                    print()

                    print('1:SEARCH FOR A BOOK')
                    print()
                    print('2:CANCEL MY MEMBERSHIP')
                    print()
                    print("3:UPDATE MY DETAILS")
                    print()
                    print('4:BORROW A BOOK')
                    print()
                    print('5:RETURN A BOOK')
                    print()
                    print('6:DISPLAY MY DUES REMAINING')
                    print()
                    print('7:DISPLAY MY LATEST BORROWED BOOK')
                    print()
                    print('8.QUIT')
                    print()
                    print()
                    print("======================================================================================================================================================================")
                    print()
                    print()
                    c=int(input('Enter your Choice: '))
                    print("**********************************************************************************************************************************************************************")

                    if c==1:
                        print("\t\t\t\t\t\t\t\t        SEARCH FOR A BOOK")
                        print("**********************************************************************************************************************************************************************")
                        search_everything_mem()
                    elif c==2:
                        print("\t\t\t\t\t\t\t\t        CANCEL MEMBERSHIP")
                        print("**********************************************************************************************************************************************************************")
                        cancelMID(MID)
                    elif c==3:
                        print("\t\t\t\t\t\t\t\t        UPDATE A CUSTOMER'S DETAILS")
                        print("**********************************************************************************************************************************************************************")
                        update_everything_mem(MID)
                    elif c==4:
                        print("\t\t\t\t\t\t\t\t        BORROW A BOOK")
                        print("**********************************************************************************************************************************************************************")
                        borrow_book(MID)
                    elif c==5:
                        print("\t\t\t\t\t\t\t\t        RETURN A BOOK")
                        print("**********************************************************************************************************************************************************************")
                        return_book(MID)
                    elif c==6:
                        print("\t\t\t\t\t\t\t\t        DISPLAY MY DUES REMAINING")
                        print("**********************************************************************************************************************************************************************")
                        show_duesremaining(MID)
                    elif c==7:
                        print("\t\t\t\t\t\t\t\t        DISPLAY MY LATEST BORROWED BOOK")
                        print("**********************************************************************************************************************************************************************")
                        show_latestbook(MID)
                    elif c==8:
                        print("                                                                    THANK YOU, STAY SAFE AND HAVE A NICE DAY!")
                        print()
                        print()
                        main_menu()
                    else:
                        print('Oops! You must’ve pressed the wrong key, please try again...')
                        command=input('Press any key: ')
                        print()
                else:
                    print("\n","Enter 1 to exit to the Main Menu","\n","Enter 2 to try again","\n")
                    p=input("Enter your choice: ")
                    if p==1:
                        main_menu()
                    else:
                        main_menu_mem()
            print()
            print()
            k=input('Press any key to return back to the Menu: ')



def main_menu_emp1():
    while True:
                print()
                print()
                print("======================================================================================================================================================================")
                print("\t\t\t\t\t\t\t\t        EMPLOYEE MENU")
                print("======================================================================================================================================================================")
                print()
                print('1: SHOW ALL ACTIVE MEMBERS: ')
                print()
                print('2: OPEN A NEW MEMBERSHIP (Customer)')
                print()
                print('3: SEARCH FOR A CUSTOMER')
                print()
                print('4: SEARCH FOR A BOOK')
                print()
                print('5: CANCEL CUSTOMER MEMBERSHIP')
                print()
                print('6: SUSPEND AN ACTIVE MEMBERSHIP')
                print()
                print('7: REACTIATE A DEACTIVATED/SUSPENDED MEMBERSHIP')
                print()
                print('8: MODIFY A CUSTOMERS DETAILS')
                print()
                print('9: ADD FEE TO A CUSTOMERS ACCOUNT')
                print()
                print('10: PAYMENT OF DUES BY A CUSTOMER')
                print()
                print('11: BOOK RELATED')
                print()
                print('12: ADD A NEW POPULAR AUTHOR')
                print()
                print('13: QUIT')
                print()
                print("======================================================================================================================================================================")
                print()
                print()
                c=int(input('Enter your Choice: '))
                print("**********************************************************************************************************************************************************************")
                if c==1:
                    print("\t\t\t\t\t\t\t\t        LIST OF ACTIVE MEMBERS")
                    print("**********************************************************************************************************************************************************************")
                    member_list()



                elif c==2:
                    print("\t\t\t\t\t\t\t\t        OPEN A NEW MEMBER MEMBERSHIP")
                    print("**********************************************************************************************************************************************************************")
                    appendlib1()
                elif c==3:
                    print("\t\t\t\t\t\t\t\t        SEARCH FOR A CUSTOMER")
                    print("**********************************************************************************************************************************************************************")
                    search_record_emp()
                elif c==4:
                    print("\t\t\t\t\t\t\t\t        SEARCH FOR A BOOK")
                    print("**********************************************************************************************************************************************************************")
                    search_everything_emp()
                elif c==5:
                    print("\t\t\t\t\t\t\t\t        CANCEL A CUSTOMER MEMBERSHIP")
                    print("**********************************************************************************************************************************************************************")
                    delete_record_emp()
                elif c==6:
                    print("\t\t\t\t\t\t\t\t        SUSPEND AN ACTIVE MEMBERSHIP")
                    print("**********************************************************************************************************************************************************************")
                    suspend_record()
                elif c==7:
                    print("\t\t\t\t\t\t\t\t        REACTIVATE A SUSPENDED MEMBERSHIP")
                    print("**********************************************************************************************************************************************************************")
                    unsuspend_record()

                elif c==8:
                    print("\t\t\t\t\t\t\t\t        MODIFY A CUSTOMERS DETAILS")
                    print("**********************************************************************************************************************************************************************")
                    update_everything_emp()
                elif c==9:
                    print("\t\t\t\t\t\t\t\t        ADD FEE TO CUSTOMERS ACCOUNT")
                    print("**********************************************************************************************************************************************************************")
                    print("\n","1.Update the Monthly Fee for all Customers","\n","2.Update the dues(UNIQUELY FOR A MEMBER)","\n","3.Return to Employee Menu","\n","4.Return to Main Menu")
                    print()
                    k=int(input("Enter the choice: "))
                    if k==1:
                        print()
                        x=int(input("Enter the Amount to be credited for all customers: "))
                        updatedues(x)
                    elif k==2:
                        print()
                        a=int(input("Enter the MID of the person: "))
                        print()
                        b=input("Enter their fee: ")
                        updateduesindividual(a,b)
                    elif k==3:
                        main_menu_emp1()
                    elif k==3:
                        main_menu()
                    else:
                        print("You have entered an Invalid key")
                        print()
                        p=input("Enter any key to exit to return to the main menu")
                        main_menu()
                elif c==10:
                    print("\t\t\t\t\t\t\t\t        PAYMENT OF DUES BY A CUSTOMER")
                    print("**********************************************************************************************************************************************************************")
                    MID=int(input("Enter the Member ID of the customer: "))
                    payback(MID)
                elif c==11:
                    print("\t\t\t\t\t\t\t\t        BOOK RELATED")
                    print("**********************************************************************************************************************************************************************")
                    book()
                elif c==12:
                    print("\t\t\t\t\t\t\t\t        ADD A NEW POPULAR AUTHOR")
                    print("**********************************************************************************************************************************************************************")
                    popular_author()
                elif c==13:
                    main_menu()
                else:
                    print('Oops! You must’ve pressed the wrong key, please try again.')
                    command=input('Press any key.')
                    main_menu_emp1()
                k=input('Press any key to continue to the Main Menu.')
                main_menu()


#OPEN A MEMBERSHIP
import mysql.connector
import datetime
from tabulate import tabulate
def member_list():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    query="select MID,Mname,telno,Address,DOB,Gender from member where MS='MEMBER'"
    mycursor.execute(query)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Date of Birth","Gender"],tablefmt="fancy_grid"))
    print()
    print("**********************************************************************************************************************************************************************")


def find_MID():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    query="select*from member"
    mycursor.execute(query)
    result=mycursor.fetchall()
    for k in result:
        pass

    if result:
        return k[0]+ 1
    else:
        return 10001



def search_MID1(id):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("select MID,MName,telno,Address,DOB,Gender,MS,pass from member where MID='{}' order by Mname".format(id))

    print()
    print()
    result=mycursor.fetchall()
    print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Date of Birth","Gender","Member Status","Password"],tablefmt="fancy_grid"))
def existencecheck(name,dob,gender):
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    query="select*from member where Mname='{}' and DOB='{}' and Gender='{}'".format(name,dob,gender)
    mycursor.execute(query)
    result=mycursor.fetchall()
    if result:
        print()
        print("THIS ACCOUNT ALREADY EXISTS, YOUR MEMBERSHIP ID IS: ",result[0][0])
        print()
        search_MID1(result[0][0])
        return 0
    else:
        return 1




def appendlib1():
    print()
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
    mycursor=mydb.cursor()
    MID=find_MID()
    MName=input("Enter the name of the member: ")
    print()
    MName=MName.upper()
    MTel=int(input("Enter the Telephone Number of the Member: "))
    print()
    MAddress=input("Enter the Member's Address (Eg: Delhi,India): ")
    MAddress=MAddress.upper()
    print()
    print("Enter the Following details based on your Date of Birth (in numeric form)")
    print()
    year=input("Enter the Year: ")
    month=input("Enter the Month: ")
    date=input("Enter the Date: ")
    if len(month)!=2:
        month="0"+month
    if len(date)!=2:
        date="0"+date
    DOB="{}-{}-{}".format(year,month,date)
    MGender=input("Enter the gender (M/F): ")
    MGender=MGender.upper()
    password=input("Enter your password (Please make sure your password is relatively unique): ")
    d=existencecheck(MName,DOB,MGender)
    if d==1:
        query="insert into member(MID,MName,telno,Address,DOB,Gender,DR,MS,pass)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        record=(MID,MName,MTel,MAddress,DOB,MGender,0,'MEMBER',password)
        mycursor.execute(query,record)
        mydb.commit()
        print("**********************************************************************************************************************************************************************")
        print("\t\t\t\t\t\t\t\t       Your Member ID is ",MID)
        print("**********************************************************************************************************************************************************************")
        search_MID1(MID)
        print()
        print()
        print("\t\t\t\t\t\t\t\t       Welcome",MName,"to the World of Books!")
        print()
        print()
        print("\t\t\t\t\t\t\t\t       Your record has now been saved into our database.... ")
    else:
        print()
        print("Be alert, this person may be a fraud who's trying to get the member's password")
        print()
def popular_author():
    def display_popular_author():
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="select*from popular_author"
        mycursor.execute(query)
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Author","Genre"],tablefmt="fancy_grid"))
        p=input("Enter any key to continue")

    def insert_popular_author():
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        author=input("Enter the Name of Author: ")
        author=author.upper()
        print()
        genre=input("Enter the Genre: ")
        genre=genre.upper()
        print()
        query="insert into popular_author values('{}','{}')".format(author,genre)
        mycursor.execute(query)
        mydb.commit()
        display_popular_author()

    def remove_popular_author():
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        name=input("Enter the name of the Author")
        print()
        query="select*from popular_author where author='{}'".format(name)
        mycursor.execute(query)
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Author","Genre"],tablefmt="fancy_grid"))
        choice=input("Are You sure you want to remove this Author? (Yes/No ")
        choice=choice.upper()
        if choice=="YES":
            query="delete from popular_author where author='{}'".format(name)
            mycursor.execute(query)
            print()
            print("This Record has been Successfully Deleted")
            print()
        elif choice=="NO":
            print()
            print("Okay, Nothing was deleted")
            print()
        else:
            print("Oops!, It looks like you have entered an invalid key")
            print()
        p=input("Enter any key to continue")
    while True:
        print()
        print("\n","1. Show all Records","\n","2. Add a New Record","\n","3. Delete a Record","\n","4. Exit to Member Menu","\n","5. Exit to Main Menu","\n")
        choice=int(input("Enter your choice"))

        if choice==1:
            display_popular_author()
        elif choice==2:
            insert_popular_author()
        elif choice==3:
            remove_popular_author()
        elif choice==4:
            main_menu_emp1()
        elif choice==5:
            main_menu()
        else:
            print("Oops, it looks like you have created an invalid option")
            print()
            p=input("Enter any key to continue")
            popular_author()

#search for a customer
import mysql.connector
from tabulate import tabulate
def search_record_emp():
    def search_MID(mid):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender,DOR,MS from member where MID={} order by Mname".format(mid))
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        else:
            print("No Member has this ID, Try Entering the Member's Full Name")
        print()
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_record_emp()
        else:
            print("Ok, have a nice day")
            main_menu_emp1()


    def search_name(name):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender,DOR,MS from member where Mname='{}' order by Mname".format(name))
        result=mycursor.fetchall()
        if result:
            print("**********************************************************************************************************************************************************************")
            print()
            print()
            print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date Of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
            print()
            print()
            print("**********************************************************************************************************************************************************************")



        else:
            print("No Member has this Name, Try Entering the Member's Full Name")
        print()
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_record_emp()
        else:
            print("Ok, have a nice day")
            main_menu_emp1()



    def search_address(add):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender,DOR,MS from member where Address='{}' order by Mname".format(add))
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        else:
            print("No Member has this Address")
        print()
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_record_emp()
        elif choice=="NO":
            print("Ok, nothing was changed")

        else:
            print("Ok, have a nice day")
            main_menu_emp1()

    def search_sus():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender,DOR,MS from member where MS='SUSPENDED'")
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        else:
            print("No Suspended Members")
        print()
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_record_emp()
        elif choice=="NO":
            print("Ok, nothing was changed")
        else:
            print("Ok, have a nice day")
            main_menu_emp1()

    def search_deact():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender,DOR,MS from member where MS='DEACTIVATED'")
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        else:
            print("No Deactivated Members")
        print()
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_record_emp()
        else:
            print()
            print()
            print("Ok, have a nice day")
            print()
            print()
            main_menu_emp1()
    def search_book_members():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender,DOR,MS from member where DOR IS NOT NULL")
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        else:
            print("No Book Holding Members")
        print()
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_record_emp()
        else:
            print()
            print()
            print("Ok, have a nice day")
            print()
            print()
            main_menu_emp1()






    while True:

        print("\n","1.Search the Member ID of a customer","\n","2.Search the Name of a customer","\n","3.Search the Address of a customer","\n","4.Search Members who have borrowed a Book","\n","5.Search all Suspended Members","\n","6.Search all Deactivated","\n","7.Exit to Employee Menu","\n","8.Exit to Login Screen")
        print()
        option=int(input("Enter the number that corresponds to the option you want to choose: "))
        print()
        if option==1:
            mid=int(input("Enter the Member ID: "))
            search_MID(mid)
        elif option==2:
            name=input("Enter the name of customer to be searched: ")
            search_name(name)
        elif option==3:
            add=input("Enter the address of customer: ")
            search_address(add)
        elif option==4:
            search_book_members()
        elif option==5:
            search_sus()
        elif option==6:
            search_deact()
        elif option==7:
            main_menu_emp1()
        elif option==8:
            main_menu()
        else:
            print("Oops!, It seems like you have entered an invalid option")
            print()
            print("Please Try Again")
            print()
            print("*****************************************************")
            print()




#SEARCH FOR A BOOK
from tabulate import tabulate
import mysql.connector
def search_everything_emp():
    def search_BookID(id):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where bookid={}".format(id))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_emp()
        else:
            print("Ok, have a nice day")
            main_menu_emp1()


    def search_bookname(name):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where bookname='{}'".format(name))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_emp()
        else:
            print("Ok, have a nice day")
            main_menu_emp1()

    def search_authorname(add):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where author='{}'".format(add))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_emp()
        else:
            print("Ok, have a nice day")
            main_menu_emp1()
    def search_genre(gen):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where genre='{}' order by bookname".format(gen))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Genre"],tablefmt="fancy_grid"))
        choice=input("Do you want to continue your search(Yes/No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_emp()
        else:
            print("Ok, have a nice day")
            main_menu_emp1()




    while True:

        print("\n","\n","1.Search the ID of a book","\n","2.Search the Name of a book","\n","3.Search an Author and their books","\n","4.Search a Genre","\n","5.Exit to Employee Menu","\n","6.Exit to Login screen")
        print()
        option=int(input("Enter the number that corresponds to the option you want to choose: "))
        if option==1:
            mid=int(input("Enter the Book id: "))
            search_BookID(mid)
        elif option==2:
            name=input("Enter the name of the book to be searched: ")
            search_bookname(name)
        elif option==3:
            add=input("Enter the name of the author to be searched: ")
            search_authorname(add)
        elif option==4:
            gen=input("Enter a genre: ")
            search_genre(gen)
        elif option==5:
            main_menu_emp1()
        elif option==6:
            main_menu()
        else:
            print("Oops!, It looks like you have entered an invalid key")
            p=input("Enter any key to continue")
            search_everything_emp()


def unsuspend_record():
    import mysql.connector
    from tabulate import tabulate
    def cancelMID(MID):
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='library')
        mycursor=mydb.cursor()
        mycursor.execute('select*from member where MID={}'.format(MID))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))

        print()
        M=input('Are you sure you want to reactivate this membership(Yes or No): ')
        M=M.upper()
        if M=="YES":
            query="update member set MS='MEMBER' where MID={}".format(MID)
            mycursor.execute(query)
            mydb.commit()
            print()
            print("This Record has been successfully reactivated")
        else:
            print('Please try later.')
            return

        print("*******************************************")
        print()
        print()



    import mysql.connector
    import mysql.connector
    from tabulate import tabulate
    def cancelMname():
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='library')
        mycursor=mydb.cursor()
        Mname=input('Enter the name of the customer to activate Membership')
        Mname=Mname.upper()
        mycursor.execute("select*from member where Mname='{}'".format(Mname))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))

        print()
        M=input('Are you sure you want to activate this membership(Yes or No): ')
        M=M.upper()
        if M=="YES":
            query="update member set MS='MEMBER' where Mname='{}'".format(Mname)
            mycursor.execute(query)
            mydb.commit()
            print()
            print("This Record has been successfully activated")
        else:
            print('Please try later.')
            return
        print("*******************************************")
        print()
        print()


    while True:
        print("\n","1.Activate by Member ID","\n","2.Activate by Member Name","\n","3.Return to Employee Menu","\n","4.Return to Login Screen","\n")
        n=int(input("Enter the Number which corresponds to the option that you want to choose"))
        if n==1:
            MID=int(input("Enter Member ID"))
            cancelMID(MID)
        elif n==2:
            cancelMname()
        else:
            break



def suspend_record():
    import mysql.connector
    from tabulate import tabulate
    def cancelMID(MID):
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='library')
        mycursor=mydb.cursor()
        mycursor.execute('select*from member where MID={}'.format(MID))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        print()
        M=input('Are you sure you want to suspend this membership(Yes or No): ')
        M=M.upper()
        if M=="YES":
            query="update member set MS='SUSPENDED' where MID={}".format(MID)
            mycursor.execute(query)
            mydb.commit()
            print()
            print("This Record has been successfully Suspended")
        else:
            print('Please try later.')
            return

        print("*******************************************")
        print()
        print()



    import mysql.connector
    import mysql.connector
    from tabulate import tabulate
    def cancelMname():
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='library')
        mycursor=mydb.cursor()
        Mname=input('Enter the name of the customer to suspend Membership')
        Mname=Mname.upper()
        mycursor.execute("select*from member where Mname='{}'".format(Mname))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        print()
        M=input('Are you sure you want to suspend this membership(Yes or No): ')
        M=M.upper()
        if M=="YES":
            query="update member set MS='SUSPENDED' where Mname='{}'".format(Mname)
            mycursor.execute(query)
            mydb.commit()
            print()
            print("This Record has been successfully Suspended")
        else:
            print('Please try later.')
            return
        print("*******************************************")
        print()
        print()


    while True:
        print("\n","1.Suspend by Member ID","\n","2.Suspend by Member Name","\n","3.Return to Employee Menu","\n","4.Return to Login Screen","\n")
        n=int(input("Enter the Number which corresponds to the option that you want to choose"))
        if n==1:
            MID=int(input("Enter Member ID"))
            cancelMID(MID)
        elif n==2:
            cancelMname()
        elif n==3:
            main_menu_emp1()
        elif n==4:
            main_menu()
        else:
            print("Oops!, It looks like you have entered an invalid key")
            print()
            p=input("Enter any key to try again")
            suspend_record()




def show_table111(MID):
    mydb=mysql.connector.connect(host='localhost',user='root',charset="utf8",passwd='1234',database='library')
    mycursor=mydb.cursor()
    mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender from member where MID={}".format(MID))
    result=mycursor.fetchall()
    print()
    print("**********************************************************************************************************************************************************************")
    print("YOUR RECORD HAS NOW CHAMGED TO............")
    print(tabulate(result,headers=['Member ID','Member Name','Telephone number','Address','Dues Remaining','Book History','Date of Birth','Gender'],tablefmt='fancy_grid'))
    print("**********************************************************************************************************************************************************************")
    print()

def reduce_DR(MID,dues):
    mydb=mysql.connector.connect(host='localhost',user='root',charset="utf8",passwd='1234',database='library')
    mycursor=mydb.cursor()
    query="update member set DR=DR-{} where MID={}".format(dues,MID)
    mycursor.execute(query)
    mydb.commit()
    print()
    show_table111(MID)

def payback(MID):
    mydb=mysql.connector.connect(host='localhost',user='root',charset="utf8",passwd='1234',database='library')
    mycursor=mydb.cursor()
    mycursor.execute("select MID,Mname,telno,Address,DR,BH,DOB,Gender from member where MID={}".format(MID))
    result=mycursor.fetchall()
    print()
    print()
    print("**********************************************************************************************************************************************************************")
    print()
    print()
    print(tabulate(result,headers=['Member ID','Member Name','Telephone number','Address','Dues Remaining','Book History','Date of Birth','Gender'],tablefmt='fancy_grid'))
    print()
    print()
    print("**********************************************************************************************************************************************************************")
    print()
    k=int(input("Enter the amount that the customer has paid: "))
    print()
    reduce_DR(MID,k)
    print()





def delete_record_emp():
    import mysql.connector
    from tabulate import tabulate
    def cancelMID(MID):
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='library')
        mycursor=mydb.cursor()
        mycursor.execute('select*from member where MID={}'.format(MID))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        print()
        M=input('Are you sure you want to cancel this membership(Yes or No): ')
        M=M.upper()
        if M=="YES":
            query="update member set MS='DEACTIVATED' where MID={}".format(MID)
            mycursor.execute(query)
            mydb.commit()
            print()
            print("This Record has been successfully Deleted")
        else:
            print('Please try later.')
            return

        print("*******************************************")
        print()
        print()



    import mysql.connector
    import mysql.connector
    from tabulate import tabulate
    def cancelMname():
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='library')
        mycursor=mydb.cursor()
        Mname=input('Enter the name of the customer to cancel Membership')
        Mname=Mname.upper()
        mycursor.execute("select*from member where Mname='{}'".format(Mname))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Member ID","Member Name","Telephone Number","Address","Dues Remaining","Book History","Date of Birth","Gender","Date of Return","Member Status"],tablefmt="fancy_grid"))
        print()
        M=input('Are you sure you want to cancel this membership(Yes or No): ')
        M=M.upper()
        if M=="YES":
            query="update member set MS='DEACTIVATED' where Mname='{}'".format(Mname)
            mycursor.execute(query)
            mydb.commit()
            print()
            print("This Record has been successfully Deleted")
        else:
            print('Please try later.')
            return
        print("*******************************************")
        print()
        print()


    while True:
        print("\n","\n","1.Cancel by Member ID","\n","2.Cancel by Member Name","\n","3.Return to Employee Menu","\n","4.Return to Login Screen","\n","\n")
        n=int(input("Enter the Number which corresponds to the option that you want to choose"))
        if n==1:
            MID=int(input("Enter Member ID"))
            cancelMID(MID)
        elif n==2:
            cancelMname()
        elif n==3:
            main_menu_emp1()
        elif n==4:
            main_menu()
        else:
            print("Oops!,It Looks like you have entered an invalid key")
            p=input("Enter any key to continue")
            delete_record_emp()

#UPDATE DETAILS
def update_everything_emp():
    import mysql.connector
    from tabulate import tabulate
    def UpdateMembername(MID,name):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()
        print("**********************************************************************************************************************************************************************")
        print()
        print()
        print("YOUR EXISTING DETAILS ARE....")
        print()
        print(tabulate(result,headers=['Member ID','Member Name','Telephone Number','Address','Dues Remaining','Book History','Date Of Birth','Gender','Date of Return',"Member Status"],tablefmt='fancy_grid'))


        M=input("Do you want to change the member name(Yes or No: )")
        M=M.upper()
        if M=="YES":
            query="update member set Mname='{}' where MID={}".format(name,MID)
            mycursor.execute(query)
            mydb.commit()
        else:
            print("You may try later....")
            return
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()
        print(tabulate(result,headers=['Member ID','Member Name','Telephone Number','Address','Dues Remaining','Book History','Date of Birth','Gender','Date of Return',"Member Status"],tablefmt='fancy_grid'))
        choice=input("Do you want to continue your search(Yes/No): ")
        choice=choice.upper()
        if choice=="YES":
            update_everything()
        else:
            print("Ok, have a nice day  :) ")
            main_menu_emp1()


    def UpdateMembertel(MID,telno):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()

        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()

        print("**********************************************************************************************************************************************************************")
        print()
        print()
        print("YOUR EXISTING DETAILS ARE......")
        print()

        print(tabulate(result,headers=['Member ID','Member Name','Telephone Number','Address','Dues Remaining','Book History','Date of Birth','Gender','Date of Return','Gender','Member Status'],tablefmt='fancy_grid'))
        print()
        print()

        print("**********************************************************************************************************************************************************************")


        M=input("Do you want to change the telephone number(Yes or No): ")
        M=M.upper()
        if M=="YES":
            query="update member set telno={} where MID={}".format(telno,MID)
            mycursor.execute(query)
            mydb.commit()
        elif M in "Nn":
            print()
            print()
            print("Ok, nothing was changed.......")
            print()
            print()
        else:
            print()
            print()
            print("YOU MAY TRY LATER........")
            print()
            print()
            return
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()

        print("**********************************************************************************************************************************************************************")
        print()
        print()
        print("YOUR NEW DETAILS ARE......")
        print()
        print(tabulate(result,headers=['Member ID','Member Name','Telephone Number','Address','Dues Remaining','Book History','Date of Birth','Gender','Date of Return','Gender','Member Status'],tablefmt='fancy_grid'))
        print()
        print()

        print("*********************************************************************************************************************************************************************")
        print()
        print()
        choice=input("Do you want to continue your search(Yes/No): ")
        choice=choice.upper()
        if choice=="YES":
            update_everything()
        else:
            print()
            print()
            print("Ok, have a nice day  :) ")
            print()
            print()
            main_menu_emp1()


    def UpdateMemberadd(MID,add):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()

        print("**********************************************************************************************************************************************************************************")
        print()
        print()

        print(tabulate(result,headers=['Member ID','Member Name','telno','Address','Dues Remaining','Book History','Date of Birth','Gender','Date of Return','Gender','Member Status'],tablefmt='fancy_grid'))
        print()
        print()

        print("**********************************************************************************************************************************************************************************")


        M=input("Do you want to change the address(Yes or No): ")
        M=M.upper()
        if M=="YES":
            query="update member set Address='{}' where MID={}".format(add,MID)
            mycursor.execute(query)
            mydb.commit()
        elif M=="No":
            print("Ok, nothing was changed.....")
        else:
            print("you may try later.....")
            return
        mycursor.execute("select * from member where MID={}".format(MID))
        result=mycursor.fetchall()
        print(tabulate(result,headers=['Member ID','Member Name','telno','Address','Dues Remaining','Book History','Date of Birth','Gender','Date of Return','Gender','Member Status'],tablefmt='fancy_grid'))
        choice=input("Do you want to continue your search(Yes/No: )")
        choice=choice.upper()
        if choice=="YES":
            update_everything()
        else:
            print("Ok, have a nice day   :) ")
            main_menu_emp1()
    print()

    print()
    mid=int(input("Please Enter the Member's five digit MID: "))
    search_MID1(mid)
    while True:
        print()
        print()

        print("\n","1.Update the Name of a Customer","\n","2.Update the Telephone No. of a Customer","\n","3.Update the Address of a Customer","\n","4.Exit")
        print()
        print()
        option=int(input("Enter the number that corresponds to the option you want to choose: "))
        if option==1:
            print()
            name=(input("Enter the new Member Name: "))
            name=name.upper()
            UpdateMembername(mid,name)
        elif option==2:
            print()
            telno=input("Enter the new Telephone No. of the customer: ")
            UpdateMembertel(mid,telno)
        elif option==3:
            print()
            add=input("Enter the new address of customer: ")
            add=add.upper()
            UpdateMemberadd(mid,add)
        else:
            break

#UPDATE DUES
def updatedues(x):
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="library")
    mycursor=mydb.cursor()
    query="update member set DR=DR+{}".format(x)
    print()
    print("An Amount of BD",x," has been credited to every member account")
    print()
    mycursor.execute(query)
    mydb.commit()

def updateduesindividual(a,b):
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="library")
    mycursor=mydb.cursor()
    query="update member set DR=DR+{} where MID={}".format(b,a)
    mycursor.execute(query)
    mydb.commit()
    print()

def checking_if_books():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="library")
    mycursor=mydb.cursor()
    query="select*from books"
    mycursor.execute(query)
    result=mycursor.fetchall()
    if result==[]:
        print("Note to User: You Do not have any Records of Books in the Database,Kindly do the Needful")
        print()
        p=input("Press any key to continue")
        print()


#APPEND INTO BOOK TABLE(new book)
import mysql.connector
def book():
    def new_book():
        import datetime
        import mysql.connector
        from tabulate import tabulate

        def find_BID():
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            query="select*from books"
            mycursor.execute(query)
            result=mycursor.fetchall()
            for k in result:
                pass

            if result:
                return k[0]+1
            else:
                return 10001



        def search_BID(id):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select bookid,bookname,genre,BS,author,price  from books where bookid='{}'".format(id))
            result=mycursor.fetchall()
            print("**********************************************************************************************************************************************************************************")
            print()
            print()

            print(tabulate(result,headers=["Book ID","Book Name","Genre","Quantity","Author","Price"],tablefmt="fancy_grid"))
            print()
            print()

            print("**********************************************************************************************************************************************************************************")


        def show_plot(bookname,bookid):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select plot from books where bookid='{}'".format(bookid))
            result=mycursor.fetchall()
            print("=>",bookname)
            print()
            print()
            print(result[0][0])
            print()
            print()

        def update_BS(bookid,b):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            query="update books set BS=BS+{} where bookid={}".format(b,bookid)
            mycursor.execute(query)
            mydb.commit()
        import mysql.connector
        from tabulate import tabulate

        def check_book(bookname,genre,author):
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            query="select*from books"
            mycursor.execute(query)
            result=mycursor.fetchall()

            for k in result:
                pass
                if k[1]==bookname:
                    if k[2]==genre:
                        if k[5]==author:
                            update_BS(k[0])
                        return 1

        def return_BID(BName):
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select bookid from books where bookname='{}'".format(BName))
            result=mycursor.fetchall()
            return result[0][0]


        def appendlib2():
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            BID=find_BID()
            BName=input("Enter the name of the book: ")
            BName=BName.upper()
            Authorname=input("Enter the name of the author: ")
            Authorname=Authorname.upper()
            Genre=input("Enter the genre of the book: ")
            Genre=Genre.upper()
            price=int(input("Enter price of the book: "))
            a=check_book(BName,Genre,Authorname)
            b=int(input("Enter the number of books to be added to the stock: "))
            plot=input("Enter the Plot of the books")
            if a==1:
                print("This book already exists")
                print()
                BID=return_BID(Bname)
                update_BS(BID,b)
            else:
                BID=find_BID()
                query="insert into books(bookid,bookname,author,genre,price,BS,plot)values(%s,%s,%s,%s,%s,%s,%s)"
                record=(BID,BName,Authorname,Genre,price,1,plot)
                mycursor.execute(query,record)
                mydb.commit()
                update_BS(BID,b-1)
            print()
            search_BID(BID)
            show_plot(BName,BID)
            print()
            print()
            print()
            print("         Your book ID is ",BID)
            print("         Remember to Wash your Hands")
            print("         Your record has now been saved into our database.")
        appendlib2()

    def show_genre(bookid):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,genre from books where bookid={}".format(bookid))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Genre"],tablefmt="fancy_grid"))
        p=input("Enter any key to continue")

    def show_bookname(bookid):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname from books where bookid={}".format(bookid))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name"],tablefmt="fancy_grid"))
        p=input("Enter any key to continue")



    def show_authorname(bookid):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where bookid={}".format(bookid))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
        p=input("Enter any key to continue")


    def show_price(bookid):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,price from books where bookid={}".format(bookid))
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Price"],tablefmt="fancy_grid"))
        p=input("Enter any key to continue")




    def change_genre(bookid):
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            genre=input("Enter the new genre of book: ")
            genre=genre.upper()
            query="update books set Genre='{}' where bookid={}".format(genre,bookid)
            mycursor.execute(query)
            mydb.commit()
            print("The Genre has been changed to",genre)
            show_genre(bookid)
    def change_bookname(bookid):
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            name=input("Enter the new name of book: ")
            name=name.upper()
            query="update books set bookname='{}' where bookid={}".format(name,bookid)
            mycursor.execute(query)
            mydb.commit()
            print("The name of the book has been changed to",name)
            show_bookname(bookid)
    def change_authorname(bookid):
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            name=input("Enter the new name of the Author: ")
            name=name.upper()
            query="update books set author='{}' where bookid={}".format(name,bookid)
            mycursor.execute(query)
            mydb.commit()
            print("The name of the author has been changed to",name)
            show_authorname(bookid)
    def change_price(bookid):
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
            mycursor=mydb.cursor()
            pri=int(input("Enter the new price of the book::-"))
            query="update books set price={} where bookid={}".format(pri,bookid)
            mycursor.execute(query)
            mydb.commit()
            print("The price of the book has been changed to",pri)
            show_price(bookid)
    def change_BS(bookid):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        pri=int(input("Enter the new Quantity of the book: "))
        query="update books set BS='{}' where bookid={}".format(pri,bookid)
        mycursor.execute(query)
        mydb.commit()
        print("The Quantity of the book has been changed to",pri)

    def show_table(bid):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        print()
        query="select bookid,boOkname,genre,BS,author,price from books where bookid={}".format(bid)
        mycursor.execute(query)
        result=mycursor.fetchall()
        print(tabulate(result,headers=["Book ID","Book Name","Genre","Quantity","Author","Price"],tablefmt="fancy_grid"))

    def show_plot(bid):
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="select bookname,plot from books where bookid={}".format(bid)
        mycursor.execute(query)
        result=mycursor.fetchall()
        print()
        print("=>",result[0][0])
        print()
        print(result[0][1])

    def change_plot(bid):
        print()
        show_plot(bid)
        print()
        plot=input("Enter the New Plot for this Book: ")
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        query="update books set plot='{}' where bookid={}".format(plot,bid)
        mycursor.execute(query)
        mydb.commit()
        show_table(bid)
        print()
        show_plot(bid)
        print()
        p=input("Enter any key to continue")




    while True:
        checking_if_books()
        print("\n","1.Append a New Book","\n","2.Change the Name of a Book","\n","3.Change the Genre of a Book","\n","4.Change the Author of a Book","\n","5.Change the Price of a Book","\n","6.Change the Quantity of the Book","\n","7.Change the plot for a book","\n","8.Return to the Employee Menu","\n","9.Return to Main Menu")
        print()
        option=int(input("Enter the option which correcponds to your choice: "))

        if option==1:
            new_book()
        elif option in [2,3,4,5,6]:
            bid=int(input("Enter The Book ID: "))
            show_table(bid)
            if option==2:
                change_bookname(bid)
            elif option==3:
                change_genre(bid)
            elif option==4:
                change_authorname(bid)
            elif option==5:
                change_price(bid)
            elif option==6:
                change_BS(bid)
        elif option==7:
            bid=int(input("Enter the Book ID: "))
            change_plot(bid)
        elif option==8:
            main_menu_emp1()
        elif option==9:
            main_menu()
        else:
            print("Oops!, It looks like you have entered an invalid key")
            z=input("Please Enter key to Continue")
            book()



def main_menu_emp():
    n=5
    while n:
        password=input("Enter The Password: ")
        if password=="AASS":
            while True:
                print()
                print()
                print("======================================================================================================================================================================")
                print("\t\t\t\t\t\t\t\t\t        EMPLOYEE MENU")
                print("======================================================================================================================================================================")
                print('1: DISPLAY ALL ACTIVE MEMBERS')
                print()
                print('2: OPEN A NEW MEMBERSHIP (Customer)')
                print()
                print('3: SEARCH FOR A CUSTOMER')
                print()
                print('4: SEARCH FOR A BOOK')
                print()
                print('5: CANCEL CUSTOMER MEMBERSHIP')
                print()
                print('6: SUSPEND AN ACTIVE MEMBERSHIP')
                print()
                print('7: REACTIATE A DEACTIVATED/SUSPENDED MEMBERSHIP')
                print()
                print('8: MODIFY A CUSTOMERS DETAILS')
                print()
                print('9: ADD FEE TO A CUSTOMERS ACCOUNT')
                print()
                print('10: PAYMENT OF DUES BY A CUSTOMER')
                print()
                print('11: BOOK RELATED')
                print()
                print('12: ADD A NEW POPULAR AUTHOR')
                print()
                print('13: QUIT')
                print()
                print()
                print("======================================================================================================================================================================")
                print()
                print()
                c=int(input('Enter your Choice: '))
                print()
                print("**********************************************************************************************************************************************************************")

                if c==1:
                    print("\t\t\t\t\t\t\t\t        LIST OF ACTIVE MEMBERS")
                    print("**********************************************************************************************************************************************************************")
                    member_list()
                elif c==2:
                    print("\t\t\t\t\t\t\t\t        OPEN A NEW MEMBER MEMBERSHIP")
                    print("**********************************************************************************************************************************************************************")
                    appendlib1()
                elif c==3:
                    print("\t\t\t\t\t\t\t\t        SEARCH FOR A CUSTOMER")
                    print("**********************************************************************************************************************************************************************")
                    search_record_emp()
                elif c==4:
                    print("\t\t\t\t\t\t\t\t        SEARCH FOR A BOOK")
                    print("**********************************************************************************************************************************************************************")
                    search_everything_emp()
                elif c==5:
                    print("\t\t\t\t\t\t\t\t        CANCEL A CUSTOMER MEMBERSHIP")
                    print("**********************************************************************************************************************************************************************")
                    delete_record_emp()
                elif c==6:
                    print("\t\t\t\t\t\t\t\t        SUSPEND AN ACTIVE MEMBERSHIP")
                    print("**********************************************************************************************************************************************************************")
                    suspend_record()
                elif c==7:
                    print("\t\t\t\t\t\t\t\t        REACTIVATE A SUSPENDED MEMBERSHIP")
                    print("**********************************************************************************************************************************************************************")
                    unsuspend_record()
                elif c==8:
                    print("\t\t\t\t\t\t\t\t        MODIFY A CUSTOMERS DETAILS")
                    print("**********************************************************************************************************************************************************************")
                    update_everything_emp()
                elif c==9:
                    print("\t\t\t\t\t\t\t\t        ADD FEE TO CUSTOMERS ACCOUNT")
                    print("**********************************************************************************************************************************************************************")
                    print("\n","1.Update the Monthly Fee for all Customers","\n","2.Update the dues(UNIQUELY FOR A MEMBER)","\n","3.Return to Employee Menu","\n","4.Return to Main Menu")
                    print()
                    k=int(input("Enter the choice: "))
                    if k==1:
                        print()
                        x=int(input("Enter the Amount to be credited for all customers: "))
                        updatedues(x)
                    elif k==2:
                        print()
                        a=int(input("Enter the MID of the person: "))
                        print()
                        b=input("Enter their fee: ")
                        updateduesindividual(a,b)
                    elif k==3:
                        main_menu_emp1()
                    elif k==3:
                        main_menu()
                    else:
                        print("You have entered an Invalid key")
                        print()
                        p=input("Enter any key to exit to return to the main menu")
                        main_menu()
                elif c==10:
                    print("\t\t\t\t\t\t\t\t        PAYMENT OF DUES BY A CUSTOMER")
                    print("**********************************************************************************************************************************************************************")
                    MID=int(input("Enter the Member ID of the customer: "))
                    payback(MID)
                elif c==11:
                    print("\t\t\t\t\t\t\t\t        BOOK RELATED")
                    print("**********************************************************************************************************************************************************************")
                    book()
                elif c==12:
                    print("\t\t\t\t\t\t\t\t        ADD A NEW POPULAR AUTHOR")
                    print("**********************************************************************************************************************************************************************")
                    popular_author()
                elif c==13:
                    main_menu()
                else:
                    print('Oops! You must’ve pressed the wrong key, please try again.')
                k=input('Press any key to continue to the Main Menu.')



        else:
            print("Incorrect Password, Try Again")
            print()
        n-=1
    print("You have typed the incorrect password 5 times")
    print("Please Try Again in 20 Seconds")
    for k in range(580000000):
        pass
    print()
    main_menu_emp()

#Main menu guest
def main_menu_guest():
    print("\t\t\t\t\t\t\t\t        GUEST MENU")
    search_everything_guest()

from tabulate import tabulate
import mysql.connector
def search_everything_guest():
    print("======================================================================================================================================================================")
    def plot(BID):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookname,plot from books where bookid={}".format(BID))
        result=mycursor.fetchall()
        print()
        print("=> ",result[0][0])
        print()
        print(result[0][1])
        print()
        print()

    def search_BookID(id):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where bookid={}".format(id))
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
            plot(result[0][0])
            print()
        else:
            print("Sorry, No Book with this ID exists")
            print()
        choice=input("Would You Like to Continue Your Search?(Yes or No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_guest()
        else:
            print("Okay, Please Do Visit Us at any one of our locations and Sign Up as a Member")
            print()
            p=input("Enter any key to continue")
            print()
            main_menu()


    def search_bookname(name):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where bookname='{}'".format(name))
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
            plot(result[0][0])
            print()
        else:
            print("Sorry, No Book with this Name exists")
            print()
        choice=input("Would You Like to Continue Your Search?(Yes or No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_guest()
        else:
            print("Okay, Please Do Visit Us at any one of our locations and Sign Up as a Member")
            print()
            p=input("Enter any key to continue")
            print()
            main_menu()

    def search_authorname(add):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select bookid,bookname,author from books where author='{}'".format(add))
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Book ID","Book Name","Author Name"],tablefmt="fancy_grid"))
            BID=int(input("Enter the Book ID of the book for which you would like t see the plot"))
            plot(BID)
            print()
        else:
            print("Sorry, No Book with this Author exists")
            print()
        choice=input("Would You Like to Continue Your Search?(Yes or No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_guest()
        else:
            print("Okay, Please Do Visit Us at any one of our locations and Sign Up as a Member")
            print()
            p=input("Enter any key to continue")
            print()
            main_menu()
    def popular_author_guest():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select author,genre from popular_author")
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Author Name","Genre"],tablefmt="fancy_grid"))
            print()
        else:
            print("Sorry, No Book with this Author exists")
            print()
        choice=input("Would You Like to Continue Your Search?(Yes or No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_guest()
        else:
            print("Okay, Please Do Visit Us at any one of our locations and Sign Up as a Member")
            print()
            p=input("Enter any key to continue")
            print()
            main_menu()

    def available_genres():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",charset="utf8",database="library")
        mycursor=mydb.cursor()
        mycursor.execute("select distinct genre from books")
        result=mycursor.fetchall()
        if result:
            print(tabulate(result,headers=["Genre"],tablefmt="fancy_grid"))
            print()
        else:
            print("Sorry, No Genres exist")
            print()
        choice=input("Would You Like to Continue Your Search?(Yes or No)")
        choice=choice.upper()
        if choice=="YES":
            search_everything_guest()
        else:
            print("Okay, Please Do Visit Us at any one of our locations and Sign Up as a Member")
            print()
            p=input("Enter any key to continue")
            print()
            main_menu()


    while True:

        print("\n","1.Search the Book ID of the book","\n","2.Search the Name of the book","\n","3.Search the Author of a book","\n","4.Display All Popular Authors","\n","5.Dispay All Available Genres","\n","6.Exit to log in screen")
        print()
        option=int(input("Enter the number that corresponds to the option you want to choose: "))
        print("**********************************************************************************************************************************************************************")
        if option==1:
            mid=int(input("Enter the Book ID: "))
            search_BookID(mid)
        elif option==2:
            name=input("Enter the name of the book to be searched: ")
            search_bookname(name)
        elif option==3:
            add=input("Enter the name of the author to be searched: ")
            search_authorname(add)
        elif option==4:
            popular_author_guest()
        elif option==5:
            available_genres()
        elif option==6:
            print("Thank you for your visit.")
            main_menu()
        else:
            print("Oops!, It looks like you have entered an Invalid Key.")
            print("Please Try Again")
            search_everything_guest()


def terms_and_conditions():
    print("TERMS AND CONDITIONS:")
    print("\n","* THE USAGE OF MOBILE PHONES OR ANY SUCH ELECTRONIC GADGETS ARE STRICTLY PROHIBITED ONCE THE MEMBER HAS ENTERED THE LIBRARY.")
    print("\n","* SMOKING, EATING AND DRINKING IS STRICTLY PROHIBITED WITHIN THE LIBRARY HALL.")
    print("\n","* ONE PERSON CAN ONLY BORROW ONE BOOK AT A TIME.")
    print("\n","* BEFORE BORROWING A NEW BOOK, THE RESPECTED MEMBER SHOULD MAKE SURE THAT THEY HAD RETURNED THEIR PREVIOUSLY BORROWED BOOK. THEY WOULDN’T BE ABLE TO BORROW A NEW BOOK OTHERWISE.")
    print("\n","* ALL RESPECTED MEMBERS SHOULD MAKE SURE THAT HAVE PAID ALL THEIR REMAINING DUES BEFORE THE END OF EVERY MONTH, HOWEVER IF THEIR DUES EXCEED A LIMIT OF 50 BHD, THEIR ACCOUNTS WILL BE AUTOMATICALLY SUSPENDED AND WILL BE REACTIVATED ONLY UNDER THE OWNER’S DISCRETION.")
    print("\n","* A MEMBER HAS A DURATION OF ONE WEEK FROM THE DAY OF BORROWING A BOOK TO RETURN IT BACK. IF FAILED TO RETURN THE BOOK WITHIN THE DUE DATE, THEY WILL HAVE TO FACE A FINE MENTIONED BY THE RESPECTIVE LIBRARIAN.")
    print("\n","* IF THE MEMBER RETURNS THE BOOK THAT THEY HAD BORROWED IN A DETERIORATED CONDITION, THE MEMBER WILL BE CHARGED WITH A FINE MENTIONED BY THE LIBRARIAN.")
    print("\n","* VIOLATIONS DONE TO THE LIBRARY DIRECTLY OR INDIRECTLY WILL BE STRICTLY HANDLED BY THE AUTHORITY.  THE MEMBER MIGHT FACE SERIOUS CONSEQUENCES WHICH MAY ALSO LEAD TO LOSING THEIR MEMBERSHIP IN THE LIBRARY FOREVER.")
    print()
    print()
    print()
    print()
    p=input("Enter any key to Exit to The Main Menu")
    main_menu()

def start_project():
    mydb=mysql.connector.connect(host='localhost',user='root',charset="utf8",passwd='1234')
    mycursor=mydb.cursor()
    mycursor.execute('show databases')
    result=mycursor.fetchall()
    n=len(result)
    c=0
    for k in result:
        if k[0]=="library":
            main_menu()
        else:
            c+=1
    if c==n:
        create_database()
        create_table_member()
        create_table_books()
        create_table_popular_author()
        main_menu()

start_project()