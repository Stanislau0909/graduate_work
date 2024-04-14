import os

import faker
import requests

from tests.test_data.data_dicts_4_api.data_applications import DataApplication as Data
from src.api_endpoits.applications import Applications as App
from conftest import get_json_about_app


class TestApplication:

    def setup_method(self):
        self.data = Data()
        self.app = App()

    def test_create_app(self, access_token_diagnost):
        self.app.create_app(jwt=access_token_diagnost, payload=self.data.data_application_vt())
        self.app.check_status_is_200ok()

    def test_status_application_after_creating(self,
                                               get_list_applications_vt):
        self.app.check_status_application_sent(get_list_applications_vt)

    def test_attach_file_to_application(self, access_token_diagnost, get_last_id_applications_vt):
        self.app.attach_with_creating_app(jwt=access_token_diagnost,
                                          get_last_id_applications_vt=get_last_id_applications_vt,
                                          file=self.data.file_1_jpeg_with_app)

        # self.app.attach_with_creating_app(jwt=access_token_diagnost,
        #                                   get_last_id_applications_vt=get_last_id_applications_vt,
        #                                   file=self.data.file_2_mp4_with_app)
        #
        # self.app.attach_with_creating_app(jwt=access_token_diagnost,
        #                                   get_last_id_applications_vt=get_last_id_applications_vt,
        #                                   file=self.data.file_2_jpg_with_app)
        self.app.check_status_is_200ok()

    def test_status_app_after_sending_files(self, get_list_applications_vt):
        self.app.check_status_application_sent(get_list_applications_vt=get_list_applications_vt)

    def test_presence_files_in_application(self, get_json_about_app, get_last_id_applications_vt):
        self.app.check_file_name_in_application(get_json_about_app=get_json_about_app,
                                                list_attachments_with_app=self.data.list_attachments_with_app)

    def test_send_sms_from_diagnost(self, access_token_diagnost, get_last_id_applications_vt, id_user_diagnost, ):
        self.app.send_sms_in_chat(jwt=access_token_diagnost,
                                  get_last_id_applications_vt=get_last_id_applications_vt,
                                  payload=self.data.data_application_vt_for_sms_diagnost(
                                      id_user_diagnost=id_user_diagnost,
                                      get_last_id_applications_vt=get_last_id_applications_vt))
        self.app.check_status_is_200ok()
        self.app.check_value_field_message(payload=self.data.data_application_vt_for_sms_diagnost(
            id_user_diagnost=id_user_diagnost, get_last_id_applications_vt=get_last_id_applications_vt)
        ['message'])

    def test_status_app_after_sms(self, get_list_applications_vt):
        self.app.check_status_application_sent(get_list_applications_vt=get_list_applications_vt)

    def test_assign_implementer(self, access_token_specilist, get_last_id_applications_vt, id_user_specvt):
        self.app.assign_implementer(get_last_id_applications_vt=get_last_id_applications_vt, jwt=access_token_specilist,
                                    payload=self.data.data_id_implementer(id_user_specvt=id_user_specvt))
        self.app.check_status_is_200ok()
        self.app.check_implementor_id_after_assign(payload=id_user_specvt)

    def test_status_app_after_assign(self, get_list_applications_vt):
        self.app.check_status_application_assign(get_list_applications_vt=get_list_applications_vt)

    def test_send_sms_from_specialist(self, access_token_specilist, get_last_id_applications_vt, id_user_specvt):
        self.app.send_sms_in_chat(jwt=access_token_specilist, get_last_id_applications_vt=get_last_id_applications_vt,
                                  payload=self.data.data_application_vt_for_sms_specialist(
                                      get_last_id_applications_vt=get_last_id_applications_vt,
                                      id_user_specvt=id_user_specvt))

        self.app.check_status_is_200ok()
        self.app.check_value_field_message(payload=self.data.data_application_vt_for_sms_specialist(
            id_user_specvt=id_user_specvt, get_last_id_applications_vt=get_last_id_applications_vt
        )['message'])

    def test_status_after_sending_sms_from_specialist(self, get_list_applications_vt):
        self.app.check_status_application_in_work(get_list_applications_vt=get_list_applications_vt)

    def test_send_file_from_diagnost(self, access_token_diagnost, get_last_id_applications_vt, id_user_diagnost):
        self.app.send_file_in_chat_from_specialist(jwt=access_token_diagnost,
                                                   get_last_id_applications_vt=get_last_id_applications_vt,
                                                   id_user=id_user_diagnost, file=self.data.file_1_for_chat_jpg)

        self.app.check_status_is_200ok()
        self.app.check_file_name(self.data.list_with_future_files()[0])

    def test_status_after_sending_from_diagnost(self, get_list_applications_vt):
        self.app.check_status_application_waiting_azk(get_list_applications_vt=get_list_applications_vt)

    def test_send_file_from_sepcialist(self, access_token_specilist, get_last_id_applications_vt, id_user_specvt):
        self.app.send_file_in_chat_from_specialist(jwt=access_token_specilist,
                                                   get_last_id_applications_vt=get_last_id_applications_vt,
                                                   id_user=id_user_specvt, file=self.data.file_2_for_chat_jpg)
        self.app.check_status_is_200ok()
        self.app.check_file_name(self.data.list_with_future_files()[1])

    def test_status_after_sending_from_specialist(self, get_list_applications_vt):
        self.app.check_status_application_in_work(get_list_applications_vt=get_list_applications_vt)

    def test_assign_to_designer(self, access_token_specilist, get_last_id_applications_vt, id_user_designer):
        self.app.assign_to_designer(jwt=access_token_specilist,
                                    get_last_id_applications_vt=get_last_id_applications_vt,
                                    id_designer=id_user_designer)
        self.app.check_status_is_200ok()
        self.app.check_result_true_after_adding_designer()

    def test_check_presence_designer_in_app(self, check_member_in_application):
        self.app.check_designer_in_after_adding(check_member_in_application=check_member_in_application)

    def test_status_after_assign_to_designer(self, get_list_applications_vt, get_messages_in_chat, get_sid):
        self.app.check_status_application_designer(get_list_applications_vt=get_list_applications_vt)

    def test_messages_after_adding_designer(self, get_messages_in_chat, get_sid):
        self.app.check_system_sms_after_adding_designer(get_messages_in_chat=get_messages_in_chat, get_sid=get_sid)

    def test_back_app_to_azk_from_designer(self, get_last_id_applications_vt, access_token_designer):
        self.app.back_app_in_status_azk_from_designer(get_last_id_applications_vt=get_last_id_applications_vt,
                                                      jwt=access_token_designer)
        self.app.check_status_is_200ok()

    def test_status_in_azk_from_designer(self, get_list_applications_vt):
        self.app.check_status_application_waiting_azk(get_list_applications_vt=get_list_applications_vt)

    def test_adding_assistant_in_app(self, access_token_specilist, get_last_id_applications_vt, id_user_assistant_azk_vt):
        self.app.adding_assistant_in_app_side_azk(jwt=access_token_specilist,
                                                  get_last_id_applications_vt=get_last_id_applications_vt,
                                                  id_user_assistant_azk_vt=id_user_assistant_azk_vt)
        self.app.check_status_is_200ok()

    def test_status_after_adding_assistant(self, get_list_applications_vt):
        self.app.check_status_application_in_work(get_list_applications_vt=get_list_applications_vt)

    def test_presence_assistant_in_app(self, check_member_in_application):
        self.app.check_assistant_side_azk_after_adding(check_member_in_application=check_member_in_application)

    def test_system_message_after_adding_assistant(self, get_messages_in_chat, get_sid):
        self.app.check_system_sms_after_adding_assistnat_azk(get_messages_in_chat=get_messages_in_chat,
                                                             get_sid=get_sid)

    def test_rate_application_by_specialist(self, access_token_specilist, get_last_id_applications_vt,
                                            take_prev_evaluations, access_token_admin, id_user_diagnost,
                                            get_date_start_from_last_app_vt):
        self.app.rate_app_from_specialist(jwt=access_token_specilist,
                                          get_last_id_applications_vt=get_last_id_applications_vt)
        self.app.check_status_is_204_No_content()
        evaluation = self.app.take_after_evaluations(access_token_admin=access_token_admin, id_user_diagnost=id_user_diagnost,
                                        get_date_start_from_last_app_vt=get_date_start_from_last_app_vt)

        self.app.compare_result(prev_result=take_prev_evaluations, final_result=evaluation)

    def test_close_application_by_specialist(self, access_token_specilist, get_last_id_applications_vt):
        self.app.close_app_from_specialist(jwt=access_token_specilist,
                                           get_last_id_applications_vt=get_last_id_applications_vt)
