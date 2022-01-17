
import os
import sys

from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

PATH_END = os.environ['PATH_END']
PATH_START = os.environ['PATH_START']


def create_list_file() -> list | None:
    for _, _, files in  os.walk('C:\data\data'):
        return files


def read_file(name_file: str) -> tuple:
    with open(f'{PATH_START}{name_file}', 'r', encoding="utf-8") as f:
        text = f.read()
        soup = BeautifulSoup(text, 'lxml')
        name = soup.find('link', rel='canonical').get('href')
    return (text, name)


def save_file(text: str, name: str) -> None:
    name = str(name[31:])
    print(name)
    with open(f'{PATH_END}{name}', 'w', encoding="utf-8") as f:
        f.write(text)


def main():
    list_names = create_list_file()
    for name_file in list_names:
        read_file(name_file)
        text, name =  read_file(name_file)
        save_file(text, name)
    sys.exit()
    


if __name__ == "__main__":
    main()
    