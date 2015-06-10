# Exponential growth model (discrete time) v1.0
# Author: Meghann Mears
# Date: 10/06/2015
# Accompanying blog piece: https://meghannmears.wordpress.com/2015/06/10/population-dynamics-as-signals-and-systems/

lambda <- 1.1 # discrete time per-capita growth rate

tmax <- 100 # number of time steps to simulate
n0 <- 1 # population size at t = 0

# Initialise array to store population size over time
n <- array(dim=tmax+1) 
n[1] <- n0

# Perform simulation
for (t in 1:tmax) {
	n[t+1] <- lambda * n[t] # this is the growth model
}

# Print population size array
n

# Plot population size over time
plot(n, xlab="t", ylab="n[t]", type="o", pch=19, cex=0.5, cex.lab=1.2,
	main = paste("Exponential growth model, r = ", r))
