# Rough outline for CFD report


#### Physics
##### Intro 1d concept converted to 2d
* following discussions will be 2d

##### Convection
###### Linear
###### Nonlinear

##### Diffusion


##### Burgers

##### (Laplace, Poisson, Navier-Stokes)

#### (???)
###### N-S channel flow
###### N-S cavity flow


#### Numerical methods
##### Rationale for differencing methods used
##### Stability (computational)


#### Code strategy
##### Optimizations for speed
* general (vectorization) + specific to Python packages (jit in numba)
* Link code on github
##### Programmatically searching for features
e.g. varying parameters to find shocks in Burgers (I should probably do that first)
