WITH MENOR AS (SELECT MIN(customers_number) QTDE FROM lawyers),
     MAIOR AS (SELECT MAX(customers_number) QTDE FROM lawyers)
SELECT
    name,
    customers_number
FROM (
    SELECT
        name,
        customers_number,
        1 AS ORDEM
    FROM lawyers
    WHERE customers_number = (SELECT QTDE FROM MAIOR)
        OR customers_number = (SELECT QTDE FROM MENOR)
    UNION ALL
    SELECT
        'Average',
        ROUND(AVG(customers_number), 0),
        2 AS ORDEM
    FROM lawyers
) AS TAB
ORDER BY ORDEM, name