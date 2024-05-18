# main.py

from modules import module1, module2
from services import api

def main():
    module1.function_in_module1()
    module2.function_in_module2()
    api.run_api()

if __name__ == "__main__":
    main()
