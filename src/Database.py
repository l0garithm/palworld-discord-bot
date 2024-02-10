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

db.execute("CREATE TABLE IF NOT EXISTS server_info(guild, required_role, players, game_servers)")

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

