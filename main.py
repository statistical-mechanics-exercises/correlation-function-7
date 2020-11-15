import matplotlib.pyplot as plt
import numpy as np

def hamiltonian( spins, H ) :
  energy = 0
  # Your code to compute the Hamiltonian goes here
  
  return energy
  
# A function that I have written for you that computes the average
# value for the spin
def average_spin( N, H, T ) :
  numer, pfunc = 0, 0 
  for i in range(2**N) :
    num, spins = i, N*[0]
    for j in range(N) :
      spins[j] = np.floor( num / 2**(N-1-j) )
      num = num - spins[j]*2**(N-1-j)
      if spins[j]==0 : spins[j] = -1
    bweight = np.exp( -hamiltonian( spins, H ) / T )
    numer = sum(spins)*bweight / N
    pfunc = pfunc + bweight
  return numer / pfunc
  
# I have set the values you should use for the magentic field strength (magfield) and the 
# temperature (temp) here.  I have then used the function that I have written for you above
# to compute the ensemble average value for the average spin.  You can use use the variable 
# called avspin whenever you need to use ensemble average of the spin.
magfield, temp = 1, 0.5
avspin = average_spin( 10, magfield, temp )

# I have defined empty lists called correlation and rvalues here.
# You have to set these equal to lists as described in the intstructions on 
# the right
rvalues, correlation = [0,1,2,3,4,5], 6*[0]
# Your code to compute the ensemble average for the correlation function goes here.



# This plots the correlation function 
plt.plot( rvalues, correlation, 'ko')
plt.plot( rvalues, correlation, 'k-')
plt.xlabel("Distance between spins")
plt.ylabel("Correlation Function")
plt.savefig("correlation_function.png")
