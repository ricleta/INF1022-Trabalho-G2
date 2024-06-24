# Tokens
tokens = (
    'INICIO', 'MONITOR', 'EXECUTE', 'TERMINO', 
    'ENQUANTO', 'FACA', 'FIM', 
    'OUT', 'ID', 'NUMERO',
    'PLUS', 'EQUAL', 'MULT', 
    'IF', 'THEN', 'ELSE', 
    'ZERO', 'EVAL', 'VEZES', 
    'COMPARE', 'GREATER', 'LESSER'
)

# Grammar
// criacao de header
programa −→ INICIO varlist MONITOR varlist EXECUTE cmds TERMINO 

// list de vars que serao usadas
varlist −→ id varlist | id

cmds −→ cmd cmds | cmd
cmd −→ ENQUANTO id FACA cmds FIM // while ... do ... END
cmd −→ id = id | id = NUMERO // EQUAL (assign, not comparison)
cmd −→ id + id | id + NUMERO | NUMERO + id// PLUS
cmd −→ id * id | id * NUMERO | NUMERO * id// MULT
cmd −→ IF condicao THEN cmds
cmd −→ IF condicao THEN cmds ELSE cmds
cmd −→ ZERO id
cmd −→ EVAL cmds VEZES NUMERO FIM | EVAL cmds VEZES id FIM
condicao −→ id == id | id == NUMERO // COMPARE
condicao −→ id > id | id > NUMERO // GREATER
condicao −→ id < id | id < NUMERO // LESSER

# Obs
- Usar IF condicao THEN IF condicao THEN cmds ELSE cmds fica ambiguo, else poderia estar dentro do primeiro ou segundo if
    - Adicionar um END_IF resolveu