import mysql.connector


class Connection:
    def __init__(self,host,port,username,password):
        self.host=host
        self.username=username
        self.password=password
        self.port=port

    def mySqlConnection(self,database):
        cnx = mysql.connector.connect(host=self.host,
                                      port=self.port,
                                      user=self.username,
                                      password=self.password,
                                      database=database)
        return cnx

    def selectResult(self,selectquery,connection):
        concursor = connection.cursor()
        concursor.execute(selectquery)
        connection.close()
        return concursor

