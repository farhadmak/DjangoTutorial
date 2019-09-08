import sqlite3

def searchByFruit(cursor, fruit):
	#conn = sqlite3.connect('../../tree_database.db')
	#c = conn.cursor()

	trees = cursor.execute("SELECT * from tree WHERE type_of_edible_fruit LIKE ?", ('%'+fruit+'%',))

	return trees

#testing
conn = sqlite3.connect('../../tree_database.db')
c = conn.cursor()
test = searchByFruit(c,'saskatoon')
for tree in test:
	print(tree)

conn.close()	