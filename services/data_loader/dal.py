import mysql.connector

_SELECT_ALL_query = "SELECT * FROM data"

class DataAccesseceLayyer:

    def __init__(self):
        pass

    def get_all_data(self):
        """ create connection to mysql and get
                     the data table"""
        res = {}
        count = 0
        try:

            db = mysql.connector.connect(host="",
                                         user="root",
                                         port="3306",
                                         database="data")
            data = db.cursor()
            data.execute(_SELECT_ALL_query)

            result = data.fetchall()

            # print all the table
            for raw in result:
                res[count] = raw
                count += 1

            return res

        except Exception as ex:
            return {"error to get all. error: ": ex}

