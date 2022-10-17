import repo_test.main as main


def test_function_one():
    assert (main.function_one() == 2)

def test_baseline():
    assert (2 == 2)