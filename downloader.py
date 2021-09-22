# bibliotecas usadas neste programa
import requests
from os.path import basename, join

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

# lógica principal
def main():
    for contador in range(1,5):
        download_one("https://keen-heyrovsky-4a34fe.netlify.app/"+str(contador)+".jpeg")

if __name__ == '__main__':
    main()
