from sys import argv

def wage(hours,hourly,sales,min_sales,commission):
    wage_hourly = hours * hourly
    wage_commission = sales * commission
    sales_per_hour = sales / hours
    
#    print """
#       Hours worked: %d
#         Hourly pay: %.2f
#              Sales: %.2f
#      Minimum sales: %.2f
#    Commission rate: %.2f
#     Sales per hour: %.2f
#    """ % (hours, hourly, sales, min_sales, commission, sales_per_hour)
    
    #GROSS INCOME
    print """
        Hourly: %.2f
    Commission: %.2f
         GROSS: %.2f
         (sales/hr: %.2f)
    """ % (wage_hourly, wage_commission, wage_hourly + wage_commission, sales_per_hour)

# function call 0
#wage(40,8.0,3000.00,3000.00,0.03)

# function call 1
#wage(
    #40 * 4
    #,8.0
    #,3000.00
    #,3000.00
    #,0.03
#)

# function call 2
#wage(
#    int(raw_input("Hours worked this pay period? "))
#    ,8.0
#    ,int(raw_input("Sales this pay period? "))
#    ,3000.00
#    ,0.03
#)

# function call 3
wage(
    int(argv[1])
    ,8.0
    ,int(argv[2])
    ,3000.00
    ,0.03
)

# vim: syntax=off

