from Domain.localitate import Localitate
from Domain.ruta_autocar import RutaAutocar


class RutaAutocarException(Exception):
    pass

class RutaAutocarValidator:
    def validate(self, rutaAutocar: RutaAutocar):
        errors = []
        if rutaAutocar.id_entity == '':
            errors.append('Id nu poate fi vid')
        if rutaAutocar.id_oras_oprire == '':
            errors.append('Id nu poate fi vid')
        if rutaAutocar.id_oras_pornire == '':
            errors.append('Id nu poate fi vid')
        if rutaAutocar.id_oras_pornire == rutaAutocar.id_oras_oprire:
            errors.append('Id-urile oraselor nu pot fi egale')
        try:
            rutaAutocar.pret = float(rutaAutocar.pret)
        except:
            errors.append('Pretul trebuie sa fie float')
        if rutaAutocar.dus_intors not in ['da', 'nu']:
            errors.append('Dus intors trebuie sa fie da sau nu')
        elif rutaAutocar.dus_intors == 'da':
            rutaAutocar.dus_intors = True
        else:
            rutaAutocar.dus_intors = False
        if len(errors)>0:
            raise ValueError(errors)
        return rutaAutocar