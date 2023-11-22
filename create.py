#installed library mysql-connector-python
import mysql.connector
#creating connection
class insert:
    def __init__(self):

        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="maahi",
            database="bank"
            )
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur=self.conn.cursor()#creating cursor
        cur.execute(f"insert into personal_details values({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.conn.commit()
        print("--------------personal information has been saved successfully----------------------")

    def bank_details(self,acn,cid,ifsc,actype):
        cur=self.conn.cursor()
        cur.execute(f"insert into bank_details values({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("------------bank_details has been saved successfully-----------------")
    
    def transaction_details(self,tid,sedacc,recacc,amount,method):
        cur=self.conn.cursor()
        cur.execute(f"insert into transaction_details values({tid},{sedacc},{recacc},{amount},'{method}')")
        self.conn.commit()
        print("-----------transaction_details has been saved successfully----------")

    def account_details(self,acnno,tid,amount,clbal):
        cur=self.conn.cursor()
        cur.execute(f"insert into account_details values({acnno},{tid},{amount},{clbal})")
        self.conn.commit()
        print("-----------account_details has been saved successfully----------")