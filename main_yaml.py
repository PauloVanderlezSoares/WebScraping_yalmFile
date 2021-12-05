from yaml_object import Yaml
from requests import get
from bs4 import BeautifulSoup
from re import findall
from yaml import dump, FullLoader, load

link = "https://www.w3schools.io/file/yaml-sample-example/"

arquivo = Yaml()
arquivo.web_scraping(link)
arquivo.comentarios()
arquivo.codigo_yaml()
