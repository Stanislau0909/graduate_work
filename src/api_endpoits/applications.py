import requests

from env_configs.env_api import ENV
from tests.test_data.data_dicts_4_api.data_applications import DataApplication as Data


class Applications:

    def __init__(self):
        self.response = None
        self.response_json = None
        self.payload = None

    def setup(self):
        self.data = Data()

    def check_status_is_200ok(self):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.response.status_code}"

    def check_status_is_204_No_content(self):
        assert self.response.status_code == 204, f"Expected status code 204, but got {self.response.status_code}"

    def create_app(self, jwt, payload):
        url = f"{ENV}/api/v1/applications/repair?auto_equipment=true"
        headers = {"Authorization": f"Bearer {jwt}"}
        self.response = requests.post(url, headers=headers, json=payload)
        self.response_json = self.response.json()

    def attach_with_creating_app(self, jwt, file, get_last_id_applications_vt):
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/attach"
        headers = {"Authorization": f"Bearer {jwt}"}
        self.response = requests.post(url, headers=headers, files=file)
        self.response_json = self.response

    def send_sms_in_chat(self, get_last_id_applications_vt, jwt, payload):
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/chat"
        headers = {"Authorization": f"Bearer {jwt}"}
        self.response = requests.post(url, headers=headers, json=payload)
        self.response_json = self.response.json()

    def check_value_field_message(self, payload):
        assert self.response_json['message'] == payload

    # def check_value_filed_sender_type(self):
    #     assert self.response_json['sender_type'] == self.payload['sender_type']
    #
    # def check_senders_user_id(self):
    #     assert self.response_json['user_id'] == self.payload['user_id']

    def check_status_application_sent(self, get_list_applications_vt):
        assert get_list_applications_vt[0]['status'] == 1

    def check_status_application_in_work(self, get_list_applications_vt):
        assert get_list_applications_vt[0]['status'] == 3

    def check_status_application_waiting_azk(self, get_list_applications_vt):
        assert get_list_applications_vt[0]['status'] == 4

    def check_status_application_designer(self, get_list_applications_vt):
        assert get_list_applications_vt[0]['status'] == 5

    def check_status_application_success(self, get_list_applications_vt):
        assert get_list_applications_vt[0]['status'] == 8

    def send_file_in_chat_from_diagnost(self, jwt, file, get_last_id_applications_vt, id_user_diagnost):
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/chat_with_attachment?application_id={get_last_id_applications_vt}&user_id={id_user_diagnost}&sender_type=true&message=&is_attachment=false"
        headers = {"Authorization": f"Bearer {jwt}"}
        self.response = requests.post(url, headers=headers, files=file)
        self.response_json = self.response.json()

    def send_file_in_chat_from_specialist(self, jwt, file, get_last_id_applications_vt, id_user):
        url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}/chat_with_attachment?application_id={get_last_id_applications_vt}&user_id={id_user}&sender_type=false&message=&is_attachment=false"
        headers = {"Authorization": f"Bearer {jwt}"}
        self.response = requests.post(url, headers=headers, files=file)
        self.response_json = self.response.json()

    def check_file_name(self, file_name):
        assert self.response_json['attachment_filename'] == file_name

    def assign_implementer(self, get_last_id_applications_vt, jwt, payload):
        url = f"{ENV}/api/v1/applications/repair/{get_last_id_applications_vt}"
        headers = {"Authorization": f"Bearer {jwt}"}
        self.response = requests.put(url, headers=headers, json=payload)
        self.response_json = self.response.json()

    def check_implementor_id_after_assign(self, payload):
        assert self.response_json['implementer'] == payload

    def check_status_application_assign(self, get_list_applications_vt):
        assert get_list_applications_vt[0]['status'] == 2

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
        self.response = requests.put(url, headers=headers, json=payload)
        self.response_json = self.response.json()
        print(self.response_json)
        print(self.response.status_code)

    def check_result_true_after_adding_designer(self):
        assert self.response_json['result'] == True

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
        self.response = requests.put(url, headers=headers, json=payload)
        self.response_json = self.response.json()

    def adding_assistant_in_app_side_azk(self, jwt, get_last_id_applications_vt, id_user_assistant_azk_vt):
        url = f"{ENV}/api/v1/applications/repair/{get_last_id_applications_vt}/assistants/{id_user_assistant_azk_vt}"
        headers = {"Authorization": f"Bearer {jwt}"}
        self.response = requests.post(url, headers=headers)
        self.response_json = self.response.json()

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

    def rate_app_from_specialist(self, jwt, get_last_id_applications_vt):
        url = f"{ENV}/api/v1/reports/score_application/specialist"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {"application_id": get_last_id_applications_vt,
                   "score_type": [7, 8, 12]}
        self.response = requests.post(url, headers=headers, json=payload)
        self.response_json = self.response

    def take_after_evaluations(self, access_token_admin, id_user_diagnost, get_date_start_from_last_app_vt):
        url = f"https://api.qa.azkts.ru/api/v1/reports/report_user_rating_rae"
        headers = {"Authorization": f"Bearer {access_token_admin}"}
        payload = {
            "type": 1,
            "user_ids": [
                id_user_diagnost
            ],
            "date_start": f"{get_date_start_from_last_app_vt}",
            "date_end": f"{get_date_start_from_last_app_vt}",
            "companies": [],
            "score_type": []
        }
        r = requests.post(url, headers=headers, json=payload)
        response = r.json()
        needs_diagnsotician = response['table'][0]
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

    def close_app_from_specialist(self, jwt, get_last_id_applications_vt):
        url = f"{ENV}/api/v1/applications/repair/{get_last_id_applications_vt}"
        headers = {"Authorization": f"Bearer {jwt}"}
        payload = {"id": get_last_id_applications_vt,
                   "status": 8}
        self.response = requests.put(url, headers=headers, json=payload)
        self.response_json = self.response.json()
        assert self.response_json['status'] == 8

    def rate_app_from_diagnostician(self):
        pass

    def close_app_from_diagnostician(self):
        pass

    def rate_app_from_admin(self):
        pass

    def close_app_from_admin(self):
        pass

