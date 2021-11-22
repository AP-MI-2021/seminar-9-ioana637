from Domain.validator_localitate import LocalitateValidator
from Domain.validator_ruta_autocar import RutaAutocarValidator
from Repository.in_memory_repository import InMemoryRepository
from Repository.json_repository import JsonRepository
from Service.loc_service import LocalitateService
from Service.ruta_service import RutaAutocarService
from Tests.all_tests import run_all_tests
from UserInterface.UI import UI


def main():
    run_all_tests()
    # repo_loc = InMemoryRepository()
    # repo_ruta = InMemoryRepository()
    repo_loc = JsonRepository('loc.json')
    repo_ruta = JsonRepository('rute.json')
    validator_loc = LocalitateValidator()
    validator_ruta = RutaAutocarValidator()
    service_loc = LocalitateService(repo_loc, validator_loc)
    service_ruta = RutaAutocarService(repo_ruta, validator_ruta, repo_loc)
    ui = UI(service_loc, service_ruta)
    ui.run()



if __name__ == '__main__':
    main()
