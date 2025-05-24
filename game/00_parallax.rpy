#Parallaxe
init 800 python:

    class MouseParallax(renpy.Displayable):
        def __init__(self, layer_info):
            super(renpy.Displayable, self).__init__()
            self.xoffset, self.yoffset = 0.0, 0.0
            self.sort_layer = sorted(layer_info, reverse=True)
            cflayer = []
            masteryet = False

            for m, n in self.sort_layer:
                if (not masteryet) and (m < 41):
                    cflayer.append("master")
                    masteryet = True
                cflayer.append(n)

            if not masteryet:
                cflayer.append("master")

            cflayer.extend(["transient","characters","screens","overlay"])
            config.layers = cflayer
            config.overlay_functions.append(self.overlay)

            # Centrer au chargement sans attendre un mouvement souris
            import pygame
            self.event(pygame.event.Event(pygame.MOUSEMOTION),
                       config.screen_width // 2,
                       config.screen_height // 2,
                       0)

        def render(self, width, height, st, at):
            return renpy.Render(width, height)

        def parallax(self, m):
            func = renpy.curry(trans)(disp=self, m=m)
            return Transform(
            function=func,
            xpos=0.5, ypos=0.5,
            xanchor=0.5, yanchor=0.5
    )

        def overlay(self):
            ui.add(self)
            for m, n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)], n)

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.MOUSEMOTION:
                self.xoffset = (float(x) / config.screen_width) - 0.5
                self.yoffset = (float(y) / config.screen_height) - 0.5
            return

    MouseParallax([
        (30, "farback"),
        (20, "back"),
        (-20, "front"),
        (-30, "inyourface")
    ])

    def trans(d, st, at, disp=None, m=None):
        factor = 0.5  # Réduire l’intensité du mouvement
        d.xoffset = int(round(m * disp.xoffset * factor))
        d.yoffset = int(round(m * disp.yoffset * factor))
        return 0