WITH DESCONTOS AS (
    SELECT
        ED.MATR,
        SUM(COALESCE(D.VALOR, 0)) AS VALOR
    FROM DESCONTO D
    INNER JOIN EMP_DESC ED ON (ED.COD_DESC = D.COD_DESC)
    GROUP BY ED.MATR
),
VENCIMENTOS AS (
    SELECT 
        EV.MATR,
        SUM(COALESCE(V.VALOR, 0)) AS VALOR
    FROM emp_venc EV
    INNER JOIN VENCIMENTO V ON (V.COD_VENC = EV.COD_VENC)
    GROUP BY EV.MATR
),
SALARIOS AS (
    SELECT
    	divis.COD_DEP,
        EMP.MATR,
        SUM(COALESCE(V.VALOR, 0) - COALESCE(D.VALOR, 0)) AS SALARIO
    FROM Empregado EMP
    INNER JOIN DIVISAO DIVIS ON (DIVIS.COD_DIVISAO = emp.LOTACAO_DIV)
    LEFT JOIN VENCIMENTOS V ON (V.MATR = EMP.MATR)
    LEFT JOIN DESCONTOS D ON (D.MATR = EMP.MATR)
    GROUP BY divis.COD_DEP,EMP.MATR
),
DADOS_DEPARTAMENTO AS (
	SELECT
	    d.NOME AS NomeDepartamento,
	    count(s.matr) AS numeroempregados,
	    round(avg(s.salario), 2)::text AS MediaSalarial,
	    round(max(s.salario), 2)::text AS MaiorSalario,
	    round(min(s.salario), 2)::text AS MenorSalario
	FROM departamento d
	INNER JOIN salarios s ON (s.cod_dep = d.cod_dep )
	GROUP BY d.NOME
)
SELECT
    NomeDepartamento AS "Nome Departamento",
    numeroempregados AS "Numero de Empregados",
    CASE WHEN MediaSalarial = '0.00' THEN '0' ELSE MediaSalarial end AS "Media Salarial",
    CASE WHEN MaiorSalario  = '0.00' THEN '0' ELSE MaiorSalario end AS "Maior Salario",
    CASE WHEN MenorSalario = '0.00' THEN '0' ELSE MenorSalario end AS "Menor Salario"
FROM DADOS_DEPARTAMENTO
ORDER BY "Media Salarial" DESC;