from Domain.localitate import Localitate, LocalitateCuNrRute
from Domain.ruta_autocar import RutaAutocar, RutaAutocarCuLocalitateOprire
from Domain.validator_localitate import LocalitateValidator
from Domain.validator_ruta_autocar import RutaAutocarValidator
from Repository.repository import Repository


class RutaAutocarService:
    def __init__(self, repo: Repository, validator: RutaAutocarValidator, repo_loc: Repository):
        self.__repo = repo
        self.__validator = validator
        self.__repo_localitate = repo_loc

    def add_ruta_autocar(self, id, id_oras_pornire, id_oras_oprire, pret, dus_intors):
        ruta = RutaAutocar(id, id_oras_oprire, id_oras_pornire, pret=pret, dus_intors=dus_intors)
        ruta = self.__validator.validate(ruta)
        if self.__repo_localitate.read(ruta.id_oras_oprire) == None or self.__repo_localitate.read(ruta.id_oras_pornire) == None:
            raise KeyError('Nu exista orasele cu id-urile specificate')
        self.__repo.create(ruta)

    def get_all(self):
        return self.__repo.read()

    def __count_nr_rute_pentru_localitate_pornire(self, id_localitate):
        count = 0
        rute = self.__repo.read()
        for ruta in rute:
            if ruta.id_oras_pornire == id_localitate:
                count+=1
        return count

    def __get_rute_pentru_localitate_pornire(self, id_localitate):
        result_list = []
        rute = self.__repo.read()
        for ruta in rute:
            if ruta.id_oras_pornire == id_localitate:
                result_list.append(ruta)
        return result_list

    def get_localitati_ord_asc_dupa_nr_rute(self):
        result_list = []
        localitati = self.__repo_localitate.read()
        for localitate in localitati:
            count = self.__count_nr_rute_pentru_localitate_pornire(localitate.id_entity)
            obj = LocalitateCuNrRute(localitate.id_entity, localitate.nume, localitate.tip, count)
            result_list.append(obj)
        return sorted(result_list, key = lambda x: x.nr_rute)

    def get_rute_cu_loc_oprire_municipiu(self):
        rute = self.__repo.read()
        result_list = []
        for ruta in rute:
            loc_oprire = self.__repo_localitate.read(ruta.id_oras_oprire)
            if loc_oprire.tip == 'municipiu':
                result_list.append(RutaAutocarCuLocalitateOprire(ruta.id, ruta.id_oras_oprire, ruta.id_oras_pornire, ruta.pret, ruta.dus_intors, loc_oprire.nume))
        return result_list

    def get_localitate_si_loc_destinatie(self):
        localitati = self.__repo_localitate.read()
        result = {}
        for localitate in localitati:
            rute_cu_loc_pornire = self.__get_rute_pentru_localitate_pornire(localitate.id_entity)
            loc_dest_list = []
            for ruta in rute_cu_loc_pornire:
                loc_dest = self.__repo_localitate.read(ruta.id_oras_oprire)
                loc_dest_list.append(loc_dest.nume)
            result[localitate.nume] = loc_dest_list
        return result