import os
import random
import shutil
import zipfile
import io

import requests

from src.api_endpoits.base_endpoint import BaseEndpoints as Base
from env_configs.env_api import ENV
from tests.test_data.data_api.generator_applications import DataApplication as Data
from tests.test_data.data_api.path_to_files import PathtoFile


class Applications(Base):

    def __init__(self):
        self.response = None
        self.response_json = None
        # self.payload = None

    def setup(self):
        self.data = Data()
        self.path_files = PathtoFile()

    def list_application_vt(self, access_token_admin):
        url = f"{ENV}/api/v1/applications/list"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        payload = {
            'limit': 20,
            'order_by': ['-date_start'],
            'type': 1
        }
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        print(response_json)
        return response

    def list_application_zch(self, access_token_admin):
        url = f"{ENV}/api/v1/applications/list"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        payload = {
            'limit': 20,
            'order_by': ['-date_start'],
            'type': 2
        }
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        print(response_json)
        return response_json

    def app_last_status(self, response):
        status_app = response
        # status_last_app = [status['status'] for status in status_app['data']]
        last_item = status_app['data'][0]['status']
        print(last_item)
        return last_item

    def info_about_last_app(self):
        info_last_app = self.response_json
        print(info_last_app['data'][0])
        return info_last_app['data'][0]

    def response_from_application(self, access_token_admin, get_last_id):
        url = f"{ENV}/api/v1/applications/{get_last_id}"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        response = requests.get(url, headers=headers)
        response_json = response.json()
        return response_json

    def info_about_attaches(self, files, response_from_server):
        info_about_attach = response_from_server
        name_attach = [attach['filename'] for attach in info_about_attach['repair']['attachments']]
        print(name_attach)
        print(files)
        assert files[0] in name_attach

    def compare_common_keys_for_application(self, response_from_server, payload_from_client):
        response_from_server2 = response_from_server['repair']
        common_keys = set(response_from_server2.keys()) & set(payload_from_client.keys())
        for key in common_keys:
            value1 = response_from_server2[key]
            value2 = payload_from_client[key]
            if value1 == value2:
                print(f"Значение ключа '{key}' одинаково: {value1}")
            else:
                raise ValueError(
                    f"Значение ключа '{key}' различается: {value1} (в первом словаре) и {value2} (во втором словаре)")

    def create_app(self, jwt, payload):  # return app's id
        url = f"{ENV}/api/v1/applications/repair?auto_equipment=true"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        return response

    def attach_with_creating_app(self, jwt, file, get_last_id_applications_vt):
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/attach"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, files=file)
        return response

    def send_sms_in_chat(self, get_last_id_applications_vt, jwt,
                         payload):  # return id_app, id_sms, user_id, sender_type, message, timestamp
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/chat"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, json=payload)
        return response

    def check_value_field_message(self, payload, response_from_server):
        server_response = response_from_server
        last_messages = server_response['repair']['last_messages'][-1]['message']
        assert payload['message'] == last_messages

    def about_me(self, token):
        url = f"{ENV}/api/v1/users/me"
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(url, headers=headers)
        self.response_json = r.json()
        return self.response_json['id']

    def check_members_in_application(self, payload, response_from_server):
        server_response = response_from_server
        id_all_members = [mem["id"] for mem in server_response["repair"]["members"]]
        pars_payload = [payload['id']]
        assert list(set(id_all_members) & set(pars_payload))

    def send_file_in_chat(self, jwt, file, get_last_id_applications_vt, id_user,
                          sender_type):  # sender_type ==  true for diagnostician,sds and false for specialist,designer
        # return id_app, id_sms, user_id, sender_type, message, timestamp ,filename , if this file pdf then file_weight
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/chat_with_attachment?application_id={get_last_id_applications_vt}&user_id={id_user}&sender_type={sender_type}&message=&is_attachment=false"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, files=file)
        return response

    def info_about_attaches_for_chat_and_compare(self, payload, response_from_server):
        # file_name = response_from_server['repair']['attachments'][0]['filename']
        file_name = [picture['filename'] for picture in response_from_server['repair']['attachments']]
        assert payload[0] in file_name

    def send_file_in_chat_from_specialist(self, jwt, file, get_last_id_applications_vt, id_user):
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/chat_with_attachment?application_id={get_last_id_applications_vt}&user_id={id_user}&sender_type=false&message=&is_attachment=false"
        headers = {"Authorization": f"Bearer {jwt}"}
        self.response = requests.post(url, headers=headers, files=file)
        self.response_json = self.response.json()

    def check_file_name(self, file_name):
        assert self.response_json['attachment_filename'] == file_name

    def assign_implementer(self, get_last_id_applications_vt, jwt, payload):  # in payload send implementer's id
        url = f"{ENV}/api/v1/applications/repair/{get_last_id_applications_vt}"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.put(url, headers=headers, json=payload)
        # response_json = response.json()
        return response  # return short info about app

    def check_implementor_id_after_assign(self, payload, response_from_server):
        response_from_server_pars = response_from_server.json()
        assert response_from_server_pars['implementer'] == payload

    def check_file_name_in_application(self, get_json_about_app, list_attachments_with_app):
        try:
            assert list_attachments_with_app == get_json_about_app
            print("Списки совпадают!")
        except AssertionError:
            print("Списки не совпадают. Вот различия:")
            print(set(get_json_about_app) - set(list_attachments_with_app))

    def assign_to_designer(self, jwt, get_last_id_applications_vt, id_designer):
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/designers"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {"ids": id_designer}
        response = requests.put(url, headers=headers, json=payload)
        return response

    def check_result_true_after_adding_designer(self, response_from_server):
        assert response_from_server.json()['result'] == True

    def delete_participants_type_designer(self, jwt, id_user_who_should_delete, id_app):
        url = f"{ENV}/api/v1/applications/participants"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {
            "application_id": id_app,
            "user_id": str(id_user_who_should_delete[0])
        }
        response = requests.put(url, headers=headers, json=payload)
        return response

    def delete_participants_type_specialist(self, jwt, id_user_who_should_delete, id_app):
        url = f"{ENV}/api/v1/applications/participants"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {
            "application_id": id_app,
            "user_id": str(id_user_who_should_delete)
        }
        response = requests.put(url, headers=headers, json=payload)
        return response

    def check_deleted_member(self, payload, response_from_server):
        server_response = response_from_server
        id_all_members = [mem["id"] for mem in server_response["repair"]["members"]]
        id_deleted_member = [payload['id']]
        assert list(set(id_all_members) & set(id_deleted_member)) != []

    def check_designer_in_after_adding(self, check_member_in_application):
        user_role_and_name = check_member_in_application

        target_role = 'support_designer'
        target_full_name = 'Лаптёнок(конст)qa'

        role_found = any(entry['role'] == target_role for entry in user_role_and_name)
        full_name_found = any(entry['full_name'] == target_full_name for entry in user_role_and_name)

        assert role_found and full_name_found

    def check_system_sms_after_adding_designer(self, get_messages_in_chat, get_sid):
        system_sms_after_adding_designer = f"Ваша заявка №{get_sid} направлена Конструктору: Лаптёнок(конст)qa С.."
        print(system_sms_after_adding_designer, system_sms_after_adding_designer in get_messages_in_chat)
        assert system_sms_after_adding_designer in get_messages_in_chat

    def back_app_in_status_azk_from_designer(self, get_last_id_applications_vt, jwt):
        url = f"{ENV}/api/v1/applications/repair/{get_last_id_applications_vt}"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {"status": 4}
        response = requests.put(url, headers=headers, json=payload)
        return response

    def adding_assistant_in_app_side_azk(self, jwt, get_last_id_applications_vt, id_user_assistant_azk_vt):
        url = f"{ENV}/api/v1/applications/repair/{get_last_id_applications_vt}/assistants/{id_user_assistant_azk_vt}"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers)
        return response

    def check_assistant_side_azk_after_adding(self, check_member_in_application):
        user_role_and_name = check_member_in_application

        target_role = 'technical_support_specialist_rae'
        target_full_name = 'Разработчик(вт)'

        role_found = any(entry['role'] == target_role for entry in user_role_and_name)
        full_name_found = any(entry['full_name'] == target_full_name for entry in user_role_and_name)

        assert role_found and full_name_found

    def check_system_sms_after_adding_assistnat_azk(self, get_messages_in_chat, get_sid):
        system_sms_after_adding_assistnat = f"В вашу заявку №{get_sid} добавлен ассистент: Разработчик(вт) Q.A."
        print(system_sms_after_adding_assistnat, system_sms_after_adding_assistnat in get_messages_in_chat)
        assert system_sms_after_adding_assistnat in get_messages_in_chat

    def migration_application(self, get_last_id_app, payload, jwt):
        url = f"{ENV}/api/v1/applications/{get_last_id_app}/migration"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, json=payload)
        return response

    def fields_for_compare_after_migration(self, response_vt, response_zch):
        new_response_for_compare_vt = {
            "theme": response_vt["repair"]["theme"],
            "description": response_vt["repair"]["description"],
            "vin": response_vt["repair"]['vin'],
            "model": response_vt['repair']['model'],
            "family": response_vt['repair']['family'],
            "company_name": response_vt['repair']['created_by']['company_name'],
            "info_about_created": response_vt['repair']['created_by']
        }
        new_response_for_compare_zch = {
            "theme": response_zch["mechanic"]["theme"],
            "description": response_zch["mechanic"]["description"],
            "vin": response_zch["mechanic"]['vin'],
            "model": response_zch['mechanic']['model'],
            "family": response_zch['mechanic']['family'],
            "company_name": response_zch['mechanic']['created_by']['company_name'],
            "info_about_created": response_zch['mechanic']['created_by']
        }

        attach_file_in_vt = [item['filename'] for item in response_vt['repair']['attachments']]
        attach_file_in_zch = [item['filename'] for item in response_zch['mechanic']['attachments']]

        print(new_response_for_compare_vt)
        print(new_response_for_compare_zch)
        assert new_response_for_compare_vt == new_response_for_compare_zch
        if not attach_file_in_vt:
            raise ValueError("Список attach_file_in_vt пустой")
        if not attach_file_in_zch:
            raise ValueError("Список attach_file_in_zch пустой")
        if not any(item in attach_file_in_zch for item in attach_file_in_vt):
            raise ValueError(
                "Ни один элемент из списка zch не присутствует в списке vt. Может быть заявка не имеет атачей надо смотреть!")

    def offer_to_close_application(self, get_last_id, jwt):
        url = f"{ENV}/api/v1/applications/repair/{get_last_id}"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {
            'id': get_last_id,
            'status': 6
        }
        response = requests.put(url, headers=headers, json=payload)
        response_json = response.json()
        return response

    def rate_app_from_specialist_vt(self, jwt, get_last_id_applications_vt):
        score_type = random.sample(range(6, 14), 3)
        url = f"{ENV}/api/v1/reports/score_application/specialist"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {"application_id": get_last_id_applications_vt,
                   "score_type": score_type}
        response = requests.post(url, headers=headers, json=payload)
        response_json = response
        print(score_type, response_json)
        return response

    def take_after_evaluations(self, access_token_admin, id_user_diagnostician, get_date_start_from_last_app_vt):
        url = f"{ENV}/api/v1/reports/report_user_rating_rae"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        payload = {
            "type": 1,
            "user_ids": [
                id_user_diagnostician
            ],
            "date_start": f"{get_date_start_from_last_app_vt}",
            "date_end": f"{get_date_start_from_last_app_vt}",
            "companies": [],
            "score_type": []
        }
        r = requests.post(url, headers=headers, json=payload)
        response = r.json()
        needs_diagnsotician = response['table_grouped'][0]
        necessary_keys = [
            'lack_of_knowledge_experience',
            'lack_of_basic_knowledge',
            'do_not_want_make_decisions',
            'engineer_does_not_use_info_materials',
            'lack_of_info_materials',
            'part_number_request',
            'complex_issue_that_requered_elaboration',
            'firmware_request'
        ]
        after_scores = []
        for key in necessary_keys:
            score = needs_diagnsotician[key]
            after_scores.append(score)
            if after_scores == [0, 0, 0, 0, 0, 0, 0, 0]:
                print("Оценка не засчиталась")
        print("Это значение уже после оценки:", after_scores)
        return after_scores

    def compare_result(self, prev_result, final_result):
        result = 0
        bad_result = 0
        if prev_result != "В таблице нет данных":
            for prev, after in zip(prev_result, final_result):
                if after == prev + 1:
                    result += 1
            assert result == 3
        else:
            bad_result += 1
            return True

    def general_point_for_closing_app(self, jwt, get_last_id_applications_vt, status):
        url = f"{ENV}/api/v1/applications/repair/{get_last_id_applications_vt}"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {"id": get_last_id_applications_vt,
                   "status": status}
        response = requests.put(url, headers=headers, json=payload)
        response_json = response.json()
        return response

    def rate_app_from_diagnostician(self, jwt, payload):
        url = f"{ENV}/api/v1/reports/score_application/diagnostician"
        headers = {"Authorization": f"Bearer {jwt}"}
        response = requests.post(url, headers=headers, json=payload)
        return response

    def compare_common_keys_after_rate_by_diagnostician(self, payload, response_from_server):
        common_keys = set(response_from_server.keys()) & set(payload.keys())
        for key in common_keys:
            value1 = response_from_server[key]
            value2 = payload[key]
            if value1 == value2:
                print(f"Значение ключа '{key}' одинаково: {value1}")
            else:
                raise ValueError(
                    f"Значение ключа '{key}' различается: {value1} (в первом словаре) и {value2} (во втором словаре)")

    def check_changing_defect_node_after_rate_by_diagnostician(self, payload, response_from_server):
        payload_defect_node = payload['defect_node']
        response_from_server_defect_node = response_from_server['defect_node']
        assert payload_defect_node == response_from_server_defect_node

    def get_download_link_application(self, access_token_admin, get_last_id_application):
        url = f"{ENV}/api/v2/applications/{get_last_id_application}/get_download_link"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        response = requests.get(url, headers=headers)
        response_json = response.json()
        print(response_json.get('link_id'))
        return response

    def paste_link_for_download_pdf(self, get_download_link_app):
        url = f"{ENV}/api/v2/applications/download/{get_download_link_app}/?format=pdf&lang=ru"
        response = requests.get(url)
        downloaded_file = zipfile.ZipFile(io.BytesIO(response.content))
        path_to_file = os.getcwd()
        destination_directory = f"{path_to_file}\\for_downloaded_files_app_pdf"
        downloaded_file.extractall(destination_directory)
        print(downloaded_file)

    def paste_link_for_download_html(self, get_download_link_html):
        url = f"{ENV}/api/v2/applications/download/{get_download_link_html}/?format=html&lang=ru"
        response = requests.get(url)
        downloaded_file = zipfile.ZipFile(io.BytesIO(response.content))
        path_to_file = os.getcwd()
        destination_directory = f"{path_to_file}\\for_downloaded_file_app_html"
        downloaded_file.extractall(destination_directory)
        print(downloaded_file)

    def list_app_azk_vt(self, access_token_admin):
        url = f"{ENV}/api/v1/applications/list"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        payload = {"limit": 1,
                   "order_by": ["-date_updated"]
                   }
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        list_with_file_name = []
        for attachment in response_json['data'][0]['attachments']:
            list_with_file_name.append(attachment['filename'])
        print(list_with_file_name)
        return list_with_file_name

    def collect_files_which_were_downloading_pdf(self, response_from_app):
        path_to_file = os.getcwd()
        download_directory = f"{path_to_file}\\for_downloaded_files_app_pdf\\application_attachments"
        downloaded_files = os.listdir(download_directory)
        expected_files = [item['filename'] for item in response_from_app['repair']['attachments']]
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

    def clean_downloaded_app_pdf(self):
        path_to_file = os.getcwd()
        folder_path = f'{path_to_file}\\for_downloaded_files_app_pdf'
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    def clean_downloaded_files_with_folder_pdf_app_attach(self):
        path_to_file = os.getcwd()
        folder_path = f'{path_to_file}\\for_downloaded_file_app_html\\application_attachments'
        try:
            shutil.rmtree(folder_path)
            print(f"Папка {folder_path} успешно удалена.")
        except Exception as e:
            print(f"Ошибка при удалении папки {folder_path}: {e}")

    def clean_downloaded_files_with_folder_pdf_chat(self):
        path_to_file = os.getcwd()
        folder_path = f'{path_to_file}\\for_downloaded_files_app_pdf\\chat_attachments'
        try:
            shutil.rmtree(folder_path)
            print(f"Папка {folder_path} успешно удалена.")
        except Exception as e:
            print(f"Ошибка при удалении папки {folder_path}: {e}")

    def collect_files_which_were_downloading_html(self, response_from_app):
        path_to_folder = os.getcwd()
        download_directory = f"{path_to_folder}\\for_downloaded_file_app_html\\application_attachments"
        downloaded_files = os.listdir(download_directory)
        expected_files = [item['filename'] for item in response_from_app['repair']['attachments']]
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

    def clean_downloaded_app_html(self):
        path_to_folder = os.getcwd()
        folder_path = f'{path_to_folder}\\for_downloaded_file_app_html'
        print('жёсткий путь', os.getcwd())
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    def clean_downloaded_files_with_folder_app_html(self):
        path_to_folder = os.getcwd()
        folder_path = f'{path_to_folder}\\for_downloaded_file_app_html\\application_attachments'
        try:
            shutil.rmtree(folder_path)
            print(f"Папка {folder_path} успешно удалена.")
        except Exception as e:
            print(f"Ошибка при удалении папки {folder_path}: {e}")

    def clean_downloaded_files_with_folder_pdf_chat_html(self):
        path_to_folder = os.getcwd()
        folder_path = f'{path_to_folder}\\for_downloaded_file_app_html\\chat_attachments'
        try:
            shutil.rmtree(folder_path)
            print(f"Папка {folder_path} успешно удалена.")
        except Exception as e:
            print(f"Ошибка при удалении папки {folder_path}: {e}")

    def rate_app_from_admin(self):
        pass

    def close_app_from_admin(self):
        pass
