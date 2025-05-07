import app

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0

if __name__ == "__main__":
    test_add()
    print("All tests passed.")
