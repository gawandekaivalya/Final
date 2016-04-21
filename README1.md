The B-Z reaction is a redox reaction that periodically moves between an oxidized and a reduced state, and has been demonstrated for various chemicals. 
This model does not attempt to replicate the actual mechanism of the chemical reaction, which is quite complex (including 18 reactions and 21 species, according to the Fields-Koros-Noyes model). 
The abstract features shared by the real reaction and this model include:
1. Two end states.
2. A positive feedback mechanism.
3. A negative feedback mechanism.

The positive feedback mechanism acts to push the system further in the direction that it is already going, reinforcing and amplifying the initial change. 
(In the chemical reaction, positive feedback comes from auto-catalysis.) 
The negative feedback mechanism pushes the system back in the opposite direction once a threshold is reached, suppressing or counteracting the effected change.


Each cell has a state which is an integer from 0 to max-state. We choose to show state 0 as black, max-state as white, and intermediate states as shades of red.

Suppose we call state 0 "healthy", max-state "sick", and anything in between "infected". 
Then the rules for how each cell changes at each step can be described as follows:

1. A cell that is sick becomes healthy.
2. A cell that is healthy may become infected, if enough of its eight neighbors are infected or sick. Whether this happens is affected by the k1 and k2 sliders. (Lower k1 means higher tendency to be infected by infected neighbors; lower k2 means higher tendency to be infected by sick neighbors.)
3. A cell that is infected computes its new state by averaging the states of itself and its eight neighbors, then adding the value of the g slider. (Higher g means infected cells get sicker more rapidly.)

1 is the negative feedback; 2 and 3 are the positive feedback.

Very much similar to Game Of Life!!
