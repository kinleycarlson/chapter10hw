import EmployeeClass as e 
import PayrollDeductionClass as pd


myemployee = e.Employee('Jimmy Smith','58475','Information Systems','Developer',6800)


deduct1 = pd.PayrollDeduction('food court','8/14/2022',22.50,'39119')
deduct2 = pd.PayrollDeduction('gift contribution','8/12/2022',25,'58475')
deduct3 = pd.PayrollDeduction('food court','8/17/2022',15.25,'21547')
deduct4 = pd.PayrollDeduction('vending machine','8/22/2022',3,'58475')
deduct5 = pd.PayrollDeduction('vending machine','8/5/2022',2.75,'58475')

def main():
    print('Name','          ','ID Number','     ','Department','     ','Job Title','    ','Monthly Salary')
    print(myemployee.get_name(),'   ',myemployee.get_ID(),' ',myemployee.get_dep(),'    ',myemployee.get_title(),'  ',format(myemployee.get_salary(),'.2f'))


    print()
    print()



    print('Description       Date    Charge  EmployeeID')
    print(deduct1.get_desc(),'      ',deduct1.get_date(),'  ',deduct1.get_amt(),'   ',deduct1.get_ID())
    print(deduct2.get_desc(),'  ',deduct2.get_date(),'  ',deduct2.get_amt(),'   ',deduct2.get_ID())
    print(deduct3.get_desc(),'      ',deduct3.get_date(),'  ',deduct3.get_amt(),'   ',deduct1.get_ID())
    print(deduct4.get_desc(),'   ',deduct4.get_date(),'  ',deduct4.get_amt(),'   ',deduct1.get_ID())
    print(deduct5.get_desc(),'   ',deduct5.get_date(),'  ',deduct5.get_amt(),'   ',deduct5.get_ID())
    
    print()
    print()

    show_report()

def show_report():
    deductions = deduct2.get_amt() +deduct4.get_amt()+ deduct5.get_amt()
    gross_pay = myemployee.get_salary()
    net_pay = gross_pay - deductions

    print('*** Employee Pay ***')
    print('Name:',myemployee.get_name())
    print('ID Number:',myemployee.get_ID())
    print('Department:',myemployee.get_dep())
    print('Gross Pay: $',format(gross_pay,'.2f'))
    print('Net Pay: $',format(net_pay,'.2f'))




main()