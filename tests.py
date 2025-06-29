from functions.get_files_content import get_files_content

def test():
    result = get_files_content("calculator", "main.py")
    print("Result for main.py file:")
    print(result)
    print("")

    result = get_files_content("calculator", "pkg/calculator.py")
    print("Result for pkg/calculator.py file:")
    print(result)
    print("")

    result = get_files_content("calculator", "/bin/cat")
    print("Result for /bin/cat file:")
    print(result)
    print("")


if __name__ == "__main__":
    test()
