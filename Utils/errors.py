class ValidationError(Exception):
    """Error que se lanza cuando se evalua una condicion del
    controllador."""

    def __init__(self, _message, _logger=None):
        self.message = _message
        self.logger = _logger
        if self.logger:
            self.logger.error(f"<-- {self.message}")

        super().__init__(self.message)

    def __str__(self):
        return self.message


class BusinessError(Exception):
    """Error que se lanza cuando se evalua una condicion del
    negocio."""

    def __init__(self, _message, _logger=None):
        self.message = _message
        self.logger = _logger
        if self.logger:
            self.logger.error(f"<-- {self.message}")

        super().__init__(self.message)

    def __str__(self):
        return self.message


class RecordFoundError(Exception):
    """Error que se lanza cuando se intenta crear un registro
    y este ya existe."""

    def __init__(self, _message, _model, _logger=None):
        self.message = _message
        self.model = _model
        self.logger = _logger
        if self.logger:
            self.logger.error(f"... {self.message}")

        super().__init__(self.message)

    def __str__(self):
        return self.message


class NoRecordsFoundError(Exception):
    """Error que se lanza cuando no se encuentran registros
    en la BD."""

    def __init__(self, _message, _model, _logger=None):
        self.message = _message
        self.model = _model
        self.logger = _logger
        if self.logger:
            self.logger.error(f"... {self.message}")

        super().__init__(self.message)

    def __str__(self):
        return self.message


class NoRecordFoundError(Exception):
    """Error que se lanza cuando se busca un registro en la BD
    y este no existe."""

    def __init__(self, _message, _model, _logger=None):
        self.message = _message
        self.model = _model
        self.logger = _logger
        if self.logger:
            self.logger.error(f"... {self.message}")

        super().__init__(self.message)

    def __str__(self):
        return self.message


class MultipleRecordsFoundError(Exception):
    """Error que se lanza cuando se encuentra mas de un registro
    donde solo deberia existe uno con determinadas caracteristicas."""

    def __init__(self, _message, _model, _logger=None):
        self.message = _message
        self.model = _model
        self.logger = _logger

        if self.logger:
            self.logger.error(f"... {self.message}")

        super().__init__(self.message)

    def __str__(self):
        return self.message


class DataBaseError(Exception):
    """Error que se lanza cuando ocurre un error en la Capa de Datos."""

    def __init__(self, _message, _model, _logger=None):
        self.message = _message
        self.model = _model
        self.logger = _logger

        if self.logger:
            self.logger.error(f"... {self.message}")

        super().__init__(self.message)

    def __str__(self):
        return self.message


class DuplicateEntryError(Exception):
    """Error que se lanza cuando el registro ya fue registrado."""

    def __init__(self, _message, _model, _logger=None):
        self.message = _message
        self.model = _model
        self.logger = _logger

        if self.logger:
            self.logger.error(f"... {self.message}")

        super().__init__(self.message)

    def __str__(self):
        return self.message


class SecurityError(Exception):
    """Error que se lanza cuando ocurre un error con alguna clase que
    valide seguridad.
    """
    pass


class ServerError(Exception):
    """Error que se lanza cuando un request no se termina
    exitosamente.
    """
