from requests import get
from bs4 import BeautifulSoup
from re import findall
from yaml import dump, FullLoader, load


class Yaml:

    def __init__(self):
        self.tags = 0

    def web_scraping(self, site):
        """Faz o web scraping da página"""

        resposta = get(site)
        self.tags = BeautifulSoup(resposta.text, "html5lib")
        print(f"Resposta: {resposta.ok}\n")

    def comentarios(self):
        """Imprime os comentários do exemplo YAML na tela"""

        print("Comentários:")
        all_comentarios = self.tags.find_all("span", attrs={"class": "c"})
        for comentario in all_comentarios:
            print(" ".join(findall(r"\w+", comentario.string)))

    def codigo_yaml(self):
        """Seleciona o código do exemplo YAML, salva em um arquivo .yaml
         e retorna os exemplos da página"""

        exemplo_yaml = self.tags.find_all(
            "code", attrs={"class": "language-Yaml"})
        with open("codigo_yaml.yml", "w") as file:
            dump(exemplo_yaml[0].text, file)
        with open("codigo_yaml.yml") as file:
            yaml_code = load(file, Loader=FullLoader)
            print("\n")
            print(yaml_code)
