import sqlite3
import pandas as pd

# Create connection and cursor to demo database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Create queries
expensive_items = "SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10"
""" 0                        1   2  3  ...   6   7   8  9
0  38            Côte de Blaye  18  1  ...  17   0  15  0
1  29  Thüringer Rostbratwurst  12  6  ...   0   0   0  1
2   9          Mishi Kobe Niku   4  6  ...  29   0   0  1
3  20   Sir Rodney's Marmalade   8  3  ...  40   0   0  0
4  18         Carnarvon Tigers   7  8  ...  42   0   0  0
5  59     Raclette Courdavault  28  4  ...  79   0   0  0
6  51    Manjimup Dried Apples  24  7  ...  20   0  10  0
7  62           Tarte au sucre  29  3  ...  17   0   0  0
8  43              Ipoh Coffee  20  1  ...  17  10  25  0
9  28        Rössle Sauerkraut  12  7  ...  26   0   0  1"""
avg_hire_age = "SELECT AVG((DATE(HireDate) - DATE(BirthDate))) AS 'Average Age at Hire' FROM Employee"
"""           0
0  37.222222"""
avg_age_by_city = "SELECT City, AVG(DATE(HireDate) - DATE(BirthDate)) AS 'Average Age at Hire' FROM Employee GROUP BY City"
"""          0     1
0  Kirkland  29.0
1    London  32.5
2   Redmond  56.0
3   Seattle  40.0
4    Tacoma  40.0"""
ten_most_expensive = "SELECT Product.*, Supplier.CompanyName FROM Product INNER JOIN Supplier ON Product.Id = Supplier.Id ORDER BY UnitPrice DESC LIMIT 10"
""" 0                           1   ...  9                                  10
0  29     Thüringer Rostbratwurst  ...   1                   Forêts d'érables
1   9             Mishi Kobe Niku  ...   1                   PB Knäckebröd AB
2  20      Sir Rodney's Marmalade  ...   0                       Leka Trading
3  18            Carnarvon Tigers  ...   0         Aux joyeux ecclésiastiques
4  28           Rössle Sauerkraut  ...   1                       Gai pâturage
5  27          Schoggi Schokolade  ...   0                 Escargots Nouveaux
6   8  Northwoods Cranberry Sauce  ...   0           Specialty Biscuits, Ltd.
7  17                Alice Mutton  ...   1                  Svensk Sjöföda AB
8  12   Queso Manchego La Pastora  ...   0  Plutzer Lebensmittelgroßmärkte AG
9  26         Gumbär Gummibärchen  ...   0               Pasta Buttini s.r.l."""
largest_category = "SELECT Category.CategoryName, COUNT(Product.CategoryId) FROM Category JOIN Product ON Category.Id = Product.CategoryId GROUP BY CategoryName ORDER BY COUNT(Product.CategoryId) DESC LIMIT 1"
"""             0   1
0  Confections  13"""
most_territories = "SELECT Employee.FirstName, Employee.LastName, COUNT(EmployeeTerritory.TerritoryId) FROM Employee JOIN EmployeeTerritory ON Employee.Id = EmployeeTerritory.EmployeeId GROUP BY LastName ORDER BY COUNT(EmployeeTerritory.TerritoryId) DESC LIMIT 1"
"""        0     1   2
0  Robert  King  10"""

# Execute queries
q1 = curs.execute(expensive_items).fetchall()
q2 = curs.execute(avg_hire_age).fetchall()
q3 = curs.execute(avg_age_by_city).fetchall()
q4 = curs.execute(ten_most_expensive).fetchall()
q5 = curs.execute(largest_category).fetchall()
q6 = curs.execute(most_territories).fetchall()

print(pd.DataFrame(q1))
print(pd.DataFrame(q2))
print(pd.DataFrame(q3))
print(pd.DataFrame(q4))
print(pd.DataFrame(q5))
print(pd.DataFrame(q6))


