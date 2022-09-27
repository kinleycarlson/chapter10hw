import EmployeeClass as e 
import PayrollDeductionClass as pd


myemployee = e.Employee('Jimmy Smith','58475','Information Systems','Developer',6800)

expense1 = pd.PayrollDeduction('food court','8/14/2022',22.50,'39119')
expense2 = pd.PayrollDeduction('gift contribution','8/12/2022',25,'58475')
expense3 = pd.PayrollDeduction('food court','8/17/2022',15.25,'21547')
expense4 = pd.PayrollDeduction('vending machine','8/22/2022',3,'58475')
expense5 = pd.PayrollDeduction('vending machine','8/5/2022',2.75,'58475')

def main():
    list = [expense1,expense2,expense3,expense4,expense5]
    for i in list:
        if i.get_ID() == myemployee.get_ID():
            net_pay = myemployee.get_salary() - i.get_amt()

    print('*** Employee Pay ***')
    print('Name:',myemployee.get_name())
    print('ID Number:',myemployee.get_ID())
    print('Department:',myemployee.get_dep())
    print('Gross Pay: $',format(myemployee.get_salary(),'.2f'),sep = '')
    print('Net Pay: $',format(net_pay,'.2f'),sep='')




main()