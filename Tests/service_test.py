from Domain.localitate import Localitate
from Domain.validator_localitate import LocalitateValidator
from Repository.in_memory_repository import InMemoryRepository
from Repository.json_repository import JsonRepository
from Service.loc_service import LocalitateService


def test_localitate_service_add():
    #  daca folositi JsonRepository folositi la crearea service-ului un JsonRepository cu un fisier de test
    repo_loc = InMemoryRepository()
    val_loc = LocalitateValidator()
    loc_service = LocalitateService(repo_loc, val_loc)
    loc_service.add_localitate('1', 'nume1', 'sat')
    assert len(loc_service.get_all()) == 1
    # E important la teste sa verificati mai multe decat un simplu assert cu lungimea liste
    # astfel testul se considera mai relevant
    assert loc_service.get_all()[0].nume == 'nume1'
    try:
        loc_service.add_localitate('1', '', 'ceva')
        assert False
    except Exception as e:
        assert True
        # puteti verifica cu assert si mesajele de eroare!!!
        assert str(e) == "['Numele nu poate fi vid', 'Tipul localitati i trebuie sa fie sat oras sau municipiu']"


