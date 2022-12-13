from logic.logic import Logic
import pytest


@pytest.fixture
def logic_fixture():
    yield Logic()

def test_logic(logic_fixture):
    result = logic_fixture.do_logic()

    assert result == "This is some very cool logic"