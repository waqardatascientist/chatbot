import sqlite3
import csv

def export_chat_history():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chats")
    rows = cursor.fetchall()

    with open("chat_history_export.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "user_id", "user_message", "bot_response"])
        writer.writerows(rows)

    conn.close()
    print("Chat history exported to chat_history_export.csv")

if __name__ == "__main__":
    export_chat_history()
