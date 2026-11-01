namespace SpriteKind {
    export const porta = SpriteKind.create()
    export const armadilha = SpriteKind.create()
    export const perigo = SpriteKind.create()
    export const danger = SpriteKind.create()
    export const venenosa = SpriteKind.create()
    export const enemy = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorLockedNorth, function (sprite, location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.greenSwitchDown, function (sprite5, location4) {
    jato2.destroy()
    pacman.say("você destrancou a porta", 200)
})
// Lógica de Animação Fluida
forever(function () {
    if (controller.up.isPressed()) {
        animation.runImageAnimation(pacman, [img`
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
            `,img`
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
            `], 200, true)
    } else if (controller.down.isPressed()) {
        animation.runImageAnimation(pacman, [img`
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
            `,img`
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
            `], 200, true)
    } else if (controller.left.isPressed()) {
        animation.runImageAnimation(pacman, [img`
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
            `,img`
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
            `], 200, true)
    } else if (controller.right.isPressed()) {
        animation.runImageAnimation(pacman, [img`
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
            `,img`
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
            `], 200, true)
    } else {
        pacman.setImage(img`
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
            `)
    }
    pause(200)
})
let projectile: Sprite = null
let pacman: Sprite = null
pacman = sprites.create(img`
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
    `, SpriteKind.Player)
pacman.setBoundingBox(2, 2, 14, 14)
// Removido: controller.moveSprite(pacman, 70, 70)
// A movimentação agora é controlada via setVelocity no loop de atualização para permitir deslize

jato2 = sprites.create(img`
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
    `, SpriteKind.porta)
jato2.setPosition(232, 8)
tiles.setTilemap(tilemap`level1`)
let bola_de_fogo = sprites.create(img`
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
    `, SpriteKind.armadilha)
bola_de_fogo.setPosition(360, 424)
tiles.placeOnRandomTile(pacman, sprites.dungeon.stairLadder)
let gosma = sprites.create(img`
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
    `, SpriteKind.enemy)
gosma.setPosition(200, 490)
scene.cameraFollowSprite(pacman)
let choque = sprites.create(img`
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
    `, SpriteKind.perigo)
choque.setPosition(232, 250)
let bola_de_neve = sprites.create(img`
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
    `, SpriteKind.danger)
bola_de_neve.setPosition(38, 120)
let aleatorio = sprites.create(img`
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
    `, SpriteKind.venenosa)
aleatorio.setPosition(152, 150)
forever(function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, bola_de_fogo, 85, 0)
    projectile.setVelocity(85, 0)
    pause(1000)
})
forever(function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, gosma, 0, -25)
    projectile.setVelocity(-100, 0)
    pause(1000)
})
forever(function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        . . . . . . . . . . . . . . . . 
        `, choque, 0, 100)
    projectile.setVelocity(-100, 0)
    pause(500)
})
forever(function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, bola_de_neve, 0, 100)
    projectile.setVelocity(0, 100)
    pause(500)
})
forever(function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, aleatorio, 0, 100)
    projectile.setVelocity(0, 50)
    pause(500)
})
