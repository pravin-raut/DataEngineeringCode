MATCH (n) DETACH DELETE n;
CREATE (Minh: DataChapter {name:'Minh k', title:'Chapter Lead- US', Joined:2013, tagline:'IT System Owner'})
CREATE (Jitin: DataChapter {name:'Jitin S', title:'Chapter Lead- India'})
CREATE (Abdul: TestingChapter {name:'Abdul K', title:'Chapter Lead- India'})
CREATE (Pravin: DataChapter {name:'Pravin R', Joined:2021})
CREATE 
		(Jitin)-[:REPORTS_TO]->(Minh) ,
		(Pravin)-[:REPORTS_TO]->(Jitin),
		(Jitin)-[:MANAGER_OF]->(Pravin) 		;
match(n) return(n) ;
