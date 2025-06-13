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

#vfx



image curtain_open = Animation(
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
    "images/VFX/Curtain_Open/Curtain_Open_00039.png", 0.04
)


image curtain_close = Animation(
    "images/VFX/Curtain_Close/Curtain_Clone_00022.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00023.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00024.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00025.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00026.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00027.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00028.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00029.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00030.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00031.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00032.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00033.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00034.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00035.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00036.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00037.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00038.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00039.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00040.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00041.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00042.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00043.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00044.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00045.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00046.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00047.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00048.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00049.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00050.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00051.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00052.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00053.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00054.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00055.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00056.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00057.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00058.png", 0.04,
    "images/VFX/Curtain_Close/Curtain_Clone_00059.png", 0.04
)


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
    "images/VFX/Joy/Joy_00001.png", 0.04,
    "images/VFX/Joy/Joy_00002.png", 0.04,
    "images/VFX/Joy/Joy_00003.png", 0.04,
    "images/VFX/Joy/Joy_00004.png", 0.04,
    "images/VFX/Joy/Joy_00005.png", 0.04,
    "images/VFX/Joy/Joy_00006.png", 0.04,
    "images/VFX/Joy/Joy_00007.png", 0.04,
    "images/VFX/Joy/Joy_00008.png", 0.04,
    "images/VFX/Joy/Joy_00009.png", 0.04,
    "images/VFX/Joy/Joy_00010.png", 0.04,
    "images/VFX/Joy/Joy_00011.png", 0.04,
    "images/VFX/Joy/Joy_00012.png", 0.04,
    "images/VFX/Joy/Joy_00013.png", 0.04,
    "images/VFX/Joy/Joy_00014.png", 0.04,
    "images/VFX/Joy/Joy_00015.png", 0.04,
    "images/VFX/Joy/Joy_00016.png", 0.04,
    "images/VFX/Joy/Joy_00017.png", 0.04,
    "images/VFX/Joy/Joy_00018.png", 0.04,
    "images/VFX/Joy/Joy_00019.png", 0.04,
    "images/VFX/Joy/Joy_00020.png", 0.04,
    "images/VFX/Joy/Joy_00021.png", 0.04,
    "images/VFX/Joy/Joy_00022.png", 0.04,
    "images/VFX/Joy/Joy_00023.png", 0.04,
    "images/VFX/Joy/Joy_00024.png", 0.04,
    "images/VFX/Joy/Joy_00025.png", 0.04,
    "images/VFX/Joy/Joy_00026.png", 0.04,
    "images/VFX/Joy/Joy_00027.png", 0.04,
    "images/VFX/Joy/Joy_00028.png", 0.04,
    "images/VFX/Joy/Joy_00029.png", 0.04,
    "images/VFX/Joy/Joy_00030.png", 0.04,
    "images/VFX/Joy/Joy_00031.png", 0.04,
    "images/VFX/Joy/Joy_00032.png", 0.04,
    "images/VFX/Joy/Joy_00033.png", 0.04,
    "images/VFX/Joy/Joy_00034.png", 0.04,
    "images/VFX/Joy/Joy_00035.png", 0.04,
    "images/VFX/Joy/Joy_00036.png", 0.04,
    "images/VFX/Joy/Joy_00037.png", 0.04,
    "images/VFX/Joy/Joy_00038.png", 0.04,
    "images/VFX/Joy/Joy_00039.png", 0.04,
    "images/VFX/Joy/Joy_00040.png", 0.04,
    "images/VFX/Joy/Joy_00041.png", 0.04,
    "images/VFX/Joy/Joy_00042.png", 0.04,
    "images/VFX/Joy/Joy_00043.png", 0.04,
    "images/VFX/Joy/Joy_00044.png", 0.04,
    "images/VFX/Joy/Joy_00045.png", 0.04,
    "images/VFX/Joy/Joy_00046.png", 0.04,
    "images/VFX/Joy/Joy_00047.png", 0.04,
    "images/VFX/Joy/Joy_00048.png", 0.04,
    "images/VFX/Joy/Joy_00049.png", 0.04,
    "images/VFX/Joy/Joy_00050.png", 0.04,
    "images/VFX/Joy/Joy_00051.png", 0.04,
    "images/VFX/Joy/Joy_00052.png", 0.04,
    "images/VFX/Joy/Joy_00053.png", 0.04,
    "images/VFX/Joy/Joy_00054.png", 0.04,
    "images/VFX/Joy/Joy_00055.png", 0.04,
    "images/VFX/Joy/Joy_00056.png", 0.04,
    "images/VFX/Joy/Joy_00057.png", 0.04,
    "images/VFX/Joy/Joy_00058.png", 0.04,
    "images/VFX/Joy/Joy_00059.png", 0.04,
    "images/VFX/Joy/Joy_00060.png", 0.04,
    "images/VFX/Joy/Joy_00061.png", 0.04,
    "images/VFX/Joy/Joy_00062.png", 0.04,
    "images/VFX/Joy/Joy_00063.png", 0.04,
    "images/VFX/Joy/Joy_00064.png", 0.04,
    "images/VFX/Joy/Joy_00065.png", 0.04
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
define A_type_sounds = ['audio/SFX/AP_TA-001.ogg','audio/SFX/AP_TA-002.ogg','audio/SFX/AP_TA-003.ogg','audio/SFX/AP_TA-004.ogg']
define D_type_sounds = ['audio/SFX/AP_T1-001.ogg','audio/SFX/AP_T1-002.ogg','audio/SFX/AP_T1-003.ogg','audio/SFX/AP_T1-004.ogg']
define M_type_sounds = ['audio/SFX/AP_T2-001.ogg','audio/SFX/AP_T2-002.ogg','audio/SFX/AP_T2-003.ogg','audio/SFX/AP_T2-004.ogg']
define G_type_sounds = ['audio/SFX/AP_T3-001.ogg','audio/SFX/AP_T3-002.ogg','audio/SFX/AP_T3-003.ogg','audio/SFX/AP_T3-004.ogg'] 
define P_type_sounds = ['audio/SFX/AP_T4-001.ogg','audio/SFX/AP_T4-002.ogg','audio/SFX/AP_T4-003.ogg','audio/SFX/AP_T4-004.ogg']
define type_silent = ['<silence 1.0>']

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
define audio.GoodVibeIntro = "audio/Music/ON_GoodVibeIntro_V2.ogg"
define audio.IntroGoodVibe1 = "audio/Music/ON_GoodVibeA_V2.ogg"
define audio.IntroGoodVibe2 = "audio/Music/ON_GoodVibeB_V2.ogg"
define audio.IntroGoodVibe3 = "audio/Music/AP_IntroGoodVib3_V1.ogg"
define audio.IntroGoodVibe4 = "audio/Music/AP_IntroGoodVib4_V1.ogg"
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
define inconnu = Character('???', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50)
define delinconnu = Character('Del?', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define player = Character('[player_name]', color="9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define staff = Character('Staff', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50)
define text = Character(color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)




label start:
    $ quick_menu = False
    scene black
    with fade

    # Initialiser la variable utilisée dans l'écran d'input
    default temp_name = ""

    # Appelle l'écran personnalisé
    call screen name_input_screen
    $ player_name = temp_name.strip()

    if player_name == "":
        $ player_name = "Anthräx"

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

    play ambiance AmbRue fadein 5.0

    $ current_textbox = "description"



    text "L'androgame..."
    text "C’est dingue à quel point ce cabaret a reprit ses lettres de noblesse."
    text "Je me souviens encore de quand je passais devant pour aller prendre le métro... Complètement défraichit, la pierre sale et les fenètres brisées."
    text "On se demandait quand est-ce qu’ils finiraient par abréger ses souffrances et le démolir."
    text "Cela fait un moment maintenant qu’il a été reprit, et après de longs et nombreux travaux, il fait à présent revivre le quartier comme je ne l’ai jamais vu auparavant."
    text "Il me décroche toujours un sourire quand je passe devant..."
    text "Et puis même au sein de la commu’, ça a fait jaser. Toutes les têtes d’affiches sont queer."
    text "Ça fait presque bizarre de nous voir se réapproprier une époque dans laquelle on n’avait pas le droit de réellement exister."
    text "Je suis sûr.e qu’on n’aurait jamais autant flamboyé que dans les années 20... C’est peut-être pour ça qu’on était \"interdits\"? On aurait trop volé la vedette aux hétéros."
    text "Les plumes, la fourrure, les paillettes, le champagne, le charleston, l’occasionnel rail de coke... Les années folles quoi."
    text "C’est ce qui m’a motivé à me lancer dans le drag finalement..."
    text "J’ai toujours été intrigué.e par cette forme d’expression. Et à voir ces artistes bourré.e.s de talent faire leur show, à deux pas de chez moi... Je me suis laissé.e tenter."
    text "Au début, j’en avais un peu honte. Je me costumais en cachette dans mon appart, et pour être honnête, c’était peut-être pour le mieux."
    text "Mes premières tentatives de make-up étaient catastrophiques... Mais au fur et à mesure, j’ai pris le coup de pinceau."
    text "Ce que je pensais être une lubie est finalement devenu un hobby."
    text "J’ai pris des classes pour apprendre à coudre et danser, au point où même mes ami.e.s ont capté ce qui se tramait et se sont prêté.e.s au jeu pour m’aider à m’améliorer."
    text "Puis j’ai créé des comptes dédiés à ma pratique sur les réseaux sociaux. Et là, tout est devenu plus sérieux..."
    text "Je faisais mon petit contenu et continuait ma vie tranquillement à côté, en passant toujours devant l’Androgame pour aller au travail."
    text "Alors quand ils ont lancé des auditions pour agrandir la troupe, j’ai longuement hésité. Je ne me sentais pas légitime de rentrer dans cette sphère."
    text "Je ne savais pas comment j’allais pouvoir concilier le burlesque et le travail, ce qu’on pourrait dire de moi ou juger de mon drag."
    text "Je pense que j’ai décidé d’arrêter d’essayer de me justifier à un moment, lorsque j’étais aux portes du bâtiment. Après tout, je n’avais rien à perdre et j’aurais regretté de ne pas avoir au moins essayé."
    text "Je ne pensais pas être sélectionné.e, encore moins de passer un entretien avec Mother, la patronne du cabaret. Je n’ai pas trop compris, mais elle m’a parlé des règles de conduite au sein de la troupe et envers les clients, puis d’une période d’essai..."
    text "J’avais du mal à réaliser, mais on a convenu d’une nouvelle date d’entretien, en journée quand le cabaret serait vide, où elle m’expliquerait plus en détails le fonctionnement des backstages."

    stop ambiance fadeout 1.0
    play music CabaretEntrance volume 0.7
    hide devanture
    show auditorium  with dissolve
    show mother at mother_center with dissolve


#0.2

    play ambiance AmbAndrogameDay fadein 0.5

    $ current_textbox = "anthrax"

    mother "Bienvenue dans l'Androgame! J'espère que tu as fait bonne route."


    queue music CabaretIntro volume 0.7
    queue music CabaretLightVerse volume 0.7


    mother "Tu avais l’air de dire dans nos échanges que tu n’habitais pas trop loin, le chemin n’a pas dû être bien  compliqué."

    $ current_textbox = "description"

    text "En effet, une fois passée la porte pivotante, la hauteur sous plafond et les lustres géométriques faillirent me donner un torticolis."
    text "Je devais presque plisser les yeux pour repérer tous les petits détails dans la marqueterie, les dorures et les formes dans le papier peint."

    $ current_textbox = "anthrax"

    anthrax "Oui. Et puis, c’est le genre d’établissement qu’il est difficile de louper!"

    mother "Aha! Tu m’en vois ravie de l’entendre."
    mother "Je ne fais pas te faire patienter plus longtemps... Commençons par te faire une petite visite des lieux. Promis, tu vas t’y retrouver bien vite"

    queue music CabaretLightChorus volume 0.7

    mother "En arrivant, tu es passé.e par le lobby, le hall d’entrée, l’accueil... Tu peux l’appeler comme tu veux. Mais dans l’idée, passé ce guichet, les clients payent!"
    mother "Ce n’est pas trop dans notre politique cette histoire du \"le client est roi\", mais tu apprendras vite que c’est là que les pourboires se cachent"

    mother "Et nous voici donc dans l’auditorium! Il sera un peu comme ton meilleur ennemi, car peu importe le trac ou qui se retrouvera dans le public, il faudra grimper sur les planches!"
   
    mother "Après, si tu es ici aujourd’hui, c’est par ce que c’est justement le genre de chose qui t’anime: te mettre en scène..."
    
    $ current_textbox = "description"

    text "Je ne l’avais pas encore abordé de cette perspective, mais l’idée d’être au milieu de cette scène, avec tous les regards tournés vers moi, m’excitait autant que me faisait appréhender."
    text "Je mis cette pensée sur le compte de l'inexpérience, et continua ma visite avec Mother"

    hide mother 

    stop ambiance fadeout 10.0


#0.5
    hide auditorium 
    show loges 
    with fade
    queue music CabaretLightSolo volume 0.7

    show mother at mother_right  with dissolve


    text "Nous sommes monté.e.s sur la scène et l'avons traversée avant de passer derrière les épais rideaux de velours. Nous sommes passé.e.s dans un véritable dédale de couloirs tandis qu'elle ouvrait quelques portes et m'expliquait la fonction de chaque pièce." 
    text "Ici, la réserve des costumes ; où les armatures de dos, de hanches, d'épaules à plumes d'autruche, de floss, d'oie ou de faisan ; et les casques grandioses à strass, sequins, perles de verre ou fausses pierres précieuses, se faisaient la compétition." 
    text "Là, l'inventaire des décors roulants, barres de pole dance, accessoires de scène et de cirque pour les tours plus acrobatiques." 
    text "Déjà que je ne savais pas encore vers quelle pratique je souhaitais me spécialiser, submergé.e par tout ceci, j'en étais d'autant plus perdu.e..."
    stop music fadeout 1.5
    text "Nous avons fini par pousser une dernière porte, celle des loges et avons été accueilli.e.s par une ambiance des plus..."
    text "Studieuse."
    
    play ambiance AmbLoges fadein 1
    play music BackstageDrumLoop volume 0.5

    show imani_neutre at pea_left  with dissolve

    $ current_textbox = "anthrax"

    imani "Ok, hear me out... Je dis simplement que si l'on veut garder une logique dans la suite de nos numéros, on va devoir inverser l'ordre dans lequel on passe pour pouvoir faire de la place aux nouvelles."

    $ current_textbox = "description"

    text "L'homme qui venait de prendre la parole était en train de gribouiller avec insistance un schéma dans son carnet, une aiguille à coudre entre les lèvres et une pièce de tissu sur les genoux, à laquelle il semblait broder des sequins un à un."

    $ current_textbox = "anthrax"

    inconnu "Girl... J'entends, et je suis d'accord sur le fond. Mais on ne les connaît même pas encore et on ne sait pas quels numéros iels vont présenter, ou si même iels en ont... Tu es en train de te faire des plans sur la comète, ma belle."

    $ current_textbox = "description"

    text "Les doigts couverts de gel et un peigne à la main, la personne qui venait de lui répondre était en train de styliser une perruque noire de jais sur une tête de mannequin en plastique." 
    text "Iel y plaquait les cheveux contre le front en de jolies boucles bien définies, et y fixait des perles nacrées avec un pistolet à colle." 
    text "Un autre garçon, plus silencieux, avait la tête baissée sur une armature de fils de fer artisanale qu'il pliait à l'aide d'une pince, et bloquait fermement avec du chaterton."
    
    hide mother 
    show aimee_neutre at gat_right  with dissolve

    $ current_textbox = "anthrax"

    inconnu "Et toi Del'? Qu'est-ce que tu en penses?"

    $ current_textbox = "description"

    text "Relevant la tête, le concerné remarqua qu'iels n'étaient plus trois dans la pièce et me fixa un instant, avant de se retourner vers ses interlocuteur.ice.s."

    hide imani_neutre 
    show leandre_neutre at del_left  with dissolve

    delinconnu "Je pense qu'on devrait leur demander directement..." 

    $ current_textbox = "description"

    text "Les deux autres se sont retourné.e.s vers l'encadrement de porte dans lequel nous nous tenions, Mother et moi." 

    $ current_textbox = "anthrax"
    
    delinconnu "Ou alors que ce serait justement l'occasion parfaite pour nous de revoir nos propres tours..." 

    stop music fadeout 1.0

    anthrax "Un court silence s'est installé, tandis que nous nous regardions dans le blanc des yeux, ne sachant pas tellement qui devait prendre la parole et que dire."

    hide aimee_neutre 
    hide leandre_neutre 
    show mother at mother_center  with dissolve

    mother "Oh! Je vois que vous faites connaissance! Les filles, je vous présente [player_name], iel nous rejoindra sous peu le temps d'arranger le spectacle, et je compte sur vous pour l'acceuillir comme il se doit."

    play music CabaretLightChorus volume 0.7

    anthrax "Semblant sortir de leur torpeur et reprendre leurs esprits, les artistes drag face à moi me sourirent et commencèrent à faire un tour des présentations."
    
    hide mother 
    show imani_neutre at pea_center with dissolve

    peacock "Pardon, on a dû te sembler hyper antipathiques avec notre absence de réaction! Moi c'est Imani. Parfois on s'appelle aussi par nos noms de scène, donc tu peux aussi m'appeler Peacock si tu en as envie."
    
    hide imani_neutre 
    show mother at mother_center with dissolve

    mother "Imani se spécialise dans tout ce qui est du ressort de la performance vocale. Lipsync, chant, reading, shading, imitation... Si tu as des conseils de ce côté à aller chercher, c'est vers elle."
    
    hide mother 
    show imani_neutre at pea_center with dissolve

    peacock "Ah oui! Et pour les pronoms, tu peux utiliser ceux dont tu as envie, je ne suis pas très regardant. Je me genre moi-même souvent au féminin."
    
    hide imani_neutre 
    show mother at mother_center with dissolve

    mother "Le petit timide là, qui essaye de faire en sorte de se faire oublier, c'est Léandre."

    $ current_textbox = "description"
    
    text "Prit en flagrant délit, le jeune homme tourna au pivoine et balbutia, mal à l'aise."
    
    hide mother 
    show leandre_neutre at del_center with dissolve

    $ current_textbox = "anthrax"
    
    leandre "N-Non! C'est juste que... J'ai toujours un peu de mal avec les nouvelles personnes. Excuse-moi... Oui, donc moi, c'est Léandre, j'utilise il/lui, et je fais principalement de l'effeuillage burlesque. C'est assez classique..."
    
    hide leandre_neutre 
    show aimee_neutre at gat_center with dissolve
    
    inconnu "C'est tout sauf classique, ton striptease!"
    
    $ current_textbox = "description"

    text "Léandre se renfrogna davantage. Apparemment, les deux étaient suffisamment bon.ne.s ami.e.s pour se taquiner et s'embarrasser ainsi."
    
    $ current_textbox = "anthrax"

    gatsby "Du coup, vu qu'on doit toujours parler à sa place, son nom de drag est Delaunay. Et moi c'est Gatsby! "
    gatsby "Parce que je suis magnifique, et que je n'avais pas plus d'inspi que ça au moment de choisir. Je me genre au neutre, c'est à dire avec ellui/iel. "
    gatsby "C'est non-négociable. "
    gatsby "Mais mon vrai prénom, c'est Aimé.e, avec un point. Pareil que Pea, tu peux aussi m'appeler comme ça si tu en as envie."
    
    stop ambiance fadeout 1
    stop music fadeout 2.0
    hide aimee_neutre 
    jump route_choice_intro





label route_choice_intro:
    show loges 
    show mother at mother_right 
    mother "Alors [player], si tu devais choisir l'un de mes \"babies\" comme marrain ou parraine, qui est-ce que tu désignerais ?" with fade
    hide loges 
    hide devanture 
    hide mother 
    stop music fadeout 0.1
    $ _window_hide()
    $ renpy.pause(0, hard=True)
    $ quick_menu = False
    jump choose_route
    with fade
    pause 2.0
