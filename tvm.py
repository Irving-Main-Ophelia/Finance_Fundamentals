# Time Value Money (TVM)

def present_value(nominal, rate, periods):
	pv = nominal / (1+rate)**periods
	return pv

def future_value(nominal, rate, periods):
	fv = nominal * (1 + rate)**periods
	return fv 

if __name__ ==  "__main__":
    nominal = int(input("Please insert the nominal: "))
rate = float(input("Now, insert the rate: "))
period = int(input("Finally, insert the period: "))
request_user = input("Type 'pv' to calculate present value or 'fv' to calculate future value: ")
if "pv" in request_user: 	
    pv = present_value(nominal, rate, period)
    print(f"The present value is: {pv}")
else:
	fv = future_value(nominal, rate, period)
	print(f"The future value is: {fv}")