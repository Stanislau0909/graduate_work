from src.gui_pages.application_page import Applicationpage as App
from tests.test_data.data_test_4_gui.data import Data
from env_configs.env import ENV


class TestApppage:

    def test_create_applicationVT(self, driver):
        app = App(driver, ENV)
        data = Data(driver, ENV)
        app.open()
        data.data_diagnost()
        app.create_app_VT()
        app.notification_about_successufully_create_app()

    def test_send_message_by_diagnostician(self, driver):
        app = App(driver, ENV)
        data = Data(driver, ENV)
        app.open()
        data.data_diagnost()
        app.open_app()
        app.send_messages_by_diagnostician()
        app.refresh_page()
        app.check_status_app_after_creating_before_assign()

    def test_send_file_by_diagnostician(self, driver):
        app = App(driver, ENV)
        data = Data(driver, ENV)
        app.open()
        data.data_diagnost()
        app.open_app()
        app.send_file_jpg_in_chat()

    def test_assign_app(self, driver):
        app = App(driver, ENV)
        data = Data(driver, ENV)
        app.open()
        data.data_specVT()
        app.refresh_page()
        app.open_app()
        app.assign_app_for_specialist()
        app.refresh_page()
        app.check_status_app_after_assign()
    def test_is_there_implementer_in_app(self, driver):
        app = App(driver, ENV)
        data = Data(driver, ENV)
        app.open()
        data.data_specVT()
        app.open_app()
        app.check_implementer_in_app()
    def test_sending_message_by_specialist(self, driver):
        app = App(driver, ENV)
        data = Data(driver, ENV)
        app.open()
        data.data_specVT()
        app.open_app()
        app.send_messages_by_specialist()
        app.refresh_page()
        app.check_status_app_sending_message_from_specialist()
    def test_change_status_app_after_sending_sms_from_di(self, driver):
        app = App(driver, ENV)
        data = Data(driver, ENV)
        app.open()
        data.data_diagnost()
        app.refresh_page()
        app.open_app()
        app.send_messages_by_diagnostician()
        app.refresh_page()
        app.check_status_app_sending_message_from_diagnostician()


















