%a.
%i. 
  %Exercise 2.1
    %1. Yes
    %2. No
    %8. Yes, X = bread
    %9. Yes, X = sausage and Y = bread
    %14. No, (X = drink(beer)) != (X = food(bread))
%ii.
  %Exercise 2.2
     house_elf(dobby). 
     witch(hermione). 
     witch(’McGonagall’). 
     witch(rita_skeeter). 
     magic(X):-  house_elf(X). 
     magic(X):-  wizard(X). 
     magic(X):-  witch(X).
     % 1. Not satisfied
     % 2. Not satisfied
     % 3. Not satisfied
     % 4. Satisfied
     % 5. Satisfied
     % Prolog does its unification and reasoning by matching two terms that can be made to represent the same structure. For instatnce from 
     % our example, food(X) = food(bread); here, both terms have the same premise 'food' and variable X would be instantiated to 'bread'. 
     % In order to make number 1,2,3 satistifed, we would need house_elf (number 1) and wizard (number 3) to represent names as well as
     % wizard(harry) (number 2). 
     
     
    
%b. 
% No, inference in propositional logic does not use unification because for propositional logic, two terms does not need to be equivalent
% (for instance, disjunction of two statement a and b, a and b do not need to be both true or both false), while unification requires 
% two terms to be equal.


%c.
% Yes, Prolog inferencing use resolution becauase it search through the knowledge bases with facts, rules, and queries to see if posed query is 
% satisfied with what the knowledge bases have. 


     
