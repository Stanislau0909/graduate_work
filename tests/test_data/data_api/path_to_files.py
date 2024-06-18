import os


class PathtoFile:

    @property
    def file_1_jpeg_with_app(self):
        full_path = os.getcwd()
        file = {'file': open(
            f"{full_path}\\attachments\\kamaz_attach_with_app.jpeg",
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
        full_path = os.getcwd()
        file = {'file': open(f"{full_path}\\attachments\\talking.mp4",
                             'rb')}
        return file

    @property
    def file_1_for_chat_jpg(self):
        path_to_file = r"\attachments\KAMAZ-4.jpg"
        file = {'file': open(r"C:\Users\Стас\Documents\AQA_16_graduate_work\tests\api_tests\attachments\KAMAZ-4.jpg",
                             'rb')}
        return file

    @property
    def file_2_for_chat_jpg(self):
        full_path = os.getcwd()
        file = {'file': open(f"{full_path}\\attachments\\KAMAZ-2.jpg",
                             'rb')}
        return file

    @property
    def file_video_3gp(self):
        full_path = os.getcwd()
        file = {
            'file': open(f"{full_path}\\attachments\\sample_woman.3gp",
                         'rb')}
        return file

    @property
    def file_video_mov(self):
        full_path = os.getcwd()
        file = {
            'file': open(f"{full_path}\\attachments\\VIDEO-33.5.mov",
                         'rb')}
        return file

    @property
    def file_picture_webp(self):
        full_path = os.getcwd()
        file = {
            'file': open(
                f"{full_path}\\attachments\\pao-kamaz-logo-5.webp",
                'rb')}
        return file

    @property
    def file_pdf(self):
        full_path = os.getcwd()
        file = {
            'file': open(
                f"{full_path}\\attachments\\Инструкция по неисправности.pdf",
                'rb')}
        return file

    @property
    def file_xlsx(self):
        full_path = os.getcwd()
        file = {
            'file': open(
                f"{full_path}\\attachments\\Количество заявок по исполнителям и категориям неисправности 2023-02-01 - 2024-03-20.xlsx",
                'rb')}
        return file

    @property
    def file_png(self):
        full_path = os.getcwd()
        file = {
            'file': open(
                f"{full_path}\\attachments\\camera_png.png",
                'rb')}
        return file
