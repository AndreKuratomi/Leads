class InvalidPhoneError(Exception):
    def __init__(self):
        self.message = {"Erro": "Formato inválido! É preciso seguir o seguinte padrão: '(XX)YYYY-ZZZZ'"}
        super().__init__(self.message)


class NotStringError(Exception):
    def __init__(self):
        self.message = {"Erro": "Todos os campos devem ser do tipo string."}
        super().__init__(self.message)


class AbsentError(Exception):
    def __init__(self):
        self.message = {"Erro": "Uma, ou mais, das chaves requeridas está ausente"}
        super().__init__(self.message)


class NotFoundError(Exception):
    def __init__(self):
        self.message = {"Erro": "Não encontrado"}
        super().__init__(self.message)
