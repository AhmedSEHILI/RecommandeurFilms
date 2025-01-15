# RecommandeurFilms 2025
## Requete SPARQL Question 5 
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX iri: <http://www.semanticweb.org/daniii93430/ontologies/2024/11/ProjetMRC2024#>
SELECT ?r1 ?film ?titre ?date_sortie ?jour_sortie ?mois_sortie ?annee_sortie ?ng ?user  ?age ?occupation ?sexe ?code_pos ?note
	WHERE { 
		?r1 a iri:Rating;
		iri:r:note ?note;
		iri:r:film ?film;
		iri:r:user ?user;
		FILTER( ?note = 5).
		?film a iri:Film ;
		iri:mv:title ?titre;
		iri:mv:dateSortie ?date_sortie;
		iri:mv:dateSortie ?jour_sortie;
		iri:mv:dateSortie ?mois_sortie;
		iri:mv:dateSortie ?annee_sortie;
		iri:mv:imdbURL ?u1;
		iri:mv:genre ?g1.
		?g1 iri:genre:name ?ng.
		?user a iri:User;
		iri:usr:age ?age;
		iri:usr:occupation ?occupation;
		iri:usr:sexe ?sexe;	
		iri:usr:zipCode ?code_pos.
	}
ORDER BY ASC(?r1)

```
