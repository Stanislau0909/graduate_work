import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from tests.test_data.data_api.generator_wiki import CreateWiki
from tests.test_data.data_api.generator_applications import SendMessage
from tests.test_data.data_api.generator_wiki import SearchWiki
from tests.test_data.data_api.generator_applications import CreateAppVT
from tests.test_data.data_api.generator_applications import Migration
from tests.test_data.data_api.generator_applications import RateAppSuccess
from tests.test_data.data_api.generator_applications import RateAppCompleted

from env_configs.env_api import CLIENT_ID_ENV
from env_configs.env_api import ENV
from src.api_endpoits.wiki_endpoints import Wiki
from self import self


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def access_token_admin():
    payload = {
        "username": "dpkappadmin",
        "password": "524598",
        "grant_type": "password",
        "client_secret": CLIENT_ID_ENV,
        "client_id": "azk"
    }
    url = f"{ENV}/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_diagnostician():
    payload = {
        "username": "diagnostqa",
        "password": "524598",
        "grant_type": "password",
        "client_secret": CLIENT_ID_ENV,
        "client_id": "azk"
    }
    url = f"{ENV}/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_sds():
    payload = {
        "username": "sdsqa",
        "password": "524598",
        "grant_type": "password",
        "client_secret": CLIENT_ID_ENV,
        "client_id": "azk"
    }
    url = f"{ENV}/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_specialist():
    payload = {
        "username": "specvtqa",
        "password": "524598",
        "grant_type": "password",
        "client_secret": CLIENT_ID_ENV,
        "client_id": "azk"
    }
    url = f"{ENV}/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_designer():
    payload = {
        "username": "konstqa",
        "password": "524598",
        "grant_type": "password",
        "client_secret": CLIENT_ID_ENV,
        "client_id": "azk"
    }
    url = f"{ENV}/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_designer_helper():
    payload = {
        "username": "designer_helper",
        "password": "524598",
        "grant_type": "password",
        "client_secret": CLIENT_ID_ENV,
        "client_id": "azk"
    }
    url = f"{ENV}/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_assistant_vt_azk():
    payload = {
        "username": "qavt",
        "password": "524598",
        "grant_type": "password",
        "client_secret": CLIENT_ID_ENV,
        "client_id": "azk"
    }
    url = f"{ENV}/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def id_user_diagnostician(access_token_diagnostician):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_diagnostician}"}
    r = requests.get(url, headers=headers)
    print(r.json()['id'])
    return r.json()["id"]


@pytest.fixture()
def id_user_sds(access_token_sds):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_sds}"}
    r = requests.get(url, headers=headers)
    print(r.json()['id'])
    return r.json()["id"]


@pytest.fixture()
def id_user_specvt(access_token_specialist):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_specialist}"}
    r = requests.get(url, headers=headers)
    return r.json()["id"]


@pytest.fixture()
def id_user_designer(access_token_designer):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_designer}"}
    r = requests.get(url, headers=headers)
    r_json = r.json()
    list_designer = []
    print(list_designer)
    list_designer.append(r_json['id'])
    return list_designer


@pytest.fixture()
def id_user_designer_helper(access_token_designer_helper):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_designer_helper}"}
    r = requests.get(url, headers=headers)
    r_json = r.json()
    list_designer = []
    print(list_designer)
    list_designer.append(r_json['id'])
    return list_designer


@pytest.fixture()
def id_user_assistant_azk_vt(access_token_assistant_vt_azk):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_assistant_vt_azk}"}
    r = requests.get(url, headers=headers)
    print(r.json()['id'])
    return r.json()["id"]


@pytest.fixture
def about_me_sds(access_token_sds):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_sds}"}
    r = requests.get(url, headers=headers)
    print(r.json())
    return r.json()


@pytest.fixture
def about_me_designer(access_token_designer):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_designer}"}
    r = requests.get(url, headers=headers)
    print(r.json())
    return r.json()


@pytest.fixture
def about_me_designer_helper(access_token_designer_helper):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_designer_helper}"}
    r = requests.get(url, headers=headers)
    print(r.json())
    return r.json()


@pytest.fixture
def about_me_assistant_azk_vt(access_token_assistant_vt_azk):
    url = f"{ENV}/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_assistant_vt_azk}"}
    r = requests.get(url, headers=headers)
    print(r.json())
    return r.json()


@pytest.fixture
def builder_message():
    return SendMessage()


@pytest.fixture()
def get_last_id_applications_vt(access_token_diagnostician):
    headers = {"Authorization": f"Bearer {access_token_diagnostician}"}
    payload = {
        "limit": 100,
        "page": 1,
        "optimisation": False,
        "filters": {},
        "order_by": [
            "-date_start"
        ],
        "type": 1
    }
    url = f"{ENV}/api/v1/applications/list"
    r = requests.post(url, headers=headers, json=payload)
    print(r.status_code)
    response = r.json()['data']

    application_total_list = []

    for application in response:
        # print(application)
        application_total_list.append(application["id"])
    print(application_total_list[0])
    return application_total_list[0]


@pytest.fixture()
def get_list_applications_vt(access_token_admin):
    headers = {"Authorization": f"Bearer {access_token_admin}"}
    payload = {
        "limit": 100,
        "page": 1,
        "optimisation": False,
        "filters": {},
        "order_by": [
            "-date_start"
        ],
        "type": 1
    }
    url = f"{ENV}/api/v1/applications/list"
    r = requests.post(url, headers=headers, json=payload)
    response = r.json()['data']
    application_total_list = []

    for application in response:
        application_total_list.append(application)
        print(application_total_list)
        return application_total_list


