import os

import faker
import pytest
import requests

from tests.test_data.data_api.path_to_files import PathtoFile
from tests.test_data.data_api.generator_applications import DataApplication as Data
from src.api_endpoits.applications import Applications as App


class TestApplication:
    path_files = PathtoFile()

    def setup_method(self):
        self.data = Data()
        self.app = App()
        self.path_file = PathtoFile()

    def test_create_app_with_some_valid_data(self, access_token_diagnostician, builder_application):
        create = self.app.create_app(jwt=access_token_diagnostician, payload=builder_application.build())
        self.app.check_status_is_200ok(create)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_diagnostician,
                                                                  get_last_id=create.json()['id'])
        payload = builder_application.build()
        self.app.compare_common_keys_for_application(response_from_server=response_from_server,
                                                     payload_from_client=payload)
        table_list_app = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        assert self.app.app_last_status(table_list_app) == 1

    @pytest.mark.parametrize('mileage', [
        1000000000,
        0
    ])
    def test_create_app_with_invalid_data_field_mileage(self, access_token_diagnostician, builder_application, mileage):
        create = self.app.create_app(jwt=access_token_diagnostician,
                                     payload=builder_application.set_mileage(mileage).build())
        self.app.check_status_is_422_Unprocessable_Entity(create)

    @pytest.mark.parametrize('engine_hours', [
        1000000000
    ])
    def test_create_app_with_invalid_data_field_engine_hours(self, access_token_diagnostician, builder_application,
                                                             engine_hours):
        create = self.app.create_app(jwt=access_token_diagnostician,
                                     payload=builder_application.set_engine_hours(engine_hours).build())
        self.app.check_status_is_422_Unprocessable_Entity(create)

    @pytest.mark.parametrize('model', [
        1 * 100001,
        0
    ])
    def test_create_app_with_invalid_data_field_model(self, access_token_diagnostician, builder_application, model):
        create = self.app.create_app(jwt=access_token_diagnostician,
                                     payload=builder_application.set_model(model).build())
        self.app.check_status_is_422_Unprocessable_Entity(create)
        print(builder_application.build())

    @pytest.mark.parametrize('defect_node', [
        'string_value'
    ])
    def test_create_app_with_invalid_data_field_defect_node(self, access_token_diagnostician, builder_application,
                                                            defect_node):
        create = self.app.create_app(jwt=access_token_diagnostician,
                                     payload=builder_application.set_defect_node(defect_node).build())
        self.app.check_status_is_422_Unprocessable_Entity(create)
        print(builder_application.build())

    @pytest.mark.parametrize('theme', [
        '',
        't' * 301
    ])
    def test_create_app_with_invalid_data_field_defect_node(self, access_token_diagnostician, builder_application,
                                                            theme):
        create = self.app.create_app(jwt=access_token_diagnostician,
                                     payload=builder_application.set_theme(theme).build())
        self.app.check_status_is_422_Unprocessable_Entity(create)

    @pytest.mark.parametrize('file', [
        pytest.param(path_files.file_2_for_chat_jpg, id='jpg'),
        pytest.param(path_files.file_1_mp4, id='mp4'),
        pytest.param(path_files.file_1_jpeg_with_app, id='jpeg'),
        pytest.param(path_files.file_picture_webp, id='webp'),
        pytest.param(path_files.file_video_3gp, id='3gp'),
        pytest.param(path_files.file_video_mov, id='mov'),
        pytest.param(path_files.file_pdf, id='pdf'),
        pytest.param(path_files.file_xlsx, id='xlsx'),
        pytest.param(path_files.file_png, id='png')

    ])
    def test_attach_file_to_application(self, access_token_diagnostician, get_last_id_applications_vt, file):
        pin_attach_to_app = self.app.attach_with_creating_app(jwt=access_token_diagnostician,
                                                              get_last_id_applications_vt=get_last_id_applications_vt,
                                                              file=file)
        self.app.check_status_is_200ok(pin_attach_to_app)

        files_list_from_payload = [file['file'].name.split('\\')[-1]]
        response_about_app_from_server = self.app.response_from_application(
            access_token_admin=access_token_diagnostician,
            get_last_id=get_last_id_applications_vt)

        self.app.info_about_attaches(files=files_list_from_payload, response_from_server=response_about_app_from_server)
        pars_app_for_status = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(pars_app_for_status)
        assert status_app == 1

    def test_send_sms_from_diagnostician(self, access_token_diagnostician, get_last_id_applications_vt,
                                         id_user_diagnostician, builder_message):
        send_message = self.app.send_sms_in_chat(jwt=access_token_diagnostician,
                                                 get_last_id_applications_vt=get_last_id_applications_vt,
                                                 payload=builder_message.set_application_id(
                                                     get_last_id_applications_vt).set_user_id(
                                                     id_user_diagnostician).build())
        self.app.check_status_is_200ok(send_message)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_diagnostician,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_diagnostician).build(), response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 1

    @pytest.mark.parametrize('file', [
        pytest.param(path_files.file_2_for_chat_jpg, id='jpg'),
        pytest.param(path_files.file_1_mp4, id='mp4'),
        pytest.param(path_files.file_1_jpeg_with_app, id='jpeg'),
        pytest.param(path_files.file_picture_webp, id='webp'),
        pytest.param(path_files.file_video_3gp, id='3gp'),
        pytest.param(path_files.file_video_mov, id='mov'),
        pytest.param(path_files.file_pdf, id='pdf'),
        pytest.param(path_files.file_xlsx, id='xlsx'),
        pytest.param(path_files.file_png, id='png')

    ])
    def test_send_file_in_chat_from_diagnostician(self, access_token_diagnostician, get_last_id_applications_vt,
                                                  id_user_diagnostician, file):
        send_file_in_chat = self.app.send_file_in_chat(jwt=access_token_diagnostician,
                                                       get_last_id_applications_vt=get_last_id_applications_vt,
                                                       id_user=id_user_diagnostician,
                                                       sender_type=True, file=file)
        self.app.check_status_is_200ok(send_file_in_chat)
        payload_files_list = [file['file'].name.split('\\')[-1]]
        response_from_server = self.app.response_from_application(access_token_admin=access_token_diagnostician,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.info_about_attaches_for_chat_and_compare(payload=payload_files_list,
                                                          response_from_server=response_from_server)

        table_of_application = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 1

    @pytest.mark.parametrize('file', [
        pytest.param(path_files.file_2_for_chat_jpg, id='jpg')

    ])
    def test_send_file_in_chat_from_spec(self, access_token_specialist, get_last_id_applications_vt,
                                         id_user_specvt, file):
        send_file = self.app.send_file_in_chat(jwt=access_token_specialist,
                                               get_last_id_applications_vt=get_last_id_applications_vt,
                                               id_user=id_user_specvt,
                                               sender_type=False, file=file)
        self.app.check_status_is_403_Forbidden(send_file)

    def test_send_sms_from_sds(self, access_token_sds, get_last_id_applications_vt,
                               id_user_sds, builder_message, about_me_sds):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_sds,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_sds).build())
        self.app.check_status_is_200ok(send_sms)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_sds,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_sds).build(), response_from_server=response_from_server)
        self.app.check_members_in_application(payload=about_me_sds, response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_sds).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 1

    def test_send_sms_from_spec_vt_in_status_1(self, access_token_specialist, get_last_id_applications_vt,
                                               id_user_specvt, builder_message):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_specialist,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_specvt).build())
        self.app.check_status_is_403_Forbidden(send_sms)

    def test_assign_implementer(self, access_token_specialist, get_last_id_applications_vt, id_user_specvt):
        assign_implementer = self.app.assign_implementer(get_last_id_applications_vt=get_last_id_applications_vt,
                                                         jwt=access_token_specialist,
                                                         payload=self.data.data_id_implementer(
                                                             id_user_specvt=id_user_specvt))
        self.app.check_status_is_200ok(assign_implementer)
        self.app.check_implementor_id_after_assign(payload=id_user_specvt, response_from_server=assign_implementer)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 2

    def test_assign_implementer_by_admin(self, access_token_admin, get_last_id_applications_vt, id_user_specvt):
        assign_implementer = self.app.assign_implementer(get_last_id_applications_vt=get_last_id_applications_vt,
                                                         jwt=access_token_admin,
                                                         payload=self.data.data_id_implementer(
                                                             id_user_specvt=id_user_specvt))
        self.app.check_status_is_200ok(assign_implementer)
        self.app.check_implementor_id_after_assign(payload=id_user_specvt, response_from_server=assign_implementer)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_admin).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 2

    def test_send_sms_from_specialist_after_assign(self, access_token_specialist, get_last_id_applications_vt,
                                                   id_user_specvt,
                                                   builder_message):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_specialist,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_specvt).set_sender_type(False).build())

        self.app.check_status_is_200ok(send_sms)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_specialist,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_specvt).build(), response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 3

    def test_send_sms_from_diagnostician_after_assign(self, access_token_diagnostician, get_last_id_applications_vt,
                                                      id_user_diagnostician, builder_message):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_diagnostician,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_diagnostician).build())
        self.app.check_status_is_200ok(send_sms)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_diagnostician,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_diagnostician).build(), response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 4

    def test_assign_to_designer(self, access_token_specialist, get_last_id_applications_vt, id_user_designer,
                                about_me_designer):
        assign_designer = self.app.assign_to_designer(jwt=access_token_specialist,
                                                      get_last_id_applications_vt=get_last_id_applications_vt,
                                                      id_designer=id_user_designer)
        self.app.check_status_is_200ok(assign_designer)
        self.app.check_result_true_after_adding_designer(response_from_server=assign_designer)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_specialist,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_members_in_application(payload=about_me_designer, response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 5

    def test_send_sms_from_diagnostician_after_adding_designer(self, access_token_diagnostician,
                                                               get_last_id_applications_vt,
                                                               id_user_diagnostician, builder_message):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_diagnostician,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_diagnostician).build())
        self.app.check_status_is_200ok(send_sms)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_diagnostician,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_diagnostician).build(), response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 5

    def test_send_sms_from_designer_after_adding_designer(self, access_token_designer,
                                                          get_last_id_applications_vt,
                                                          id_user_designer, builder_message):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_designer,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_designer).build())
        self.app.check_status_is_200ok(send_sms)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_designer,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_designer).build(), response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_designer).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 5

    def test_send_sms_from_specialist_in_status_5(self, access_token_specialist, get_last_id_applications_vt,
                                                  id_user_specvt,
                                                  builder_message):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_specialist,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_specvt).set_sender_type(False).build())

        self.app.check_status_is_200ok(send_sms)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_specialist,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_specvt).build(), response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 3

    def test_assign_to_designer_after_working(self, access_token_specialist, get_last_id_applications_vt,
                                              id_user_designer, about_me_designer):
        assign_designer = self.app.assign_to_designer(jwt=access_token_specialist,
                                                      get_last_id_applications_vt=get_last_id_applications_vt,
                                                      id_designer=id_user_designer)
        self.app.check_status_is_200ok(assign_designer)
        self.app.check_result_true_after_adding_designer(response_from_server=assign_designer)
        respnse_from_server = self.app.response_from_application(access_token_admin=access_token_specialist,
                                                                 get_last_id=get_last_id_applications_vt)
        self.app.check_members_in_application(payload=about_me_designer, response_from_server=respnse_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 5

    def test_assign_add_second_designer_by_designer(self, access_token_designer, get_last_id_applications_vt,
                                                    id_user_designer_helper,
                                                    about_me_designer, access_token_designer_helper):
        assign_designer = self.app.assign_to_designer(jwt=access_token_designer,
                                                      get_last_id_applications_vt=get_last_id_applications_vt,
                                                      id_designer=id_user_designer_helper)
        self.app.check_status_is_200ok(assign_designer)
        self.app.check_result_true_after_adding_designer(response_from_server=assign_designer)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_designer,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_members_in_application(payload=about_me_designer, response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_designer).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 5

    def test_delete_helper_designer_by_main_designer(self, access_token_designer, id_user_designer_helper,
                                                     get_last_id_applications_vt, about_me_designer_helper):
        delete_designer = self.app.delete_participants_type_designer(jwt=access_token_designer,
                                                                     id_user_who_should_delete=id_user_designer_helper,
                                                                     id_app=get_last_id_applications_vt)
        self.app.check_status_is_200ok(delete_designer)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_designer,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_deleted_member(payload=about_me_designer_helper, response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_designer).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 5

    def test_delete_designer_myself(self, access_token_designer, id_user_designer,
                                    get_last_id_applications_vt, about_me_designer, access_token_admin):
        delete_myself = self.app.delete_participants_type_designer(jwt=access_token_designer,
                                                                   id_user_who_should_delete=id_user_designer,
                                                                   id_app=get_last_id_applications_vt)
        self.app.check_status_is_200ok(delete_myself)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_admin,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_deleted_member(payload=about_me_designer, response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_admin).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 4

    def test_assign_to_designer_second_time(self, access_token_specialist, get_last_id_applications_vt,
                                            id_user_designer,
                                            about_me_designer):
        assign_designer_second_time = self.app.assign_to_designer(jwt=access_token_specialist,
                                                                  get_last_id_applications_vt=get_last_id_applications_vt,
                                                                  id_designer=id_user_designer)
        self.app.check_status_is_200ok(assign_designer_second_time)
        self.app.check_result_true_after_adding_designer(response_from_server=assign_designer_second_time)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_specialist,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_members_in_application(payload=about_me_designer, response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 5

    def test_back_app_to_azk_from_designer(self, get_last_id_applications_vt, access_token_designer,
                                           access_token_admin):
        back_to_azk_by_button = self.app.back_app_in_status_azk_from_designer(
            get_last_id_applications_vt=get_last_id_applications_vt,
            jwt=access_token_designer)
        self.app.check_status_is_200ok(back_to_azk_by_button)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_admin).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 4

    def test_add_helper_for_implementer_by_implementor(self, access_token_specialist, get_last_id_applications_vt,
                                                       id_user_assistant_azk_vt, about_me_assistant_azk_vt):
        adding_assistant = self.app.adding_assistant_in_app_side_azk(jwt=access_token_specialist,
                                                                     get_last_id_applications_vt=get_last_id_applications_vt,
                                                                     id_user_assistant_azk_vt=id_user_assistant_azk_vt)
        self.app.check_status_is_200ok(adding_assistant)
        self.app.check_result_true_after_adding_designer(response_from_server=adding_assistant)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_specialist,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_members_in_application(payload=about_me_assistant_azk_vt,
                                              response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 3

    def test_send_sms_from_helper_implementer(self, get_last_id_applications_vt, access_token_assistant_vt_azk,
                                              builder_message, id_user_assistant_azk_vt):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_assistant_vt_azk,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_sender_type(False).set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_assistant_azk_vt).build())
        self.app.check_status_is_200ok(send_sms)
        response_from_server = self.app.response_from_application(access_token_admin=access_token_assistant_vt_azk,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_assistant_azk_vt).build(), response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_assistant_vt_azk).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 3

    def test_delete_myself_like_assistant_side_azk(self, access_token_assistant_vt_azk, id_user_assistant_azk_vt,
                                                   get_last_id_applications_vt, about_me_designer, access_token_admin):
        delete_participant = self.app.delete_participants_type_specialist(jwt=access_token_assistant_vt_azk,
                                                                          id_user_who_should_delete=id_user_assistant_azk_vt,
                                                                          id_app=get_last_id_applications_vt)
        self.app.check_status_is_200ok(delete_participant)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_assistant_vt_azk).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 3

    @pytest.mark.parametrize('file', [
        pytest.param(path_files.file_2_for_chat_jpg, id='jpg'),
        pytest.param(path_files.file_1_mp4, id='mp4')

    ])
    def test_changing_status_after_send_file_by_diagnostician(self, access_token_diagnostician,
                                                              get_last_id_applications_vt,
                                                              id_user_diagnostician, file):
        send_file = self.app.send_file_in_chat(jwt=access_token_diagnostician,
                                               get_last_id_applications_vt=get_last_id_applications_vt,
                                               id_user=id_user_diagnostician,
                                               sender_type=True, file=file)
        self.app.check_status_is_200ok(send_file)
        files_list = [file['file'].name.split('\\')[-1]]
        response_from_server = self.app.response_from_application(access_token_admin=access_token_diagnostician,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.info_about_attaches_for_chat_and_compare(payload=files_list, response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 4

    @pytest.mark.parametrize('file', [
        pytest.param(path_files.file_1_jpeg_with_app, id='jpeg'),
        pytest.param(path_files.file_video_mov, id='mov'),
        pytest.param(path_files.file_pdf, id='pdf'),
        pytest.param(path_files.file_xlsx, id='xlsx'),
        pytest.param(path_files.file_png, id='png')

    ])
    def test_changing_status_after_send_file_by_specialist(self, access_token_specialist,
                                                           get_last_id_applications_vt,
                                                           id_user_specvt, file):
        send_file = self.app.send_file_in_chat(jwt=access_token_specialist,
                                               get_last_id_applications_vt=get_last_id_applications_vt,
                                               id_user=id_user_specvt,
                                               sender_type=False, file=file)
        self.app.check_status_is_200ok(send_file)
        files_list = [file['file'].name.split('\\')[-1]]
        response_from_server = self.app.response_from_application(access_token_admin=access_token_specialist,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.info_about_attaches_for_chat_and_compare(payload=files_list, response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 3

    def test_migration_application_in_other_category(self, access_token_specialist, builder_migration,
                                                     get_last_id_applications_vt):
        migration_app = self.app.migration_application(jwt=access_token_specialist, payload=builder_migration.build(),
                                                       get_last_id_app=get_last_id_applications_vt)
        self.app.check_status_is_200ok(migration_app)

        response_vt = self.app.list_application_vt(access_token_specialist).json()
        get_vt_fields = response_vt['data'][0]['id']
        vt_fields = self.app.response_from_application(access_token_specialist, get_vt_fields)
        response_zch = self.app.list_application_zch(access_token_specialist)
        get_zch_fields = response_zch['data'][0]['id']
        zch_fields = self.app.response_from_application(access_token_specialist, get_zch_fields)

        self.app.fields_for_compare_after_migration(response_vt=vt_fields, response_zch=zch_fields)

    def test_migration_second_time_that_app_except_400(self, access_token_specialist, builder_migration,
                                                       get_last_id_applications_vt):
        migration_app = self.app.migration_application(jwt=access_token_specialist, payload=builder_migration.build(),
                                                       get_last_id_app=get_last_id_applications_vt)
        self.app.check_status_is_400_Bad_request(migration_app)

    def test_offer_close_app_by_specialist(self, get_last_id_applications_vt, access_token_specialist):
        offer_to_close = self.app.offer_to_close_application(jwt=access_token_specialist,
                                                             get_last_id=get_last_id_applications_vt)
        self.app.check_status_is_200ok(offer_to_close)
        assert offer_to_close.json()['status'] == 6

    def test_rate_application_by_specialist(self, access_token_specialist, get_last_id_applications_vt,
                                            access_token_admin, id_user_diagnostician, get_date_start_from_last_app_vt,
                                            take_prev_evaluations):
        rete_app = self.app.rate_app_from_specialist_vt(jwt=access_token_specialist,
                                                        get_last_id_applications_vt=get_last_id_applications_vt)
        self.app.check_status_is_204_No_Content(rete_app)
        self.app.take_after_evaluations(access_token_admin=access_token_admin,
                                        id_user_diagnostician=id_user_diagnostician,
                                        get_date_start_from_last_app_vt=get_date_start_from_last_app_vt)

    def test_send_sms_after_offer_to_close_by_specialist(self, access_token_specialist, get_last_id_applications_vt,
                                                         builder_message,
                                                         id_user_specvt):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_specialist,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_user_id(id_user_specvt).set_application_id(
                                                 get_last_id_applications_vt).set_sender_type(False).build()
                                             )
        self.app.check_status_is_403_Forbidden(send_sms)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 6

    def test_assign_designer_after_offer_to_close_by_specialist(self, access_token_specialist,
                                                                get_last_id_applications_vt,
                                                                id_user_designer, about_me_designer):
        assign_designer = self.app.assign_to_designer(jwt=access_token_specialist,
                                                      get_last_id_applications_vt=get_last_id_applications_vt,
                                                      id_designer=id_user_designer)
        self.app.check_status_is_403_Forbidden(assign_designer)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 6

    def test_send_sms_after_offer_to_close_by_diagnostician(self, access_token_diagnostician,
                                                            get_last_id_applications_vt,
                                                            id_user_diagnostician, builder_message):
        send_sms = self.app.send_sms_in_chat(jwt=access_token_diagnostician,
                                             get_last_id_applications_vt=get_last_id_applications_vt,
                                             payload=builder_message.set_application_id(
                                                 get_last_id_applications_vt).set_user_id(
                                                 id_user_diagnostician).build())
        self.app.check_status_is_200ok(send_sms)
        self.app.response_from_application(access_token_admin=access_token_diagnostician,
                                           get_last_id=get_last_id_applications_vt)

        response_from_server = self.app.response_from_application(access_token_admin=access_token_diagnostician,
                                                                  get_last_id=get_last_id_applications_vt)
        self.app.check_value_field_message(
            payload=builder_message.set_application_id(get_last_id_applications_vt).set_user_id(
                id_user_diagnostician).build(), response_from_server=response_from_server)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 4

    @pytest.mark.parametrize('status', [
        8
    ])
    def test_close_application_by_specialist_force_close_successfully_completed(self, access_token_specialist,
                                                                                get_last_id_applications_vt, status):
        close_app = self.app.general_point_for_closing_app(jwt=access_token_specialist,
                                                           get_last_id_applications_vt=get_last_id_applications_vt,
                                                           status=status)
        self.app.check_status_is_200ok(close_app)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == status

    def test_rate_app_by_diagnostician_without_defect_node(self, access_token_diagnostician, builder_rate_completed,
                                                           get_last_id_applications_vt):
        rate_app = self.app.rate_app_from_diagnostician(jwt=access_token_diagnostician,
                                                        payload=builder_rate_completed.set_application_id(
                                                            get_last_id_applications_vt).add_comment_field().build())
        self.app.check_status_is_200ok(rate_app)
        response_from_server = rate_app.json()
        payload = builder_rate_completed.set_application_id(get_last_id_applications_vt).add_comment_field().build()
        print(payload)
        self.app.compare_common_keys_after_rate_by_diagnostician(response_from_server=response_from_server,
                                                                 payload=payload)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 8

    def test_download_app_in_pdf(self, access_token_admin, get_last_id_applications_vt, get_list_applications_vt):
        self.app.clean_downloaded_app_pdf()
        self.app.clean_downloaded_files_with_folder_pdf_app_attach()
        self.app.clean_downloaded_files_with_folder_pdf_chat()
        get_link_for_download = self.app.get_download_link_application(access_token_admin=access_token_admin,
                                                                       get_last_id_application=get_last_id_applications_vt)
        self.app.check_status_is_200ok(get_link_for_download)
        self.app.paste_link_for_download_pdf(get_download_link_app=get_link_for_download.json()['link_id'])
        response_about_app = self.app.response_from_application(access_token_admin=access_token_admin,
                                                                get_last_id=get_last_id_applications_vt)
        self.app.collect_files_which_were_downloading_pdf(response_from_app=response_about_app)

    def test_download_app_in_html(self, access_token_admin, get_last_id_applications_vt):
        self.app.clean_downloaded_app_html()
        self.app.clean_downloaded_files_with_folder_pdf_chat_html()
        self.app.clean_downloaded_files_with_folder_app_html()
        get_link_for_download = self.app.get_download_link_application(access_token_admin=access_token_admin,
                                                                       get_last_id_application=get_last_id_applications_vt)
        self.app.check_status_is_200ok(get_link_for_download)
        self.app.paste_link_for_download_html(get_download_link_html=get_link_for_download.json()['link_id'])
        response_about_app = self.app.response_from_application(access_token_admin=access_token_admin,
                                                                get_last_id=get_last_id_applications_vt)
        self.app.collect_files_which_were_downloading_html(response_from_app=response_about_app)

    @pytest.mark.parametrize('status', [
        7
    ])
    def test_close_app_by_specialist_force_close_success(self, access_token_diagnostician, builder_application, status,
                                                         access_token_specialist, id_user_specvt):
        create_app = self.app.create_app(jwt=access_token_diagnostician, payload=builder_application.build())
        self.app.check_status_is_200ok(create_app)
        assign = self.app.assign_implementer(jwt=access_token_specialist,
                                             get_last_id_applications_vt=create_app.json()['id'],
                                             payload=self.data.data_id_implementer(id_user_specvt=id_user_specvt))
        self.app.check_status_is_200ok(assign)
        closing = self.app.general_point_for_closing_app(jwt=access_token_specialist,
                                                         get_last_id_applications_vt=create_app.json()['id'],
                                                         status=status)
        self.app.check_status_is_200ok(closing)
        list_app_vt = self.app.list_application_vt(access_token_admin=access_token_specialist).json()
        check_status = self.app.app_last_status(list_app_vt)
        assert check_status == 7

    @pytest.mark.parametrize('status', [
        8
    ])
    def test_close_app_by_diagnostician_success(self, access_token_diagnostician, builder_application,
                                                access_token_specialist, id_user_specvt, status):
        create_app = self.app.create_app(jwt=access_token_diagnostician, payload=builder_application.build())
        self.app.check_status_is_200ok(create_app)
        assign = self.app.assign_implementer(jwt=access_token_specialist,
                                             get_last_id_applications_vt=create_app.json()['id'],
                                             payload=self.data.data_id_implementer(id_user_specvt=id_user_specvt))
        self.app.check_status_is_200ok(assign)
        closing = self.app.general_point_for_closing_app(jwt=access_token_diagnostician,
                                                         get_last_id_applications_vt=create_app.json()['id'],
                                                         status=status)
        self.app.check_status_is_200ok(closing)
        list_app_vt = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        check_status = self.app.app_last_status(list_app_vt)
        assert check_status == 8

    def test_rate_app_by_diagnostician_with_defect_node(self, access_token_diagnostician, builder_rate_success,
                                                        get_last_id_applications_vt, builder_application,
                                                        access_token_specialist, id_user_specvt):
        rate_app = self.app.rate_app_from_diagnostician(jwt=access_token_diagnostician,
                                                        payload=builder_rate_success.set_application_id(
                                                            get_last_id_applications_vt).add_comment_field().build())
        self.app.check_status_is_200ok(rate_app)
        response_from_server = rate_app.json()
        payload = builder_rate_success.set_application_id(get_last_id_applications_vt).add_comment_field().build()
        print(payload)
        self.app.check_changing_defect_node_after_rate_by_diagnostician(payload=payload,
                                                                        response_from_server=response_from_server)
        self.app.compare_common_keys_after_rate_by_diagnostician(response_from_server=response_from_server,
                                                                 payload=payload)
        table_of_application = self.app.list_application_vt(access_token_admin=access_token_diagnostician).json()
        status_app = self.app.app_last_status(table_of_application)
        assert status_app == 8
