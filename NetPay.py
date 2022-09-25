import EmployeeClass as ec
import PayrollDeductionClass as pd
def main():
    employees = ec.Employee('Jimmy Smith','58475','Information Systems','Developer',6800)

    #employees.set_dep('mis')
    #print('the employee dep is',employees.get_dep('mis'))

    deduct1 = pd.PayrollDeduction('food court','8/14/2022',22.50,'39119')
    deduct2 = pd.PayrollDeduction('gift contribution','8/12/2022',25,'58475')
    deduct3 = pd.PayrollDeduction('food court','8/17/2022',15.25,'21547')
    deduct4 = pd.PayrollDeduction('vending machine','8/22/2022',3,'58475')
    
    deduct1.set_amt()
    print(deduct1.get_amt())



main()