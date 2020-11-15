# Plotting the ensemble average for the correlation function

As you have probably already guessed, you will, in this exercise, compute the ensemble average for the correlation function.  

I would like you to do this for a system of 10 spins that interact through the following Hamiltonian:

![](https://render.githubusercontent.com/render/math?math=E=-H\sum_{i=1}^Ns_i-\sum_{i=1}^Ns_is_i%2B1})

Your first coding task will thus be to write a function called `hamiltonian`, that takes two arguments:

1. `spins` - the values of the spin coordinates for a particular microstate (the ![](https://render.githubusercontent.com/render/math?math=s_i) values in the formula above) 
2. `H` - the magnetic field strength (the H value in the formula above).

This function should return the energy of the microstate calculated using the formula above.  Remembering, of course, that ![](https://render.githubusercontent.com/render/math?math=s_{N%2B1=s_1).

You will notice that I have written a function `average_spin` that computes the ensemble average for the spins for you.  Furthermore, I have included a call to this function, so the variable called `avspin` takes a value equal to the ensemble average of the spin.

Your one remaining task is thus to compute the ensemble average for the correlation function.  To do this, you will need to copy what was done in `average_spin` and generate all the possible microstates for the system.  For each of these microstates, you need to compute the correlation function for every value of the separation between spins.  A weighted average of these quantities then needs to be calculated.  The weights in these averages will be the Boltzmann weights.

Notice that when computing the Boltzmann weights, you need to use the variables:

1. `myfield` - the magnetic field strength
1. `temp` - the temperature 

in the way, they have been used in my function to calculate the average spin.

The final ensemble averages for the values of the correlation function at each of the values of r should be stored in the list called `correlation`.  The final result from the program is a graph showing how the correlation function changes as the distance between spins increases. 
