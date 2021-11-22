from Domain.localitate import Localitate
from Repository.in_memory_repository import InMemoryRepository
from Repository.json_repository import JsonRepository

def test_localitate_repository():
    repo_loc = InMemoryRepository()
    localitate = Localitate('1', 'loc1', 'sat')
    assert len(repo_loc.read()) == 0
    repo_loc.create(localitate)
    assert len(repo_loc.read()) == 1
    assert repo_loc.read('1').nume == 'loc1'
    assert repo_loc.read('1').tip == 'sat'

# !!! e important sa aveti teste si pentru cazurile in care functia din repo arunca eroare
    localitate2 = Localitate('1', 'loc2', 'oras')
    assert len(repo_loc.read()) == 1
    try:
        repo_loc.create(localitate2)
        assert False
    except KeyError as er:
        assert True
    assert len(repo_loc.read()) == 1
    assert repo_loc.read('1').nume == 'loc1'
    assert repo_loc.read('1').tip == 'sat'

    #   TODO e suficient sa aveti teste pentru functiile din repo pe care ele folositi
    # test delete
    # test update

def test_localitate_json_repository():
    # Daca folositi json repo, il testati doar pe acela si
    # sa folositi un alt fisier fata de cel folosit in main pentru aplicatia mare
    # La finalul rularii testului fisierul trebuie sa fie gol, deci stergeti datele adaugate la testare :)
    repo_loc = JsonRepository('loc_test.json')
    localitate = Localitate('1', 'loc1', 'sat')
    assert len(repo_loc.read()) == 0
    repo_loc.create(localitate)
    assert len(repo_loc.read()) == 1
    assert repo_loc.read('1').nume == 'loc1'
    assert repo_loc.read('1').tip == 'sat'

    # !!! e important sa aveti teste si pentru cazurile in care functia din repo arunca eroare
    localitate2 = Localitate('1', 'loc2', 'oras')
    assert len(repo_loc.read()) == 1
    try:
        repo_loc.create(localitate2)
        assert False
    except KeyError as er:
        assert True
    assert len(repo_loc.read()) == 1
    assert repo_loc.read('1').nume == 'loc1'
    assert repo_loc.read('1').tip == 'sat'

    #   TODO e suficient sa aveti teste pentru functiile din repo pe care ele folositi
    # test delete
    # test update

    repo_loc.delete('1')
    assert len(repo_loc.read()) == 0





