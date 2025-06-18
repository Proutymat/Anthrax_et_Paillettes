# fonctions custom

image splash = "splashscreen.png"
image splash2 = "splashscreen2.png"

label before_main_menu:
     # Ne pas afficher la textbox ni le quick menu
    $ _window = False
    $ quick_menu = False
    $ _game_menu_screen = None

    # Écran noir de transition 

    # Affiche l'image de splash
    show splash with dissolve
    pause 1

    show splash2 with fade
    pause 1

    scene black with fade

    return

init python:   

    import os

    def get_available_translations():
        tl_path = os.path.join(renpy.config.gamedir, "tl")
        available_translations = []
        if os.path.isdir(tl_path):
            for folder_name in os.listdir(tl_path):
                # Exclude "None" folder and any hidden files
                if folder_name != "None" and not folder_name.startswith('.'):
                    available_translations.append(folder_name)
        return available_translations


init python:
    def type_sound(event, interact=True, cps=35, boopfile=type_sounds, **kwargs):
        speed = int((0.1/cps)*1000)/1000
        silence = "<silence " + str(speed) + ">"
    
        if not interact:
            return

        if event == "show" :
            for i in range(100):
                print(silence)
                renpy.sound.queue(renpy.random.choice(boopfile))
                renpy.sound.queue(silence)

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def pausedialogue():
        if renpy.music.is_playing('sound'):
            renpy.pause((20-renpy.music.get_pos('sound')),hard=True)

    renpy.music.register_channel("ambiance", "sfx", True)
    renpy.music.register_channel("sfx","sfx", False)
    renpy.music.register_channel("vfxL","sfx", False)
    renpy.music.register_channel("vfxC","sfx", False)
    renpy.music.register_channel("vfxR","sfx", False)

    renpy.music.set_pan(-0.8, 0, 'vfxL')
    renpy.music.set_pan(0,0, 'vfxC')
    renpy.music.set_pan(0.8,0,'vfxR')


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

#Assets personnages
image mother:
    "images/Personnages/mother.png"
    zoom 0.35

image delaunay_neutre:
    "images/Personnages/delaunay_neutre.png"
    zoom 0.35

image leandre_neutre:
    "images/Personnages/leandre_neutre.png"
    zoom 0.35

image gatsby_neutre:
    "images/Personnages/gatsby_neutre.png"
    zoom 0.35

image aimee_neutre:
    "images/Personnages/aimee_neutre.png"
    zoom 0.35

image peacock_neutre:
    "images/Personnages/peacock_neutre.png"
    zoom 0.35

image imani_neutre:
    "images/Personnages/imani_neutre.png"
    zoom 0.35

#Assets backgrounds
image devanture = "Backgrounds/devanture.png"

image auditorium = "Backgrounds/auditorium.png"

image bar = "Backgrounds/bar.png"

image loges: 
    "Backgrounds/loges.png"
    zoom 1.02

image rideau = "Backgrounds/rideau.png"

image balcon = "Backgrounds/balcon.png"

image wip = "images/WIP.png"
#vfx

image curtain : 
    "images/VFX/Curtain_Close/Curtain_Close_00000.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00001.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00002.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00003.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00004.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00005.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00006.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00007.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00008.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00009.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00010.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00011.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00012.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00013.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00014.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00015.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00016.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00017.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00018.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00019.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00020.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00021.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00022.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00023.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00024.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00025.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00026.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00027.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00028.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00029.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00030.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00031.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00032.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00033.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00034.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00035.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00036.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00037.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00038.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00039.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00040.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00041.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00042.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00043.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00044.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00045.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00046.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00047.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00048.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00049.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00050.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00051.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00052.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00053.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00054.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00055.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00056.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00057.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00000.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00001.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00002.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00003.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00004.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00005.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00006.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00007.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00008.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00009.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00010.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00011.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00012.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00013.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00014.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00015.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00016.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00017.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00018.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00019.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00020.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00021.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00022.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00023.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00024.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00025.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00026.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00027.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00028.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00029.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00030.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00031.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00032.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00033.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00034.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00035.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00036.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00037.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00038.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00039.png", 0.04,
    "images/Backgrounds/transparent_background.png"
    
    

image curtain_open:
    "images/VFX/Curtain_Open/Curtain_Open_00000.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00001.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00002.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00003.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00004.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00005.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00006.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00007.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00008.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00009.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00010.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00011.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00012.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00013.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00014.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00015.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00016.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00017.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00018.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00019.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00020.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00021.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00022.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00023.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00024.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00025.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00026.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00027.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00028.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00029.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00030.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00031.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00032.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00033.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00034.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00035.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00036.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00037.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00038.png", 0.04,
    "images/VFX/Curtain_Open/Curtain_Open_00039.png", 0.04,
    "images/Backgrounds/transparent_background.png"
    



image curtain_close :
    "images/VFX/Curtain_Close/Curtain_Close_00000.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00001.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00002.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00003.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00004.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00005.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00006.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00007.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00008.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00009.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00010.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00011.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00012.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00013.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00014.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00015.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00016.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00017.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00018.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00019.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00020.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00021.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00022.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00023.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00024.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00025.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00026.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00027.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00028.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00029.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00030.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00031.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00032.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00033.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00034.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00035.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00036.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00037.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00038.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00039.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00040.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00041.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00042.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00043.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00044.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00045.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00046.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00047.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00048.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00049.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00050.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00051.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00052.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00053.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00054.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00055.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00056.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Close_00057.png", 0.04,
    "images/Backgrounds/transparent_background.png"



