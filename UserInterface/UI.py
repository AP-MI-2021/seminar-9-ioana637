import json

from Domain.validator_ruta_autocar import RutaAutocarException
from Service.loc_service import LocalitateService
from Service.ruta_service import RutaAutocarService


class UI:
    def __init__(self, loc_service: LocalitateService, ruta_service: RutaAutocarService):
        self.__ruta_service = ruta_service
        self.__localitate_service = loc_service

    def __print_menu(self):
        print("""
        1. Add localitate
        2. Add ruta autocar
        3. Afișarea localităților ordonate crescător după numărul de rute dus-întors care pornesc din ele. Se va afișa și acest număr.
        4. Afișarea tuturor rutelor care se opresc într-o localitate minicipiu. Se vor afișa și denumirile localităților între care e definită ruta.
        5. Print un obiect în care cheile sunt numele localităților, iar valoarea unei chei X este o listă cu numele localităților în care ajung direct autocare care pornesc din X
        6. Print localitati
        7. Print rute
        x. Exit
        """)

    def handle_add_loc(self):
        try:
            id = input('Id')
            nume = input('Nume')
            tip = input('Tip (oras, sat, municipiu)')
            self.__localitate_service.add_localitate(id, nume, tip)
        except Exception as e:
            print(e)

    def handle_add_ruta(self):
        try:
            id = input('Id')
            id_oras_pornire = input('Id oras pornire')
            id_oras_oprire = input('Id oras oprire')
            pret = input('Pret')
            dus_intors = input('Dus intors (da/nu)')
            self.__ruta_service.add_ruta_autocar(id,id_oras_pornire, id_oras_oprire, pret, dus_intors)
        except RutaAutocarException as e:
            print(e)
        except KeyError as e:
            print(e)

    def handle_print_all_rute(self):
        self.print_list(self.__ruta_service.get_all())

    def handle_print_all_localitati(self):
        self.print_list(self.__localitate_service.get_all())

    def handle_loc_ordonate_asc(self):
        self.print_list(self.__ruta_service.get_localitati_ord_asc_dupa_nr_rute())

    def handle_print_rute_loc_municipiu(self):
        self.print_list(self.__ruta_service.get_rute_cu_loc_oprire_municipiu())

    def handle_nume_localitati_si_loc_prin_care_trec(self):
    #     TODO print as json
        dict_result = self.__ruta_service.get_localitate_si_loc_destinatie()
        json_string = json.dumps(dict_result, indent=4)
        print(json_string)

    def print_list(self, list):
        for el in list:
            print(el)

    def run(self):
        while True:
            self.__print_menu()
            cmd = input('Dati comanda')
            if cmd == '1':
                self.handle_add_loc()
            elif cmd == '2':
                self.handle_add_ruta()
            elif cmd == '3':
                self.handle_loc_ordonate_asc()
            elif cmd == '4':
                self.handle_print_rute_loc_municipiu()
            elif cmd == '5':
                self.handle_nume_localitati_si_loc_prin_care_trec()
            elif cmd == '6':
                self.handle_print_all_localitati()
            elif cmd == '7':
                self.handle_print_all_rute()
            elif cmd == 'x':
                break
            else:
                print('Comanda invalida')