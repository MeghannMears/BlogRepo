# Logistic growth model v1.0
# using MIT course 6.01 systems and signals libraries, available from
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/software-and-tools/
# Author: Meghann Mears
# Date: 10/06/2015
# Accompanying blog piece: https://meghannmears.wordpress.com/2015/06/10/population-dynamics-as-signals-and-systems/

# Import MIT 6.01 libraries
import lib601.sig as sig
import lib601.sm as sm
import lib601.ts as ts

# Growth rate r
r = 0.5

# Carrying capacity K
K = 100

# Define pure function for carrying capacity term
# Cannot be defined using adders/gains/delays due to exponentiation of input
def CarryingCapacityTerm(r, K):
    return sm.PureFunction(lambda x: x**2 * r / K)

# State machine for logistic growth
def LogisticGrowthSystem(r):
    return sm.FeedbackAdd( \
                sm.Wire(), \
                sm.ParallelAdd( \
                    sm.ParallelAdd(sm.Delay(0), sm.Cascade( \
                        sm.Delay(0), sm.Gain(r))), \
                    sm.Cascade(sm.Cascade( \
                        sm.Delay(0), CarryingCapacityTerm(r, K)), sm.Gain(-1)) \
                ) \
            )

# Time steps to simulate
tmax = 100

# Transduce signal from unit sample (i.e. N at t[0] = 1) and draw
ts.TransducedSignal(sig.UnitSampleSignal(), LogisticGrowthSystem(r)).\
            plot(0, tmax, newWindow = 'Logistic Growth, r = ' + str(r))

# Text output from transducing unit sample
# (transduce method not used due to error documented below)
UnitSample = [1] + [0] * tmax
logistic = LogisticGrowthSystem(r)
logistic.start()
for i in range(len(UnitSample)):
    print 'In: ' + str(UnitSample[i]) + \
          ' Out: ' +  str(logistic.step(UnitSample[i])) + \
          ' Next State: ' + str(logistic.state)

###################
## Debug testing ##
###################

## This runs fine: 
#LogisticGrowthSystem(r).transduce(UnitSample)

## This does not:
#LogisticGrowthSystem(r).transduce(UnitSample, verbose = True)

## Manually starting and stepping through the system works fine:
## (Enter one line at a time to see output)
#test = LogisticGrowthSystem(r)
#test.start()
#test.step(1)
#test.step(0)

## Unless you set verbose to True:
## (and enter it one line at a time)
## (no error produced if all the lines are entered at once,
## but no output appears either)
#test = LogisticGrowthSystem(r)
#test.start(verbose = True)
#test.step(1) # Produces an error 

## Same error occurs with minimal code using sm.ParallelAdd:
#def BugTest():
#    return sm.ParallelAdd(sm.Gain(2), sm.Gain(3))

#bug = BugTest()

## This will produce an error is verbose is left at True
#bug.transduce([0,1,0,1], verbose=True)
## As will this:
#bug.start(verbose=True)
#bug.step(0)
#bug.step(1)
#bug.step(0)
#bug.step(1)
