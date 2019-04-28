


% You burn a witch. Witch can be burnt because she is a wood. Wood does not sink in the water, so she has to weigh the same as a duck, 
% which also floats. 

% This Prolog is built according to what Bedevere argued at the end of the script. 


witch(X) :- burn(X).
burn(X) :- wood(X). 
floats(X) :-
  wood(X); 
  duck(X).
wood(X) :- sameWeightasDuck(X).

sameWeightasDuck(woman).

%query: ?- witch(woman)
% answer would be "yes". 
