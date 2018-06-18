from tkinter.filedialog import askopenfilename #import askfileopen from tkinter module to open csv file
import tkinter

stre="emails.csv" #store the default csv file name
searchkeywords="" #initialise searchkeywords to store keywords

def open1():       #define method to execute on clicking upload button
    filename = askopenfilename()
    global stre
    print(filename)
    stre = str(filename)
    global searchkeywords
    searchkeywords = e1.get()  #get keywords from entry boxx
    print(searchkeywords)

def quit(self):     #define method for closing window

    exit(0)


def open2():      #define method for opening default csv file
    global searchkeywords
    searchkeywords = e1.get()
    print(searchkeywords)
    top.quit()



top = tkinter.Tk()        #create a new gui window
E=tkinter.Label(top,text="enter the keywords seperated by commas:eg(python,opencv,code)->")
B = tkinter.Button(top, text ="SUBMIT ", command = top.quit)
C = tkinter.Button(top, text ="UPLOAD", command = open1)
A = tkinter.Label(top, text ="Upload CSV files in which contains rows in the following format:\n"
                             "<date in dd/mm/yy>$<emailid>$<mail content>\n"
                             "ex: 30/09/17$shubhi.prakash03@gmail.com$will be doing it by tomorrow \n"
                             "Output will be displayed in the terminal\n"
                  )
D = tkinter.Button(top, text ="Open default", command = open2)
A.grid(row=0)
C.grid(row=1)
B.grid(row=2)
D.grid(row=3 )
E.grid(row=4,column=0)
e1=tkinter.Entry(top)
e1.insert(0, "Python,OpenCV")
e1.grid(row=4,column=1,columnspan=28)
top.mainloop()

import csv   #import csv module for reading csv files
import time   #import time  module for dealing with data parameters
from time import mktime
from datetime import datetime


def parse(text):                    #method for parsing dateformat
    for fmt in ('%Y-%m-%d', '%d/%m/%y',''):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')



filename= stre.replace("\\", "/")

fields = []
rows = []


with open(filename, 'r') as csvfile:   #open csv file

    csvreader = csv.reader(csvfile)


    fields = next(csvreader)


    for row in csvreader:
        rows.append(row)


    print("Total no. of rows: %d \n" % (csvreader.line_num))


dic=[]
listdate=[]
listmail=[]
listmatter=[]

for row in rows[:csvreader.line_num]:  #create dictionary containing email,date and content of the csv file

    for col in row:
        #print(col)
        dic.append({"date":str(str(col).split('$')[0]),"name":str(str(col).split("$")[1]),"matter":str(str(col).split("$")[2])})


    #print('\n')


myset=set()                     #get all unique emails using set
for i in dic:
   myset.add(str(i["name"]))

print("THE UNIQUE EMAIL  ADDRESSESS ARE: \n ")
for i in myset:
    print(i+"\n")

print("********************\n")

print("THE LAST DATE OF CONVERSATION FOR THE EMAILS ARE:\n")

searcharr=searchkeywords.split(",")
print(searcharr)
currentdate=datetime.today().strftime('%d/%m/%y')   #get current date

#--------
myData = [["UNIQUE EMAILS", "LAST DATE OF CONVERSATION", "DAYS ELAPSED"]]


#---------
for i in myset:                                    #compare all date for a given email to get the latest date
    min = "20/12/01"
    maxdate = time.strptime(min, "%d/%m/%y")
    for j in range(len(dic)):
        if(i==dic[j]["name"]):

            try:
             if(maxdate<time.strptime(dic[j]["date"],"%d/%m/%y")):
                maxdate = time.strptime(dic[j]["date"],"%d/%m/%y")
            except:
             pass
    latestdate = datetime.fromtimestamp(mktime(maxdate)).strftime("%d/%m/%Y")
    latestdateobj= datetime.fromtimestamp(mktime(maxdate))
    print("--------------------")
    print("email:",i)
    print("last date of conservation: ", latestdate)
    now = datetime.today()
    delta = now - latestdateobj                          #calculate the number of days elapsed
    print("Days elapsed from last date: ",delta.days)
    myData.append([i,latestdate,delta.days])



print("--------------------")

print("KEYWORD SEARCH")
flag=True
for a in dic:                    #find if the given keywords are present in the content of the emails

    for b in searcharr:
        if( b in a["matter"] ):
            flag=False
            print("Keyword \""+b+"\" found in "+a["name"]+" dated:"+a["date"])

if(flag==True):
    print("no mails contains the required keywords")




#-------------eof---------------------




myFile = open('ParsedEmails.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete")













