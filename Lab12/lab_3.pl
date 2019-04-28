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
