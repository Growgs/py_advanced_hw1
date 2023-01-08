import gamepy
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

def print_hi(name):
    print(f'Hi, {name}')

def date_time():
    t = date.today()
    print(t)

if __name__ == '__main__':
    print_hi('Unit')
    calculate_salary()
    get_employees()
    date_time()



