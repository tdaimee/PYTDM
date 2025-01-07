import os

# Répertoires d'exercices pour chaque niveau
exercices_facile = "/home/letailleur/PYTDM/PYTDM/facile"
exercices_intermediaire = "/home/letailleur/PYTDM/PYTDM/intermediaire"
exercices_difficile = "/home/letailleur/PYTDM/PYTDM/difficile"

# Fonction pour afficher le titre en ASCII
import pyfiglet
def afficher_titre():
    ascii_title = pyfiglet.figlet_format("PYTDM")
    print(ascii_title)

# Fonction pour permettre à l'utilisateur d'éditer un fichier d'exercice
def editer_code_exercice(exercice_choisi):
    print(f"\nÉditez le code de l'exercice dans le fichier : {exercice_choisi}")
    input(f"Appuyez sur [Entrée] pour ouvrir l'éditeur. Utilisez 'exit' pour quitter une fois terminé.")
    
    # Utiliser un éditeur comme nano pour permettre à l'utilisateur de modifier le fichier
    os.system(f"vim {exercice_choisi}")
    
    # Après que l'utilisateur ait sauvegardé et quitté l'éditeur, on continue
    print("\nCode sauvegardé. Vérification en cours...\n")
    verifier_code_utilisateur(exercice_choisi)

# Fonction pour vérifier le code soumis par l'utilisateur en comparant avec la solution
def verifier_code_utilisateur(fichier_utilisateur):
    try:
        # Déterminer le fichier de solution correspondant
        solution_fichier = fichier_utilisateur.replace(".txt", ".py").replace("exercice", "solution")
        
        # Vérifier que le fichier de solution existe
        if not os.path.exists(solution_fichier):
            print(f"Aucune solution trouvée pour l'exercice.")
            return
        
        # Lire le code utilisateur
        with open(fichier_utilisateur, 'r') as f:
            code_utilisateur = f.read()
        
        # Lire le code de la solution
        with open(solution_fichier, 'r') as f:
            solution_code = f.read()
        
        # Exécuter et comparer les deux codes
        print("Exécution du code utilisateur...")
        exec(code_utilisateur)
        
        print("\nExécution de la solution...")
        exec(solution_code)
        
        # Si tout se passe bien, afficher un message de réussite
        print("\nLe code est correct ! Félicitations.")
    except Exception as e:
        print(f"Erreur dans votre code ou dans la solution : {e}")

# Fonction pour afficher le menu principal
def afficher_menu():
    while True:
        print("Bienvenue dans PYTDM ! L'entraîneur Python")
        print("Choisissez une difficulté :")
        print("1. Facile")
        print("2. Intermédiaire")
        print("3. Difficile")
        print("4. Quitter")

        choix = input("Votre choix : ")
        
        if choix == "1":
            choisir_exercice("facile")
        elif choix == "2":
            choisir_exercice("intermediaire")
        elif choix == "3":
            choisir_exercice("difficile")
        elif choix == "4":
            print("Merci et à bientôt !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Fonction pour choisir un exercice à partir du répertoire sélectionné
def choisir_exercice(difficulte):
    exercices_dir = f"/home/letailleur/PYTDM/PYTDM/{difficulte}"
    
    # Liste des fichiers d'exercices
    exercices = [f for f in os.listdir(exercices_dir) if f.endswith('.txt')]

    if not exercices:
        print(f"Aucun exercice trouvé dans le répertoire {difficulte}.")
        return
    
    print(f"Exercices disponibles ({difficulte}) :")
    for i, exercice in enumerate(exercices, 1):
        print(f"{i}. {exercice}")
    print(f"{len(exercices) + 1}. Retour au menu principal")

    choix = input("Votre choix : ")
    if choix == str(len(exercices) + 1):
        return
    
    try:
        exercice_choisi = exercices[int(choix) - 1]
        exercice_fichier = os.path.join(exercices_dir, exercice_choisi)
        
        # Permet à l'utilisateur d'éditer son code pour l'exercice choisi
        editer_code_exercice(exercice_fichier)
    except (ValueError, IndexError):
        print("Choix invalide, retour au menu principal.")

# Exécution du programme principal
if __name__ == "__main__":
    afficher_titre()  # Affichage du titre en ASCII
    afficher_menu()   # Affichage du menu principal
