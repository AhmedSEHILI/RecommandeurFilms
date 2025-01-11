import csv
import os
import random
os.system('cat projetMRC2024_squelette.rdf')
try :
    file = open("ml-100k/u1.base")
except :
    print("fichier introuvable")

ll = list(csv.reader(file,delimiter='\t')) 
url_onto = "http://www.semanticweb.org/daniii93430/ontologies/2024/11/ProjetMRC2024"
cp = 1
liste_genres = ["unknown" , "Action" , "Adventure" , "Animation" ,
              "Children's" , "Comedy" , "Crime" , "Documentary" , "Drama" , "Fantasy" ,
              "Film-Noir" , "Horror" , "Musical" , "Mystery" , "Romance" , "Sci-Fi" ,
              "Thriller" ,"War" , "Western" ]
mois_num = { 'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4 , 'May' : 5,
    'Jun' : 6, 'Jul' : 7,'Aug' : 8, 'Sep' : 9 ,'Oct' : 10, 'Nov' : 11, 'Dec' :12
}
mois_num_date = { 'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr' : '04' , 'May' : '05',
    'Jun' : '06', 'Jul' : '07','Aug' : '08', 'Sep' : '09' ,'Oct' : '10', 'Nov' :'11', 'Dec' :'12'
}        
liste_ratings = random.choices(ll,k=200)       
for line in liste_ratings :
    print('\t<owl:NamedIndividual rdf:about="{nom_onto}#Rating{id}">\
        \n\t\t<rdf:type rdf:resource="{nom_onto}#Rating"/>\
        \n\t\t<r:film rdf:resource="{nom_onto}#Film{id_film}"/>\
        \n\t\t<r:user rdf:resource="{nom_onto}#User{id_user}"/>\
        \n\t\t<r:note rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{note}</r:note>\
        \n\t</owl:NamedIndividual>\n'.format(nom_onto = url_onto, id = cp,id_film =line[1], id_user = line[0],note=line[2]))
    cp+=1

try :
    genre_file = open("ml-100k/u.genre")
except :
    print("fichier introuvable")  

ll = list(csv.reader(genre_file,delimiter='|')) 
cp = 0
for line in ll :
    print('\t<owl:NamedIndividual rdf:about="{nom_onto}#Genre{id_genre}">\
        \n\t\t<rdf:type rdf:resource="{nom_onto}#Genre"/>\
        \n\t\t<genre:name>{nom_genre}</genre:name>\
        \n\t</owl:NamedIndividual>\n'.format(nom_onto = url_onto, id_genre = line[1],nom_genre = line[0]))

try :
    user_file = open("ml-100k/u.user")
except :
    print("fichier introuvable")  

ll = list(csv.reader(user_file,delimiter='|')) 
for line in ll :
    print('\t<owl:NamedIndividual rdf:about="{nom_onto}#User{id_user}">\
        \n\t\t<rdf:type rdf:resource="{nom_onto}#User"/>\
        \n\t\t<usr:age rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">{age}</usr:age>\
        \n\t\t<usr:occupation>{occupation}</usr:occupation>\
        \n\t\t<usr:sexe>{sexe}</usr:sexe>\
        \n\t\t<usr:zipCode>{zipCode}</usr:zipCode>\
    \n\t</owl:NamedIndividual>'.format(nom_onto = url_onto, id_user = line[0],age = line[1],sexe = line[2], occupation = line[3], zipCode=line[4]))
try :
    movies_file = open("ml-100k/u.item",encoding='latin-1')
except :
    print("fichier introuvable")

ll = list(csv.reader(movies_file,delimiter='|')) 
for line in ll :
    genres =  ''
    for id_genre in [i for i,e in enumerate([int(x) for x in line[5:]]) if e == 1] :
        genres+= '\n\t\t<mv:genre rdf:resource="{nom_onto}#Genre{id_g}"/>'.format(nom_onto = url_onto, id_g=id_genre)
        
    if len(line[2]) != 0:
        dateS = line[2].split('-')
        num_mois = mois_num[dateS[1]]
        dateS[1] = mois_num_date[dateS[1]]
        print('\t<owl:NamedIndividual rdf:about="{nom_onto}#Film{id_film}">\
        \n\t\t<rdf:type rdf:resource="{nom_onto}#Film"/>'.format(nom_onto = url_onto,id_film = line[0])+genres+
        '\n\t\t<mv:anneeSortie rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{anneeSortie}</mv:anneeSortie>\
        \n\t\t<mv:jourSortie rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{jourSortie}</mv:jourSortie>\
        \n\t\t<mv:moisSortie rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{moisSortie}</mv:moisSortie>\
        \n\t\t<mv:dateSortie>{dateSortie}</mv:dateSortie>\
        \n\t\t<mv:imdbURL>{url_film}</mv:imdbURL>\
        \n\t\t<mv:title>{titre}</mv:title>\
        \n\t</owl:NamedIndividual>'.format(titre = line[1].replace('&','&amp;'), url_film = line[4].replace('&','&amp;'),anneeSortie = int(dateS[2]),moisSortie=num_mois,jourSortie=int(dateS[0]),dateSortie=['','-'.join(dateS[::-1])][len(line[2]) != 0]))

    else :    
        print('\t<owl:NamedIndividual rdf:about="{nom_onto}#Film{id_film}">\
            \n\t\t<rdf:type rdf:resource="{nom_onto}#Film"/>'.format(nom_onto = url_onto,id_film = line[0])+genres+
            '\n\t\t<mv:imdbURL>{url_film}</mv:imdbURL>\
            \n\t\t<mv:title>{titre}</mv:title>\
            \n\t</owl:NamedIndividual>'.format(titre = line[1].replace('&','&amp;'), url_film = line[4].replace('&','&amp;')))

print('</rdf:RDF>')