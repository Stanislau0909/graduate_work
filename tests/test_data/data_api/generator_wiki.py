from faker import Faker

faker = Faker()


class CreateWiki:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_custom_id(self, custom_id=faker.bothify(text='####-####')):
        self.result['custom_id'] = custom_id
        return self

    def set_family(self, family=3):
        self.result['family'] = family
        return self

    def set_defect_node(self, defect=5):
        self.result['defect_node'] = defect
        return self

    def set_theme(self, theme=faker.text()):
        self.result['theme'] = theme
        return self

    def set_description(self, description=faker.text()):
        self.result['description'] = description
        return self

    def set_text(self, text=faker.text()):
        self.result['text'] = text
        return self

    def set_model(self, model=54901):
        self.result['model'] = model
        return self

    def reset(self):
        self.set_custom_id()
        self.set_family()
        self.set_defect_node()
        self.set_theme()
        self.set_description()
        self.set_text()
        self.set_model()
        return self

    def build(self):
        return self.result


class SearchWiki:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_keyword(self, keyword='.'):
        self.result['keywords'] = keyword
        return self

    def reset(self):
        self.set_keyword()
        return self

    def build(self):
        return self.result






# example_wiki = CreateWiki().build()
#
#
# for key, value in example_wiki.items():
#     print(f"{key}: {value}")

# wiki = {
#   "custom_id": "EXID01",
#   "family": 1,
#   "defect_node": 1,
#   "theme": "Theme",
#   "description": "Test description",
#   "text": "Tested text",
#   "model": "12345"
# }

