SELECT a.client_id
FROM account a
JOIN transaction t ON a.id = t.account_id
WHERE t.transaction_date >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 month'
  AND t.transaction_date < DATE_TRUNC('month', CURRENT_DATE)
  AND t.type = 'покупка'
GROUP BY a.client_id
HAVING COALESCE(SUM(t.amount), 0) < 5000;