@pytest.fixture()
def id_app_vt(access_token_diagnostician):
    url = f"{ENV}/api/v1/applications/repair?auto_equipment=true"
    headers = {"Authorization": f"Bearer {access_token_diagnostician}"}
    body = {

        "description": "test",
        "family": 3,
        "model": 54901,
        "theme": "Тестовая заявка в работу не брать",
        "vin": "QWERTYQWERTYQunic",
        "defect_node": 2,
        "mileage": 5000,
        "error_codes": "",
        "engine_hours": 0,
        "engine_number": "4A-GE",

    }
    r = requests.post(url, headers=headers, json=body)
    return r.json()['id']


@pytest.fixture()
def get_json_about_app(access_token_diagnostician, get_last_id_applications_vt):
    url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}"
    headers = {"Authorization": f"Bearer {access_token_diagnostician}"}
    r = requests.get(url, headers=headers)
    r_json = r.json()['repair']['attachments']
    files_name = []

    for i in r_json:
        files_name.append(i['filename'])
        if len(files_name) > 3:
            break
    print(files_name)
    return files_name


@pytest.fixture
def builder_application():
    print(CreateAppVT().build())
    return CreateAppVT()


@pytest.fixture
def builder_migration():
    return Migration()


@pytest.fixture
def builder_rate_success():
    return RateAppSuccess()


@pytest.fixture
def builder_rate_completed():
    return RateAppCompleted()


@pytest.fixture()
def check_member_in_application(get_last_id_applications_vt, access_token_admin):
    url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}"
    headers = {"Authorization": f"Bearer {access_token_admin}"}
    r = requests.get(url, headers=headers)
    r_json = r.json()['repair']['members']
    people_with_need_role = []
    for member in r_json:
        role = member["role"]
        last_name = member['last_name']
        people_with_need_role.append({"role": role, "full_name": last_name})
    print(people_with_need_role)
    return people_with_need_role


@pytest.fixture()
def get_messages_in_chat(get_last_id_applications_vt, access_token_admin):
    url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}"
    headers = {"Authorization": f"Bearer {access_token_admin}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    messages = []
    for message in data['repair']['last_messages']:
        if message['is_attachment'] != True:
            messages.append(message['message'])
    print(messages, len(messages))
    return messages


@pytest.fixture()
def get_sid(get_last_id_applications_vt, access_token_admin):
    url = f"{ENV}/api/v1/applications/{get_last_id_applications_vt}"
    headers = {"Authorization": f"Bearer {access_token_admin}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    sid = data['repair']['sid']
    print(sid)
    return sid


@pytest.fixture()
def get_date_start_from_last_app_vt(access_token_admin):
    headers = {"Authorization": f"Bearer {access_token_admin}"}
    payload = {
        "limit": 100,
        "page": 1,
        "optimisation": False,
        "filters": {},
        "order_by": [
            "-date_start"
        ],
        "type": 1
    }
    url = f"{ENV}/api/v1/applications/list"
    r = requests.post(url, headers=headers, json=payload)
    response = r.json()['data']
    date_start_app = response[0]['date_start']
    clear_date = []
    for only_date in date_start_app:
        if only_date != "T":
            clear_date.append(only_date)
        else:
            break
    str_date = ''.join(clear_date)
    print(str_date)
    return str_date


@pytest.fixture()
def take_prev_evaluations(access_token_admin, id_user_diagnostician, get_date_start_from_last_app_vt):
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
    prev_scores = []
    oops = "В таблице нет данных"
    if r.status_code == 200:
        needs_diagnsotician = response['table_grouped'][0]
        for key in necessary_keys:
            score = needs_diagnsotician[key]
            prev_scores.append(score)
        print("Это значение перед оценкой", prev_scores)
        return prev_scores
    else:
        print(oops)
        return oops


# NEXT FUNCTION FOR APPLICATION WIKI


@pytest.fixture
def builder_wiki():
    print(CreateWiki().build())
    return CreateWiki()


@pytest.fixture
def builder_search_wiki():
    print(SearchWiki().build())
    return SearchWiki()


@pytest.fixture
def get_last_id_wiki_rae(access_token_admin):
    url = f"{ENV}/api/v1/azk_wiki/list"
    headers = {"Authorization": f"Bearer {access_token_admin}"}
    payload = {
        "limit": 20,
        "page": 1,
        "order_by": [
            "-date_updated"
        ],
        "keywords": [],
        "filters": {}
    }

    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()
    last = [i.get('id') for i in response_json['data']]
    print(last[0])
    return last[0]


@pytest.fixture
def get_id_attaches(access_token_admin):
    return Wiki().get_id_attach_files_in_wiki(access_token_admin)[0]


@pytest.fixture
def get_download_link_wiki_azk(access_token_admin, get_last_id_wiki_rae):
    url = f"{ENV}/api/v2/wiki/{get_last_id_wiki_rae}/get_download_link"
    headers = {"Authorization": f"Bearer {access_token_admin}"}
    self.response = requests.get(url, headers=headers)
    self.response_json = self.response.json()
    print(self.response_json.get('link_id'))
    return self.response_json.get('link_id')


@pytest.fixture
def list_wiki_azk(access_token_admin):
    url = f"{ENV}/api/v1/azk_wiki/list"
    headers = {"Authorization": f"Bearer {access_token_admin}"}
    payload = {"limit": 1,
               "order_by": ["-date_updated"]
               }
    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()
    return response_json
