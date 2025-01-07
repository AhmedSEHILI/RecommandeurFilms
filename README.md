# RecommandeurFilms 2025
## Requete SPARQL Question 5 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX iri: <http://www.semanticweb.org/daniii93430/ontologies/2024/11/ProjetMRC2024#>
SELECT ?f1 ?t1 ?d1 ?u1  ?ng ?n1
	WHERE { 
		?r1 a iri:Rating;
		iri:r:note ?n1;
		iri:r:film ?f1;
		FILTER( ?n1 = 5).
		?f1 a iri:Film ;
		iri:mv:title ?t1;
		iri:mv:dateSortie ?d1;
		iri:mv:imdbURL ?u1;
		iri:mv:genre ?g1.
		?g1 iri:genre:name ?ng
	}
	
ORDER BY ASC(?f1)
