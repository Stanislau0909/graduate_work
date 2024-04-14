from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ApplicationPageLocators:
        #Первое модальное окно при создании заявки
        BUTTON_FOR_CREATE_APP = (By.XPATH, "//button[@class= 'Button--YUouf accent--3a4zQ md--3cLPB ApplicationsPage-Tools_btn']")
        LIST_TYPES_APPS = (By.XPATH, "//div[@class= 'selector---Eebj md--GBbBs']")
        REPAIR_APP = (By.XPATH, "//div[@class= 'item--AsZ9e md--1_JQH'][1]")
        MECHANIC_APP = (By.XPATH, "//div[@class= 'item--AsZ9e md--1_JQH'][2]")
        FIRMWARE_APP = (By.XPATH, "//div[@class= 'item--AsZ9e md--1_JQH'][3]")
        SUBMIT_CHOSEN_CATEGORY_APP = (By.XPATH, "//button[@class= 'Button--YUouf accent--3a4zQ sm--5RYLw']")

        #Второе модальное окно при создании заявки ВТ
        LIST_FAMILY = (By.XPATH, "//div[@class='selector---Eebj md--GBbBs']")
        FAMILY_K3 = (By.XPATH, "(//div[@class='item--AsZ9e md--1_JQH'])[1]")
        VIN = (By.XPATH, "(//input[@class='input  '])[1]")
        MILEAGE = (By.XPATH, "(//input[@class='input  '])[3]")
        LIST_DEFECT_NODE = (By.XPATH, "(//div[@class='selector---Eebj md--GBbBs'])[2]")
        DEFECT_NODE_AUTO = (By.XPATH, "(//span[@class='label--OKIJs'])[1]")
        MODEL = (By.XPATH, "(//input[@class='input  '])[4]")
        THEME = (By.XPATH, "(//input[@class='input  '])[6]")
        DESCRIPTION = (By.XPATH, "(//input[@type='simple'])[3]")
        CREATE_BUTTON = (By.XPATH, "//button[@class='Button--YUouf accent--3a4zQ sm--5RYLw']")


        #Открытие меню с действиями для заявки рядом возле темы
        OPEN_FIRST_APP_TABLE = (By.XPATH, "(//tr[@class='row--2v6NO'])[1]")
        MENU_NEAR_THEME = (By.XPATH, "(//div[@id='dropdown-container'])[1]")
        BUTTON_ASSIGN = (By.XPATH, "(//div[@class='ApplicationInfo-MenuItem'])[1]")
        LIST_SPECIALIST = (By.XPATH, "(//div[@class='selector---Eebj md--GBbBs'])[1]")
        IMPUT_FOR_ENTER_DATA_SPEIALIST = (By.XPATH, "(//input[@class='searchInput--hC7pm md--3_Bxv'])[1]")
        FIRST_FOUND_SPECIALIST_IN_LIST: tuple[str, str] = (By.XPATH, "(//div[@class='options--3nP_q open--1KxzK'])[1]")
        SUBMIT_ASSIGN = (By.XPATH, "(//button[@class='Button--YUouf accent--3a4zQ sm--5RYLw'])[2]")

        BUTTON_CLOSE = (By.XPATH, "(//div[@class='ApplicationInfo-MenuItem'])[2]")
        BUTTON_SEND_TO_DESIGNER = (By.XPATH,"(//div[@class='ApplicationInfo-MenuItem'])[5]")
        BUTTON_MIGRATION = (By.XPATH,"(//div[@class='ApplicationInfo-MenuItem'])[3]")

        #Открытие меню возле инпута чата и сам инпут
        MENU_NEAR_CHAT = (By.XPATH, "//div[@class='ChatInput-MenuButton']")
        BUTTON_MEMBER = (By.XPATH, "(//div[@class='ChatInput-DropdownItem'])[1]")
        BUTTON_ADD_FILE = (By.XPATH, "(//div[@class='ChatInput-DropdownItem'])[2]")
        DRAG_AND_DROP = (By.XPATH, "//input[@type='file']")


        INPUT_FOR_MESSAGES = (By.XPATH, "//textarea[@class='ChatInput-Input__input']")
        BUTTON_FOR_SENDING_MESSAGE = (By.XPATH, "//div[@class='ChatInput-SendButton']")
        FIRST_MESSAGE = (By.XPATH, "//div[@data-index=0]")
        SECOND_MESSAGE = (By.XPATH, "//div[@data-index=2]")
        THIRD_MESSAGE = (By.XPATH, "//div[@data-index=3]")
        OPEN_EXTRA_TAB = (By.XPATH, "//button[@class='Chip--28e2m md--2CCot primary--3jRtb inverted--1nZXn']")
        CHECK_PICTURE_IN_EXTRA_TAB = (By.XPATH, "(//div[@class='AdditionalInfo-AttachmentItem'])[1]")
        #Локаторы для выхода из приложения




        #Локаторы для проверки внутри заявки
        CHECK_STATUS_APP = "//span[@class='t-t--14 t-wt--regular t-v--text']"
        CHECK_STATUS_APP_WITH_BY = (By.XPATH, "//span[@class='t-t--14 t-wt--regular t-v--text']")
        CHECK_IMPLEMENTER_IN_APP = (By.XPATH, "(//span[@class='t-pt--15 t-wt--regular t-v--text MainInfoRAE-InfoItemValue'])[9]")
        SUCCESSFULY_CREATE_APP = (By.XPATH , "//div[@class='notification Success']")









