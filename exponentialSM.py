# Exponential growth model v1.0
# using MIT course 6.01 systems and signals libraries, available from
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/software-and-tools/
# Author: Meghann Mears
# Date: 10/06/2015
# Accompanying blog piece:https://meghannmears.wordpress.com/2015/06/10/population-dynamics-as-signals-and-systems/

# Import MIT 6.01 libraries
import lib601.sig as sig
import lib601.sm as sm
import lib601.ts as ts

# Growth rate - lambda (not called lambda for obvious Python reasons)
lamb = 1.1

# State machine for exponential growth
def ExponentialGrowthSystem(lamb):
    return sm.FeedbackAdd(sm.Wire(), sm.Cascade(sm.Delay(0), sm.Gain(lamb)))

# Time steps to simulate
tmax = 100

# Transduce signal from unit sample (i.e. N at t[0] = 1) and draw
ts.TransducedSignal(sig.UnitSampleSignal(), ExponentialGrowthSystem(lamb)). \
        plot(0, tmax, newWindow = 'Exponential growth, lambda = '+str(lamb))

# Text output from transducing unit sample
UnitSample = [1] + [0] * tmax
ExponentialGrowthSystem(lamb).transduce(UnitSample, verbose=True)
