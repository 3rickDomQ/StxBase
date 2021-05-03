# Python's Libraries
import random
import string

# Third-party Libraries
from django.template import loader


class Staker(object):

    @classmethod
    def fill_Dic_WithAnother(self, _dic_base, _dic_new_data):
        """LLena o actualiza un diccionario de un modelo de Django

        :param _dic_base: Diccionario al que se actualizaran los valores
        :type _dic_base: Diccionario de tipo Model
        :param _dic_new_data: Diccionario que contiene los valores
        :type _dic_new_data: dict
        :return: Diccionario con valores actualizados
        :rtype: dict
        """
        for key, value in _dic_new_data.items():
            setattr(_dic_base, key, value)

        return _dic_base


class Scribe(object):

    @classmethod
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length)).upper()

        return result_str

    @classmethod
    def fill_DictWithOtherEmpty(self, _target_dict, _from_data, _set_empty=False):
        for key, value in _from_data.items():
            if _set_empty is False:
                if value:
                    setattr(_target_dict, key, value)

            else:
                setattr(_target_dict, key, value)

        return _target_dict

    @classmethod
    def fill_DictWithOther(self, _target_dict, _from_data):
        for key, value in _from_data.items():
            setattr(_target_dict, key, value)

        return _target_dict

    @classmethod
    def fill_ModelWithOther(self, _target_model, _from_model):
        for key, value in _from_model.items():
            if type(value) == list:
                continue
            setattr(_target_model, key, value)

        return _target_model

    @classmethod
    def get_DicFromModel(
        self,
        _model,
        _except_field=None,
        _nulls=False,
        _empties=False,
        _primaries=False
    ):
        data = {}

        for field in _model._meta.fields:
            if _primaries is False and field.primary_key is True:
                continue

            if _nulls is False and getattr(_model, field.name) is None:
                continue

            if _empties is False and getattr(_model, field.name) == "":
                continue

            if _empties is False and getattr(_model, field.name) == 0:
                continue

            if _except_field == getattr(_model, field.name):
                continue

            data[field.name] = getattr(_model, field.name)

        return data


class EmailSubjectTemplate(object):

    def __init__(self, _path_template, _data):
        self.path_template = _path_template
        self.data = _data

    def render(self):
        subject_str = loader.render_to_string(self.path_template, self.data)
        subject_str = ''.join(subject_str.splitlines())

        return subject_str


class EmailBodyTemplate(object):

    def __init__(self, _path_template, _data):
        self.path_template = _path_template
        self.data = _data

    def render(self):
        body_str = loader.render_to_string(self.path_template, self.data)

        return body_str
