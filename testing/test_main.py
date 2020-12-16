import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_rvalues(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( 6==len(this_x), "You have calculated the correlation function for the wrong number of points" )
        for i in range(6) : self.assertTrue( np.abs(this_x[i]-i)<1e-8, "The r values at which you have computed the correlation function are wrong" )
    
    def test_hamiltonian(self) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
               spins[j] = np.floor( num / 2**(4-j) )
               num = num - spins[j]*2**(4-j)
               if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            coup_eng = spins[0]*spins[len(spins)-1]
            for i in range(len(spins)-1) : coup_eng = coup_eng + spins[i]*spins[i+1]
            self.assertTrue( hamiltonian( spins, 1)==-coup_eng-sumspins, "The Hamiltonian has been implemented wrongly" )
            self.assertTrue( hamiltonian( spins, -1)==-coup_eng+sumspins, "The Hamiltonian has been implemented wrongly" )
            self.assertTrue( hamiltonian( spins, 0)==-coup_eng, "The Hamiltonian has been implemented wrongly" )
            self.assertTrue( hamiltonian( spins, 2)==-coup_eng-2*sumspins, "The Hamiltonian has been implemented wrongly" )
    
    def test_correlation(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        mycorr = 6*[0]
        for i in range(2**10) :
            num, spins = i, 10*[0]
            for j in range(10) :
                spins[j] = np.floor( num / 2**(9-j) )
                num = num - spins[j]*2**(9-j)
                if spins[j]==0 : spins[j] = -1
            bweight = np.exp( -hamiltonian( spins, magfield) / temp )
            for j in range(6) :
                for k in range(10) : mycorr[j] = mycorr[j] + bweight*(spins[k]-avspin)*(spins[(k+j)%10] - avspin )
    
        for j in range(6) : self.assertTrue( np.abs( mycorr[j]/mycorr[0]-this_y[j]) < 1E-8, "The values that you have computed for the correlation function are wrong" )
