from src.gui_pages.base_page import BasePage
from src.Locators.auth_locators import AuthPageLocators as LocatorsAuth
import time



class AuthPage(BasePage):

    def check_title_tab_application(self):
        self.text_check = "Заявки"
        self.element_is_visable(LocatorsAuth.NAME_APP)
        name_title = self.elemets_is_present(LocatorsAuth.NAME_APP).text
        return name_title

    def log_out(self):
        self.name_modal = "Система информационной поддержки “AZK-TS”"
        self.element_is_visable(LocatorsAuth.LOG_OUT).click()
        # time.sleep(1)
        self.element_is_visable(LocatorsAuth.MODAL_LOG_OUT).click()
        self.title_auth_modal = self.element_is_visable(LocatorsAuth.MODAL_AUTH).text
        return self.title_auth_modal


    def notifixation_ru(self):
        self.name_error = "Неверный логин или пароль"
        nofication_ru = self.element_is_visable(LocatorsAuth.NOTIFICATION_INCORECT_PASS).text
        return nofication_ru

    def check_reset_pass(self):
        invalid_email = "test123@mail.ru"
        self.error_email = "На данный почтовый адрес регистрация не производилась"
        self.element_is_visable(LocatorsAuth.BUTTON_FORGET_PASS).click()
        self.element_is_visable(LocatorsAuth.INPUT_FOR_EMAIL).send_keys(invalid_email)
        self.elemets_is_present(LocatorsAuth.SUBMIT_RESET_PASS).click()
        self.check_butt = self.element_is_visable(LocatorsAuth.NOTIFICATION_ERROR_FOR_EMAIL).text
        return self.check_butt
















    def back_to_auth(self):
        self.element_is_visable(LocatorsAuth.BACK_TO_AUTH).click()

