import pymysql
class Validate:
    def additem(self,item):
        sql = "insert into item values('"+item.getitemname()+"','"+item.getcost()+"')"
        print sql
        db = pymysql.connect("localhost","root","password","itemexp" )
        cursor = db.cursor()
	print sql
        cursor.execute(sql)
        db.commit()
        db.close()
