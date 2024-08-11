@namespace
class SpriteKind:
    porta = SpriteKind.create()
    armadilha = SpriteKind.create()
    perigo = SpriteKind.create()
    danger = SpriteKind.create()
    venenosa = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_locked_north,
    on_overlap_tile)

def on_up_pressed():
    animation.run_image_animation(pacman,
        [img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . f f f f f f f . . . . .
            . . . f 5 5 5 f f f 5 f . . . .
            . . f 5 1 f 5 f f f 5 5 f . . .
            . f 5 5 f f 5 5 5 5 5 5 5 f . .
            . f 5 5 5 5 5 5 5 5 5 5 5 f . .
            . f 5 5 5 5 5 5 5 5 5 5 5 f . .
            . f 5 5 5 5 5 5 5 5 5 5 5 f . .
            . f 5 5 5 5 5 5 5 5 5 5 5 f . .
            . f 5 5 5 5 5 5 5 5 5 5 5 f . .
            . f 5 5 5 5 5 5 5 5 5 5 5 f . .
            . . f 5 5 5 5 5 5 5 5 5 f . . .
            . . . f 5 5 5 5 5 5 5 f . . . .
            . . . . f f f f f f f . . . . .
            . . . . . . . . . . . . . . . .
        """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile2(sprite2, location2):
    pacman.say("errou")
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.green_switch_up,
    on_overlap_tile2)

def on_on_overlap(sprite3, otherSprite):
    pacman.destroy()
    game.over(False)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_overlap_tile3(sprite4, location3):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_locked_west,
    on_overlap_tile3)

def on_left_pressed():
    animation.run_image_animation(pacman,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . f 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 1 f 5 5 5 5 5 5 5 5 f . 
                        . . f 5 f f 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . . f f f 5 5 5 5 5 5 5 5 5 f . 
                        . . f f f 5 5 5 5 5 5 5 5 5 f . 
                        . . f f f 5 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . . . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . . . f 5 5 5 5 5 5 5 f . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile4(sprite5, location4):
    jato2.destroy()
    pacman.say("você destrancou a porta", 200)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.green_switch_down,
    on_overlap_tile4)

def on_overlap_tile5(sprite6, location5):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_locked_south,
    on_overlap_tile5)

def on_right_pressed():
    animation.run_image_animation(pacman,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . f 5 5 5 5 5 5 5 5 f 1 5 f . . 
                        . f 5 5 5 5 5 5 5 5 f f 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 f f f . . 
                        . f 5 5 5 5 5 5 5 5 5 f f f . . 
                        . f 5 5 5 5 5 5 5 5 5 f f f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(pacman,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . f 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 5 5 5 5 5 f f 5 5 f . 
                        . . . f 5 5 f f f 5 f 1 5 f . . 
                        . . . . f 5 f f f 5 5 5 f . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_overlap_tile6(sprite7, location6):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_locked_east,
    on_overlap_tile6)

def on_overlap_tile7(sprite8, location7):
    pacman.say("essa alavanca n funciona", 200)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.purple_switch_up,
    on_overlap_tile7)

def on_overlap_tile8(sprite9, location8):
    if pacman.overlaps_with(jato2):
        jato2.say("ache a chave")
    else:
        game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile8)

projeto: Sprite = None
projectile: Sprite = None
jato2: Sprite = None
pacman: Sprite = None
pacman = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . f f f f f f f . . . . . 
            . . . f 5 5 5 5 5 5 5 f . . . . 
            . . f 5 5 5 5 5 5 5 5 5 f . . . 
            . f 5 5 5 5 5 5 5 f 1 5 5 f . . 
            . f 5 5 5 5 5 5 5 f f 5 5 f . . 
            . f 5 5 5 5 5 5 5 5 5 5 f f . . 
            . f 5 5 5 5 5 5 5 5 5 f f f . . 
            . f 5 5 5 5 5 5 5 5 5 f f f . . 
            . f 5 5 5 5 5 5 5 5 5 5 f f . . 
            . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
            . . f 5 5 5 5 5 5 5 5 5 f . . . 
            . . . f 5 5 5 5 5 5 5 f . . . . 
            . . . . f f f f f f f . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(pacman, 70, 70)
jato2 = sprites.create(img("""
        8 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
            8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 
            8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 
            8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 
            8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 
            8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 
            8 7 7 7 7 f f f f f 7 7 7 7 7 9 
            8 7 7 7 f f f f f f f 7 7 7 7 9 
            8 7 7 f f f f f f f f f 7 7 7 9 
            8 7 7 f f f f f f f f f 7 7 7 9 
            8 7 c c c c c c c c c c c 7 7 9 
            8 7 7 b b b b b b b b b 7 7 7 9 
            8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 
            8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 
            8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 
            8 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    """),
    SpriteKind.porta)
jato2.set_position(232, 8)
tiles.set_tilemap(tilemap("""
    level1
"""))
bola_de_fogo = sprites.create(img("""
        b b b b b b b b b b b b b b b b 
            b b 4 4 4 4 4 4 4 4 4 4 4 b b b 
            b 4 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
            b 4 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
            b 4 4 4 c c c c c c c 4 4 4 4 b 
            b 4 4 4 c f d f d f c 4 4 4 4 b 
            b 4 4 4 c f 2 f 2 f c 4 4 4 4 b 
            b 4 4 4 c f d f d f c 4 4 4 4 b 
            b 4 4 4 c f 2 f 2 f c 4 4 4 4 b 
            b 4 4 4 c f d f d f c 4 4 4 4 b 
            b 4 4 4 c c c c c c c 4 4 4 4 b 
            b 4 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
            b 4 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
            b 4 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
            b b b 4 4 4 4 4 4 4 4 4 4 b b b 
            b b b b b b b b b b b b b b b b
    """),
    SpriteKind.armadilha)
bola_de_fogo.set_position(360, 424)
tiles.place_on_random_tile(pacman, sprites.dungeon.stair_ladder)
gosma = sprites.create(img("""
        b b b b b b b b b b b b b b b b 
            b b 7 7 7 7 7 7 7 7 7 7 7 b b b 
            b 7 7 7 7 7 7 7 7 7 7 7 7 7 7 b 
            b 7 7 7 7 7 7 7 7 7 7 7 7 7 7 b 
            b 7 7 7 c c c c c c c 7 7 7 7 b 
            b 7 7 7 c f d f d f c 7 7 7 7 b 
            b 7 7 7 c f 2 f 2 f c 7 7 7 7 b 
            b 7 7 7 c f d f d f c 7 7 7 7 b 
            b 7 7 7 c f 2 f 2 f c 7 7 7 7 b 
            b 7 7 7 c f d f d f c 7 7 7 7 b 
            b 7 7 7 c c c c c c c 7 7 7 7 b 
            b 7 7 7 7 7 7 7 7 7 7 7 7 7 7 b 
            b 7 7 7 7 7 7 7 7 7 7 7 7 7 7 b 
            b 7 7 7 7 7 7 7 7 7 7 7 7 7 7 b 
            b b b 7 7 7 7 7 7 7 7 7 7 b b b 
            b b b b b b b b b b b b b b b b
    """),
    SpriteKind.enemy)
gosma.set_position(200, 490)
scene.camera_follow_sprite(pacman)
choque = sprites.create(img("""
        b b b b b b b b b b b b b b b b 
            b b 5 5 5 5 5 5 5 5 5 5 5 b b b 
            b 5 5 5 5 5 5 5 5 5 5 5 5 5 5 b 
            b 5 5 5 5 5 5 5 5 5 5 5 5 5 5 b 
            b 5 5 5 c c c c c c c 5 5 5 5 b 
            b 5 5 5 c f d f d f c 5 5 5 5 b 
            b 5 5 5 c f 2 f 2 f c 5 5 5 5 b 
            b 5 5 5 c f d f d f c 5 5 5 5 b 
            b 5 5 5 c f 2 f 2 f c 5 5 5 5 b 
            b 5 5 5 c f d f d f c 5 5 5 5 b 
            b 5 5 5 c c c c c c c 5 5 5 5 b 
            b 5 5 5 5 5 5 5 5 5 5 5 5 5 5 b 
            b 5 5 5 5 5 5 5 5 5 5 5 5 5 5 b 
            b 5 5 5 5 5 5 5 5 5 5 5 5 5 5 b 
            b b b 5 5 5 5 5 5 5 5 5 5 b b b 
            b b b b b b b b b b b b b b b b
    """),
    SpriteKind.perigo)
choque.set_position(232, 250)
bola_de_neve = sprites.create(img("""
        b b b b b b b b b b b b b b b b 
            b b 1 1 1 1 1 1 1 1 1 1 1 b b b 
            b 1 1 1 1 1 1 1 1 1 1 1 1 1 1 b 
            b 1 1 1 1 1 1 1 1 1 1 1 1 1 1 b 
            b 1 1 1 c c c c c c c 1 1 1 1 b 
            b 1 1 1 c f d f d f c 1 1 1 1 b 
            b 1 1 1 c f 2 f 2 f c 1 1 1 1 b 
            b 1 1 1 c f d f d f c 1 1 1 1 b 
            b 1 1 1 c f 2 f 2 f c 1 1 1 1 b 
            b 1 1 1 c f d f d f c 1 1 1 1 b 
            b 1 1 1 c c c c c c c 1 1 1 1 b 
            b 1 1 1 1 1 1 1 1 1 1 1 1 1 1 b 
            b 1 1 1 1 1 1 1 1 1 1 1 1 1 1 b 
            b 1 1 1 1 1 1 1 1 1 1 1 1 1 1 b 
            b b b 1 1 1 1 1 1 1 1 1 1 b b b 
            b b b b b b b b b b b b b b b b
    """),
    SpriteKind.danger)
bola_de_neve.set_position(38, 120)
aleatorio = sprites.create(img("""
        b b b b b b b b b b b b b b b b 
            b b 2 2 2 2 2 2 2 2 2 2 2 b b b 
            b 8 2 2 2 2 2 2 2 2 2 2 2 a a b 
            b 8 8 2 2 2 2 2 2 2 2 2 a a a b 
            b 8 8 8 c c c c c c c a a a a b 
            b 8 8 8 c f d f d f c a a a a b 
            b 8 8 8 c f 2 f 2 f c a a a a b 
            b 8 8 8 c f d f d f c a a a a b 
            b 8 8 8 c f 2 f 2 f c a a a a b 
            b 8 8 8 c f d f d f c a a a a b 
            b 8 8 8 c c c c c c c a a a a b 
            b 8 8 8 2 9 9 9 9 9 9 2 a a a b 
            b 8 8 2 9 9 9 9 9 9 9 9 2 a a b 
            b 8 2 9 9 9 9 9 9 9 9 9 9 2 a b 
            b b b 9 9 9 9 9 9 9 9 9 9 b b b 
            b b b b b b b b b b b b b b b b
    """),
    SpriteKind.venenosa)
aleatorio.set_position(152, 150)

def on_forever():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . 4 4 4 4 . . . . . . . . . 
                    5 5 5 2 2 2 4 4 . . . . . . . . 
                    5 2 2 2 2 1 2 4 . . . . . . . . 
                    5 5 2 2 2 1 2 4 4 . . . . . . . 
                    . 5 5 2 2 2 2 4 . . . . . . . . 
                    . . . 4 2 2 4 4 . . . . . . . . 
                    . . . . 4 4 4 . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        bola_de_fogo,
        85,
        0)
    pause(1000)
    projeto.set_velocity(85, 0)
forever(on_forever)

def on_forever2():
    global projeto
    projeto = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 8 8 8 8 . . . 
                    . . . . . . . . 8 8 9 9 9 8 8 8 
                    . . . . . . . . 8 9 1 9 9 9 9 8 
                    . . . . . . . 8 8 9 1 9 9 9 8 8 
                    . . . . . . . . 8 9 9 9 9 8 8 . 
                    . . . . . . . . 8 8 9 9 8 . . . 
                    . . . . . . . . . 8 8 8 . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        gosma,
        0,
        -25)
    projeto.set_velocity(-100, 0)
    pause(1000)
forever(on_forever2)

def on_forever3():
    global projeto
    projeto.set_velocity(-100, 0)
    pause(500)
    projeto = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 9 5 9 5 9 . . . . . . 
                    . . . . . 5 9 5 9 5 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 5 9 5 9 5 . . . . . . 
                    . . . . . 9 5 9 5 9 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        choque,
        0,
        100)
forever(on_forever3)

def on_forever4():
    global projeto
    projeto = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 9 9 9 9 9 9 9 . . . . . 
                    . . . 9 1 1 1 1 1 1 1 9 . . . . 
                    . . 9 1 1 1 1 1 1 d 1 1 9 . . . 
                    . 9 1 1 1 1 1 1 1 1 d 1 1 9 . . 
                    . 9 1 1 1 1 1 1 1 1 1 d 1 9 . . 
                    . 9 1 1 1 1 1 1 1 1 1 d 1 9 . . 
                    . 9 1 1 1 1 1 1 1 1 1 d 1 9 . . 
                    . 9 1 1 1 1 1 1 1 1 1 d 1 9 . . 
                    . 9 1 1 1 1 1 1 1 1 1 d 1 9 . . 
                    . 9 1 1 1 1 1 1 1 1 d 1 1 9 . . 
                    . . 9 1 1 1 1 1 1 d 1 1 9 . . . 
                    . . . 9 1 1 1 1 1 1 1 9 . . . . 
                    . . . . 9 9 9 9 9 9 9 . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        bola_de_neve,
        0,
        100)
    projeto.set_velocity(0, 100)
    pause(500)
forever(on_forever4)

def on_forever5():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . f 2 2 2 2 2 2 2 f . . . . 
                    . . f 2 2 2 2 2 2 2 2 2 f . . . 
                    . f 2 2 2 2 2 2 2 2 2 2 2 f . . 
                    . f 2 2 2 2 2 2 2 2 2 2 2 f . . 
                    . f 2 2 2 2 f f f 2 2 2 2 f . . 
                    . f f f f f f 1 f f f f f f . . 
                    . f 1 1 1 1 f f f 1 1 1 1 f . . 
                    . f 1 1 1 1 1 1 1 1 1 1 1 f . . 
                    . f 1 1 1 1 1 1 1 1 1 1 1 f . . 
                    . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . . f 1 1 1 1 1 1 1 f . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        aleatorio,
        0,
        100)
    projeto.set_velocity(0, 50)
    pause(500)
forever(on_forever5)
