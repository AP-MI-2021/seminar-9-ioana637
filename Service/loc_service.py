from Domain.localitate import Localitate
from Domain.validator_localitate import LocalitateValidator
from Repository.repository import Repository


class LocalitateService:
    def __init__(self, repo: Repository, validator: LocalitateValidator):
        self.__repo = repo
        self.__validator = validator

    def add_localitate(self, id, nume, tip):
        loc = Localitate(id, nume, tip)
        loc = self.__validator.validate(loc)
        self.__repo.create(loc)

    def get_all(self):
        return self.__repo.read()


