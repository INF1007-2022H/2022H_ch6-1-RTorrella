#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tabnanny import check


def order(values: list = None) -> list:
    
    if values is None:
        values = []
        while len(values) < 10:
            values.append(input( "Entrer une valeur  : " ))
       
    liste_Floats = []
    liste_Str = []

    for i in values:
        if type(i) is float : 
            liste_Floats.append(i)
        else:
            liste_Str.append(i)

    
    return sorted(liste_Floats) + sorted(liste_Str)


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        while len(words) < 2 :
            words.append(input("Entrer un mot : "))
        
    condition = sorted(list(words[0])) == sorted(list(words[1]))
    

    if condition:
        return True 
    else:
        return False


def contains_doubles(items: list) -> bool:
    
    listeSansDoublons = []

    for i in items : 
        if i not in listeSansDoublons:
            listeSansDoublons.append(i)

    if items != listeSansDoublons :
        return True
    else:
        return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    meilleureMoyenne = {}
    listeMoyenne = []
    for nom, note in student_grades.items():
        moyenne = sum(note) / len(note)
        
        if moyenne not in listeMoyenne:
            listeMoyenne.append(moyenne)
            
    meilleureMoyenne = {nom : max(listeMoyenne)}

    return meilleureMoyenne


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    fréquence = {}
    for lettre in sentence:
        fréquence[lettre]= sentence.count(lettre)

    tableauLettres = sorted(fréquence, key=fréquence.get, reverse=True)
    for car in tableauLettres:
        if fréquence[car] > 5:
            print(f"Le caractère {car} revient {fréquence[car]} fois.")


    return fréquence


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données

    recette = input("Entrer le nom de votre recette : ")
    ingrédient = input("Entrer le nom des différents ingrédients. Séparer les par une virgule : ").split(", ")



    return {recette: ingrédient}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("Quel est le nom de votre recette ? ")

    if nom in ingredients:
        print(ingredients[nom])
    else:
        print("Cette recette ne fait pas partie de notre livre de recettes.")
        print(ingredients)
        
    


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
