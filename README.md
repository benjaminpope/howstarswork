# How Stars Work

## Benjamin Pope

[![Quarto Publish](https://github.com/benjaminpope/howstarswork/actions/workflows/publish.yml/badge.svg)](https://github.com/benjaminpope/howstarswork/actions/workflows/publish.yml)

We live around a star, the Sun. It is overwhelmingly the most important feature of our environment -- too bright to look at! -- and drives the dynamics of our climate, our economy, and our daily routine. We understand it in remarkable detail: we can measure its internal sounds and buoyancy waves as it rings like a bell, and using the science of helioseismology we can accurately reconstruct its physical properties almost all the way to the core. We can see its magnetised wind as the Southern Lights, and measure it quantitatively on satellites. We we can even measure neutrinos directly reaching us from the nuclear furnace at its core. 

More broadly, stars are to astronomy what atoms are to chemistry: innumerable building blocks of a much larger universe of galaxies and cosmology. Each has remarkably simple physics, really parametrized to a very good approximation only by their mass and composition, and at higher order their rotation period; these physics are so simple and reliable that we can accurately model the spectra of whole galaxies in the distant universe just using laboratory physics and our understanding of stars nearby. 

Analytic reasoning is usually good enough to get rough understanding of the important phenomena in stellar physics, usually as scaling relations - but these are usually only accurate to an order of magnitude or so, and *real* models require computer calculations. In this course we will attempt to do a bit of both.

This is a series of notes, aimed at a second-year undergraduate level, about how stars work: exploring their simplicity and complexity, assuming only a first year undergrad level of classical mechanics, quantum mechanics, and thermal physics, and other physics that we will introduce *ad hoc* as we go along. These notes are based in part on the excellent lectures from which I originally learned as an undergraduate at Berkeley, by Eliot Quataert; on Peter Tuthill and Mike Ireland's courses at Sydney; and on the PHYS2082 course developed at UQ by Holger Baumgardt, and by myself. 

We will use *cgs* units for most calculations in this text, except where otherwise noted. 

## Building This Book

This book is compiled using Jupyter-Books, which allows us to include Python calculations in the text; I aim to make this available in the Open Astrophysics Library when it is in a mature state. We will follow the style guide of Edward Tufte, using margins for asides and illustrations to avoid interrupting the flow of the text.

You can compile it by cloning this repo and, in the top-level directory, using 

```bash
jupyter-book build content
```