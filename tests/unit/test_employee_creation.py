def test_employee_creation():
    employee = Employee(name="John Doe", email="john@example.com")
    assert employee.name == "John Doe"
    assert employee.email == "john@example.com"
