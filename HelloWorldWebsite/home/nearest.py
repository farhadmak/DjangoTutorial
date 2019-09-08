import sqlite3
import math

def nearest(cursor, lat, lon):
    #result = cursor.execute(" SELECT * FROM tree ORDER BY sqrt( (latitude - ?)**2 + (longitude - ?)**2 ) DESC LIMIT 1;", (lat, lon))

    trees = cursor.execute("SELECT * FROM tree WHERE bears_edible_fruit = 'Yes'") #cursor.fetchone()
    closest = trees.fetchone()
    #print(closest)
    distance = math.sqrt((closest[15] - lat)**2 + (closest[16] - lon)**2)
    for tree in trees:
    	nDistance = math.sqrt((tree[15] - lat)**2 + (tree[16] - lon)**2)
    	if  nDistance < distance:
    		closest = tree
    		distance = nDistance

    return (closest)

#tests
mydb = sqlite3.connect('../../tree_database.db')
mycursor = mydb.cursor()
print(nearest(mycursor, 53.4, -113.490929))