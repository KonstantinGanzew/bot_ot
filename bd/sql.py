import sqlite3 as sq

async def db_start():
    global db, cur
    db = sq.connect('user.db')
    cur = db.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo TEXT, age TEXT, desc TEXT, name TEXT)')
    db.commit()

async def create_profil(user_id):
    user = cur.execute('SELECT 1 FROM profile WHERE user_id == {key}'.format(key=user_id)).fetchone()
    if not user:
        cur.execute('INSERT INTO profile VALUES(?, ?, ?, ?, ?)', (user_id, '', '', '', ''))
        db.commit()