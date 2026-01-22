def salary_calc(basic, hra, bonus= 0):
    return basic + hra + bonus

print(salary_calc(30000, 8000, 5000))