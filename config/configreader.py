import configparser

def readdata(file_path):

    con=configparser.ConfigParser()
    con.read(file_path)
    return con


# properties=readdata(r"C:\Users\hp\PycharmProjects\pageObjectModelframework\config\config.ini")
# url=properties.get("LoginData","Base_url")
# print("jhhgkugyguk",url)
#
