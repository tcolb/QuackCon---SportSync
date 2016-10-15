import sqlite3


# cur.execute("CREATE TABLE IF NOT EXISTS game_test (play TEXT, detail TEXT)")
# con.commit()

def insert_play(play, detail):
	con = sqlite3.connect('matches.db')
	cur = con.cursor()
	cur.execute("INSERT INTO game_test (play,detail) VALUES (?,?)", (play,detail))
	con.commit()
	con.close()

def retrieve_play():
	con = sqlite3.connect('matches.db')
	cur = con.cursor()
	cur.execute("SELECT play, detail FROM game_test")
	plays = cur.fetchall()
	con.close()