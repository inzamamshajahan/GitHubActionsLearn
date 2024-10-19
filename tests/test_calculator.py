from src.calculator import add_numbers

def test_add_numbers():
  """
  This function tests the add_numbers function.
  """
  assert add_numbers(2, 3) == 5
  assert add_numbers(-2, 3) == 1
  assert add_numbers(2.5, 3.5) == 6.0