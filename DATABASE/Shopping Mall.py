import psycopg2
conn=psycopg2.connect(host="localhost",
                      dbname="Shopping_mall",
                      user="postgres",
                      password="123456")
cur=conn.cursor()
# cur.execute("create table bill(billno int,c_id int,product_id int,quantity int)")
# cur.execute("create table customer(c_id int,c_name text,c_address text, c_phone int) ")
# cur.execute("create table stock(product_id int, product_name text, price int, quantity int)")
def menu(title):
    for i,t in zip(range(len(title)),title):
        print("press ",i ,"for ",t)

    op=int(input("Enter your option :"))
    return op
menu_list=["Customer","Stock","Bill","Exit"]
sub_menu_list=["Entry","View","Search by id","update","delete","Main Menu"]
op1=1
while op1 != menu_list.index("Exit"):
    format("Shopping mart Pvt Ltd ")
    op1 = menu(menu_list)
    if op1 == menu_list.index("Customer"):
        format("customer")
        op2=0
        while op2 != sub_menu_list.index("Main Menu"):
            op2=menu(sub_menu_list)
            if op2 == sub_menu_list.index("Entry"):
                format("Entry")
                op3="yes"
                while op3.lower()=="yes":
                    id = int(input("Enter Customer id:"))
                    name = input("Enter Customer name :")
                    address = input("Enter Address :")
                    phone = int(input("Enter Phone number:"))
                    cur.execute("insert into customer values(%s,%s,%s,%s)",(id,name,address,phone))
                    conn.commit()
                    op3=input("do you want to add another customer(yes/no)?:")
            elif op2== sub_menu_list.index("View"):
                format("View")
                cur.execute("select * from customer")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
            elif op2== sub_menu_list.index("Search by id"):
                format("Search by id")
                rid = int(input("Enter id:"))
                cur.execute(
                    "select * from customer where c_id=%s",(rid,))
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
            elif op2 == sub_menu_list.index("update"):
                format("update")
                rid = int(input("enter the id. you want to update"))
                rno = int(input("enter roll no:"))
                sname = input("enter name:")
                add= input("enter address:")
                num = int(input("enter phone number:"))
                cur.execute("update customer set c_id=%s, c_name=%s, c_address=%s, c_phone=%s where c_id=%s",(rno, sname, add, num, rid))
                cur.execute("select * from customer")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
                conn.commit()
            elif op2 == sub_menu_list.index("delete"):
                format("delete")
                rid = int(input("Enter the Roll no. you want to delete:"))
                cur.execute("delete from customer where c_id=%s",(rid,))
                cur.execute("select * from customer")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
                conn.commit()
            elif op2 == sub_menu_list.index("Main Menu"):
                print("Back to main menu ")
            else :
                print("Wrong option is selected try again !!")
    elif op1== menu_list.index("Stock"):
        format("Stock")
        op2=0
        while op2 != sub_menu_list.index("Main Menu"):
            op2 = menu(sub_menu_list)
            if op2 == sub_menu_list.index("Entry"):
                format("Entry")
                op3 = "yes"
                while op3.lower() == "yes":
                    id = int(input("Enter product id:"))
                    name = input("Enter product name :")
                    price = int(input("Enter price :"))
                    qun = int(input("Enter quantity:"))
                    cur.execute("insert into stock values(%s,%s,%s,%s)", (id,name,price,qun))
                    conn.commit()
                    op3 = input("do you want to add another product(yes/no)?:")
            elif op2 == sub_menu_list.index("View"):
                format("View")
                cur.execute("select * from stock")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
            elif op2== sub_menu_list.index("Search by id"):
                format("Search by id")
                rid = int(input("Enter id:"))
                cur.execute(
                    "select * from stock where product_id=%s", (rid,))
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
            elif op2==sub_menu_list.index("update"):
                format("update")
                rid = int(input("enter the id. you want to update"))
                rno = int(input("enter roll no:"))
                pname = input("enter name:")
                price = input("enter address:")
                num = int(input("enter phone number:"))
                cur.execute("update stock set product_id=%s, product_name=%s, price=%s, quantity=%s where product_id=%s",(rno, pname, price, num, rid))
                cur.execute("select * from stock")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
                conn.commit()
            elif op2 == sub_menu_list.index("delete"):
                format("delete")
                rid = int(input("Enter the Roll no. you want to delete:"))
                cur.execute("delete from stock where product_id=%s", (rid,))
                cur.execute("select * from stock")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
                conn.commit()
            elif op2 == sub_menu_list.index("Main Menu"):
                print("Back to main menu ")
            else:
                print("Wrong option is selected try again !!")
    elif op1 == menu_list.index("Bill"):
        format("Bill")
        op2 = 0
        while op2 != sub_menu_list.index("Main Menu"):
            op2 = menu(sub_menu_list)
            if op2 == sub_menu_list.index("Entry"):
                format("Entry")
                op3 = "yes"
                while op3.lower() == "yes":
                    id = int(input("Enter bill no.:"))
                    cid = int(input("Enter Customer id :"))
                    pid = int(input("Enter product id:"))
                    qun = int(input("Enter quantity:"))
                    price =int(input("Enter Product Price:"))
                    cur.execute("insert into bill values(%s,%s,%s,%s,%s)", (id,cid,pid,qun,price))
                    conn.commit()
                    op3 = input("do you want to add another bill(yes/no)?:")
            elif op2 == sub_menu_list.index("View"):
                format("View")
                cur.execute("select *,qun*price from bill")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
            elif op2 == sub_menu_list.index("Search by id"):
                format("Search by id")
                rid = int(input("Enter bill_no:"))
                cur.execute("select * from bill where bill_no=%s",(rid,))
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
            elif op2 == sub_menu_list.index("update"):
                format("update")
                rid = int(input("enter the bill_no. you want to update"))
                id = int(input("Enter bill no.:"))
                cid = int(input("Enter Customer id :"))
                pid = int(input("Enter product id:"))
                qun = int(input("Enter quantity:"))
                cur.execute("update bill set bill_no=%s, c_id=%s, product_id=%s, quantity=%s where bill_no=%s",(id, cid, pid, qun, rid))
                cur.execute("select * from bill")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
                conn.commit()
            elif op2 == sub_menu_list.index("delete"):
                format("delete")
                rid = int(input("Enter the Roll no. you want to delete:"))
                cur.execute("delete from bill where bill_no=%s", (rid,))
                cur.execute("select * from bill")
                for row in cur:
                    for value in row:
                        print(value, end="\t")
                    print("")
                conn.commit()
            elif op2 == sub_menu_list.index("Main Menu"):
                print("Back to main menu ")
            else:
                print("Wrong option is selected try again !!")
    elif op1 == menu_list.index("Exit"):
        print("you are exited ")
    else :
        print(" wrong option selected try again !!")
cur.close()
conn.close()