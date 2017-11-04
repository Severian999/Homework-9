# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:36:48 2017

@author: Don Gass
"""
import matplotlib.pyplot as plt

def monthly_payment(loan_amount, yearly_interest_rate, 
                    number_of_months, initial_payment=0):
    '''
        loan_amount = total amout of loan eg. 200000
        yearly_interest_rate = passed as percentage eg. 5% is 0.05
        number_of_months = total length of repayment period in months
        Returns two lists:
            months: 0 to number_of_months
            cumulative_payment: total of payments made for each month
    '''
    months = list(range(number_of_months + 1))
    m_rate = yearly_interest_rate/12
    payment = loan_amount * m_rate * ((1 + m_rate)**number_of_months) / \
        (1 + m_rate)**number_of_months - 1
    cumulative_payment = [(i * payment) + initial_payment 
                          for i, x in enumerate(months)]
    return months, cumulative_payment

# Calculate and plot for 30 yr fixed at 7% APR    
months, cumulative_payment = monthly_payment(200000, 0.07, 360)
plt.plot(months, cumulative_payment, label="30 yr fixed, 7% APR")

# Calculate and plot for 30 yr fixed at 5% APR after paying $6500 point payment
# up front
months, cumulative_payment = monthly_payment(200000, 0.05, 360, 6500)
plt.plot(months, cumulative_payment, 
         label="30 yr fixed, 5% APR, $6500 pnt payment")

# Calculate and plot for 4 yrs @ 4.5%, then 26 years @ 9.5%
months, cumulative_payment = monthly_payment(200000, 0.045, 360, 0)
period_one = cumulative_payment[:49] # 0 month plus 48 payments
__, cumulative_payment = monthly_payment(200000 - max(period_one), 0.095,
                                             312, max(period_one))
period_two = cumulative_payment[1:] #get all but the 0 month payment
cumulative_payment = period_one + period_two
plt.plot(months, cumulative_payment, label="2-rate loan, 4yr @ 4.5%, 26 yr @ 9.5%" )

# Setup plot labels, legends, etc.
plt.xlabel("Months (0 - 360)")
plt.ylabel("Cumulative payments made")
plt.title("30 yr fixed vs points vs 2-rate loan")
plt.legend(shadow=True, loc="upper left")
plt.tight_layout()
plt.savefig("task3_plot.png", dpi=300)

plt.show()

 
                    