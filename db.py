import sqlite3

def init_db():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            user_message TEXT,
            bot_response TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_chat(user_id, user_message, bot_response):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('INSERT INTO chats (user_id, user_message, bot_response) VALUES (?, ?, ?)',
              (user_id, user_message, bot_response))
    conn.commit()
    conn.close()

def load_chat(user_id):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('SELECT user_message, bot_response FROM chats WHERE user_id = ?', (user_id,))
    chats = c.fetchall()
    conn.close()
    return chats
