
MATCH (n) DETACH DELETE n;

LOAD CSV WITH HEADERS FROM "file:///C:/Users/Dell/OneDrive/Pravin/Neo4j/Employee.csv" AS csvLine
MERGE  (:Employee {id: toInteger(csvLine.id), name: csvLine.EMPNAME, designation: csvLine.Designation,DOJ: csvLine.DOJ});


LOAD CSV WITH HEADERS FROM "file:///C:/Users/Dell/OneDrive/Pravin/Neo4j/Relationship1.csv" AS csvLine1
MATCH (p1:Employee {id:toInteger(csvLine1.Emp)}), (p2:Employee {id:toInteger(csvLine1.Manager)})
WITH p1, p2, csvLine1
CALL apoc.create.relationship(p1, csvLine1.Relationship, {Relationship: csvLine1.Relationship}, p2) YIELD rel
RETURN *


match(n) return(n) ;

match(n:Employee) 
WHERE n.name = 'Pravin' 
return(n) ;


match(n:Employee) 
WHERE n.name = 'Jitin' 
return(n) ;


