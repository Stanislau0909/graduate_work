import os


class DataApplication:

    def data_application_vt(self):
        body = {
            "description": "test for description,Chicago Keith recently came back from a trip to Chicago, Illinois. This midwestern metropolis is found along the shore of Lake Michigan. ",
            "family": 3,
            "model": 54901,
            "theme": "Тестовая заявка в работу не брать!",
            "vin": "QWERTYQWERTYQunic",
            "defect_node": 4,
            "mileage": 5000,
            "error_codes": "",
            "engine_hours": 0,
            "engine_number": "",
        }
        return body

    def data_application_vt_for_sms_diagnost(self, id_user_diagnost, get_last_id_applications_vt):
        body = {

            "application_id": f"{get_last_id_applications_vt}",
            "user_id": f"{id_user_diagnost}",
            "sender_type": True,
            "message": "Привет, как дела , давайте поработаем немного , чувствую денёк будет продуктивным",
            "is_attachment": False

        }
        return body

    def data_application_vt_for_sms_specialist(self, id_user_specvt, get_last_id_applications_vt):
        body = {

            "application_id": f"{get_last_id_applications_vt}",
            "user_id": f"{id_user_specvt}",
            "sender_type": True,
            "message": "Привет привет, отвечает специалист и ожидает смену статуса на 'В работе СДС' - тестовое сообщение ",
            "is_attachment": False

        }
        return body

    def data_id_implementer(self, id_user_specvt):
        payload = {"implementer": f"{id_user_specvt}"}
        return payload

    @property
    def file_1_jpeg_with_app(self):
        path_to_file = r"\attachments\kamaz_attach_with_app.jpeg"
        file = {'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\kamaz_attach_with_app.jpeg", 'rb')}
        return file

    @property
    def list_attachments_with_app(self):
        list_file_name = ['kamaz_attach_with_app.jpeg', 'short_video_with_app.mp4', 'kamaz.jpg']
        return list_file_name

    def list_with_future_files(self):
        future_list = ['KAMAZ-4.jpg', 'KAMAZ-2.jpg']
        return future_list

    @property
    def file_2_mp4_with_app(self):
        path_to_file = r"\attachments\short_video_with_app.mp4"
        file = {'file': open(f"{os.getcwd()}{path_to_file}", 'rb')}
        return file

    @property
    def name_file_2_mp4_with_app(self):
        file_name = "short_video_with_app.mp4"
        return file_name

    @property
    def file_2_jpg_with_app(self):
        path_to_file = r"\attachments\kamaz.jpg"
        file = {'file': open(f"{os.getcwd()}{path_to_file}", 'rb')}
        return file

    @property
    def file_1_mp4(self):
        path_to_file = r"\attachments\talking.mp4"
        file = {'file': open(f"{os.getcwd()}{path_to_file}", 'rb')}
        return file

    @property
    def file_1_for_chat_jpg(self):
        path_to_file = r"\attachments\KAMAZ-4.jpg"
        file = {'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\KAMAZ-4.jpg", 'rb')}
        return file

    @property
    def file_2_for_chat_jpg(self):
        path_to_file = r"\attachments\KAMAZ-2.jpg"
        file = {'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\KAMAZ-2.jpg", 'rb')}
        return file
