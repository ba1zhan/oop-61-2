import sqlite3

from django.template.defaultfilters import title

conn = sqlite3.connect("articles.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    title TEXT,
    year INTEGER,
    avtor TEXT
)
""")

conn.commit()


def create_articles(title, year, avtor):
    cursor.execute(
        'INSERT INTO articles(title, year, avtor) VALUES(?,?,?)',
        (title, year, avtor)
    )

conn.commit()
print(f'Статья добавлена {title}')


def get_all_articles():
    cursor.execute("SELECT rowid, * FROM articles")
    return cursor.fetchall()

def get_by_rowid(row_id):
    cursor.execute(
        "SELECT rowid, * FROM articles WHERE rowid = ?",
        (row_id,)
    )
    return cursor.fetchone()

def update_article(row_id, title, year, avtor):
    cursor.execute(
        """
        UPDATE articles
        SET title = ?, year = ?, avtor = ?
        WHERE rowid = ?
        """,
        (title, year, avtor, row_id)
    )
    conn.commit()
def delete_article(row_id):
    cursor.execute(
        "DELETE FROM articles WHERE rowid = ?",
        (row_id,)
    )
    conn.commit()

create_articles("Python и базы данных", 2024,"Байжан")
create_articles("SQLite просто", 2025, "Байжан")

print("Все статьи:")
print(get_all_articles())

print("Статья с rowid = 1:")
print(get_by_rowid(1))

update_article(1, "Продвинутый Python", 2025, "Байжан")

delete_article(2)

print("После обновления и удаления:")
print(get_all_articles())

conn.close()


