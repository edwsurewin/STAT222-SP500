install.packages("tseries")
library("tseries")

n <- 1100
a <- c(0.1, 0.5, 0.2)  # ARCH(2) coefficients
e <- rnorm(n)  
x <- double(n)
x[1:2] <- rnorm(2, sd = sqrt(a[1]/(1.0-a[2]-a[3]))) 
for(i in 3:n)  # Generate ARCH(2) process
{
  x[i] <- e[i]*sqrt(a[1]+a[2]*x[i-1]^2+a[3]*x[i-2]^2)
}
x <- ts(x[101:1100])
x.arch <- garch(x, order = c(0,2))  # Fit ARCH(2) 
summary(x.arch)                     # Diagnostic tests
plot(x.arch)                        

data(EuStockMarkets)  
dax <- diff(log(EuStockMarkets))[,"DAX"]
dax.garch <- garch(dax)  # Fit a GARCH(1,1) to DAX returns
summary(dax.garch)       # ARCH effects are filtered. However, 
plot(dax.garch)          # conditional normality seems to be violated





----
  
#install.packages("tseries")
library("tseries")
data = read.csv("/Users/edwsurewin/Dropbox/Berkeley MA/222/STAT222-SP500/SP500.csv")
dat <- diff(log(data[,"Open"]))
dat <- ts(dat[1:501])
dat.garch <- garch(dat)
summary(dat.garch)    
plot(dat.garch)     


---
ARIMA MODEL:
ar = arima(data[,"Open"], order = c(1, 1, 1))

___

install.packages(rugarch)
require(rugarch)

_----
  
ts.sim <- arima.sim(list(order = c(1,1,1), ar = 0.7, ma = 0.8), n = 200)
ts.plot(ts.sim)

--
  
  

install.packages("fGarch")
library(fGarch)

## Univariate GARCH Time Series Fitting

# example 1
fit = garchFit(~garch(1, 1), data = garchSim())

# example 2
x.vec = as.vector(garchSim(garchSpec(rseed = 1985), n = 200)[,1])
garchFit(~ garch(1,1), data = x.vec, trace = FALSE)

--
  
## garchSim - Univariate GARCH/APARCH Time Series Simulation
  
## garchSpec - Univariate GARCH Time Series Speciﬁcation
  
  
# GARCH(1,1) - specify omega/alpha/beta
spec = garchSpec(model = list(omega = 1e-6, alpha = 0.1, beta = 0.8))
garchSim(spec, n = 10)

# AR([1,5])-GARCH(1,1) - use default garch values and subset ar[.]
spec = garchSpec(model = list(mu = 0.001, ar = c(0.5,0,0,0,0.1)))
garchSim(spec, n = 10)

# ARMA(1,2)-GARCH(1,1) - use default garch values
spec = garchSpec(model = list(ar = 0.5, ma = c(0.3, -0.3)))  
garchSim(spec, n = 10)

--

## volatility-methods
  
## Swiss Pension func Index -
x = as.timeSeries(data(LPP2005REC))
## garchFit
fit = garchFit(LPP40 ~ garch(1, 1), data = 100*x, trace = FALSE)
fit
## volatility -
# Standard Deviation:
volatility = volatility(fit, type = "sigma")
head(volatility)
class(volatility)
# Variance:
volatility = volatility(fit, type = "h")
head(volatility)
class(volatility)