image flirt = Animation(
    "images/VFX/Flirt/Flirt_00001.png", 0.03,
    "images/VFX/Flirt/Flirt_00002.png", 0.03,
    "images/VFX/Flirt/Flirt_00003.png", 0.03,
    "images/VFX/Flirt/Flirt_00004.png", 0.03,
    "images/VFX/Flirt/Flirt_00005.png", 0.03,
    "images/VFX/Flirt/Flirt_00006.png", 0.03,
    "images/VFX/Flirt/Flirt_00007.png", 0.03,
    "images/VFX/Flirt/Flirt_00008.png", 0.03,
    "images/VFX/Flirt/Flirt_00009.png", 0.03,
    "images/VFX/Flirt/Flirt_00010.png", 0.03,
    "images/VFX/Flirt/Flirt_00011.png", 0.03,
    "images/VFX/Flirt/Flirt_00012.png", 0.03,
    "images/VFX/Flirt/Flirt_00013.png", 0.03,
    "images/VFX/Flirt/Flirt_00014.png", 0.03,
    "images/VFX/Flirt/Flirt_00015.png", 0.03,
    "images/VFX/Flirt/Flirt_00016.png", 0.03,
    "images/VFX/Flirt/Flirt_00017.png", 0.03,
    "images/VFX/Flirt/Flirt_00018.png", 0.03,
    "images/VFX/Flirt/Flirt_00019.png", 0.03,
    "images/VFX/Flirt/Flirt_00020.png", 0.03,
    "images/VFX/Flirt/Flirt_00021.png", 0.03,
    "images/VFX/Flirt/Flirt_00022.png", 0.03,
    "images/VFX/Flirt/Flirt_00023.png", 0.03,
    "images/VFX/Flirt/Flirt_00024.png", 0.03,
    "images/VFX/Flirt/Flirt_00025.png", 0.03,
    "images/VFX/Flirt/Flirt_00026.png", 0.03,
    "images/VFX/Flirt/Flirt_00027.png", 0.03,
    "images/VFX/Flirt/Flirt_00028.png", 0.03,
    "images/VFX/Flirt/Flirt_00029.png", 0.03,
    "images/VFX/Flirt/Flirt_00030.png", 0.03,
    "images/VFX/Flirt/Flirt_00031.png", 0.03,
    "images/VFX/Flirt/Flirt_00032.png", 0.03,
    "images/VFX/Flirt/Flirt_00033.png", 0.03,
    "images/VFX/Flirt/Flirt_00034.png", 0.03,
    "images/VFX/Flirt/Flirt_00035.png", 0.03,
    "images/VFX/Flirt/Flirt_00036.png", 0.03,
    "images/VFX/Flirt/Flirt_00037.png", 0.03,
    "images/VFX/Flirt/Flirt_00038.png", 0.03,
    "images/VFX/Flirt/Flirt_00039.png", 0.03,
    "images/VFX/Flirt/Flirt_00040.png", 0.03,
    "images/VFX/Flirt/Flirt_00041.png", 0.03,
    "images/VFX/Flirt/Flirt_00042.png", 0.03,
    "images/VFX/Flirt/Flirt_00043.png", 0.03,
    "images/VFX/Flirt/Flirt_00044.png", 0.03,
    "images/VFX/Flirt/Flirt_00045.png", 0.03,
    "images/VFX/Flirt/Flirt_00046.png", 0.03,
    "images/VFX/Flirt/Flirt_00047.png", 0.03,
    "images/VFX/Flirt/Flirt_00048.png", 0.03,
    "images/VFX/Flirt/Flirt_00049.png", 0.03,
    "images/VFX/Flirt/Flirt_00050.png", 0.03,
    "images/VFX/Flirt/Flirt_00051.png", 0.03,
    "images/VFX/Flirt/Flirt_00052.png", 0.03,
    "images/VFX/Flirt/Flirt_00053.png", 0.03,
    "images/VFX/Flirt/Flirt_00054.png", 0.03,
    "images/VFX/Flirt/Flirt_00055.png", 0.03,
    "images/VFX/Flirt/Flirt_00056.png", 0.03,
    "images/VFX/Flirt/Flirt_00057.png", 0.03,
    "images/VFX/Flirt/Flirt_00058.png", 0.03,
    "images/VFX/Flirt/Flirt_00059.png", 0.03,
    "images/VFX/Flirt/Flirt_00060.png", 0.03,
    "images/VFX/Flirt/Flirt_00061.png", 0.03,
    "images/VFX/Flirt/Flirt_00062.png", 0.03,
    "images/VFX/Flirt/Flirt_00063.png", 0.03,
    "images/VFX/Flirt/Flirt_00064.png", 0.03,
    "images/VFX/Flirt/Flirt_00065.png", 0.03,
    "images/VFX/Flirt/Flirt_00066.png", 0.03,
    "images/VFX/Flirt/Flirt_00067.png", 0.03,
    "images/VFX/Flirt/Flirt_00068.png", 0.03,
    "images/VFX/Flirt/Flirt_00069.png", 0.03,
    "images/VFX/Flirt/Flirt_00070.png", 0.03,
    "images/VFX/Flirt/Flirt_00071.png", 0.03,
    "images/VFX/Flirt/Flirt_00072.png", 0.03,
    "images/VFX/Flirt/Flirt_00073.png", 0.03,
    "images/VFX/Flirt/Flirt_00074.png", 0.03
)

