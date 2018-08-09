# bibliotecas usadas neste programa
import requests
from os.path import basename, join
import sqlite3

# funções utilitárias
def download_one(url):
    filename = basename(url)
    target = join("./", filename)

    try:
        print("Fazendo o download de %s" % filename)

        with open(target, 'wb+') as f:
            response = requests.get(url, stream=True)
            for chunk in response.iter_content(4096):
                f.write(chunk)

        print("Download pronto!")

    except Exception as e:
        print("Erro no download %s" % e)

def open_db():
    conn = sqlite3.connect('urls.db')
    print("Opened database successfully\n")
    return conn

def close_db(conn):
    conn.commit()
    conn.close()

# lógica principal
def main():
    conn = open_db()

    query = "SELECT url FROM urls LIMIT 100"

    cursor = conn.execute(query)
    for values in cursor:
        download_one(values[0])

    close_db(conn)

if __name__ == '__main__':
    main()
