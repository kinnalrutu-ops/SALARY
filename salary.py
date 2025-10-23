

salary = float(input("Enter employee's salary: "))


bonus = salary * 0.10
total_with_bonus = salary + bonus

tax = total_with_bonus * 0.05
final_salary = total_with_bonus - tax

print("Original Salary:", salary)
print("Bonus Added:", total_with_bonus)
print("After Tax Deduction:", final_salary)
