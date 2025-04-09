# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define m = Character('Mother', color="#c8ffc8")

# Ma liste de musique
define audio.testmusic = "RedSex-Vessel.mp3" 


# Le jeu commence ici
label start:

    play music testmusic fadein 1.0

    m "C'est toi Anthräx ?"

    m "Bienvenue dans la troupe !"

    return
