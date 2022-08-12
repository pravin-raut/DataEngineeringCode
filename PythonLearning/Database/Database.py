import Connection as Cn
import GetData as GD
conClass = Cn.Connection('ms.itversity.com',3306,'retail_user','itversity')
mysqlcnx = conClass.mySqlConnection("retail_export")


resultset = conClass.selectResult("select batting_team,count(*) from IPL_DETAIL_BALL_WISE_PRAVIN_NEW group by batting_team",mysqlcnx)
print(resultset)
for x in resultset:
    name,no=x
    print(x)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = (name,no)


GetDataClass=GD.ApiAccess("http://api.open-notify.org/astros.json")
ouput=GetDataClass.getrequestdata()
print(ouput)