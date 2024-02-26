import sqlite3

DB_GUILD = 'guild'
DB_REQUIRED_ROLE = 'required_role'
DB_PLAYERS = 'players'
DB_GAME_SERVERS = 'game_servers'
DATABASE_PATH = 'server_info.db'

# connection = sqlite3.connect("server_info.db")

# db = connection.cursor()

# def dict_factory(db, row):
#     fields = [column[0] for column in db.description]
#     return {key: value for key, value in zip(fields, row)}

# db.row_factory = dict_factory

def createTables():
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("CREATE TABLE IF NOT EXISTS servers(id INTEGER PRIMARY KEY AUTOINCREMENT, name, host, port, password, guild, ssh_user, ssh_pass)")
        db.execute("CREATE TABLE IF NOT EXISTS guilds(guild_id PRIMARY KEY, name, required_role)")
        # db.execute("CREATE TABLE IF NOT EXISTS guildservers(id INTEGER PRIMARY KEY AUTOINCREMENT, guild, server)")
        # commit()

# db.execute("""
#                INSERT INTO server_info VALUES
#                (1158872977048342608, '@everyone', NULL, NULL)
#                """)
# connection.commit()

def insert(values):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                INSERT INTO server_info VALUES(:guild, :required_role, :players, :game_servers)
                """, values)
        conn.commit()

def insert_server(name, ip, port, pw, guild, ssh_user, ssh_pass):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                INSERT INTO servers (name, host, port, password, guild, ssh_user, ssh_pass) VALUES(?, ?, ?, ?, ?, ?, ?)
                """, (str(name), str(ip), str(port), str(pw), str(guild), str(ssh_user), str(ssh_pass)))
        # db.execute("""
        #         INSERT INTO guildservers (guild, server) VALUES(?,?)
        #            """, (guild, db.lastrowid))
        conn.commit()
    
def update(rowId, col, value):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                UPDATE server_info SET %s = ? WHERE guild = ?
                """ % (col), (str(value), rowId))
        # print(f'Value: {value}, Guild: {rowId}')

def get_guild(guildId):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        rows = db.execute("""
                    SELECT guild_id FROM guilds WHERE guild_id = ?
                    """, (str(guildId),))
        rows = db.fetchone()
        return rows

def insert_guild(guildId, name, required_role = ''):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                    INSERT INTO guilds (guild_id, name, required_role) VALUES(?,?,?)
                    """, (str(guildId), str(name), str(required_role)))
        conn.commit()

def update_guild(guild_id, required_role):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                UPDATE guilds SET required_role = ? WHERE guild_id = ?
                """, (str(required_role), str(guild_id)))
        conn.commit()

def delete_guild(guild_id):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                DELETE FROM guilds WHERE guild_id = ?
                """, (str(guild_id),))
        db.execute("""
                   DELETE FROM servers WHERE guild = ?
                   """, (str(guild_id),))
        conn.commit()

def get_guild_servers(guildID):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                SELECT name, host FROM servers WHERE guild = ?
                """, (str(guildID),))
        rows = db.fetchall()

        return rows
    
def get_server(guildID, name):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                SELECT name, host, port, password, guild FROM servers WHERE guild = ? AND name = ?
                """, (str(guildID), str(name)))
        server = db.fetchone()
        # print(guildID)
        # print(name)
        return server
    
def get_guild_server_names(guildID):
    with sqlite3.connect(DATABASE_PATH) as conn:
        db = conn.cursor()
        db.execute("""
                    SELECT name FROM servers WHERE guild = ?
                   """, (str(guildID),))
        rows = db.fetchall()
        return rows

def pull_guild(guildID):
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            db = conn.cursor()
            db.execute("SELECT * FROM guilds WHERE guild_id = ?", (str(guildID),))
            guild = db.fetchone()

            return guild
            
    except sqlite3.Error as err:
        print(err)
    # rows = db.fetchall()

    # return rows
    
# def commit():
#     connection.commit()

