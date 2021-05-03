# Django's Libraries
from django.urls import reverse_lazy


class PageDto(object):

    def __init__(self, _url, _value1=None, _value2=None):
        self.url = _url
        self.value1 = _value1
        self.value2 = _value2

    def get_Url(self):
        if self.value1:
            if self.value2:
                return reverse_lazy(
                    self.url,
                    kwargs={
                        'param1': self.value1,
                        'param2': self.value2,
                    }
                )
            else:
                return reverse_lazy(
                    self.url,
                    kwargs={
                        'param1': self.value1
                    }
                )

        else:
            return reverse_lazy(self.url)


class ContextItemDto(object):

    def __init__(self, _key, _value):
        self.key = _key
        self.value = _value
