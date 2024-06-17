import requests
import random
from faker import Faker
import os

from env_configs.env_api import ENV

faker = Faker()

# random_number = random.randint(1, 7)
# print(random_number)


# def test_list_application(access_token_admin):
#     url = f"{ENV}/api/v1/applications/list"
#     headers = {"Authorization": f"Bearer {access_token_admin}"}
#     payload = {
#         'limit': 20,
#         'order_by': ['-date_start']
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     response_json = response.json()
#     print(response_json)
#     for i in response_json['data']:
#         print(i)
#
#
# def test_current_application(access_token_admin, get_last_id_applications_vt):
#     url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}"
#     headers = {"Authorization": f"Bearer {access_token_admin}"}
#     response = requests.get(url, headers=headers)
#     response_json = response.json()
#     print(response_json['repair'])
#     new_dict = {
#         "theme": response_json["repair"]["theme"],
#         "description": response_json["repair"]["description"],
#         "vin": response_json["repair"]['vin'],
#         "model": response_json['repair']['model'],
#         "family": response_json['repair']['family'],
#         "company_name": response_json['repair']['created_by']['company_name'],
#         "info_about_created": response_json['repair']['created_by']
#     }
#     print(new_dict)
#
#
# def test_random_value():
#     random_values = random.sample(range(1, 9), 3)
#     print(random_values)
#
#
# def test_take_after_evaluations(access_token_admin, id_user_diagnostician, get_date_start_from_last_app_vt):
#     url = f"{ENV}/api/v1/reports/report_user_rating_rae"
#     headers = {"Authorization": f"Bearer {access_token_admin}"}
#     payload = {
#         "type": 1,
#         "user_ids": [
#             id_user_diagnostician
#         ],
#         "date_start": f"{get_date_start_from_last_app_vt}",
#         "date_end": f"{get_date_start_from_last_app_vt}",
#         "companies": [],
#         "score_type": []
#     }
#     r = requests.post(url, headers=headers, json=payload)
#     response = r.json()
#     needs_diagnsotician = response['table_grouped'][0]
#     necessary_keys = [
#         'lack_of_knowledge_experience',
#         'lack_of_basic_knowledge',
#         'do_not_want_make_decisions',
#         'engineer_does_not_use_info_materials',
#         'lack_of_info_materials',
#         'part_number_request',
#         'complex_issue_that_requered_elaboration',
#         'firmware_request'
#     ]
#     after_scores = []
#     for key in necessary_keys:
#         score = needs_diagnsotician[key]
#         after_scores.append(score)
#         if after_scores == [0, 0, 0, 0, 0, 0, 0, 0]:
#             print("Оценка не засчиталась")
#     print("Это значение уже после оценки:", after_scores)
#     return after_scores


class RateAppSuccess:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_application_id(self, payload='1234432432'):
        self.result['id'] = payload
        return self

    def set_info_availability(self, info=random.choice(range(1, 6))):
        self.result['information_availability'] = info
        return self

    def set_response_accuracy(self, response_acc=random.choice(range(1, 6))):
        self.result['response_accuracy'] = response_acc
        return self

    def set_response_time(self, response_time=random.choice(range(1, 6))):
        self.result['response_time'] = response_time
        return self

    def reset(self):
        self.set_application_id()
        self.set_info_availability()
        self.set_response_accuracy()
        self.set_response_time()
        self.add_comment_field()
        return self

    def add_comment_field(self, comment=faker.text()):
        total_sum = (
                self.result['information_availability']
                + self.result['response_accuracy']
                + self.result['response_time']
        )
        if total_sum < 15:
            self.result['comment'] = comment
        else:
            del self.result['comment']
        print(total_sum)
        return self

    def build(self):
        return self.result


rate = RateAppSuccess()
print(rate.set_response_accuracy(5).set_response_time(4).set_info_availability(5).add_comment_field().build())


print(os.getcwd())