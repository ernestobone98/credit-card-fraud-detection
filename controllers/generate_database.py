import random, os

cur_dir = os.getcwd()
sep = os.path.sep

# -------------------------------------- Data Informations: Pull statistics from the internet -------------------------------------- #

first_name_man = ["Leo","Gabriel","Raphael","Arthur","Louis","Jules","Adam","Mael" ,"Lucas","Hugo",
                    "Noah","Liam","Gabin","Sacha","Paul","Nathan","Aaron","Mohamed","Ethan","Tom","Eden",
                    "Leon","Noe","Tiago","Theo","Isaac","Marius","Victor","Ayden","Martin","Nael",
                    "Mathis","Axel","Robin","Timeo","Enzo","Marceau","Valentin","Nino","Eliott","Nolan",
                    "Malo","Milo", "Antoine" ,"Samuel","Augustin" ,"Amir","Lyam","Rayan","Yanis","Ibrahim",
                    "Gaspard","Sohan","Clement","Matheo","Simon","Baptiste","Maxence","Imran","Kais","Come",
                    "Soan","Evan","Maxime","Camil","Alexandre","Owen","Ismael","Lenny","Pablo","Leandre",
                    "Naim","Ilyan","Thomas","Joseph","Oscar","Elio","Noa","Malone","Diego","Noam",
                    "Livio","Charlie","Charly","Basile","Milan","Ilyes","Ali","Anas","Logan","Mathys",
                    "Alessio","William","Timothee","Auguste","Ayoub","Adem","Wassim","Youssef","Marin"]

name_man = ["Martin","Bernard","Thomas","Petit","Robert","Richard","Durand","Dubois","Moreau","Laurent",
        "Simon","Michel","Lefebvre","Leroy","Roux","David","Bertrand","Morel","Fournier","Girard",
        "Bonnet","Dupont","Lambert","Fontaine","Rousseau","Vincent","Muller","Lefevre","Faure","Andre",
        "Mercier","Blanc","Guerin","Boyer","Garnier","Chevalier","Francois","Legrand","Gauthier","Garcia",
        "Perrin","Robin","Clement","Morin","Nicolas","Henry","Roussel","Mathieu","Gautier","Masson",
        "Marchand","Duval","Denis","Dumont","Marie","Lemaire","Noel","Meyer","Dufour","Meunier","Brun",
        "Blanchard","Giraud","Joly","Riviere","Lucas","Brunet","Gaillard","Barbier","Arnaud","Martinez",
        "Gerard","Roche","Renard","Schmitt","Roy","Leroux","Colin","Vidal","Caron","Picard",
        "Roger","Fabre","Aubert","Lemoine","Renaud","Dumas","Lacroix","Olivier","Philippe","Bourgeois",
        "Pierre","Benoit","Rey","Leclerc","Payet","Rolland","Leclerc","Guillaume","Lecomte"]

jobs = ["Agriculteurs exploitants","Artisans","Commercants","Chefs d'entreprise","Cadres",
               "Professions intellectuelles superieures","Professions intermediaires","Employes",
               "Ouvriers","Personne sans activite professionnelle"]

cities = ["Paris","Marseille","Lyon","Toulouse","Nice","Nantes","Montpellier","Strasbourg",
            "Bordeaux","Lille","Rennes","Reims","Toulon","Saint-etienne","Le Havre","Grenoble",
            "Dijon","Angers","Villeurbanne","Saint-Denis","Nimes","Clermont-Ferrand","Le Mans",
            "Aix-en-Provence","Brest","Tours","Amiens","Limoges","Annecy","Boulogne-Billancourt",
            "Perpignan","Besancon","Metz","Orleans","Saint-Denis","Rouen","Argenteuil","Montreuil",
            "Mulhouse","Caen","Nancy","Saint-Paul","Roubaix","Tourcoing","Nanterre","Vitry-sur-Seine",
            "Creteil","Avignon","Poitiers","Aubervilliers","Dunkerque","Aulnay-sous-Bois","Colombes",
            "Asnieres-sur-Seine","Versailles","Saint-Pierre","Courbevoie","Le Tampon","Cherbourg-en-Cotentin",
            "Fort-de-France","Rueil-Malmaison","Beziers","Champigny-sur-Marne","Pau","La Rochelle",
            "Saint-Maur-des-Fosses","Cannes","Calais","Antibes","Drancy","Mamoudzou","Ajaccio","Merignac",
            "Saint-Nazaire","Colmar","Issy-les-Moulineaux","Noisy-le-Grand","evry-Courcouronnes","Venissieux",
            "Cergy","Levallois-Perret","Valence","Bourges","Pessac","Cayenne","Ivry-sur-Seine","Quimper",
            "La Seyne-sur-Mer","Antony","Villeneuve-d'Ascq","Clichy","Troyes","Montauban","Neuilly-sur-Seine",
            "Pantin","Niort","Chambery","Sarcelles","Le Blanc-Mesnil","Lorient"]

