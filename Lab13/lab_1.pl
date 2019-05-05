%a.
% i. Exercise 3.2

directlyIn(katarina, olga).

directlyIn(olga, natasha).

directlyIn(natasha, irina).

in(X, Y) :- directlyIn(X, Y).

in(X, Y) :- directlyIn(X, Z), 
              in(Z, Y). 
              
% ii. Exercise 4.5

tran(eins,one). 
tran(zwei,two). 
tran(drei,three). 
tran(vier,four). 
tran(fuenf,five). 
tran(sechs,six). 
tran(sieben,seven). 
tran(acht,eight). 
tran(neun,nine).

listtran([], []). 
listtran([G|X], [E|Y]) :- tran(G, E), 
                            listtran(X, Y).
                            


%b. 
% Yes, Prolog does implement a version of generalized modus ponens. Following is the example
  % if X is a mammal, it is an animal.
  % Cats are mammals. 
  % Thus, cats are animals. 

animals(x) :- mammals(X). 
mammals(cats).

% -? animals(cats) returns true


