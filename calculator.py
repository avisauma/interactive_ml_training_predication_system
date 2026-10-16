def add_bonus(sal,bonus):
    return sal+ bonus
def pf(sal):
    return sal*12/100
def insurance():
    return 2000
def total_salary(sal,bonus):
    return sal+ bonus-pf(sal)-insurance()