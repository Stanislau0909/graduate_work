import pytest

from src.api_endpoits.wiki_endpoints import Wiki as W
from tests.test_data.data_api.path_to_files import PathtoFile


class TestWiki:
    wiki = W()
    path_files = PathtoFile()

    def test_create_wiki_without_files(self, access_token_specialist, builder_wiki):
        self.wiki.create_wiki_manual(jwt=access_token_specialist, payload=builder_wiki.build())
        self.wiki.check_status_is_201created()
        self.wiki.check_types_data_in_create_wiki()

    @pytest.mark.parametrize("model", [
        '1234567891234567891234567891231'
    ])
    def test_create_wiki_invalid_data_field_model(self, access_token_specialist, builder_wiki, model):
        self.wiki.create_wiki_manual(jwt=access_token_specialist, payload=builder_wiki.set_model(model).build())
        self.wiki.check_status_is_422_Unprocessable_Entity()

    @pytest.mark.parametrize("custom_id", [
        '1234567891'
    ])
    def test_create_wiki_invalid_data_field_custom_id(self, access_token_specialist, builder_wiki, custom_id):
        self.wiki.create_wiki_manual(jwt=access_token_specialist, payload=builder_wiki.set_custom_id(custom_id).build())
        self.wiki.check_status_is_422_Unprocessable_Entity()

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
    def test_adding_attach_in_wiki(self, access_token_admin, get_last_id_wiki_rae, file):
        self.wiki.adding_attach_in_wiki(jwt=access_token_admin, get_last_id_wiki_rae=get_last_id_wiki_rae, file=file)
        self.wiki.check_status_is_200ok()

    def test_delete_attach_in_wiki(self, access_token_admin, get_last_id_wiki_rae, get_id_attaches):
        deleted_file = self.wiki.delete_files_in_wiki(jwt=access_token_admin, get_last_id_wiki_rae=get_last_id_wiki_rae,
                                                      id_attach_in_wiki=get_id_attaches)
        update_list_id_files = self.wiki.get_id_attach_files_in_wiki(jwt=access_token_admin)
        self.wiki.check_status_is_200ok()
        assert deleted_file not in update_list_id_files

    @pytest.mark.parametrize('family, defect_node,  model', [
        (2, 3, 77766)
    ])
    def test_edit_fields_in_wiki(self, access_token_specialist, get_last_id_wiki_rae, builder_wiki, family,
                                 defect_node, model):
        changed_wiki_from_backend = self.wiki.edit_fields_wiki(jwt=access_token_specialist,
                                                               get_last_id_wiki_rae=get_last_id_wiki_rae,
                                                               payload=builder_wiki.set_family(
                                                                   family).set_defect_node(
                                                                   defect_node).set_model(model).build())
        our_payload = builder_wiki.set_family(2).set_defect_node(3).set_model(77766).build()
        self.wiki.check_status_is_200ok()

        compare_value_general_key = {k: (changed_wiki_from_backend.get(k), our_payload.get(k)) for k in
                                     set(changed_wiki_from_backend.keys()) & set(our_payload.keys()) if
                                     changed_wiki_from_backend.get(k) != our_payload.get(k)}
        assert compare_value_general_key

    @pytest.mark.parametrize('theme', [
        ['Утечка ОЖ из-под боковой заглушки ГБЦ'],
        ['Выполнить проверку отключением пультов спального места, если при отключении пультов '],
        ['123 ! ___ !!!!!! .....'],
        [' -1']
    ])
    def test_search_field_theme_in_wiki(self, access_token_admin, builder_search_wiki, theme):
        self.wiki.check_search_input(jwt=access_token_admin, payload=builder_search_wiki.set_keyword(theme).build())
        self.wiki.check_field_theme_keywords(payload=theme)
        self.wiki.check_status_is_200ok()
        print(theme)


    def test_download_wiki_pdf(self, access_token_admin, get_last_id_wiki_rae):
        self.wiki.clean_downloaded_wiki()
        self.wiki.clean_downloaded_files_with_folder()
        link_for_download = self.wiki.get_download_link_wiki_azk(access_token_admin=access_token_admin, get_last_id_wiki_rae=get_last_id_wiki_rae)
        self.wiki.paste_link_for_download_pdf(get_download_link_wiki_azk=link_for_download)
        self.wiki.collect_files_which_were_downloading(expected_files=self.wiki.list_wiki_azk(access_token_admin))
        self.wiki.check_status_is_200ok()

    def test_download_wiki_html(self, access_token_admin, get_last_id_wiki_rae):
        self.wiki.clean_downloaded_wiki_html()
        self.wiki.clean_downloaded_files_with_folder_html()
        link_for_download = self.wiki.get_download_link_wiki_azk(access_token_admin=access_token_admin, get_last_id_wiki_rae=get_last_id_wiki_rae)
        self.wiki.paste_link_for_download_html(get_download_link_wiki_azk=link_for_download)
        self.wiki.collect_files_which_were_downloading_html(expected_files=self.wiki.list_wiki_azk(access_token_admin))
        self.wiki.check_status_is_200ok()