men(ion).
men(colea).
men(ion_samoil).
men(ion_samoil_senior).
men(alexandru).
men(valeriu).
men(gheorghe).
men(unknown).


women(valentina).
women(vera).
women(elena).
women(nastasia).
women(ecaterina).
women(agafia).


parent(vera,valentina).
parent(vera,elena).
parent(vera,gheorghe).
parent(ion_samoil,valentina).
parent(ion_samoil,elena).
parent(valentina,ion).
parent(valentina,colea).
parent(unknown,ion).
parent(elena,alexandru).
parent(elena,ecaterina).
parent(elena,nastasia).
parent(valeriu,alexandru).
parent(valeriu,nastasiua).
parent(valeriu,ecaterina).
parent(ion_samoil_senior,vera).
parent(agafia,vera).





father(X,Y):- men(X),
parent(X,Y).

mother(X,Y):- women(X),
parent(X,Y).

ancestor(X,Z):-parent(X,Y), parent(Y,Z).
;   
grandfather(X,Z):-men(X), parent(X,Y), parent(Y,Z).
grandmather(X,Z):-women(X), parent(X,Y), parent(Y,Z).
keep_ancestor(X,Z):-parent(X,Y),ancestor(Y,Z).