image angry = Animation(
    "images/VFX/Angry/Angry_00001.png", 0.03,
    "images/VFX/Angry/Angry_00002.png", 0.03,
    "images/VFX/Angry/Angry_00003.png", 0.03,
    "images/VFX/Angry/Angry_00004.png", 0.03,
    "images/VFX/Angry/Angry_00005.png", 0.03,
    "images/VFX/Angry/Angry_00006.png", 0.03,
    "images/VFX/Angry/Angry_00007.png", 0.03,
    "images/VFX/Angry/Angry_00008.png", 0.03,
    "images/VFX/Angry/Angry_00009.png", 0.03,
    "images/VFX/Angry/Angry_00010.png", 0.03,
    "images/VFX/Angry/Angry_00011.png", 0.03,
    "images/VFX/Angry/Angry_00012.png", 0.03,
    "images/VFX/Angry/Angry_00013.png", 0.03,
    "images/VFX/Angry/Angry_00014.png", 0.03,
    "images/VFX/Angry/Angry_00015.png", 0.03,
    "images/VFX/Angry/Angry_00016.png", 0.03,
    "images/VFX/Angry/Angry_00017.png", 0.03,
    "images/VFX/Angry/Angry_00018.png", 0.03,
    "images/VFX/Angry/Angry_00019.png", 0.03,
    "images/VFX/Angry/Angry_00020.png", 0.03,
    "images/VFX/Angry/Angry_00021.png", 0.03,
    "images/VFX/Angry/Angry_00022.png", 0.03,
    "images/VFX/Angry/Angry_00023.png", 0.03,
    "images/VFX/Angry/Angry_00024.png", 0.03,
    "images/VFX/Angry/Angry_00025.png", 0.03,
    "images/VFX/Angry/Angry_00026.png", 0.03,
    "images/VFX/Angry/Angry_00027.png", 0.03,
    "images/VFX/Angry/Angry_00028.png", 0.03,
    "images/VFX/Angry/Angry_00029.png", 0.03,
    "images/VFX/Angry/Angry_00030.png", 0.03,
    "images/VFX/Angry/Angry_00031.png", 0.03,
    "images/VFX/Angry/Angry_00032.png", 0.03,
    "images/VFX/Angry/Angry_00033.png", 0.03,
    "images/VFX/Angry/Angry_00034.png", 0.03,
    "images/VFX/Angry/Angry_00035.png", 0.03,
    "images/VFX/Angry/Angry_00036.png", 0.03,
    "images/VFX/Angry/Angry_00037.png", 0.03,
    "images/VFX/Angry/Angry_00038.png", 0.03,
    "images/VFX/Angry/Angry_00039.png", 0.03,
    "images/VFX/Angry/Angry_00040.png", 0.03,
    "images/VFX/Angry/Angry_00041.png", 0.03,
    "images/VFX/Angry/Angry_00042.png", 0.03,
    "images/VFX/Angry/Angry_00043.png", 0.03,
)


image joy = Animation(
    "images/VFX/Joy/Joy_00001.png", 0.06,
    "images/VFX/Joy/Joy_00002.png", 0.06,
    "images/VFX/Joy/Joy_00003.png", 0.06,
    "images/VFX/Joy/Joy_00004.png", 0.06,
    "images/VFX/Joy/Joy_00005.png", 0.06,
    "images/VFX/Joy/Joy_00006.png", 0.06,
    "images/VFX/Joy/Joy_00007.png", 0.06,
    "images/VFX/Joy/Joy_00008.png", 0.06,
    "images/VFX/Joy/Joy_00009.png", 0.06,
    "images/VFX/Joy/Joy_00010.png", 0.06,
    "images/VFX/Joy/Joy_00011.png", 0.06,
    "images/VFX/Joy/Joy_00012.png", 0.06,
    "images/VFX/Joy/Joy_00013.png", 0.06,
    "images/VFX/Joy/Joy_00014.png", 0.06,
    "images/VFX/Joy/Joy_00015.png", 0.06,
    "images/VFX/Joy/Joy_00016.png", 0.06,
    "images/VFX/Joy/Joy_00017.png", 0.06,
    "images/VFX/Joy/Joy_00018.png", 0.06,
    "images/VFX/Joy/Joy_00019.png", 0.06
)

image sadness = Animation(
    "images/VFX/Sadness/Sadness_00001.png", 0.05,
    "images/VFX/Sadness/Sadness_00002.png", 0.05,
    "images/VFX/Sadness/Sadness_00003.png", 0.05,
    "images/VFX/Sadness/Sadness_00004.png", 0.05,
    "images/VFX/Sadness/Sadness_00005.png", 0.05,
    "images/VFX/Sadness/Sadness_00006.png", 0.05,
    "images/VFX/Sadness/Sadness_00007.png", 0.05,
    "images/VFX/Sadness/Sadness_00008.png", 0.05,
    "images/VFX/Sadness/Sadness_00009.png", 0.05,
    "images/VFX/Sadness/Sadness_00010.png", 0.05,
    "images/VFX/Sadness/Sadness_00011.png", 0.05,
    "images/VFX/Sadness/Sadness_00012.png", 0.05,
    "images/VFX/Sadness/Sadness_00013.png", 0.05,
    "images/VFX/Sadness/Sadness_00014.png", 0.05,
    "images/VFX/Sadness/Sadness_00015.png", 0.05,
    "images/VFX/Sadness/Sadness_00016.png", 0.05,
    "images/VFX/Sadness/Sadness_00017.png", 0.05,
    "images/VFX/Sadness/Sadness_00018.png", 0.05,
    "images/VFX/Sadness/Sadness_00019.png", 0.05,
    "images/VFX/Sadness/Sadness_00020.png", 0.05,
    "images/VFX/Sadness/Sadness_00021.png", 0.05,
    "images/VFX/Sadness/Sadness_00022.png", 0.05,
    "images/VFX/Sadness/Sadness_00023.png", 0.05,
    "images/VFX/Sadness/Sadness_00024.png", 0.05,
    "images/VFX/Sadness/Sadness_00025.png", 0.05,
    "images/VFX/Sadness/Sadness_00026.png", 0.05,
    "images/VFX/Sadness/Sadness_00027.png", 0.05,
    "images/VFX/Sadness/Sadness_00028.png", 0.05,
    "images/VFX/Sadness/Sadness_00029.png", 0.05,
    "images/VFX/Sadness/Sadness_00030.png", 0.05,
    "images/VFX/Sadness/Sadness_00031.png", 0.05,
    "images/VFX/Sadness/Sadness_00032.png", 0.05,
    "images/VFX/Sadness/Sadness_00033.png", 0.05,
    "images/VFX/Sadness/Sadness_00034.png", 0.05,
    "images/VFX/Sadness/Sadness_00035.png", 0.05,
    "images/VFX/Sadness/Sadness_00036.png", 0.05,
    "images/VFX/Sadness/Sadness_00037.png", 0.05,
    "images/VFX/Sadness/Sadness_00038.png", 0.05,
    "images/VFX/Sadness/Sadness_00039.png", 0.05,
    "images/VFX/Sadness/Sadness_00040.png", 0.05,
    "images/VFX/Sadness/Sadness_00041.png", 0.05,
    "images/VFX/Sadness/Sadness_00042.png", 0.05,
    "images/VFX/Sadness/Sadness_00043.png", 0.05,
    "images/VFX/Sadness/Sadness_00044.png", 0.05,
    "images/VFX/Sadness/Sadness_00045.png", 0.05,
    "images/VFX/Sadness/Sadness_00046.png", 0.05,
    "images/VFX/Sadness/Sadness_00047.png", 0.05,
    "images/VFX/Sadness/Sadness_00048.png", 0.05,
    "images/VFX/Sadness/Sadness_00049.png", 0.05,
    "images/VFX/Sadness/Sadness_00050.png", 0.05,
    "images/VFX/Sadness/Sadness_00051.png", 0.05,
    "images/VFX/Sadness/Sadness_00052.png", 0.05,
    "images/VFX/Sadness/Sadness_00053.png", 0.05,
    "images/VFX/Sadness/Sadness_00054.png", 0.05,
    "images/VFX/Sadness/Sadness_00055.png", 0.05,
    "images/VFX/Sadness/Sadness_00056.png", 0.05,
    "images/VFX/Sadness/Sadness_00057.png", 0.05,
    "images/VFX/Sadness/Sadness_00058.png", 0.05,
    "images/VFX/Sadness/Sadness_00059.png", 0.05,
    "images/VFX/Sadness/Sadness_00060.png", 0.05,
    "images/VFX/Sadness/Sadness_00061.png", 0.05,
    "images/VFX/Sadness/Sadness_00062.png", 0.05,
    "images/VFX/Sadness/Sadness_00063.png", 0.05,
    "images/VFX/Sadness/Sadness_00064.png", 0.05,
    "images/VFX/Sadness/Sadness_00065.png", 0.05,
    "images/VFX/Sadness/Sadness_00066.png", 0.05,
    "images/VFX/Sadness/Sadness_00067.png", 0.05,
    "images/VFX/Sadness/Sadness_00068.png", 0.05,
    "images/VFX/Sadness/Sadness_00069.png", 0.05,
    "images/VFX/Sadness/Sadness_00070.png", 0.05,
    "images/VFX/Sadness/Sadness_00071.png", 0.05,
    "images/VFX/Sadness/Sadness_00072.png", 0.05,
    "images/VFX/Sadness/Sadness_00073.png", 0.05,
    "images/VFX/Sadness/Sadness_00074.png", 0.05
)

    
image sparkling_click = Animation(
    "images/VFX/Sparkling Click/Stars_00001.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00002.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00003.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00004.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00005.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00006.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00007.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00008.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00009.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00010.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00011.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00012.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00013.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00014.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00015.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00016.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00017.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00018.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00019.png", 0.03,
    "images/VFX/Sparkling Click/Stars_00020.png", 0.03,
)

