barbat(viorel).
barbat(pavel).
barbat(mihai).
barbat(vladimer).
barbat(slavic).

femeie(tatiana).
femeie(sanda).
femeie(nina).
femeie(tamara).
femeie(ema).
femeie(lina).
femeie(sofia).
femeie(victoria).

parent(viorel, mihai).
parent(viorel, sanda).
parent(tatiana, mihai).
parent(tatiana, sanda).
parent(vladimer,tatiana).
parent(nina,tatiana).
parent(pavel,viorel).
parent(tamara,viorel).
parent(nina,slavic).
parent(vladimer,slavic).
parent(slavic,ema).
parent(slavic,lina).
parent(slavic,sofia).

casatoriti(tatiana,viorel).
casatoriti(nina,vladimer).
casatoriti(tamara,pavel).
casatoriti(slavic,victoria).

mama(X,Y):-femeie(X),parent(X,Y).
tata(X,Y):-parent(X,Y),barbat(X).
copil(Y,X):-parent(X,Y).
fratesisora(X,Y):-parent(Z,X),parent(Z,Y),Y\=X.
%sora(X,Y):-parent(Z,X),parent(Z,Y),femeie(X).%
bunica(X,Y):-parent(X,Z),parent(Z,Y),femeie(X).
bunel(X,Y):-parent(X,Z),parent(Z,Y),barbat(X).
nepot(X,Y):-parent(X,Z),parent(Z,Y).
stramos(X,Z):-parent(X,Z).
stramos(X,Z):-parent(X,Y),stramos(Y,Z).
verisor(X,Y):-parent(Z,X),fratesisora(Z,W),parent(W,Y).
unchi(X,Y):-(parent(Z,X),fratesisora(Z,W),casatoriti(W,Y)); parent(Z,X),fratesisora(Z,Y).
