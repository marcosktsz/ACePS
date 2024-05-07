# cook levin -> SAT è NP completo

    come si dimostra:

    - SAT appartiene a NP
    - circuit-SAT < SAT
    - circuit-SAT è NP completo

    circuit-SAT è NP completo:
      - circuit-SAT appartiene a NP ✅
      - ogni problema NP si riduce a circuit-SAT (NP-Hard)

# LEMMA:

    per ogni problema B in P e per ogni N esiste un circuito booleano CN tale che per ogni istanza x di B tale che x è di lunghezza n
    Cn(x) = B(x), inoltre Cn è costruibile in tempo polinomiale

## Dimostriamo che circuit-SAT è NP Hard, ovvero per ogni problema A appartenente ad NP, A < circuit-SAT

                   polytime
    dato x ∈ I(A) ---------> Circuito booleano che dipende da x ed A tale che A(x) == yes <==> CxA soddisfacibile

## ridure circuit-SAT a SAT

    per ogni porta logica del circuito si crea una nuova variabile corrispondente all'output di quella porta. Ad ogni porta logica corrisponderà una formula del tipo [and/or/not(input) = output], la quale messa in And con
    tutte le altre ritornerà la formula phi relativa a SAT

    es:
        [x1] [x2]  [x3]
          |    |     |
        [   or   ] [not]
              |     |
            [   and   ]
                 |

    diventa:
        [(x1 or x2) = y1] and [not(x3) = y2] and [(y2 and y1) = y3] and y3
