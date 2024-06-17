import os
import random
from faker import Faker

faker = Faker()


class DataApplication:
    def data_id_implementer(self, id_user_specvt):
        payload = {"implementer": f"{id_user_specvt}"}
        return payload

    def list_with_future_files(self):
        future_list = ['KAMAZ-4.jpg', 'KAMAZ-2.jpg']
        return future_list

    @property
    def list_attachments_with_app(self):
        list_file_name = ['kamaz_attach_with_app.jpeg', 'short_video_with_app.mp4', 'kamaz.jpg']
        return list_file_name


class CreateAppVT:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_description(self, description=faker.text()):
        self.result['description'] = description
        return self

    @staticmethod
    def random_for_family():
        random_id = random.randint(1, 7)
        return random_id

    def set_family(self, family=""):
        random_id_for_family = self.random_for_family()
        self.result['family'] = family or random_id_for_family
        return self

    def set_model(self, model=faker.bothify(text='#####')):
        self.result['model'] = int(model)
        return self

    def set_theme(self, theme=faker.text()):
        self.result['theme'] = theme
        return self

    def set_vin(self, vin=faker.bothify(text='???##############')):
        self.result['vin'] = vin.upper()
        return self

    @staticmethod
    def random_for_defect_node():
        id_defect_node_with_field_engine = [2, 3, 5, 6, 20, 21]
        random_id = random.choice(id_defect_node_with_field_engine)
        return random_id

    def set_defect_node(self, defect_node=''):
        random_defect_node_id = self.random_for_defect_node()
        self.result['defect_node'] = defect_node or random_defect_node_id
        return self

    def set_mileage(self, mileage=faker.bothify(text='#####')):
        self.result['mileage'] = int(mileage)
        return self

    def set_error_codes(self, error_codes=faker.bothify(text='##-##-##')):
        self.result['error_codes'] = error_codes
        return self

    def set_engine_hours(self, engine_hours=0):
        self.result['engine_hours'] = engine_hours
        return self

    def set_engine_number(self, engine_number=faker.bothify(text='###.###-##')):
        self.result['engine_number'] = engine_number
        return self

    def reset(self):
        self.set_description()
        self.set_family()
        self.set_model()
        self.set_theme()
        self.set_vin()
        self.set_defect_node()
        self.set_mileage()
        self.set_error_codes()
        self.set_engine_hours()
        self.set_engine_number()
        return self

    def build(self):
        return self.result


class SendMessage:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_application_id(self, id_application=None):
        self.result['application_id'] = id_application
        return self

    def set_user_id(self, id_user=None):
        self.result['user_id'] = id_user
        return self

    def set_sender_type(self, sender_type=True):
        self.result['sender_type'] = sender_type
        return self

    def set_message(self, message=faker.text()):
        self.result['message'] = message
        return self

    def set_is_attachment(self, is_attachment=False):
        self.result['is_attachment'] = is_attachment
        return self

    def reset(self):
        self.set_application_id()
        self.set_user_id()
        self.set_sender_type()
        self.set_message()
        self.set_is_attachment()
        return self

    def build(self):
        return self.result


class Migration:
    def __init__(self):
        self.result = {}
        self.reset()

    def set_exclude_media(self, exclude_media=''):
        self.result["exclude_media"] = list(exclude_media)
        return self

    def set_type(self, type_defect_node=2):
        self.result['type'] = type_defect_node
        return self

    def set_move(self, move=False):
        self.result['move'] = move
        return self

    @staticmethod
    def get_defect_node_id():
        id_defect_node_with_field_engine = range(1, 38)
        return random.choice(id_defect_node_with_field_engine)

    def set_defect_node(self, defect_node=''):
        random_defect_node_id = self.get_defect_node_id()
        self.result['mechanic'] = {'defect_node': defect_node or random_defect_node_id}

        if self.result['mechanic']['defect_node'] not in [1, 3, 4, 19, 22]:
            self.result['mechanic']['engine_number'] = ''
        else:
            self.set_engine_number()
        return self

    def set_engine_number(self, engine_number=faker.bothify(text='???.###??#').upper()):
        self.result['mechanic']['engine_number'] = engine_number
        return self

    def reset(self):
        self.set_type()
        self.set_exclude_media()
        self.set_defect_node()
        self.set_move()
        return self

    def build(self):
        return self.result


class RateAppCompleted:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_application_id(self, payload=None):
        self.result['application_id'] = payload
        return self

    def set_info_availability(self, info=random.choice(range(1, 6))):
        self.result['information_availability'] = info
        return self

    def set_response_accuracy(self, response_acc=random.choice(range(1, 6))):
        self.result['response_accuracy'] = response_acc
        return self

    def set_response_time(self, response_time=random.choice(range(1, 6))):
        self.result['response_time'] = response_time
        return self

    def reset(self):
        self.set_application_id()
        self.set_info_availability()
        self.set_response_accuracy()
        self.set_response_time()
        self.add_comment_field()
        return self

    def add_comment_field(self, comment=faker.text()):
        total_sum = (
                self.result['information_availability']
                + self.result['response_accuracy']
                + self.result['response_time']
        )
        if total_sum < 15:
            self.result['comment'] = comment
        else:
            del self.result['comment']
        print(total_sum)
        return self

    def build(self):
        return self.result


class RateAppSuccess:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_application_id(self, payload=None):
        self.result['application_id'] = payload
        return self

    def set_info_availability(self, info=random.choice(range(1, 6))):
        self.result['information_availability'] = info
        return self

    def set_response_accuracy(self, response_acc=random.choice(range(1, 6))):
        self.result['response_accuracy'] = response_acc
        return self

    def set_response_time(self, response_time=random.choice(range(1, 6))):
        self.result['response_time'] = response_time
        return self

    def set_defect_node(self, defect_node=random.choice(range(1, 27))):
        self.result['defect_node'] = defect_node
        return self

    def reset(self):
        self.set_application_id()
        self.set_info_availability()
        self.set_response_accuracy()
        self.set_response_time()
        self.set_defect_node()
        self.add_comment_field()
        return self

    def add_comment_field(self, comment=faker.text()):
        total_sum = (
                self.result['information_availability']
                + self.result['response_accuracy']
                + self.result['response_time']
        )
        if total_sum < 15:
            self.result['comment'] = comment
        else:
            del self.result['comment']
        print(total_sum)
        return self

    def build(self):
        return self.result
