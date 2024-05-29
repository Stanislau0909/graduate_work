from tests.test_data.data_gui.data import Data
from src.gui_pages.auth_page import AuthPage as Auth
from env_configs.env_gui import ENV



class TestAuthPage:

    def test_auth(self, driver):
        auth_page = Auth(driver, ENV)
        data = Data(driver, ENV)
        auth_page.open()
        data.data_admin()
        auth_page.check_title_tab_application()
        assert auth_page.check_title_tab_application() == auth_page.text_check

    def test_logout(self, driver):
        auth_page = Auth(driver, ENV)
        data = Data(driver, ENV)
        auth_page.open()
        data.data_admin()
        auth_page.log_out()
        assert auth_page.title_auth_modal == auth_page.name_modal

    def test_invalidpassword(self, driver):
        auth_page = Auth(driver, ENV)
        auth_page.open()
        data = Data(driver, ENV)
        data.incorect_cred()
        assert auth_page.notifixation_ru() == auth_page.name_error

    def test_check_work_resetPass_negative(self, driver):
        auth_page = Auth(driver, ENV)
        auth_page.open()
        auth_page.check_reset_pass()
        assert auth_page.check_butt == auth_page.error_email













