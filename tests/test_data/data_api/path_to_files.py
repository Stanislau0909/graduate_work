import os


class PathtoFile:

    @property
    def file_1_jpeg_with_app(self):
        path_to_file = r"\attachments\kamaz_attach_with_app.jpeg"
        file = {'file': open(
            r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\kamaz_attach_with_app.jpeg",
            'rb')}
        return file

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
        file = {'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\talking.mp4",
                             'rb')}
        return file

    @property
    def file_1_for_chat_jpg(self):
        path_to_file = r"\attachments\KAMAZ-4.jpg"
        file = {'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\KAMAZ-4.jpg",
                             'rb')}
        return file

    @property
    def file_2_for_chat_jpg(self):
        path_to_file = r"\attachments\KAMAZ-2.jpg"
        file = {'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\KAMAZ-2.jpg",
                             'rb')}
        return file

    @property
    def file_video_3gp(self):
        file = {
            'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\sample_woman.3gp",
                         'rb')}
        return file

    @property
    def file_video_mov(self):
        file = {
            'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\VIDEO-33.5.mov",
                         'rb')}
        return file

    @property
    def file_picture_webp(self):
        file = {
            'file': open(
                r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\pao-kamaz-logo-5.webp",
                'rb')}
        return file

    @property
    def file_pdf(self):
        file = {
            'file': open(
                r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\Инструкция по неисправности.pdf",
                'rb')}
        return file

    @property
    def file_xlsx(self):
        file = {
            'file': open(
                r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\Количество заявок по исполнителям и категориям неисправности 2023-02-01 - 2024-03-20.xlsx",
                'rb')}
        return file

    @property
    def file_png(self):
        file = {
            'file': open(
                r"C:\Users\Стас\Documents\AQA_16_graduate work\tests\api_tests\attachments\camera_png.png",
                'rb')}
        return file
