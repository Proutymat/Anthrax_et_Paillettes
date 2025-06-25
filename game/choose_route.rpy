init python:

    import random

    ui_hover = [
        "audio/SFX/AP_UI_Hover-001.ogg",
        "audio/SFX/AP_UI_Hover-002.ogg",
        "audio/SFX/AP_UI_Hover-003.ogg",
        "audio/SFX/AP_UI_Hover-004.ogg",
        "audio/SFX/AP_UI_Hover-005.ogg",
        "audio/SFX/AP_UI_Hover-006.ogg",
    ]

    ui_click = [
        "audio/SFX/AP_UI_Click-001.ogg",
        "audio/SFX/AP_UI_Click-002.ogg",
        "audio/SFX/AP_UI_Click-003.ogg",
        "audio/SFX/AP_UI_Click-004.ogg",
        "audio/SFX/AP_UI_Click-005.ogg",
        "audio/SFX/AP_UI_Click-006.ogg",
    ]

    ui_back = [
        "audio/SFX/AP_UI_Back_V4-001.ogg",
        "audio/SFX/AP_UI_Back_V4-002.ogg",
        "audio/SFX/AP_UI_Back_V4-003.ogg",
        "audio/SFX/AP_UI_Back_V4-004.ogg",
        "audio/SFX/AP_UI_Back_V4-005.ogg",
        "audio/SFX/AP_UI_Back_V4-006.ogg",
    ]

    def play_ui_hover():
        renpy.play(random.choice(ui_hover), channel="sound")

    def play_ui_click():
        renpy.play(random.choice(ui_click), channel="sound")

    def play_ui_back():
        renpy.play(random.choice(ui_back), channel="sound")

define audio.CrushChoice = "audio/Music/AP_CrushChoice.ogg"

label route_return:
    scene black
    with fade
    $ renpy.pause(0.1)
    jump choose_route

default hovered_character = None

transform fade_vfx:
    alpha 0.0
    linear 0.2 alpha 1.0

define short_fade = Fade(0.1, 1, 0.2)

label choose_route:
    scene black
    play music CrushChoice
     
    if _preferences.language == "English":
        show expression "images/Backgrounds/crush_choice_background_eng.png"

    else : 
        show expression "images/Backgrounds/crush_choice_background_fr.png"
        
    $ persistent.bg_parallax = False
    $ quick_menu = False

    window hide

    call screen route_choice_buttons

    return


screen route_choice_buttons():
    modal True

    fixed:

        # === VFX arrière-plan selon le crush en hover ===
        if hovered_character == "delaunay":
            add "light_solo_left" at fade_vfx
        elif hovered_character == "gatsby":
            add "light_solo_middle" at fade_vfx
        elif hovered_character == "peacock":
            add "light_solo_right" at fade_vfx


        # === HBOX avec boutons ===
        hbox:
            xalign 0.52
            yalign 0.5
            offset (0, 30)
            spacing 30

            # -- Delaunay --
            imagebutton:
                auto "images/routes/delaunay_route_%s.png"
                hovered SetVariable("hovered_character", "delaunay")
                unhovered SetVariable("hovered_character", None)
                action [Function(play_ui_click), Show("crush_confirm", name="Léandre", destination="delaunay_start")]

            # -- Gatsby --
            imagebutton:
                auto "images/routes/gatsby_route_%s.png"
                hovered SetVariable("hovered_character", "gatsby")
                unhovered SetVariable("hovered_character", None)
                action [Function(play_ui_click), Show("crush_confirm", name="Aimé.e", destination="gatsby_start")]

            # -- Peacock --
            imagebutton:
                auto "images/routes/peacock_route_%s.png"
                hovered SetVariable("hovered_character", "peacock")
                unhovered SetVariable("hovered_character", None)
                action [Function(play_ui_click), Show("crush_confirm", name="Imani", destination="peacock_start")]
