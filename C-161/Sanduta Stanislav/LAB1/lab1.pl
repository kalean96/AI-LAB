male(calistru).
male(gheorghe).
male(ivan).
male(nicolae).
male(jora).
male(boris).
male(igor).
male(eugen).
male(vladislav).
male(stanislav).

female(anna).
female(maria1).
female(maria2).
female(svetlana).
female(arina).
female(valentina).
female(angela).
female(inna).
female(vilena).

%!  calistru & anna
parent_of(calistru, ivan).
parent_of(calistru, nicolae).
parent_of(calistru, maria2).
parent_of(calistru, jora).
parent_of(anna, ivan).
parent_of(anna, nicolae).
parent_of(anna, maria2).
parent_of(anna, jora).

%!  gheorghe & maria1
parent_of(gheorghe, boris).
parent_of(gheorghe, svetlana).
parent_of(gheorghe, igor).
parent_of(maria1, boris).
parent_of(maria1, svetlana).
parent_of(maria1, igor).

%!  angela & igor
parent_of(igor, arina).
parent_of(igor, valentina).
parent_of(igor, eugen).
parent_of(angela, arina).
parent_of(angela, valentina).
parent_of(angela, eugen).

%!  jora & svetalana
parent_of(jora, inna).
parent_of(svetlana, inna).

%!  inna & vladislav
parent_of(vladislav, stanislav).
parent_of(vladislav, vilena).
parent_of(inna, stanislav).
parent_of(inna, vilena).

/* Rules */
father_of(X,Y):- male(X), parent_of(X,Y).

mother_of(X,Y):- female(X), parent_of(X,Y).

grandfather_of(X,Y):- male(X), parent_of(X,Z), parent_of(Z,Y).

grandmother_of(X,Y):- female(X), parent_of(X,Z), parent_of(Z,Y).

brother_of(X,Y):- %(X,Y or Y,X)%
    male(X),
    father_of(F,Y),
    father_of(F,X),
    X \= Y.

brother_of(X,Y):-
    male(X),
    mother_of(M,Y),
    mother_of(M,X),
    X \= Y.

sister_of(X, Y) :- %(X,Y or Y,X)%
    female(X),
    father_of(F, Y),
    father_of(F,X),
    X \= Y.

sister_of(X, Y) :-
    female(X),
    mother_of(F, Y),
    mother_of(F,X),
    X \= Y.

aunt_of(X,Y):- female(X),
    parent_of(Z,Y), sister_of(X,Z).

uncle_of(X,Y):- male(X),
    parent_of(Z,Y), brother_of(Z,X).

husband_of(X,Y):- male(X),
    female(Y), parent_of(Y,Z), parent_of(X,Z).

wife_of(X,Y):- female(X),
    male(Y), parent_of(Y,Z), parent_of(X,Z).

cousin_of(X,Y):- parent_of(Z,Y),
    parent_of(T, X), (brother_of(Z,T); sister_of(Z,T)).
