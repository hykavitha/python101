
# class MySQLStorePipeline(scrapy.Item):
#     config = {
#         'user': 'kavitha',
#         'password': 'root123',
#         'host': '127.0.0.1',
#         'database': 'web_scraping',
#         'raise_on_warnings': True
#     }
#
#     add_quote = ("INSERT INTO web_scraping.quotes2"
#                  "(quote, author, tags, last_upd_timestampquotes) "
#                  "VALUES (%s, %s, %s, %s)")
#     cnx=''
#     cursor = ''
#     def __init__(self):
#         print("#############################################################coming here ########")
#         self.cnx = mysql.connector.connect(**self.config)
#         print(self.cnx)
#
#         self.cursor = self.cnx.cursor()
#
#     def process_item(self, item, spider):
#         print("**********************", item)
#         print(type(item))
#         try:
#             self.cursor.execute(self.add_quote, (item['text'],
#                                                  item['author'],
#                                                  item['tags'],
#                                                  self.getTime()))
#                                                 # AttributeError: Use item['cnx'] = < mysql.connector.connection.MySQL                               self.getTime()))
#
#             self.cnx.commit() # print("\n\ninserted--->", item)
#         except mysql.connector.Error as err:
#             # if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             #     print("Something is wrong with your user name or password")
#             # elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             #     print("Database does not exist")
#             # else:
#             print(err)
#         else:
#             self.cnx.close()
#         return item
#
#     def getTime(self):
#         now = datetime.now()
#
#         today_now = now.strftime("%Y-%m-%d %H:%M:%S")
#         return today_now