image light_solo_left:
    "VFX/LightSoloLeft/LightSoloLeft_00001.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00002.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00003.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00004.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00005.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00006.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00007.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00008.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00009.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00010.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00011.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00012.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00013.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00014.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00015.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00016.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00017.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00018.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00019.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00020.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00021.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00022.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00023.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00024.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00025.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00026.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00027.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00028.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00029.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00030.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00031.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00032.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00033.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00034.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00035.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00036.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00037.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00038.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00039.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00040.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00041.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00042.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00043.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00044.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00045.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00046.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00047.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00048.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00049.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00050.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00051.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00052.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00053.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00054.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00055.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00056.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00057.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00058.png"
    pause 0.03
    "VFX/LightSoloLeft/LightSoloLeft_00059.png"
    pause 0.03
    repeat

image light_solo_middle:
    "VFX/LightSoloMiddle/LightSoloMiddle_00001.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00002.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00003.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00004.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00005.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00006.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00007.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00008.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00009.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00010.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00011.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00012.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00013.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00014.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00015.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00016.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00017.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00018.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00019.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00020.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00021.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00022.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00023.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00024.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00025.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00026.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00027.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00028.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00029.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00030.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00031.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00032.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00033.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00034.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00035.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00036.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00037.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00038.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00039.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00040.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00041.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00042.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00043.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00044.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00045.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00046.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00047.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00048.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00049.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00050.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00051.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00052.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00053.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00054.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00055.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00056.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00057.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00058.png"
    pause 0.03
    "VFX/LightSoloMiddle/LightSoloMiddle_00059.png"
    pause 0.03
    repeat


image light_solo_right:
    "VFX/LightSoloRight/LightSoloRight_00001.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00002.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00003.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00004.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00005.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00006.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00007.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00008.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00009.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00029.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00030.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00031.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00032.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00033.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00034.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00035.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00036.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00037.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00038.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00039.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00040.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00041.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00042.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00043.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00044.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00045.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00046.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00047.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00048.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00049.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00050.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00051.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00052.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00053.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00054.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00055.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00056.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00057.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00058.png"
    pause 0.03
    "VFX/LightSoloRight/LightSoloRight_00059.png"
    pause 0.03
    repeat


