__author__ = 'd15123547'

def simple_interest(principle, rate, periods):
    if rate >= 1:
        rate = rate/100
    else:
        rate = rate
    balance = principle+principle*rate*periods

    return balance

def simple_interest2(principle,rate,periods,numberOfTime):
    yield_ld = periods*numberOfTime
    balance = principle
    if rate >= 1:
        rate = rate/100
    else:
        rate = rate
    total = principle*(1+rate/numberOfTime)**(numberOfTime*periods)
    #Any ideals to format that rate without too much 0000?
    print(format(principle,',') ,'at', format(rate,"%"),'compounded quarterly for' ,periods, 'years yields', '{:.2f}'.format(total))
    for i in range(0,yield_ld):
        balance = balance+balance*rate/numberOfTime
        print("Quarter:",'{0:2d}'.format(i+1),"Balance:",'{:.2f}'.format(balance))

    return

def main():
    print('Please select the calculation methods:')
    print('Interest/Year  Please enter: 1 ')
    print('Interest/Month Please enter: 2')
    menu=int(input('Please select:'))
    if menu==1:
        try:
            principle = int(input('How much you wish to save?'))
            rate = float(input('Interest/year?'))
            #fix it late around!
            periods=int(input('Years wish to save?'))
            print(simple_interest(principle, rate, periods))
        except:
            print("Don't Fxxx with me use number only without any symbol!!!!")

    elif menu == 2:
        try:
            principle=int(input('How much you wish to save?:'))
            numberOfTime=int(input('Number Of Interest periods/ year?:'))
            rate=float(input('Interest/Period?'))
            #fix it late around!
            periods=int(input('How many years you wish to save?:'))
            print(simple_interest2(principle, rate, periods,numberOfTime))
        except:
            print("Don't Fxxx with me use number only without any symbol!!!!")
    else:
        print('Please Using Correct Menu Code!')



main()
