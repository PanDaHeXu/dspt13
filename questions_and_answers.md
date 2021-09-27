### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

#In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?
The primary key of the Employee table is the EmployeeId of the Territory table, which has a different primary key.
#What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
A NoSQL database (like MongoDB) would be appropriate for a real estate agency scanning in contracts that may have many similar sections, but not all the same. A relationship database would be would needed for banking where ACIDity is critical.
#What is "NewSQL", and what is it trying to achieve?
NewSQL is relational database system that is trying to match the scalability of NoSQL systems with the ACIDity of SQL systems.