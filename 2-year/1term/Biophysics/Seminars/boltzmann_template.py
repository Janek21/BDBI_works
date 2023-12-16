import os, sys, math 

# Set the constants that you will use in the script such as the Boltzmann constant (k) and the Avogadro number (an)
k = 1.38*(10**-23)
an = 6.023*(10**23)

def calculate_energy_per_molecule(e):
    # We assume that input energy is in kJ/mol
    return (e*1000/an)

def calculate_energy_kt_ratio(e,T):
    return (e/(k*T))

def calculate_probability_term(exp):
    return (math.e**(-exp))

def calculate_boltzmann_probability(p,q):
    return(p/q)

# The input energies are in kJ/mol #
e0 = 0.0
e1 = float(input())
e2 = float(input())

### Initialize the lists of values that will be plotted ###
values0 = []
values1 = []
values2 = []

### Step 1: Calculate energies per molecule (this can be a function) ###
e0 = 0.0
em1 = calculate_energy_per_molecule(e1)
em2 = calculate_energy_per_molecule(e2)

### Start iterating on different temperatures ###
for T in range(1,3000,10):

    ### Step 2: Calculate the ratio between energy and kT (the exponent of the probability term) ###
    exp0 = 0.0
    exp1 = calculate_energy_kt_ratio(em1,T)
    exp2 = calculate_energy_kt_ratio(em2,T)

    ### Step 3: Calculate the probability term of the Boltzmann distribution (e raised to minus the exponent we just calculated) ###
    p0 = 1.0
    p1 = calculate_probability_term(exp1)
    p2 = calculate_probability_term(exp2)

    ### Step 4: Calculate the partition function (q) ###
    q = p0+p1+p2

    ### Step 5: Calculate the probability for each state according to the Boltzmann distribution ###
    b0 = (p0/q)
    b1 = (p1/q)
    b2 = (p2/q)

    ### Store the values to plot the lines ###
    values0.append(b0)
    values1.append(b1)
    values2.append(b2)

### Make the plots ###
import matplotlib.pyplot as plt
temperatures = range(0,3000,10)
plt.plot(temperatures, values0, color="blue")
plt.plot(temperatures, values1, color="green")
plt.plot(temperatures, values2, color="red")


plt.ylabel('% of population')
plt.xlabel('Temperature (K)')
plt.show()

