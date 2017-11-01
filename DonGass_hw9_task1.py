#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:11:44 2017

@author: Don Gass
"""

import matplotlib.pyplot as plt

money_spent = list(range(20, 101))
total_bars = [(n + (n-1)//9) for n in money_spent]
total_cost = [(x/total_bars[i]) for i, x in enumerate(money_spent)]

plt.plot(money_spent, total_cost, label="Averge cost of chocolate bar")
plt.xlabel("Money spent (in $)")
plt.ylabel("Average cost / bar")
plt.title("Chocolate Bar Coupon Problem")
plt.legend(shadow=True, loc="upper right")
plt.savefig("task1_plot.png", dpi=300)

plt.show()