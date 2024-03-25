from abc import ABC


class DatabaseManager(ABC):
    """
    The class DatabaseManager is a template for managing a database and its associated repositories.
    """

    @property
    def client(self):
        raise NotImplementedError

    @property
    def database(self):
        raise NotImplementedError

    @property
    def competition_repo(self):
        raise NotImplementedError