init python:

    del_right = Transform(
        zoom=0.86,       
        xalign=0.78,
        yanchor=1.0,
        ypos=1.0,
        xzoom=1
    )

    del_left = Transform(
        zoom=0.86,
        xalign=0.23,
        yanchor=1.0,
        ypos=1.0,
        xzoom=-1
    )

    del_center = Transform(
        zoom=0.86,
        xalign=0.47,
        yanchor=1.0,
        ypos=1.0,
        xzoom=1
    )

    gat_right = Transform(
        zoom=0.89,
        xalign=0.85,
        yanchor=1.0,
        ypos=1.0,
        xzoom=1
    )

    gat_left = Transform(
        zoom=0.89,
        xalign=0.18,
        yanchor=1.0,
        ypos=1.0,
        xzoom=-1
    )

    gat_center = Transform(
        zoom=0.89,
        xalign=0.5,
        yanchor=1.0,
        ypos=1.0,
        xzoom=1
    )

    pea_right = Transform(
        zoom=0.987,
        xalign=0.88,
        yanchor=1.0,
        ypos=1.02,
        xzoom=1
    )

    pea_left = Transform(
        zoom=0.987,
        xalign=0.2,
        yanchor=1.0,
        ypos=1.02,
        xzoom=-1
    )

    pea_center = Transform(
        zoom=0.987,
        xalign=0.5,
        yanchor=1.0,
        ypos=1.02,
        xzoom=1
    )

    mother_right = Transform(
        zoom=0.985,
        xalign=0.88,
        yanchor=1.0,
        ypos=1.09,
        xzoom=1
    )

    mother_left = Transform(
        zoom=0.985,
        xalign=0.15,
        yanchor=1.0,
        ypos=1.09,
        xzoom=-1
    )

    mother_center = Transform(
        zoom=0.985,
        xalign=0.54,
        yanchor=1.0,
        ypos=1.09,
        xzoom=1
    )

    flirt_center = Transform(
        zoom=0.80,
        xalign=0.54,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    flirt_right = Transform(
        zoom=0.80,
        xalign=1.55,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    flirt_left = Transform(
        zoom=0.80,
        xalign=-0.5,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    sadness_center = Transform(
        zoom=0.80,
        xalign=0.4,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    sadness_right = Transform(
        zoom=0.80,
        xalign=1.49,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    sadness_left = Transform(
        zoom=0.80,
        xalign=-0.5,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    sadness_pea_center = Transform(
        zoom=0.80,
        xalign=0.4,
        yanchor=1.0,
        ypos=0.65,
        xzoom=1
    )

    sadness_pea_right = Transform(
        zoom=0.80,
        xalign=1.49,
        yanchor=1.0,
        ypos=0.65,
        xzoom=1
    )

    sadness_pea_left = Transform(
        zoom=0.80,
        xalign=-0.35,
        yanchor=1.0,
        ypos=0.65,
        xzoom=1
    )

    angry_center = Transform(
        zoom=0.80,
        xalign=0.54,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    angry_right = Transform(
        zoom=0.80,
        xalign=1.55,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    angry_left = Transform(
        zoom=0.80,
        xalign=-0.5,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    joy_center = Transform(
        zoom=0.80,
        xalign=0.54,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    joy_right = Transform(
        zoom=0.80,
        xalign=1.55,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )

    joy_left = Transform(
        zoom=0.80,
        xalign=-0.5,
        yanchor=1.0,
        ypos=0.7,
        xzoom=1
    )


# Liste des sfx
define type_sounds = ['audio/SFX/TextMix-001.ogg','audio/SFX/TextMix-002.ogg','audio/SFX/TextMix-003.ogg','audio/SFX/TextMix-004.ogg','audio/SFX/TextMix-005.ogg','audio/SFX/TextMix-006.ogg','audio/SFX/TextMix-007.ogg','audio/SFX/TextMix-008.ogg','audio/SFX/TextMix-009.ogg','audio/SFX/TextMix-010.ogg']
define A_type_sounds = ['audio/SFX/AP_TA-001.ogg','audio/SFX/AP_TA-002.ogg','audio/SFX/AP_TA-003.ogg','audio/SFX/AP_TA-004.ogg','audio/SFX/AP_TA-005.ogg','audio/SFX/AP_TA-006.ogg']
define D_type_sounds = ['audio/SFX/AP_TL-001.ogg','audio/SFX/AP_TL-002.ogg','audio/SFX/AP_TL-003.ogg','audio/SFX/AP_TL-004.ogg','audio/SFX/AP_TL-005.ogg','audio/SFX/AP_TL-006.ogg']
define M_type_sounds = ['audio/SFX/AP_TM-001.ogg','audio/SFX/AP_TM-002.ogg','audio/SFX/AP_TM-003.ogg','audio/SFX/AP_TM-004.ogg','audio/SFX/AP_TM-005.ogg','audio/SFX/AP_TM-006.ogg']
define G_type_sounds = ['audio/SFX/AP_TG-001.ogg','audio/SFX/AP_TG-002.ogg','audio/SFX/AP_TG-003.ogg','audio/SFX/AP_TG-004.ogg','audio/SFX/AP_TG-005.ogg','audio/SFX/AP_TG-006.ogg']
define P_type_sounds = ['audio/SFX/AP_TP-001.ogg','audio/SFX/AP_TP-002.ogg','audio/SFX/AP_TP-003.ogg','audio/SFX/AP_TP-004.ogg','audio/SFX/AP_TP-005.ogg','audio/SFX/AP_TP-006.ogg']
define type_silent = ['<silence 1.0>']
define audio.IntroConstruction = 'audio/SFX/AP_SFX_Intro_Construction.ogg'
define audio.IntroRagots = 'audio/SFX/AP_SFX_Intro_Ragots.ogg'
define audio.IntroRoaring = 'audio/SFX/AP_SFX_Intro_Roaring20s.ogg'
define audio.IntroSmartphone = 'audio/SFX/AP_SFX_Intro_Roaring20s.ogg'
define audio.DoorAndrogame = 'audio/SFX/AP_SFX_Intro_DoorAndrogame.ogg'
define audio.ShortEllipse = 'audio/SFX/AP_SFX_Intro_Ellipse_V2.ogg'
define audio.LongEllipse = 'audio/SFX/AP_SFX_Intro_LongEllipse_V2.ogg'
define audio.Gribouillis = 'audio/SFX/AP_SFX_Gribouillis.ogg'
define audio.Corset = 'audio/SFX/AP_SFX_Corset.ogg'
define audio.GelCheveux = 'audio/SFX/AP_SFX_Intro_GelCheveux.ogg'
define audio.DoorLoges = 'audio/SFX/AP_SFX_Intro_DoorLoges.ogg'
define audio.VFXJoy = 'audio/SFX/AP_VFX_Joy.ogg'
define audio.VFXFlirt = 'audio/SFX/AP_VFX_Flirt.ogg'
define audio.VFXSadness = 'audio/SFX/AP_VFX_Sadness.ogg'
define audio.VFXAnger = 'audio/SFX/AP_VFX_Anger.ogg'
define audio.Gradient = 'audio/SFX/AP_VFX_Gradient_V2.ogg'

# SONS d'UI
# pour jouer aléatoirement un son de la liste : renpy.sound.play(renpy.random.choice(nomliste))
define ui_hover = ['audio/SFX/AP_UI_Hover-001.ogg','audio/SFX/AP_UI_Hover-002.ogg','audio/SFX/AP_UI_Hover-003.ogg','audio/SFX/AP_UI_Hover-004.ogg','audio/SFX/AP_UI_Hover-005.ogg','audio/SFX/AP_UI_Hover-006.ogg']
define ui_click = ['audio/SFX/AP_UI_Click-001.ogg','audio/SFX/AP_UI_Click-002.ogg','audio/SFX/AP_UI_Click-003.ogg','audio/SFX/AP_UI_Click-004.ogg','audio/SFX/AP_UI_Click-005.ogg','audio/SFX/AP_UI_Click-006.ogg']
define ui_back = ['audio/SFX/AP_UI_Back_V4-001.ogg','audio/SFX/AP_UI_Back_V4-002.ogg','audio/SFX/AP_UI_Back_V4-003.ogg','audio/SFX/AP_UI_Back_V4-004.ogg','audio/SFX/AP_UI_Back_V4-005.ogg','audio/SFX/AP_UI_Back_V4-006.ogg']

# Liste des ambiances
define audio.AmbAndrogameDay = "audio/Amb/Amb_CabaretDay_V3.ogg"
define audio.AmbLoges = "audio/Amb/Amb_LogesDay_V4.ogg"
define audio.AmbRue = "audio/Amb/Amb_Rue_V2.ogg"
define audio.AmbLogesNight = "audio/Amb/Amb_LogesNight_V3.ogg"
define audio.AmbDelShow = "audio/Amb/AP_Amb_ShowDel_V1.ogg"
define audio.BarDay = "audio/Amb/Amb_BarDay_V4.ogg"

# Liste des réactions de foule
define audio.CrowdDel1 = "audio/Amb/AP_Crowd_ShowDelSt1.ogg"
define audio.CrowdDel2 = "audio/Amb/AP_Crowd_ShowDelSt2.ogg"
define audio.CrowdDel3 = "audio/Amb/AP_Crowd_ShowDelSt3.ogg"
define audio.CrowdDel4 = "audio/Amb/AP_Crowd_ShowDelSt4.ogg"

# Liste des musiques
define audio.CabaretEntrance = "audio/Music/ON_CabaretEntrance_V1.ogg"
define audio.CabaretIntro = "audio/Music/ON_CabaretIntro_V1_.ogg"
define audio.CabaretLightVerse = "audio/Music/ON_CabaretLightVerse_V1.ogg"
define audio.CabaretLightChorus = "audio/Music/ON_CabaretLightChorus_V1.ogg"
define audio.CabaretLightSolo = "audio/Music/ON_CabaretLightSolo_V1.ogg"
define audio.BackstageSt1 = "audio/Music/AP_Stinger1_V1.ogg"
define audio.BackstageSt2 = "audio/Music/AP_Stinger2_V1.ogg"
define audio.BackstageSt3 = "audio/Music/AP_Stinger3_V1.ogg"
define audio.BackstageSt4 = "audio/Music/AP_Stinger4_V1.ogg"
define audio.BackstageLoop = "audio/Music/AP_LogesTruc_V1.ogg"
define audio.BackstageDrumLoop = "audio/Music/ON_BackStageLoop_V1.ogg"
define audio.BarMusic = "audio/Music/RUN_BarNeutral_V1.ogg"
define audio.ShowDelaunay = "audio/Music/AP_ShowDelaunay_V2.ogg"
define audio.ShowGatsby = "audio/Music/AP_ShowGatsby_V1.ogg"
define audio.ShowPeacock = "audio/Music/AP_ShowPeacock_V1.ogg"

# Déclarez les personnages utilisés dans le jeu.
define mother = Character('Mother', color="#b51963", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=30, callback=type_sound, cb_cps=30, cb_boopfile=M_type_sounds)
define anthrax = Character('Anthräx', color="#9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=35, callback=type_sound, cb_cps=35, cb_boopfile=A_type_sounds)
define delaunay = Character('Delaunay', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define gatsby = Character('Gatsby', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=G_type_sounds)
define peacock = Character('Peacock', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=P_type_sounds)  
define leandre = Character('Léandre', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define aimee = Character('Aimé.e', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=G_type_sounds)
define imani = Character('Imani', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=P_type_sounds)
define inconnu = Character('???', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=G_type_sounds)
define delinconnu = Character('Del?', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define player = Character('[player_name]', color="9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=A_type_sounds)
define staff = Character('Staff', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50)
define text = Character(color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)




label start:
    $ quick_menu = False
    scene black
    with fade
    stop music fadeout 1.0

    # Initialiser la variable utilisée dans l'écran d'input
    default temp_name = ""

    # Appelle l'écran personnalisé
    call screen name_input_screen
    $ player_name = temp_name.strip()

    if player_name == "":
        $ player_name = "Anthräx"

    if _preferences.language == "English":
        call screen name_confirm_screen(
        message="Would you keep [player_name] ?",
        yes_action=Jump("onboarding"),
        no_action=Jump("start"),
        style_prompt="confirm_prompt_text")

    else:
        call screen name_confirm_screen(
        message="Tu veux bien garder [player_name] ?",
        yes_action=Jump("onboarding"),
        no_action=Jump("start"),
        style_prompt="confirm_prompt_text")



    if yes_action:
        $ persistent.bg_parallax = True
        jump onboarding
    else:
        $ persistent.bg_parallax = False
        jump start



#0.1    
label onboarding:
    $ persistent.bg_parallax = True
    show devanture
    with fade
    $ quick_menu = True  

    play ambiance AmbRue fadein 0.5

    $ current_textbox = "description"

    text "L'Androgame..."

    play music IntroConstruction noloop
    text "Cela fait un moment maintenant qu'il a été reprit, et après de longs travaux, il fait à présent revivre le quartier comme je ne l'avais jamais vu auparavant."
    queue music IntroRagots noloop
    text "Et puis même au sein de la commu', ça a fait jaser. Toutes les têtes d'affiches sont queer."
    text "Ça fait presque bizarre de nous voir nous réapproprier une époque dans laquelle on n'avait pas le droit d'exister."
    text "Je suis sûr·e que l’on n’aurait jamais autant flamboyé que dans les années 20... C’est peut-être pour ça qu’on était \"interdit.e.s\" ?"
    queue music IntroRoaring noloop
    text "On aurait trop volé la vedette aux hétéros."
    text "Les plumes, la fourrure, les paillettes, le champagne, le charleston, l’occasionnel rail de coke... Les années folles quoi."
    text "C’est ce qui m’a motivé·e à me lancer dans le drag finalement..."
    text "J’ai toujours été intrigué·e par cette forme d’expression. Et à voir ces artistes bourré·e·s de talent faire leur show, à deux pas de chez moi..."
    text "J'ai commencé à me costumer en cachette dans mon appart, et pour être honnête, c'était peut-être pour le mieux."
    text "Mes premières tentatives de make-up étaient catastrophiques... Mais au fur et à mesure, j’ai pris le coup de pinceau."
    text "Ce que je pensais être une lubie est finalement devenu un hobby."
    queue music IntroSmartphone noloop
    text "Je faisais mon petit contenu sur les réseaux sociaux et continuais ma vie tranquillement à côté, en passant toujours devant L’Androgame pour aller au travail."
    text "Alors quand ils ont lancé des auditions pour agrandir la troupe, j'ai longuement hésité. Mais on n'a qu'une vie !"
    text "Je ne pensais pas être sélectionné·e ! Et encore moins passer un entretien avec Mother, la patronne du cabaret. "
    
    stop ambiance fadeout 1.0
    play music CabaretEntrance volume 0.7
    hide devanture
    scene black with fade
    show auditorium  with dissolve
    play sfx DoorAndrogame
    show mother at mother_center with dissolve



#0.2

    play ambiance AmbAndrogameDay fadein 0.5

    $ current_textbox = "mother"

    show joy at joy_center
    play vfxC VFXJoy
    mother "Bienvenue dans L'Androgame ! J'espère que tu as fait bonne route."
    hide joy with dissolve

    queue music CabaretIntro volume 0.7
    queue music CabaretLightVerse volume 0.7


    $ current_textbox = "description"

    #overlay description
    text "Une fois passée la porte pivotante, la hauteur sous plafond et les lustres géométriques faillirent me donner un torticolis. "
    text "Je devais presque plisser les yeux pour repérer tous les petits détails dans la marqueterie, les dorures et les reliefs dans le papier peint."
    # retirer overlay

    $ current_textbox = "anthrax"

    anthrax "Oui. Et puis, c’est le genre d’établissement qu’il est difficile de louper !"
    
    $ current_textbox = "mother"

    show joy at joy_center
    play vfxC VFXJoy
    mother "Aha ! Tu m’en vois ravie de l’entendre."
    hide joy with dissolve

    mother "Je ne vais pas te faire patienter plus longtemps... Commençons par te faire une petite visite des lieux. Promis, tu vas t’y retrouver bien vite."
    hide mother with dissolve

    show mother at mother_right with dissolve
    show joy at joy_right
    play vfxR VFXJoy
    mother "Nous voici donc dans l'auditorium !"
    hide joy with dissolve

    mother "Il sera un peu comme ton meilleur ennemi, car peu importe le trac ou qui se retrouvera dans le public, il faudra grimper sur les planches !"
   
    show joy at joy_right
    play vfxR VFXJoy
    mother "Après, si tu es ici aujourd’hui, c’est parce que c’est justement le genre de chose qui t’anime : te mettre en scène..."
    hide joy with dissolve

    stop music fadeout 5.0
    stop ambiance fadeout 5.0


#0.5
    hide auditorium 
    hide mother with dissolve
    scene black with fade

    play sfx LongEllipse volume 0.8
    
    $ current_textbox = "description" 

    text "Nous sommes monté·e·s sur la scène et l'avons traversée avant de passer derrière les épais rideaux de velours." 
    text "Les coulisses étaient un véritable dédale de couloirs tandis qu'elle ouvrait quelques portes et me présentait chaque pièce."
    text "Ici, la réserve des costumes; où les armatures de dos, de hanches, d'épaules à plumes d'autruche, de floss, d'oie ou de faisan;"
    text "Et les casques grandioses à strass, sequins, perles de verre ou fausses pierres précieuses, se faisaient la compétition." 
    text "Là, l'inventaire des décors roulants, barres de pole dance, accessoires de scène et de cirque pour les tours plus acrobatiques." 
    stop music fadeout 1.5
    play sfx DoorLoges
    text "Nous avons fini par pousser une dernière porte, celle des loges..."

    stop sfx fadeout 1.0
    
    show loges

    play ambiance AmbLoges fadein 1

    show imani_neutre at pea_left with dissolve

    $ current_textbox = "peacock"
    
    show angry at angry_left
    play vfxL VFXAnger
    imani "Ok, hear me out... Je dis simplement que si l'on veut garder une logique dans la suite de nos numéros, on va devoir inverser l'ordre dans lequel on passe..."
    hide angry with dissolve

    imani "Pour pouvoir faire de la place aux nouvelles !"
    
    $ current_textbox = "description"
    #ajouter un overlay entre la descri et le personnage
    play sfx Gribouillis
    text "L'homme qui venait de prendre la parole était en train de gribouiller avec insistance un croquis dans son carnet..."
    text "Une aiguille à coudre entre les lèvres et une pièce de tissu sur les genoux, à laquelle il semblait broder des sequins uns à uns."
    #retirer l'overlay

    $ current_textbox = "gatsby"

    show aimee_neutre at gat_right with dissolve
    inconnu "Girl... J'entends, et je suis d'accord sur le fond. Mais on ne les connaît même pas encore et on ne sait pas quels numéros iels vont présenter, ou si même iels en ont..."
    hide imani_neutre with dissolve
    
    show joy at joy_right
    play vfxR VFXJoy
    inconnu "Tu es en train de te faire des plans sur la comète, ma belle."
    hide joy

    $ current_textbox = "description"

    #ajouter un overlay entre la descri et le personnage
    play sfx GelCheveux
    text "Les doigts couverts de gel et un peigne à la main, la personne qui venait de lui répondre était en train de styliser une perruque noire de jais sur une tête de mannequin." 
    text "Iel y plaquait les cheveux contre le front en de jolies boucles bien définies, et y fixait des perles nacrées avec un pistolet à colle."
    #retirer l'overlay

    $ current_textbox = "gatsby"

    show aimee_neutre at gat_right  with dissolve

    inconnu "Et toi Del'? Qu'est-ce que tu en penses ?"

    $ current_textbox = "description"

    show leandre_neutre at del_left with dissolve
    #ajouter un overlay entre la descri et le personnage
    play sfx Corset
    text "Un autre garçon, plus silencieux, avait la tête baissée sur un corset tout de dentelle, qu'il laçait précautionneusement."
    hide aimee_neutre with dissolve 
    text "Relevant la tête, le concerné remarqua qu'iels n'étaient plus trois dans la pièce et me fixa un instant, avant de se retourner vers ses interlocuteur·ice·s."
    #retirer l'overlay
    

    $ current_textbox = "delaunay"

    show joy at joy_left
    play vfxL VFXJoy
    delinconnu "Je pense qu'on devrait leur demander directement..."
    hide joy
    
    delinconnu "Ou alors que ce serait justement l'occasion parfaite pour nous de revoir nos tours respectifs..." 
    

    stop music fadeout 1.0

    $ current_textbox = "description"

    show aimee_neutre at gat_right with dissolve
    show imani_neutre at pea_center with dissolve
    #ajouter un overlay entre la descri et le personnage
    text "Un court silence s'installa, tandis que nous nous regardions tous.te.s dans le blanc des yeux, ne sachant pas tellement qui devait prendre la parole et que dire." 
    #retirer l'overlay

    #possibilité de les retirer toustes en même temps?
    hide leandre_neutre with dissolve
    hide aimee_neutre with dissolve
    hide imani_neutre with dissolve

    show mother at mother_center with dissolve

    $ current_textbox = "mother"
    
    show joy at joy_center
    play vfxC VFXJoy
    mother "Bon ! Les filles, je vous présente [player_name], iel nous rejoindra sous peu, le temps d'arranger le spectacle, et je compte sur vous pour l'accueillir comme il se doit."
    hide joy
    hide mother with dissolve

    play music CabaretLightChorus volume 0.7

    $ current_textbox = "peacock"

    show imani_neutre at pea_right with dissolve
    imani "Pardon, on a dû te sembler super judgy avec notre absence de réaction ! Moi c'est Imani."

    show flirt at flirt_right
    play vfxR VFXFlirt
    imani "Parfois on s'appelle aussi par nos noms de scène, donc tu peux aussi m'appeler Peacock, si tu en as envie..."
    hide flirt

    $ current_textbox = "mother"
    
    show mother at mother_left with dissolve
    mother "Imani se spécialise dans tout ce qui est du ressort de la performance vocale. Lipsync, chant, reading, shading, imitation..."

    mother "Si tu as des conseils à aller chercher de ce côté, c'est vers elle."
    
    $ current_textbox = "peacock"

    imani "Ah oui ! Et pour les pronoms, tu peux utiliser ceux dont tu as envie, je ne suis pas très regardant. Je me genre moi-même souvent au féminin."
    hide imani_neutre with dissolve

    $ current_textbox = "mother"
    
    mother "Le petit timide là, qui essaye de faire en sorte de se faire oublier, c'est Léandre."

    $ current_textbox = "description"
    hide mother 
    #ajouter overlay
    show leandre_neutre at del_right with dissolve
    text "Prit en flagrant délit, le jeune homme tourna au pivoine et balbutia, mal à l'aise."
    #retirer overlay

    $ current_textbox = "delaunay"
    
    leandre "N-Non ! C'est juste que... J'ai toujours un peu de mal avec les nouvelles personnes. Excuse-moi..."
    show flirt at flirt_right
    play vfxR VFXFlirt
    leandre "Oui, donc moi, c'est Léandre, j'utilise il/lui, et je fais principalement de l'effeuillage burlesque. C'est assez classique..."
    hide flirt

    $ current_textbox = "gatsby"
    show aimee_neutre at gat_left with dissolve
    show joy at joy_left
    play vfxL VFXJoy
    inconnu "C'est tout sauf classique, ton striptease !"
    hide joy
    
    $ current_textbox = "description"

    show angry at angry_right
    play vfxR VFXAnger
    text "Léandre se renfrogna davantage. Apparement, les deux étaient suffisamment bon·ne·s ami·e·s pour se taquiner et s'embarasser ainsi."
    hide angry
    hide leandre_neutre with dissolve

    $ current_textbox = "gatsby"

    gatsby "Du coup, vu qu'on doit toujours parler à sa place, son nom de drag est Delaunay."
    show joy at joy_left
    play vfxL VFXJoy
    gatsby "Et moi c'est Gatsby ! Parce que je suis magnifique, et que je n'avais pas plus d'inspi que ça au moment de choisir."
    hide joy
    gatsby "Je me genre au neutre, c'est à dire avec ellui/iel. C'est non-négociable.~"
    show flirt at flirt_left
    play vfxL VFXFlirt
    aimee "Mais mon vrai prénom, c'est Aimé.e. Bien trouvé, non?"
    hide flirt
    hide aimee_neutre with dissolve
    
    stop ambiance fadeout 1
    stop music fadeout 2.0
    jump route_choice_intro



label route_choice_intro:
    show loges 
    show mother at mother_center
    $ current_textbox = "mother"
    mother "Alors [player_name], si tu devais choisir l'un de mes \"babies\" comme marrain ou parraine, qui est-ce que tu désignerais ?" with fade
    hide loges 
    hide devanture 
    hide mother with dissolve
    stop music fadeout 0.1
    $ _window_hide()
    $ renpy.pause(0, hard=True)
    $ quick_menu = False
    jump choose_route
    with fade
    pause 2.0
