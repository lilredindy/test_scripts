UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;

DELETE FROM table_name
WHERE condition;



SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s); 

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;


$query="SELECT DISTINCT customerId FROM purchases WHERE quantity>3";

$query="SELECT customerId, SUM(price) FROM orders GROUP BY customerId";

$query="SELECT SUM(quantity) FROM orders WHERE productId=345";
$query="SELECT SUM(quantity*price) FROM orders WHERE productId=345";


SELECT * FROM Country 
	JOIN CountryLanguage ON
		Country.Code=CountryLanguage.CountryCode
	JOIN City ON
		Country.Code=City.CountryCode;

$query="SELECT personId FROM people WHERE (gender='female' AND age>60) OR (gender='male' AND age>65)";


