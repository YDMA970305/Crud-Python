class Cliente_NotFound_Exception(Exception):
    def __init__(self, message):
        super().__init__(message)