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

def insert_guild(guildId, name, required_role):
    db.execute("""
                INSERT INTO guilds (guild_id, name, required_role) VALUES(?,?,?)
                """, (str(guildId), str(name), str(required_role)))
    commit()
    print("Hello")

def update_guild(guild_id, required_role):
    db.execute("""
               UPDATE guilds SET required_role = ? WHERE guild_id = ?
               """, (str(required_role), str(guild_id)))
    commit()
    
def pull_guild(guildID):
    try:
        guild = db.execute("SELECT * FROM guilds WHERE guild_id = ?", (guildID))
    except(LookupError):
        print(LookupError)
    # rows = db.fetchall()

    return rows
    
def commit():
    connection.commit()

