import shutil

import requests
import pytest
import os
from urllib.parse import unquote
import zipfile
import io

from src.api_endpoits.base_endpoint import BaseEndpoints as Base

from tests.test_data.data_api.generator_applications import DataApplication as Data
from env_configs.env_api import ENV


class Wiki(Base):

    def __init__(self):
        self.payload = None
        self.data = Data()

    def create_wiki_manual(self, jwt, payload):
        url = f"{ENV}/api/v1/azk_wiki"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        print(response_json)
        print(os.getcwd())
        return response

    def check_types_data_in_create_wiki(self):
        assert (type(self.response_json['id'])) == str

    def adding_attach_in_wiki(self, jwt, get_last_id_wiki_rae, file):
        url = f"{ENV}/api/v1/azk_wiki/{get_last_id_wiki_rae}/attach"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, files=file)
        response_json = response.json()
        print(response_json)
        return response

    def get_id_attach_files_in_wiki(self, jwt):
        url = f"{ENV}/api/v1/azk_wiki/list"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {"limit": 1,
                   "order_by": ["-date_updated"]
                   }
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        id_files = [id_attach.get('id') for id_attach in response_json['data'][0]['attachments']]
        return id_files

    def get_all_field_json_wiki(self, jwt):
        url = f"{ENV}/api/v1/azk_wiki/list"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {"limit": 1,
                   "order_by": ["-date_updated"]
                   }
        self.response = requests.post(url, headers=headers, json=payload)
        self.response_json = self.response.json()
        id_files = [id_attach.get('id') for id_attach in self.response_json['data'][0]['attachments']]
        return id_files

    def delete_files_in_wiki(self, jwt, get_last_id_wiki_rae, id_attach_in_wiki):
        url = f"{ENV}/api/v1/azk_wiki/{get_last_id_wiki_rae}/attach/{id_attach_in_wiki}"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.delete(url, headers=headers)
        response_json = response.json()
        print(response_json['id'])
        return response

    def edit_fields_wiki(self, jwt, payload, get_last_id_wiki_rae):
        url = f"{ENV}/api/v1/azk_wiki/{get_last_id_wiki_rae}"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.put(url, headers=headers, json=payload)
        response_json = response.json()
        print(response_json)
        return response

    def check_search_input(self, jwt, payload):
        url = f"{ENV}/api/v1/azk_wiki/list"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        # print(self.response_json)
        return response

    def check_field_theme_keywords(self, payload, response):
        my_list_result = response
        print(my_list_result['data'])
        print(my_list_result['meta'])
        if my_list_result['data'] == False:
            print('list is empty')
        else:
            parsing_necessary_filed = [text.get('theme') for text in my_list_result['data']]
            if parsing_necessary_filed:
                parsing_necessary_filed2 = parsing_necessary_filed[0].split()
                any(item in payload for item in parsing_necessary_filed2)
            else:
                print('list is empty')

    def get_download_link_wiki_azk(self, access_token_admin, get_last_id_wiki_rae):
        url = f"{ENV}/api/v2/wiki/{get_last_id_wiki_rae}/get_download_link"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        response = requests.get(url, headers=headers)
        response_json = response.json()
        print(response_json.get('link_id'))
        return response

    def paste_link_for_download_pdf(self, get_download_link_wiki_azk):
        url = f"{ENV}/api/v2/wiki/download/{get_download_link_wiki_azk}/?format=pdf&lang=ru"
        response = requests.get(url)
        full_path = os.getcwd()
        downloaded_file = zipfile.ZipFile(io.BytesIO(response.content))
        destination_directory = f"{full_path}\\for_downloaded_files_wiki"
        downloaded_file.extractall(destination_directory)
        print(downloaded_file)
        return response

    def paste_link_for_download_html(self, get_download_link_wiki_azk):
        url = f"{ENV}/api/v2/wiki/download/{get_download_link_wiki_azk}/?format=html&lang=ru"
        response = requests.get(url)
        full_path = os.getcwd()
        downloaded_file = zipfile.ZipFile(io.BytesIO(response.content))
        destination_directory = f"{full_path}\\for_downloaded_files_wiki_html"
        downloaded_file.extractall(destination_directory)
        print(downloaded_file)
        return response

    def list_wiki_azk(self, access_token_admin):
        url = f"{ENV}/api/v1/azk_wiki/list"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        payload = {"limit": 1,
                   "order_by": ["-date_updated"]
                   }
        self.response = requests.post(url, headers=headers, json=payload)
        self.response_json = self.response.json()
        list_with_file_name = []
        for attachment in self.response_json['data'][0]['attachments']:
            list_with_file_name.append(attachment['filename'])
        print(list_with_file_name)
        return list_with_file_name

    def collect_files_which_were_downloading(self, expected_files):
        full_path = os.getcwd()
        download_directory = f"{full_path}\\for_downloaded_files_wiki\\attachments"
        downloaded_files = os.listdir(download_directory)
        for file in expected_files:
            found = False
            for downloaded_file in downloaded_files:
                if file == downloaded_file:
                    found = True
                    break
            assert found, f"Файл {file} не был скачан"
        print(downloaded_files)
        print("Все файлы успешно скачаны!")

        if set(downloaded_files) == set(expected_files):
            print("Списки идентичны")
        else:
            raise AssertionError("Списки не один в один")

    def clean_downloaded_wiki(self):
        full_path = os.getcwd()
        folder_path = f'{full_path}\\for_downloaded_files_wiki'
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    def clean_downloaded_files_with_folder(self):
        full_path = os.getcwd()
        folder_path = f'{full_path}\\for_downloaded_files_wiki\\attachments'
        try:
            shutil.rmtree(folder_path)
            print(f"Папка {folder_path} успешно удалена.")
        except Exception as e:
            print(f"Ошибка при удалении папки {folder_path}: {e}")

    def collect_files_which_were_downloading_html(self, expected_files):
        full_path = os.getcwd()
        download_directory = f"{full_path}\\for_downloaded_files_wiki_html\\attachments"
        downloaded_files = os.listdir(download_directory)
        for file in expected_files:
            found = False
            for downloaded_file in downloaded_files:
                if file == downloaded_file:
                    found = True
                    break
            assert found, f"Файл {file} не был скачан"
        print(downloaded_files)
        print("Все файлы успешно скачаны!")

        if set(downloaded_files) == set(expected_files):
            print("Списки идентичны")
        else:
            raise AssertionError("Списки не один в один")

    def clean_downloaded_wiki_html(self):
        full_path = os.getcwd()
        folder_path = f'{full_path}\\for_downloaded_files_wiki_html'
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    def clean_downloaded_files_with_folder_html(self):
        full_path = os.getcwd()
        folder_path = f'{full_path}\\for_downloaded_files_wiki_html\\attachments'
        try:
            shutil.rmtree(folder_path)
            print(f"Папка {folder_path} успешно удалена.")
        except Exception as e:
            print(f"Ошибка при удалении папки {folder_path}: {e}")

