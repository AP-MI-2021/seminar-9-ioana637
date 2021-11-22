from Tests.domain_test import test_ruta_autocar
from Tests.repository_test import test_localitate_repository, test_localitate_json_repository
from Tests.service_test import test_localitate_service_add


def run_all_tests():
    test_ruta_autocar()
    test_localitate_repository()
    test_localitate_json_repository()
    test_localitate_service_add()
