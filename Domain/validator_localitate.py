from Domain.localitate import Localitate


class LocalitateValidator:
    def validate(self, localitate: Localitate):
        errors = []
        if localitate.id_entity == '':
            errors.append('Id nu poate fi vid')
        if localitate.nume == '':
            errors.append('Numele nu poate fi vid')
        if localitate.tip not in ['sat', 'oras', 'municipiu']:
            errors.append('Tipul localitati i trebuie sa fie sat oras sau municipiu')
        if len(errors)>0:
            raise ValueError(errors)
        return localitate