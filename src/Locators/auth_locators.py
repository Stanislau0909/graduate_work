from selenium.webdriver.common.by import By

class AuthPageLocators:

    LOGIN =(By.XPATH , "//input[@type='login']")
    PASSWORD = (By.XPATH ,"//input[@type='password']")
    ENTER = (By.XPATH , "//button[@type='submit']")
    NOTIFICATION_ERROR = (By.XPATH, "//p[@class ='body--3Rrht md--1Lt75 left--2thvY notification-title']")
    NAME_APP = (By.XPATH, "//span[@class = 't-h--28 t-wt--medium t-v--text ApplicationsPage-Title']")
    LOG_OUT = (By.XPATH, "//button[@class='Button--YUouf transparent--1jZrL lg--ARmiK onlyIcon--3ubWU']")
    MODAL_LOG_OUT = (By.XPATH , "//div[@class='icon icon-size__lg icon-theme__success']")
    MODAL_AUTH = (By.XPATH , "//span[@class ='t-pt--17 t-wt--medium t-v--text AuthForm-Title']")
    NOTIFICATION_INCORECT_PASS = (By.XPATH , "//div[@class='notification Danger' ]")
    BUTTON_FORGET_PASS = (By.XPATH, "//span[@class='t-pt--15 t-wt--regular t-v--info AuthForm-Title']")
    INPUT_FOR_EMAIL = (By.XPATH, "//input[@type='login']")
    BUTTON_RESET_PASS_INACTIVE = (By.XPATH, "//div[@class='err-t']")
    SUBMIT_RESET_PASS = (By.XPATH,"//button[@type='submit']")
    NOTIFICATION_ERROR_FOR_EMAIL = (By.XPATH, "//*[text()='На данный почтовый адрес регистрация не производилась']")
    BACK_TO_AUTH = (By.XPATH, "//button[@type='button']")
