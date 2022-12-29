import sqlite3

class Base_de_datos():

    matches=sqlite3.connect("Matches")
    cursor=matches.cursor()

    def __init__(self):

        matches=sqlite3.connect("Matches")

        try:

            self.cursor.execute("""
				CREATE TABLE MATCHES (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				TOURNAMENT INTEGER,
                ROUND INTEGER,
				PLAYER1 VARCHAR(10),
                PLAYER2 VARCHAR(20),
                PLAYER1_SKILL INTEGER,
                PLAYER2_SKILL INTEGER,
                WINNER VARCHAR (10))
				""")

        except:

		          sqlite3.OperationalError

    def add_match(self,match_information):

        self.cursor.execute("INSERT INTO MATCHES VALUES (NULL,?,?,?,?,?,?)",match_information)
        self.matches.commit()

    """def remove_cocktail(self,cocktail):

        orden="DELETE FROM COCTELES WHERE COCKTAIL='"+cocktail+"'"
        self.cursor.execute(orden)
        self.matches.commit()"""

    def see_match(self,ID):

        orden="SELECT * FROM MATCHES WHERE ID="+str(ID)
        self.cursor.execute(orden)

        return self.cursor.fetchall()

    def see_tournament(self,tournament):

        orden="SELECT * FROM MATCHES WHERE TOURNAMENT="+str(tournament)
        self.cursor.execute(orden)

        return self.cursor.fetchall()

    def see_player(self,name):

        orden="SELECT * FROM MATCHES WHERE PLAYER1="+name+" AND PLAYER2="+name
        self.cursor.execute(orden)

        return self.cursor.fetchall()
