'''Exercise 1.4'



killer(butch)
#I gave property 'killer' to the name 'butch' = butch is a killer


married(mia, marsellus)
#I gave property 'married' to the names 'Mia' and (,) Marcellus = Mia and Marcellus are married

dead(zed)
#I gave property 'dead' to the name 'Zed' = Zed is dead


kill(marsellus,X):-
    footmassage(X, mia)
#For the head, I gave property 'kill' to the name 'Marsellus' and variable 'X' followed by rule 'if' (:-).
#And for the rule, I gave property 'footmassage' to the name 'Mia' by variable 'X'
#= Marsellus kills X (can be anyone) if X gives footmassage to mia.


loves(mia,Y):-
    goodDancer(Y)
#I gave property 'love' to the name 'Mia' and variable 'Y' followed by rule 'if' (:-).
#And for the rule, i gave property 'Good Dancer' to variable 'Y'.
#= Mia loves Y (can be anyone) if Y is a good dancer.

6.
eat(Jules,Z):-
    nutritious(Z);
    tasty(Z)
#I gave property 'eat' to the name 'Jules' and variable 'Z' followed by rule 'if' (:-).
#And for the rule, I gave property 'nutritious' or (;) 'tasty' to variable 'Z'.
#= Jules eats Z (can be anything) if it is nutritious or tasty.


'''Exercise 1.5'
1.Yes
# wizard(ron) - stated as a fact in the knowledge base

2.No
# There is no property called 'witch'

3.No
# There is no name called 'hermione'

4.No
# There is no property called 'witch' nor name called 'hermione'

5.Yes
# wizard(x) :- hasBroom(x), hasWand(x). Harry is quidditchPlayer which makes it true that he is a broom.
#Harry has a wand as it is stated as a fact (hasWand(harry)). Thus, Harry has a broom and a wand which makes
#him a wizard.

6.Yes
# wizard(Y):- hasBroom(Y), hasWand(Y).
# hasBroom(Y):-

5.No
# There is no property called 'witch' 

#Consider the well-known modus ponens. Does Prolog implement a version of modus ponens in propositional logic form? 
#If so, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not?

Prolog supports representations in the form of Horn clauses. Compare and contrast the representational power they provide
with that of propositional logic.

Logical implementations generally distinguish the basic operations of TELL and ASK. Does Prolog support this distinction?
If so, how; if not, why not?
