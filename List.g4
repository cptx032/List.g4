grammar List;

/*
Parser rules
*/

programa : comando+;
comando : NOME '=' exp #atribuicao
			| 'print' exp #impressao
;
exp : exp '.' exp #concatenacao
		| lista #definicaoLista
		| exp '+' exp #soma
		| NOME #variavel
		| INT #integer
		| 'false' #booleanFalse
		| 'true' #booleanTrue
;
lista : '[' exp (',' exp)* ']';
NOME : [a-zA-Z]+;
INT : [0-9]+;
SPACE : [ \n\t\r]->skip;