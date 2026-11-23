SELECT
    f.Contract,
    COUNT(*) AS total_clientes,
    COUNT(*) FILTER (WHERE c.Churn = 'Yes') AS bajas,
    ROUND(100.0 * COUNT(*) FILTER (WHERE c.Churn = 'Yes') / COUNT(*), 2) AS tasa_churn_pct,
    ROUND(AVG(f.MonthlyCharges), 2) AS cargo_mensual_medio
FROM clientes c
JOIN servicios s ON c.customerID = s.customerID
JOIN facturacion f ON c.customerID = f.customerID
GROUP BY f.Contract
ORDER BY tasa_churn_pct DESC;
