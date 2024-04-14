import os
import time
from faker import Faker

from src.gui_pages.base_page import BasePage
from src.Locators.applitation_locators import ApplicationPageLocators as Applocators


class Applicationpage(BasePage):
    def create_app_VT(self):
        faker = Faker("ru_RU")
        vin = faker.bothify(text='???##############').upper()
        milage = faker.bothify(text='#####')
        model = faker.bothify(text='#####')
        theme = "ТЕСТОВАЯ ЗАЯВКА В РАБОТУ НЕ БРАТЬ!"
        description = "ТЕСТОВАЯ ЗАЯВКА , ЗДЕСЬ ТЕКСТ ДЛЯ ТЕСТА, Камаз-54901 он же К5 магистральный седельный тягач, со своим эксклюзивным мотором P6. " \
                      "На правах флагманской модели КАМАЗ, с полным соответствием всеми принятым стандартам автомобилестроения. В этой теме обсуждаем эту модель, " \
                      "рассказываем о вопросах эксплуатации, ремонта и обслуживания. Пишите, свой отзыв о этой модели. Самые интересные отзывы отправим на завод и обязательно пришлем ответ!"

        self.explicit_wait_to_be_clickable(Applocators.BUTTON_FOR_CREATE_APP).click()
        self.explicit_wait_to_be_clickable(Applocators.LIST_TYPES_APPS).click()
        self.explicit_wait_to_be_clickable(Applocators.REPAIR_APP).click()
        self.explicit_wait_to_be_clickable(Applocators.SUBMIT_CHOSEN_CATEGORY_APP).click()
        self.explicit_wait_to_be_clickable(Applocators.LIST_FAMILY).click()
        self.explicit_wait_to_be_clickable(Applocators.FAMILY_K3).click()
        self.element_is_visable(Applocators.VIN).send_keys(vin)
        self.element_is_visable(Applocators.MILEAGE).send_keys(milage)
        self.element_is_visable(Applocators.MODEL).send_keys(model)
        self.explicit_wait_to_be_clickable(Applocators.LIST_DEFECT_NODE).click()
        self.explicit_wait_to_be_clickable(Applocators.DEFECT_NODE_AUTO).click()
        self.element_is_visable(Applocators.THEME).send_keys(faker.text())
        self.element_is_visable(Applocators.DESCRIPTION).send_keys(description)
        self.explicit_wait_to_be_clickable(Applocators.CREATE_BUTTON).click()

    def check_status_app(self):
        self.name_status_sent = "Отправлена"
        self.name_status_assign = "Назначена"
        self.name_status_in_work = "В работе СДС"
        self.name_status_wait_azk = "Ожидает ответа АЗК"
        self.name_status_designer = "Конструктор"
        self.name_status_wait_closing = "Ожидает закрытия"
        self.name_status_Completed = "Завершена"
        self.name_status_Completed_successfully = "Успешно завершена"
        self.cheking_status_app = self.explicit_wait_to_be_clickable(Applocators.CHECK_STATUS_APP).text
        return self.cheking_status_app

    def check_status_app_after_creating_before_assign(self):
        self.name_status_sent = "Отправлена"
        self.wait_for_text_in_element(Applocators.CHECK_STATUS_APP, self.name_status_sent)
        self.cheking_status_app = self.element_is_visable(Applocators.CHECK_STATUS_APP_WITH_BY).text
        print(self.cheking_status_app)
        assert self.cheking_status_app in self.name_status_sent


    def check_status_app_after_assign(self):
        self.name_status_sent = "Назначена"
        self.wait_for_text_in_element(Applocators.CHECK_STATUS_APP, self.name_status_sent)
        self.cheking_status_app = self.element_is_visable(Applocators.CHECK_STATUS_APP_WITH_BY).text
        print(f"self.cheking_status_app: {self.cheking_status_app}")
        print(f"self.name_status_sent: {self.name_status_sent}")
        assert self.cheking_status_app in self.name_status_sent

    def check_status_app_sending_message_from_specialist(self):
        self.name_status_sent = "В работе"
        self.wait_for_text_in_element(Applocators.CHECK_STATUS_APP, self.name_status_sent)
        self.cheking_status_app = self.element_is_visable(Applocators.CHECK_STATUS_APP_WITH_BY).text
        print(f"self.cheking_status_app: {self.cheking_status_app}")
        print(f"self.name_status_sent: {self.name_status_sent}")
        assert self.cheking_status_app in self.name_status_sent

    def check_status_app_sending_message_from_diagnostician(self):
        self.name_status_sent = "Ожидание ответа"
        self.wait_for_text_in_element(Applocators.CHECK_STATUS_APP, self.name_status_sent)
        self.cheking_status_app = self.element_is_visable(Applocators.CHECK_STATUS_APP_WITH_BY).text
        print(f"self.cheking_status_app: {self.cheking_status_app}")
        print(f"self.name_status_sent: {self.name_status_sent}")
        assert self.cheking_status_app in self.name_status_sent

    def notification_about_successufully_create_app(self):
        self.notification = "Заявка успешно создана"
        self.success = self.element_is_visable(Applocators.SUCCESSFULY_CREATE_APP).text
        assert self.success == self.notification



    def assign_app_for_specialist(self):
        my_specialist = "Лаптёнок(вт)"
        needs_text = 'Лаптёнок(вт)  С. В.'
        self.explicit_wait_to_be_clickable(Applocators.MENU_NEAR_THEME).click()
        self.explicit_wait_to_be_clickable(Applocators.BUTTON_ASSIGN).click()

        self.explicit_wait_to_be_clickable(Applocators.LIST_SPECIALIST).click()
        self.explicit_wait_to_be_clickable(Applocators.IMPUT_FOR_ENTER_DATA_SPEIALIST).click()
        self.element_is_visable(Applocators.IMPUT_FOR_ENTER_DATA_SPEIALIST).send_keys(my_specialist)
        time.sleep(1)
        self.explicit_wait_to_be_clickable(Applocators.FIRST_FOUND_SPECIALIST_IN_LIST).click()
        self.explicit_wait_to_be_clickable(Applocators.SUBMIT_ASSIGN).click()

    def check_implementer_in_app(self):
        my_specialist = "Лаптёнок(вт) С. В."
        take_value = self.element_is_visable(Applocators.CHECK_IMPLEMENTER_IN_APP).text
        assert my_specialist == take_value

    def open_app(self):
        self.explicit_wait_to_be_clickable(Applocators.OPEN_FIRST_APP_TABLE).click()

    def send_messages_by_diagnostician(self):
        text_from_diagnostician = "Привет привет, сегодня очень срочно нужно обработать данную заявку, надеюсь на быстрый отклик!!!"
        self.explicit_wait_to_be_clickable(Applocators.INPUT_FOR_MESSAGES).send_keys(text_from_diagnostician)
        self.explicit_wait_to_be_clickable(Applocators.BUTTON_FOR_SENDING_MESSAGE).click()
        self.check_message = self.element_is_visable(Applocators.FIRST_MESSAGE).text
        print(self.check_message)
        assert text_from_diagnostician in self.check_message

    def send_messages_by_specialist(self):
        text_from_diagnostician = "Добрый, вижу вашу заявку уже взял в работу, ждите скоро отвечу!!!"
        self.explicit_wait_to_be_clickable(Applocators.INPUT_FOR_MESSAGES).send_keys(text_from_diagnostician)
        self.explicit_wait_to_be_clickable(Applocators.BUTTON_FOR_SENDING_MESSAGE).click()
        self.check_message = self.element_is_visable(Applocators.SECOND_MESSAGE).text
        print(self.check_message)
        assert text_from_diagnostician in self.check_message

    def send_messages_by_diagnostician_second(self):
        text_from_diagnostician = "Отлично получил ваше сообщение, работаем !!!"
        self.explicit_wait_to_be_clickable(Applocators.INPUT_FOR_MESSAGES).send_keys(text_from_diagnostician)
        self.explicit_wait_to_be_clickable(Applocators.BUTTON_FOR_SENDING_MESSAGE).click()
        self.check_message = self.element_is_visable(Applocators.THIRD_MESSAGE).text
        print(self.check_message)
        assert text_from_diagnostician in self.check_message

    def send_file_jpg_in_chat(self):
        cwd = os.getcwd()
        file_1_jpg = r"\attachments\KAMAZ-4.jpg"
        self.explicit_wait_to_be_clickable(Applocators.MENU_NEAR_CHAT).click()
        self.explicit_wait_to_be_clickable(Applocators.BUTTON_ADD_FILE).click()
        self.upload_file(Applocators.DRAG_AND_DROP, r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\gui_tests\attachments\KAMAZ-4.jpg")
        self.explicit_wait_to_be_clickable(Applocators.BUTTON_FOR_SENDING_MESSAGE).click()
        self.explicit_wait_to_be_clickable(Applocators.OPEN_EXTRA_TAB).click()
        assert self.element_is_visable(Applocators.CHECK_PICTURE_IN_EXTRA_TAB)


    def send_file_mp4_in_chat(self):
        cwd = os.getcwd()
        file_2_mp4 = r"\attachments\short_video_with_app.mp4"
        self.explicit_wait_to_be_clickable(Applocators.MENU_NEAR_CHAT).click()
        self.explicit_wait_to_be_clickable(Applocators.BUTTON_ADD_FILE).click()
        self.upload_file(Applocators.DRAG_AND_DROP, f"{cwd}{file_2_mp4}")
        self.explicit_wait_to_be_clickable(Applocators.BUTTON_FOR_SENDING_MESSAGE).click()
        time.sleep(1)



























