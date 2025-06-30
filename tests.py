from functions.run_python import run_python_file

def test():
    print("Running main.py")
    print(run_python_file("calculator", "main.py"))
    print("=====================================")
    print("Running tests.py")
    print(run_python_file("calculator", "tests.py"))
    print("=====================================")
    print("Running ../main.py")
    print(run_python_file("calculator", "../main.py"))
    print("=====================================")
    print("Running nonexistent.py")
    print(run_python_file("calculator", "nonexistent.py"))
    print("=====================================")

if __name__ == "__main__":
    test()
