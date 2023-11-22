from create import insert
from read import read
from update import update
from delete import delete 
obj=insert()
objread=read()
objupdate=update()
objdelete=delete()
print("------------------banking management system------------------")
print("for inserting the data press 1:")
print("for reading the data press 2:")
print("for updating the data press 3:")
print("for deleting the data press 4:")

opr=int(input("please enter your operation:"))
def myopr():
    print("----for personal information press 1----")
    print("----for bank details press 2----")
    print("----for transaction details press 3----")
    print("----for account details press 4----")
    vr=int(input("please select your table:"))
    if vr==1:
        return "personal_details"
    elif vr ==2:
        return "bank_details"
    elif vr ==3:
        return "transaction_details"
    elif vr ==4:
        return "account_details"

if opr==1:
    h= myopr()
    if h=='personal_details':
        cid=int(input("enter the customer id:"))
        fname=input("please enter the first name:")
        lname=input("please enter the last name:")
        addr=input("please enter the address:")
        pn=int(input("please enter the phn number:"))
        an=input("please enter the aadhar number:")
        pan=input("please enter pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)
    if h=="bank_details":
        acn=int(input("please enter account number:"))
        cid = int(input("please enter customerid:"))
        ifsc = input("please enter ifsc code:")
        actype = input("please enter account type:")
        obj.bank_details(acn,cid,ifsc,actype)
    if h=="transaction_details":
        tid=int(input("enter your transaction id:"))
        sedacc=int(input("enter sender account number:"))
        recacc=int(input("enter receiver account number:"))
        amount=int(input("enter the amount to send:"))
        method=input("enter the method:")
        obj.transaction_details(tid,sedacc,recacc,amount,method)
    if h=="account_details":
        accno=int(input("enter the accn number:"))
        tid=int(input("enter the transaction id:"))
        amount=int(input("enter the amount:"))
        clbal=int(input("enter the closing balance:"))
        trtype=input("enter the transaction type:")
        obj.account_details(accno,tid,amount,clbal,trtype)
if opr==2:
    j=myopr()
    cusid=int(input("enter the customerid for fetching data:"))
    objread.specific_info(cusid,j)
if opr==3:
    m=myopr()
    cusid=int(input("enter the customer id:"))
    colname=input("enter the column name:")
    newval=input("enter the new values:")
    objupdate.myupdate(m,colname,newval,cusid)
if opr==4:
    a=myopr()
    cusid=int(input("enter the customer id:"))
    objdelete.specific_delete(a,cusid)