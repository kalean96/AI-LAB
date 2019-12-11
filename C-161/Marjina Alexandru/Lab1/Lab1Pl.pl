/* Fapte */
male(alex).
male(fiodor).
male(pavel).
male(pimen).
male(ion).
male(alexandru).

female(daniela).
female(angela).
female(maria).
female(eliza).
female(lilia).
female(aliona).
female(vera).
female(mariana).
female(eugenia).

parent(fiodor,alex).
parent(fiodor,daniela).
parent(angela,alex).
parent(angela,daniela).
parent(pavel,fiodor).
parent(pavel,alexandru).
parent(pavel,aliona).
parent(pavel,vera).
parent(pavel,mariana).
parent(pavel,eugenia).
parent(eliza,fiodor).
parent(eliza,alexandru).
parent(eliza,aliona).
parent(eliza,vera).
parent(eliza,mariana).
parent(eliza,eugenia).
parent(pimen,angela).
parent(pimen,ion).
parent(pimen,lilia).
parent(maria,angela).
parent(maria,ion).
parent(maria,lilia).

/* Reguli */
father(X,Y):- male(X),parent(X,Y).

mother(X,Y):- female(X),parent(X,Y).

grandfather(X,Y):- male(X),parent(X,Z),parent(Z,Y).

grandmother(X,Y):- female(X),parent(X,Z),parent(Z,Y).

sister(X,Y):- %(X,Y or Y,X)%
    female(X),
    father(F, Y), father(F,X),X \= Y.

brother(X,Y):- %(X,Y or Y,X)%
    male(X),
    father(F, Y), father(F,X),X \= Y.

uncle(X,Y):- parent(Z,Y), brother(Z,X).
	
aunt(X,Y):- parent(Z,Y), sister(Z,X).

ancestor(X,Y):- parent(X,Y).
ancestor(X,Y):- parent(X,Z),ancestor(Z,Y).
