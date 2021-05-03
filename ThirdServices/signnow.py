from Utils.errors import ServerError


class SignowService(object):

    def __init__(self, _server):
        self.server = _server
        self.url_token = "https://api-eval.signnow.com/oauth2/token"
        self.url_upload_file = "https://api-eval.signnow.com/document/"
        self.url_invite = "https://api-eval.signnow.com/document/{}/invite"
        self.url_download_file = "https://api-eval.signnow.com/document/{}/download?type=collapsed"

    def get_AccessToken(self, _token, _data):
        try:
            response = self.server.post_form(
                self.url_token,
                _data,
                _token,
                _type="Basic"
            )
            token = response['access_token']
            return token

        except ServerError as e:
            msg = (
                "Ocurrio un error obteniendo un Token valido"
                f" de Signnow, {e}"
            )
            raise ServerError(msg)

    def upload_Document(self, _access_token, _file_path):
        with open(_file_path, "rb") as open_file:
            file_data = {"file": open_file}

            try:
                response = self.server.post_file(
                    self.url_upload_file,
                    file_data,
                    _token=_access_token
                )
                return response['id']

            except ServerError as e:
                msg = (
                    f"Ocurrio un error al subir archivo a Signnow, {e}"
                )
                raise ServerError(msg)

    def invite_ToSign(self, _access_token, _document_id, _data):
        url = self.url_invite.format(_document_id)

        try:
            self.server.post(url, _data, _token=_access_token)
            return True

        except ServerError as e:
            msg = (
                f"Ocurrio un error al invitar para firma, {e}"
            )
            raise ServerError(msg)

    def download_Document(self, _access_token, _document_id, _file_path):
        url = self.url_download_file.format(_document_id)
        try:
            response = self.server.get_file(url, _token=_access_token)
            file_name = response.headers.get('content-disposition').replace('"', '')
            file_name = file_name.replace('attachment; filename=', '')
            path = f"{_file_path}/{file_name}"
            open(path, 'wb').write(response.content)
            return path, file_name

        except ServerError as e:
            msg = (
                f"Ocurrio un error al subir archivo a Signnow, {e}"
            )
            raise ServerError(msg)
