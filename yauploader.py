#!/usr/bin/python3


from configuration import token
import requests
import time


class YaUploader:
    URL = 'https://cloud-api.yandex.net/v1/disk'
    date = time.strftime('%d%m%Y_%H%M%S')
    folder_name = f'test/{date}'

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + self.token
        }

    def disk_info(self):
        url = self.URL
        headers = self.headers
        response = requests.get(url, headers=headers)
        return response.json()

    def _create_folder(self):
        url = self.URL + '/resources'
        folder = self.folder_name
        headers = self.headers
        params = {'path': folder, 'overwrite': 'true'}
        response = requests.put(url=url, headers=headers, params=params)
        return response.json()

    def _path_to_file(self, file_name):
        url = self.URL + '/resources/upload'
        folder = self.folder_name
        headers = self.headers
        params = {'path': f'{folder}/{file_name}', 'overwrite': 'true'}
        response = requests.get(url=url, headers=headers, params=params)
        return response.json()

    def upload(self, file_name):
        self._create_folder()
        href = self._path_to_file(file_name=file_name).get('href')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print(f'Загрузка файла {file_name} в папку {self.folder_name} произведена успешно.')


if __name__ == '__main__':
    ya = YaUploader(token)
    ya.upload(file_name='hw_8.txt')
