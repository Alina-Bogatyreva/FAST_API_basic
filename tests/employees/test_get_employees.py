from tests.clients.clients_bundle import employee_client


def test_positive():
    response = employee_client.get_employees()
    assert response.status_code == 200

