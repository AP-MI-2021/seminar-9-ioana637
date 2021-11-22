from Domain.ruta_autocar import RutaAutocar


def test_ruta_autocar():
    ruta_autocar = RutaAutocar('1', '2', '3', 4.5, True)
    assert ruta_autocar.id_entity == '1'
    assert ruta_autocar.id_oras_oprire == '2'
    assert ruta_autocar.id_oras_pornire == '3'
    assert ruta_autocar.pret == 4.5
    assert ruta_autocar.dus_intors == True

    ruta_autocar.pret = 100.5
    ruta_autocar.id_entity = '2'
    ruta_autocar.id_oras_oprire = 'o1'
    ruta_autocar.id_oras_pornire = 'o2'
    ruta_autocar.dus_intors = False

    assert ruta_autocar.id_entity == '2'
    assert ruta_autocar.id_oras_oprire == 'o1'
    assert ruta_autocar.id_oras_pornire == 'o2'
    assert ruta_autocar.pret == 100.5
    assert ruta_autocar.dus_intors == False


