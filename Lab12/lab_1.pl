%a.
%Exercise 1.4



killer(butch).
%gave property 'killer' to the name 'butch' = butch is a killer


married(mia, marsellus).
%gave property 'married' to the names 'Mia' and (,) Marcellus = Mia and Marcellus are married

dead(zed).
%gave property 'dead' to the name 'Zed' = Zed is dead


kill(marsellus,X):-
    footmassage(X, mia).
%gave property 'kill' to the name 'Marsellus' and variable 'X' followed by rule 'if' (:-).
%And for the rule, I gave property 'footmassage' to the name 'Mia' by variable 'X'



loves(mia,Y):-
    goodDancer(Y).
%gave property 'love' to the name 'Mia' and variable 'Y' followed by rule 'if' (:-).
%And for the rule, i gave property 'Good Dancer' to variable 'Y'.



eats(Jules,Z):-
    nutritious(Z);
    tasty(Z).
%gave property 'eat' to the name 'Jules' and variable 'Z' followed by rule 'if' (:-).
%#And for the rule, I gave property 'nutritious' or (;) 'tasty' to variable 'Z'.





%Exercise 1.5

wizard(ron). 
hasWand(harry). 
quidditchPlayer(harry). 
wizard(X):-  hasBroom(X),  hasWand(X). 
hasBroom(X):-  quidditchPlayer(X).


%1.Yes
%wizard(ron) - stated as a fact in the knowledge base

%2.No
% There is no property called 'witch'

%3.No
% There is no name called 'hermione'

%4.No
% There is no property called 'witch' nor name called 'hermione'

%5.Yes
% wizard(x) :- hasBroom(x), hasWand(x). Harry is quidditchPlayer which makes it true that he is a broom.
%Harry has a wand as it is stated as a fact (hasWand(harry)). Thus, Harry has a broom and a wand which makes
%him a wizard.

%6.Yes
% wizard(Y):- hasBroom(Y), hasWand(Y).
% It is true for both wizards, Ron and Harry (y can be Ron or Harry) 

%7.No
% There is no property called 'witch' 






%b.
%Consider the well-known modus ponens. Does Prolog implement a version of modus ponens in propositional logic form? 
%If so, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not?

% modus ponens = 
    % p -> q 
    % p is true
    % therefore q must be true
% Yes, Prolog implements modus ponens with :- (if)
q :- p.
p.
% ?- q. then the output would be "yes" 



%c. 
%Prolog supports representations in the form of Horn clauses. Compare and contrast the representational power they provide
%with that of propositional logic.

%Horn clauses provides the representational power in terms of describing relations between terms, while propositional provides 
%power as concisly denoting truth of the term. 





%d. 
%Logical implementations generally distinguish the basic operations of TELL and ASK. Does Prolog support this distinction?
%If so, how; if not, why not?

%Yes, Prolog support the distinction between TELL and ASK. For instance, we can ask Prolog whether Mia plays air guitar
%?- playAirGuitar(mia). We can tell Prolog which of the individuals Prolog knows about is a woman by ?- woman(X). Thus, it becomes 
%'asking' if we pose query with atom, and it becomes 'telling' if we pose query with variable. 
