# Assignment 4: Desiging LL(1) parser

Information table:

We have to design an LL(1) parser for:
```
E --> E+T
E --> E-T
E --> T
T --> T*F
T --> T/F
T --> F
F --> num
F --> id
F --> (E)
```

However, the above the grammer is left recursive, so we first need to remove
left recursions as follows: 

```
E --> TX
X --> +TX | -TX | eps
T --> FY
Y --> *FY | /FY | eps
F --> num | id | (E)
```

Parsing table:

|     | num | id  | (   | +   | -   | *   | /   | $   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E   | TX  | TX  | TX  |     |     |     |     |     |
| X   |     |     | eps | +TX | -TX |     |     | eps |
| T   | FY  | FY  | FY  |     |     |     |     |     |
| Y   |     |     | eps | eps | eps | *FY | /FY | eps |
| F   | num | id  | (E) |     |     |     |     |     |

## Members and contributions

* Shobhit Belwal (1901191)
  * subroutine for making parse table
  * code for checking if a string is accepted by the grammar
  * removing left recursion
  * Lex rule

* Ujjwal Goel (1901209)
  * subroutine for finding first set
  * subroutine for finding follow set
  * verifcation of parsing table