import math
import numpy as np
from scipy.stats import norm

'''T= 1
S0 = 200
Ke = 220
rf = .0925
stand_dev = .2'''

def d_values(T, S0, Ke, rf, stand_dev):
	d1 = (np.log(S0 / Ke) + (rf + stand_dev**2 / 2)*T) / (stand_dev * math.sqrt(T))
	# d2 = (ln(S0 / K) + (rf - stand_dev**2 / 2)*T) / (stand_dev * math.sqrt(T))
	d2 = d1 - (stand_dev * math.sqrt(T))
	return d1, d2


def call_black_scholes(S0, d1, Ke, rf, T, d2):
    c = S0 * norm.cdf(d1) - Ke**(-rf*T) * norm.cdf(d2)
    return c

def put_black_scholes(S0, d1, Ke, rf, T, d2):
    p = Ke**(-rf*T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    return p

if __name__ == '__main__':
	print("Let's start with Black & Scholes pricing formula!")
print("Use always float numbers. v.g. If it's a year, type 1.0 or if it's 20%, type .2")
T = float(input("Insert the Time to exercise: "))
S0 = float(input("Insert the current subyacent price: "))
Ke= float(input("Insert the strike to exercise: "))
rf = float(input("Insert the Risk Free Rate: "))
stand_dev = float(input("Insert the Standard Deviation: "))
d1, d2 = d_values(T, S0, Ke, rf, stand_dev)
call_put= input("Select the option you need to exercise: 'call' or 'put' -> ").strip().lower()
if "call" in call_put:
	call_price = call_black_scholes(S0, d1, Ke, rf, T, d2)
	print(f"Done! The call price is: ${call_price:.2f}")
else:
	put_price = put_black_scholes(S0, d1, Ke, rf, T, d2)
	print(f"Done! The put price is: ${put_price:.2f}")