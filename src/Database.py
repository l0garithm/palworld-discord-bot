import sqlite3

DB_GUILD = 'guild'
DB_REQUIRED_ROLE = 'required_role'
DB_PLAYERS = 'players'
DB_GAME_SERVERS = 'game_servers'

connection = sqlite3.connect("server_info.db")

db = connection.cursor()

# def dict_factory(db, row):
#     fields = [column[0] for column in db.description]
#     return {key: value for key, value in zip(fields, row)}

# db.row_factory = dict_factory

db.execute("CREATE TABLE IF NOT EXISTS servers(id INTEGER PRIMARY KEY AUTOINCREMENT, host, port, password)")
db.execute("CREATE TABLE IF NOT EXISTS guilds(id INTEGER PRIMARY KEY AUTOINCREMENT, guild_id, name, required_role)")
db.execute("CREATE TABLE IF NOT EXISTS guildservers(id INTEGER PRIMARY KEY AUTOINCREMENT, guild, server)")

# db.execute("""
#                INSERT INTO server_info VALUES
#                (1158872977048342608, '@everyone', NULL, NULL)
#                """)
# connection.commit()

def insert(values):
    db.execute("""
               INSERT INTO server_info VALUES(:guild, :required_role, :players, :game_servers)
               """, values)
    commit()

def insert_server(ip, port, pw):
    db.execute("""
               INSERT INTO servers (host, port, password) VALUES(?, ?, ?)
               """, (str(ip), str(port), str(pw)))
    commit()
    
def update(rowId, col, value):
    db.execute("""
               UPDATE server_info SET %s = ? WHERE guild = ?
               """ % (col), (str(value), rowId))
    # print(f'Value: {value}, Guild: {rowId}')
    commit()


def pull_guilds():
    rows = db.execute("SELECT * FROM server_info")
    # rows = db.fetchall()

    return rows
    
def commit():
    connection.commit()

