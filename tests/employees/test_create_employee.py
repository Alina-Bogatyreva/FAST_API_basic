import random
import string

from tests.clients.clients_bundle import employee_client
from tests.configuration import ROLE


def test_positive():
    # precondition - предусловие. Создание данных
    name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    role = random.choice(ROLE)

    # request execution
    response = employee_client.create_employee(name, role)

    assert response.status_code == 200, "fail"
