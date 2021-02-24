def computePay(wage, worked):
    pay = wage*40 if worked > 40 else wage*worked
    otPay = wage*((worked-40)*1.5) if worked > 40 else 0
    return round((pay+otPay)*.7,2)
