from src.gui_pages.base_page import BasePage
from src.Locators.auth_locators import AuthPageLocators as LocatorsAuth


class Data(BasePage):

    def data_admin(self):
        login = 'dpkappadmin'
        password = 524598
        self.element_is_visable(LocatorsAuth.LOGIN).send_keys(login)
        self.element_is_visable(LocatorsAuth.PASSWORD).send_keys(password)
        self.element_is_visable(LocatorsAuth.ENTER).click()


    def data_diagnost(self):
        login = 'diagnostqa'
        password = 524598
        self.element_is_visable(LocatorsAuth.LOGIN).send_keys(login)
        self.element_is_visable(LocatorsAuth.PASSWORD).send_keys(password)
        self.element_is_visable(LocatorsAuth.ENTER).click()
        assert self.element_is_visable(LocatorsAuth.NAME_APP)

    def data_sds(self):
        login = 'sdsqa'
        password = 524598
        self.element_is_visable(LocatorsAuth.LOGIN).send_keys(login)
        self.element_is_visable(LocatorsAuth.PASSWORD).send_keys(password)
        self.element_is_visable(LocatorsAuth.ENTER).click()
        assert self.element_is_visable(LocatorsAuth.NAME_APP)

    def data_specVT(self):
        login = 'specvtqa'
        password = 524598
        self.element_is_visable(LocatorsAuth.LOGIN).send_keys(login)
        self.element_is_visable(LocatorsAuth.PASSWORD).send_keys(password)
        self.element_is_visable(LocatorsAuth.ENTER).click()
        assert self.element_is_visable(LocatorsAuth.NAME_APP)


    def data_specZCH(self):
        login = 'speczchqa'
        password = 524598
        self.element_is_visable(LocatorsAuth.LOGIN).send_keys(login)
        self.element_is_visable(LocatorsAuth.PASSWORD).send_keys(password)
        self.element_is_visable(LocatorsAuth.ENTER).click()
        assert self.element_is_visable(LocatorsAuth.NAME_APP)

    def data_designer(self):
        login = 'konstqa'
        password = 524598
        self.element_is_visable(LocatorsAuth.LOGIN).send_keys(login)
        self.element_is_visable(LocatorsAuth.PASSWORD).send_keys(password)
        self.element_is_visable(LocatorsAuth.ENTER).click()
        assert self.element_is_visable(LocatorsAuth.NAME_APP)

    def incorect_cred(self):
        login = 'test'
        password = 1234
        self.element_is_visable(LocatorsAuth.LOGIN).send_keys(login)
        self.element_is_visable(LocatorsAuth.PASSWORD).send_keys(password)
        self.element_is_visable(LocatorsAuth.ENTER).click()