first_name_woman = ["Jade","Louise","Emma","Alice","Ambre","Lina","Rose","Chloe","Mia","Lea",
                    "Anna","Mila","Julia","Romy","Lou","Ines","Lena","Agathe","Juliette","Inaya",
                    "Nina","Zoe","Leonie","Jeanne","Iris","Eva","Charlie","Lola","Adele","Victoire",
                    "Manon","Luna","Camille","Romane","Lucie","Margaux","Olivia","Victoria","Alix",
                    "Louna","Mya","Sofia","Charlotte","Sarah","Giulia","Lya","Margot","Nour","Lyana",
                    "Capucine","Clemence","Thea","Elena","Alba","Emy","Clara","Lana","Aya","Lyna",
                    "Yasmine","Gabrielle","Alya","Alicia","Roxane","Zelie","Lise","Lily","Leana",
                    "Maya","Mathilde","Livia","Valentine","Anais","Apolline","Thays","Lila","Maelys",
                    "Assia","Heloise","Ava","Joy","Alma","Lilou","Maria","Constance","Elise","Maelle",
                    "Celia","Marie","Ella","Amelia","Elsa","Lisa","Noemie","Salome","Emmy","Celeste","Albane","Soline","Nora"]

name_woman = ["Marchand","Duval","Denis","Dumont","Marie","Lemaire","Noel","Meyer","Dufour",
                "Meunier","Brun","Blanchard","Giraud","Joly","Riviere","Lucas","Brunet","Gaillard",
                "Barbier","Arnaud","Martinez","Gerard","Roche","Renard","Schmitt","Roy","Leroux","Colin",
                "Vidal","Caron","Picard","Roger","Fabre","Aubert","Lemoine","Renaud","Dumas","Lacroix",
                "Olivier","Philippe","Bourgeois","Pierre","Benoit","Rey","Leclerc","Payet","Rolland","Leclerc",
                "Guillaume","Lecomte","Martin","Bernard","Thomas","Petit","Robert","Richard","Durand","Dubois",
                "Moreau","Laurent","Simon","Michel","Lefebvre","Leroy","Roux","David","Bertrand","Morel","Fournier",
                "Girard","Bonnet","Dupont","Lambert","Fontaine","Rousseau","Vincent","Muller","Lefevre","Faure",
                "Andre","Mercier","Blanc","Guerin","Boyer","Garnier","Chevalier","Francois","Legrand","Gauthier",
                "Garcia","Perrin","Robin","Clement","Morin","Nicolas","Henry","Roussel","Mathieu","Gautier","Masson"]

adressmail = ["marcogzapro", # Expert 1
              "chavy98", # Expert 2
              "benjamin.bernaud", # Boss
              "quentin2908"]

probabilities = [60, 0, 15, 25]

def create_phones():
    phones = ""
    second = random.randint(6,7)
    suffix = random.randint(10000000,100000000)
    phones += "0{}{}".format(second, suffix)
    return phones

def random_info_creation(s, n): # s = man or woman / n = id
    if s == 'm':
        f_name = random.choice(first_name_man)
        name = random.choice(name_man)
        age = random.choice([i for i in range(18,81)])
    elif s == 'w':
        f_name = random.choice(first_name_woman)
        name = random.choice(name_woman)
        age = random.choice([i for i in range(18,87)])
        
    job = 'Retraite' if age >= 66 else random.choice(jobs)
    city = random.choice(cities)
    number = create_phones()
    id = n
    adress_mail = random.choices(adressmail, weights=probabilities, k=1)[0]+"@gmail.com"
    
    return [id, f_name, name, age, job, city, number, adress_mail]
    
if __name__ == '__main__':
    f_out = f"{cur_dir}{sep}models{sep}clients.csv"
    m_client = 50 # number of men client
    w_client = 50 # number of women client
    client_list = []
    
    # Creation of information
    for i in range(m_client):
        client_list.append(random_info_creation('m', len(client_list)+1))
    for i in range(w_client):
        client_list.append(random_info_creation('w', len(client_list)+1))
        
    print(len(client_list), client_list)
    # Information writing
    with open(f_out, "w") as text_file:
        text_file.write("ID,Prenom,Nom,Age,Job,Ville,Tel,Adresse mail\n")
        for i in range(m_client + w_client):
            text_file.write(','.join(map(str, client_list[i])) + "\n")
