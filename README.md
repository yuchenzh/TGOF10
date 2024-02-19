# Using built-in background turbulence generator

## Physics
The OpenFOAM (seems to) uses a Passot-Pouquet spectrum.
$E(k) = E_a (\frac{k}{k0})^4 e^{-2(\frac{k}{k0})^2}$
Two parameters need to be set, in constant/boxTurbDict, which are $E_a$ and $k_0$
- $E_a$ will influence the scale of velocity, but not the distribution. 
- $k_0$ is the characteristic wave number. Adjust $k_0$ will change the scale of the turbulence.
- The Reynolds number $Re = \frac{ul}{\nu}$. Adjust $E_a$ will allow you to adjust the velocity.
Adjusting $k_0$ will affect the integral length scale. The dynamic viscosity is a property of the fluid itself.

## Integral length calculation
The integral length $l$ is calculated by 
$\int_{0}^{+\infty}k^{-1}E(k)dk /\int_{0}^{+\infty}E(k)dk$, 
suggested by https://en.wikipedia.org/wiki/Integral_length_scale.

It is evident that $E_a$ will not influence the $l$.

To make the calculation of $l$ easier, a Python script is offered here (An installation of Python 3 is required).
Run 
```bash
python integralLength.py <k0value>
```

Please note that an integral to positive infinity might not be numerically stable, to specify a upper limit, try
```bash
python integralLength.py <k0value> <upperLimit>
```

## Generation Strategy
Generate a initial turbulent velocity field with in a domain larger than your target domain.
And map the velocity back to your target domain!

## 2D generator
OpenFOAM does not provide a 2D initial turbulence generator. But we can easily implement one.
I offered one, modified from "boxTurb". The velocity in the $z$ direction is set to 0.

To compile it, go to the boxTurb2D folder and run
```bash
wmake
```

Run 
```bash
boxTurb2D
```
to generate the 2D background turbulence.

A 2D geometry is required.

Configure $E_a$ and $k_0$ in constant/boxTurbDict

See the box2d case for more information.

## 3D generator
OpenFOAM provides a built-in 3D initial turbulence generator. See the test case. 
Run 
```bash
boxTurb
```
to generate the 3D background turbulence.

Configure $E_a$ and $k_0$ in constant/boxTurbDict

See the box3d case for more infomation.

## Something to note
- The domain to generate the turbulence should be a box.
- The number of cells in each direction should be $2^n$, for $n \in \mathbb{N}$.


## Relevant functions in OpenFOAM
The spectrum is implemented in https://cpp.openfoam.org/v10/Ek_8H_source.html.

The generator is implemented in https://cpp.openfoam.org/v10/turbGen_8C_source.html.

Please note that K is a mesh with wave number information.

