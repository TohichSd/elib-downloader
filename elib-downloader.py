import shutil
import time
import sys
from requests import Session
from pathlib import Path
from json import loads, dumps
from PIL import Image

LOGIN_URL = 'http://elib.mpei.ru/login.php'
BASE_PAGE_URL = 'http://elib.mpei.ru/plugins/SecView/getDoc.php?id={id}&page={page}&type=small/fast'


def main():
    print('elib downloader by TohichSd\nhttps://github.com/TohichSd/elib-downloader\n')
    session = login()
    book_id = input('Введите ID книги: ')
    Path('./tmp').mkdir(exist_ok=True)
    images = []
    page_num = 0
    page_res = session.get(BASE_PAGE_URL.format(id=book_id, page=page_num))
    while 'phperror' not in page_res.text:
        with open('tmp/' + str(page_num + 1) + '.jpg', 'wb') as file:
            file.write(page_res.content)
        print('Загружено {} страниц'.format(page_num + 1), end='\r')
        images.append(Image.open('./tmp/' + str(page_num + 1) + '.jpg').convert('RGB'))
        page_num += 1
        page_res = session.get(BASE_PAGE_URL.format(id=book_id, page=page_num))
    images[0].save('result.pdf', save_all=True, append_images=images[1:])
    shutil.rmtree('./tmp')
    print('\nКнига сохранена в result.pdf')
    input('Нажмите Enter для закрытия...')


def login():
    session = Session()
    login_data = {'action': 'login',
                  'cookieverify': '',
                  'language': 'ru_UN'}
    with open('config.json', 'a+') as config_file:
        config_file.seek(0)
        content = config_file.read()
        config = {'username': '', 'password': ''}
        if len(content) > 0:
            config = loads(content)
        if config['username'] and config['password']:
            login_data['username'] = config['username']
            login_data['password'] = config['password']
        else:
            username = input('Введите логин: ')
            password = input('Введите пароль: ')
            login_data['username'] = username
            login_data['password'] = password
            json_config = dumps({'username': username, 'password': password})
            config_file.write(json_config)

        login_res = session.post(LOGIN_URL, data=login_data)
        if login_res.url.startswith(LOGIN_URL):
            open('config.json', 'w').close()
            raise Exception('Не удалось войти в электронную библиотеку')
        return session


if __name__ == '__main__':
    time.sleep(10)
    try:
        main()
    except Exception:
        print('error')
