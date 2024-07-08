# Hydrostatic Equilibrium

The fundamental physics of stars is determined by a handful of principles: 

```{margin} 
hydrostatic from Greek ὕδωρ, 'water', and στάσις, 'standing'; just like water in a tank.
```
- the star is everywhere in pressure balance under its own gravity, or *hydrostatic equilibrium*; 
- its cooling by radiation must be met by 
    - *energy production* in its interior by nuclear fusion or gravitational contraction, 
    - and *energy transport* to its surface by radiation, convection, and conduction; 
- how its material responds to pressure (parametrized the *equation of state*) and to light (parametrized by *opacity*); and
- in its interior and a star is typically rotating and magnetic, which we will neglect in most of these notes.

Let's talk about hydrostatic equilibrium first.

An ordinary star like the Sun, throughout its whole body, is to a very good approximation an *ideal gas*, and is fully ionized except in its outermost layer. This means that the gas pressure satisfies the equation of state

```{margin}
where $\textcolor{blue}{p}$ is the <font color='blue'>pressure</font>, $n$ is the number density (particles per volume) of the gas, $\textcolor{red}{k_B}$ is <font color='red'>Boltzmann's constant</font> ($1.38\times10^{-16}$ erg/K), and $\textcolor{orange}{T}$ is the <font color='orange'>temperature</font> in kelvin.
```
$$
\textcolor{blue}{p} = n \textcolor{red}{k_B} \textcolor{orange}{T}
$$


In a star like the Sun, the pressure is mostly provided by gas pressure. In hotter stars, *photon* or *radiation pressure* is dominant, but in the Sun this is $\sim 10^{-3} p_\text{gas}$. 

Even in the Sun, though, the gas is not *quite* a classical ideal gas: quantum mechanics is already relevant. There is an equation we will derive later in these notes for the pressure due to the *degeneracy* of a gas where the quantum wavefunctions of its constituent particles are nearly overlapping: 

```{margin}
where $\textcolor{purple}{\hbar}$ is the <font color='purple'>quantum of action $h/2\pi$</font> ($1.0546 \times 10^{-27} \text{erg}\cdot\text{s}$), and $\textcolor{yellow}{m_e}$ the <font color='yellow'>mass of the electron</font>.
```
$$
p_\text{degeneracy} = \frac{\textcolor{purple}{\hbar}}{5 \textcolor{yellow}{m_e}} (\frac{3}{8 \pi})^{2/3} n^{5/3}
$$

It turns out this is about a quarter of the gas pressure at the core of the Sun! 

## The Equation of Hydrostatic Equilibrium

```{margin}
i.e. $M_r$ is the total mass integrated out up to a radius $r$.
```
Consider a thin shell of radius $r$ (and surface area $A = 4\pi r^2$), thickness $dr$, and mass density $\rho$, enclosing a mass $M_r$. 

```{margin}
[Newton's Shell Theorem](https://en.wikipedia.org/wiki/Shell_theorem) states that the gravitational attraction of a symmetric shell of matter, and therefore by linearity of a ball of matter, can be treated as if the mass were concentrated at a point at the centre. 
```
The mass of this shell is $M_\text{shell} = \rho A dr$, and from Newton's law of gravitation the magnitude of the gravitational force of the whole shell inwards is 

$$ 
\frac{- G M_r M_\text{shell}}{r^2}
$$

So now we can calculate the net force on this shell (and therefore acceleration $a$), and require the forces to be in balance:

$$
F_\text{net} = M_\text{shell} a = P_\text{below} \cdot A - P_\text{above} \cdot A - \frac{G M_r M_\text{shell}}{r^2}
$$

Letting $P_\text{above} = P_\text{below} + dP$, 

$$
M_\text{shell} a = a \rho A dr = - A dP  - \frac{G M_r M_\text{shell}}{r^2}
$$

and therefore rearranging, in equilibrium ($a = 0$) we have 

```{margin}
*Tattoo this equation on the back of your eyelids.
```
$$ 
\frac{dP}{dr} = -\rho \frac{G M_r}{r^2}
$$

## Dynamical Timescale