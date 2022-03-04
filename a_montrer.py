import sqlite3

##########

FILENAME = 'clients.db'
cur = sqlite3.connect(FILENAME)

##########

def init():
    cur.execute('CREATE TABLE Clients (Id INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT, Prenom TEXT, Age INTEGER, Job TEXT, City TEXT, Tel TEXT)')

def new_client(client):
    cur.execute("INSERT INTO Clients (Nom, Prenom, Age, Job, City, Tel) VALUES (?,?,?,?,?,?)",(client))

def close():
    cur.commit()
    cur.close()

def check_doublons():
    l = cur.execute('''
                    SELECT   Tel, Id
                    FROM     clients
                    GROUP BY Tel
                    HAVING   COUNT(Tel) > 1''')
    #res = l.fetchall()
    #print(res, len(res))
    for client in l:
        cur.execute(f'''
                    DELETE FROM clients
                    WHERE id="{client[1]}"''')


#########################################################################
if __name__ == '__main__':
    conn = sqlite3.connect(FILENAME)
    cur = conn.cursor()
    req = "CREATE TABLE CLIENT (id integer primary key autoincrement, prenom text, nom text, age integer, job text, city text, tel text)"
    cur.execute(req)
    conn.commit()
    conn.close()


