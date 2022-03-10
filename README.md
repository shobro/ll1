# LL(1)

We have to design an LL(1) parser for:
```
E -> E+T
E -> E-T
E -> T
T -> T*F
T -> T/F
T -> F
F -> num
F -> id
F -> (E)
```

However, the above the grammer is left recursive, so we first need to remove
left recursions as follows: 

```
E --> TX
X --> +TX | -TX | eps
T --> FY
Y --> *FY |  /FY | eps
F --> num | id | (E)
```
