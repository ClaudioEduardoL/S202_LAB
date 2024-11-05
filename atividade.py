//Questão 1

//A
MATCH (t:Teacher {name: 'Renzo'})
RETURN t.ano_nasc AS anoNascimento, t.cpf AS cpfProfessor;
//B
MATCH (t:Teacher)
WHERE t.name STARTS WITH 'M'
RETURN t.name AS nomeProfessor, t.cpf AS cpfProfessor;

//C
MATCH (c:City)
RETURN c.name AS nomeCidade;
//D
MATCH (s:School)
WHERE s.number >= 150 AND s.number <= 550
RETURN s.name AS nomeEscola, s.address AS enderecoEscola, s.number AS numeroEscola;

//Questão 2

//A
MATCH (t:Teacher)
RETURN MIN(t.ano_nasc) AS anoProfessorMaisVelho, MAX(t.ano_nasc) AS anoProfessorMaisJovem;
//B
MATCH (c:City)
RETURN AVG(c.population) AS mediaDePopulacao;
//C
MATCH (c:City {cep: '37540-000'})
RETURN REPLACE(c.name, 'a', 'A') AS nomeComAlteracao;

//D
MATCH (t:Teacher)
RETURN SUBSTRING(t.name, 2, 1) AS terceiroCaractereNome;