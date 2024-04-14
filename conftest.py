import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture()
def access_token_admin():
    payload = {
        "username": "dpkappadmin",
        "password": "524598",
        "grant_type": "password",
        "client_secret": "ebNLe1qZ5GfiAUJp74HUMLmkwRnTcucG",
        "client_id": "azk"
    }
    url = "https://api.qa.azkts.ru/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_diagnost():
    payload = {
        "username": "diagnostqa",
        "password": "524598",
        "grant_type": "password",
        "client_secret": "ebNLe1qZ5GfiAUJp74HUMLmkwRnTcucG",
        "client_id": "azk"
    }
    url = "https://api.qa.azkts.ru/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_specilist():
    payload = {
        "username": "specvtqa",
        "password": "524598",
        "grant_type": "password",
        "client_secret": "ebNLe1qZ5GfiAUJp74HUMLmkwRnTcucG",
        "client_id": "azk"
    }
    url = "https://api.qa.azkts.ru/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_designer():
    payload = {
        "username": "konstqa",
        "password": "524598",
        "grant_type": "password",
        "client_secret": "ebNLe1qZ5GfiAUJp74HUMLmkwRnTcucG",
        "client_id": "azk"
    }
    url = "https://api.qa.azkts.ru/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def access_token_assistant_vt_azk():
    payload = {
        "username": "qavt",
        "password": "524598",
        "grant_type": "password",
        "client_secret": "ebNLe1qZ5GfiAUJp74HUMLmkwRnTcucG",
        "client_id": "azk"
    }
    url = "https://api.qa.azkts.ru/auth/realms/azkts/protocol/openid-connect/token"
    r = requests.post(url, data=payload)
    return r.json()['access_token']


@pytest.fixture()
def id_user_diagnost(access_token_diagnost):
    url = "https://api.qa.azkts.ru/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_diagnost}"}
    r = requests.get(url, headers=headers)
    print(r.json()['id'])
    return r.json()["id"]


@pytest.fixture()
def id_user_specvt(access_token_specilist):
    url = "https://api.qa.azkts.ru/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_specilist}"}
    r = requests.get(url, headers=headers)
    return r.json()["id"]


@pytest.fixture()
def id_user_designer(access_token_designer):
    url = "https://api.qa.azkts.ru/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_designer}"}
    r = requests.get(url, headers=headers)
    r_json = r.json()
    list_designer = []
    print(list_designer)
    list_designer.append(r_json['id'])
    return list_designer


@pytest.fixture()
def id_user_assistant_azk_vt(access_token_assistant_vt_azk):
    url = "https://api.qa.azkts.ru/api/v1/users/me"
    headers = {"Authorization": f"Bearer {access_token_assistant_vt_azk}"}
    r = requests.get(url, headers=headers)
    print(r.json()['id'])
    return r.json()["id"]


@pytest.fixture()
def get_last_id_applications_vt(access_token_diagnost):
    headers = {"Authorization": f"Bearer {access_token_diagnost}"}
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
    url = "https://api.qa.azkts.ru/api/v1/applications/list"
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
    url = "https://api.qa.azkts.ru/api/v1/applications/list"
    r = requests.post(url, headers=headers, json=payload)
    response = r.json()['data']
    application_total_list = []

    for application in response:
        application_total_list.append(application)
        print(application_total_list)
        return application_total_list


@pytest.fixture()
def id_app_vt(access_token_diagnost):
    url = "https://api.qa.azkts.ru/api/v1/applications/repair?auto_equipment=true"
    headers = {"Authorization": f"Bearer {access_token_diagnost}"}
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
def get_json_about_app(access_token_diagnost, get_last_id_applications_vt):
    url = f"https://api.qa.azkts.ru/api/v1/applications/{get_last_id_applications_vt}"
    headers = {"Authorization": f"Bearer {access_token_diagnost}"}
    r = requests.get(url, headers=headers)
    r_json = r.json()['repair']['attachments']
    files_name = []

    for i in r_json:
        files_name.append(i['filename'])
        if len(files_name) > 3:
            break
    print(files_name)
    return files_name


@pytest.fixture()
def check_member_in_application(get_last_id_applications_vt, access_token_admin):
    url = f"https://api.qa.azkts.ru/api/v1/applications/{get_last_id_applications_vt}"
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
    url = f"https://api.qa.azkts.ru/api/v1/applications/{get_last_id_applications_vt}"
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
    url = f"https://api.qa.azkts.ru/api/v1/applications/{get_last_id_applications_vt}"
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
    url = "https://api.qa.azkts.ru/api/v1/applications/list"
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
def take_prev_evaluations(access_token_admin, id_user_diagnost, get_date_start_from_last_app_vt):
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
        needs_diagnsotician = response['table'][0]
        for key in necessary_keys:
            score = needs_diagnsotician[key]
            prev_scores.append(score)
        print(prev_scores)
        return prev_scores
    else:
        print(oops)
        return oops






# @pytest.fixture(scope='session')
# def data_admin(driver):
#     authpage = AuthPage(driver,ENV)
#     login = 'dpkappadmin'
#     password =524598
#     authpage.element_is_visable(LocatorsAuth.LOGIN).send_kyes(login)
#     authpage.element_is_visable(LocatorsAuth.PASSWORD).send_keys(password)
#     authpage.element_is_visable(LocatorsAuth.ENTER).click()
#     yield driver
