import pytest
from employee import Employee

@pytest.fixture
def employee001():
    employee001 = Employee('ryan', 'reynolds', 50_000)
    return employee001
    

def test_default_raise(employee001):
    employee001.give_raise()
    assert employee001.annual_salary == (50_000+5_000)


def test_custom_raise(employee001):
    employee001.give_raise(100_000)
    assert employee001.annual_salary == (50_000+100_000)