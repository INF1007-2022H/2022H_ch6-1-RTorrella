#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tabnanny import check


def order(values: list = None) -> list:
    
    if values is None:
        values = []
        while len(values) < 10:
            values.append(input( "Entrer une valeur (int, float ou str) : " ))
       
    
    liste_Entiers = []
    liste_Floats = []
    liste_Str = []

    for i in values:
        type_val = type(i)
        if type_val is int :
            liste_Entiers.append(i)
        elif type_val is float : 
            liste_Floats.append(i)
        elif type_val is str :
            liste_Str.append(i)

    liste_triée = sorted(liste_Entiers) + sorted(liste_Floats) + sorted(liste_Str)
    return liste_triée


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        while len(words) < 2 :
            words.append(input("Entrer un mot : "))
        
    vérif_1 = sorted(list(words[0]))
    vérif_2 = sorted(list(words[1]))

    if vérif_1 == vérif_2:
        return True 
    else:
        return False


def contains_doubles(items: list) -> bool:
    items = []
    while len(items) != 1 :
        items.append(input("Entrer une valeur : "))

    listeSansDoublons = []

    for i in items : 
        if i not in listeSansDoublons:
            listeSansDoublons.append(i)

    if items == listeSansDoublons :
        return True
    else:
        return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

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
