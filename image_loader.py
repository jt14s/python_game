import pygame
from pygame.locals import *

#######################################################################################################
#Paladin character images #############################################################################
#######################################################################################################

#walk images
PaladinR1 = pygame.image.load('images/characters/paladin/walk/right/right1.png')
PaladinR2 = pygame.image.load('images/characters/paladin/walk/right/right2.png')
PaladinR3 = pygame.image.load('images/characters/paladin/walk/right/right3.png')

PaladinL1 = pygame.image.load('images/characters/paladin/walk/left/left1.png')
PaladinL2 = pygame.image.load('images/characters/paladin/walk/left/left2.png')
PaladinL3 = pygame.image.load('images/characters/paladin/walk/left/left3.png')

PaladinU1 = pygame.image.load('images/characters/paladin/walk/up/up1.png')
PaladinU2 = pygame.image.load('images/characters/paladin/walk/up/up2.png')
PaladinU3 = pygame.image.load('images/characters/paladin/walk/up/up3.png')
        
PaladinD1 = pygame.image.load('images/characters/paladin/walk/down/down1.png')
PaladinD2 = pygame.image.load('images/characters/paladin/walk/down/down2.png')
PaladinD3 = pygame.image.load('images/characters/paladin/walk/down/down3.png')

#attack images
PaladinAttackR1 = pygame.image.load('images/characters/paladin/attack/right/attack1.png')
PaladinAttackR2 = pygame.image.load('images/characters/paladin/attack/right/attack2.png')
PaladinAttackR3 = pygame.image.load('images/characters/paladin/attack/right/attack3.png')

PaladinAttackL1 = pygame.image.load('images/characters/paladin/attack/left/attack1.png')
PaladinAttackL2 = pygame.image.load('images/characters/paladin/attack/left/attack2.png')
PaladinAttackL3 = pygame.image.load('images/characters/paladin/attack/left/attack3.png')

PaladinAttackU1 = pygame.image.load('images/characters/paladin/attack/up/attack1.png')
PaladinAttackU2 = pygame.image.load('images/characters/paladin/attack/up/attack2.png')
PaladinAttackU3 = pygame.image.load('images/characters/paladin/attack/up/attack3.png')

PaladinAttackD1 = pygame.image.load('images/characters/paladin/attack/down/attack1.png')
PaladinAttackD2 = pygame.image.load('images/characters/paladin/attack/down/attack2.png')
PaladinAttackD3 = pygame.image.load('images/characters/paladin/attack/down/attack3.png')

#special images
PaladinAOE1 = pygame.image.load('images/characters/paladin/special/special1.png')
PaladinAOE2 = pygame.image.load('images/characters/paladin/special/special2.png')
PaladinAOE3 = pygame.image.load('images/characters/paladin/special/special3.png')
PaladinAOE4 = pygame.image.load('images/characters/paladin/special/special4.png')
PaladinAOE5 = pygame.image.load('images/characters/paladin/special/special5.png')
PaladinAOE6 = pygame.image.load('images/characters/paladin/special/special6.png')

#######################################################################################################
#Assasin character images #############################################################################
#######################################################################################################

#standing images
AssassinStandR = pygame.image.load('images/characters/assassin/walk/right/stand.png')
AssassinStandL = pygame.image.load('images/characters/assassin/walk/left/stand.png')
AssassinStandU = pygame.image.load('images/characters/assassin/walk/up/stand.png')


#walk images
AssassinR1 = pygame.image.load('images/characters/assassin/walk/right/right1.png')
AssassinR2 = pygame.image.load('images/characters/assassin/walk/right/right2.png')
AssassinR3 = pygame.image.load('images/characters/assassin/walk/right/right3.png')
AssassinR4 = pygame.image.load('images/characters/assassin/walk/right/right4.png')

AssassinL1 = pygame.image.load('images/characters/assassin/walk/left/left1.png')
AssassinL2 = pygame.image.load('images/characters/assassin/walk/left/left2.png')
AssassinL3 = pygame.image.load('images/characters/assassin/walk/left/left3.png')
AssassinL4 = pygame.image.load('images/characters/assassin/walk/left/left4.png')

AssassinU1 = pygame.image.load('images/characters/assassin/walk/up/up1.png')
AssassinU2 = pygame.image.load('images/characters/assassin/walk/up/up2.png')
AssassinU3 = pygame.image.load('images/characters/assassin/walk/up/up3.png')
AssassinU4 = pygame.image.load('images/characters/assassin/walk/up/up4.png')
        
AssassinD1 = pygame.image.load('images/characters/assassin/walk/down/down1.png')
AssassinD2 = pygame.image.load('images/characters/assassin/walk/down/down2.png')
AssassinD3 = pygame.image.load('images/characters/assassin/walk/down/down3.png')
AssassinD4 = pygame.image.load('images/characters/assassin/walk/down/down4.png')

#attack images
AssassinAttackR1 = pygame.image.load('images/characters/assassin/attack/right/attack1.png')
AssassinAttackR2 = pygame.image.load('images/characters/assassin/attack/right/attack2.png')
AssassinAttackR3 = pygame.image.load('images/characters/assassin/attack/right/attack3.png')

AssassinAttackL1 = pygame.image.load('images/characters/assassin/attack/left/attack1.png')
AssassinAttackL2 = pygame.image.load('images/characters/assassin/attack/left/attack2.png')
AssassinAttackL3 = pygame.image.load('images/characters/assassin/attack/left/attack3.png')

AssassinAttackU1 = pygame.image.load('images/characters/assassin/attack/up/attack1.png')
AssassinAttackU2 = pygame.image.load('images/characters/assassin/attack/up/attack2.png')
AssassinAttackU3 = pygame.image.load('images/characters/assassin/attack/up/attack3.png')

AssassinAttackD1 = pygame.image.load('images/characters/assassin/attack/down/attack1.png')
AssassinAttackD2 = pygame.image.load('images/characters/assassin/attack/down/attack2.png')
AssassinAttackD3 = pygame.image.load('images/characters/assassin/attack/down/attack3.png')

AssassinHitBoxH = pygame.image.load('images/characters/assassin/attack/assassin_hit_box_h.png')
AssassinHitBoxV = pygame.image.load('images/characters/assassin/attack/assassin_hit_box_v.png')

#######################################################################################################
#Mage character images ################################################################################
#######################################################################################################

#walk images
MageR1 = pygame.image.load('images/characters/mage/walk/right/stand.png')
MageR2 = pygame.image.load('images/characters/mage/walk/right/walk.png')

MageL1 = pygame.image.load('images/characters/mage/walk/left/stand.png')
MageL2 = pygame.image.load('images/characters/mage/walk/left/walk.png')

MageU1 = pygame.image.load('images/characters/mage/walk/up/stand.png')
MageU2 = pygame.image.load('images/characters/mage/walk/up/walk.png')

MageD1 = pygame.image.load('images/characters/mage/walk/down/stand.png')
MageD2 = pygame.image.load('images/characters/mage/walk/down/walk.png')

#attack images
MageAttackR1 = pygame.image.load('images/characters/mage/attack/right/attack1.png')
MageAttackR2 = pygame.image.load('images/characters/mage/attack/right/attack2.png')
MageAttackR3 = pygame.image.load('images/characters/mage/attack/right/attack3.png')

MageAttackL1 = pygame.image.load('images/characters/mage/attack/left/attack1.png')
MageAttackL2 = pygame.image.load('images/characters/mage/attack/left/attack2.png')
MageAttackL3 = pygame.image.load('images/characters/mage/attack/left/attack3.png')

MageAttackU1 = pygame.image.load('images/characters/mage/attack/up/attack1.png')
MageAttackU2 = pygame.image.load('images/characters/mage/attack/up/attack2.png')
MageAttackU3 = pygame.image.load('images/characters/mage/attack/up/attack3.png')

MageAttackD1 = pygame.image.load('images/characters/mage/attack/down/attack1.png')
MageAttackD2 = pygame.image.load('images/characters/mage/attack/down/attack2.png')
MageAttackD3 = pygame.image.load('images/characters/mage/attack/down/attack3.png')

#projectile images
MageProjectileR1 = pygame.image.load('images/characters/mage/attack/right/projectile1.png')
MageProjectileR2 = pygame.image.load('images/characters/mage/attack/right/projectile2.png')

MageProjectileL1 = pygame.image.load('images/characters/mage/attack/left/projectile1.png')
MageProjectileL2 = pygame.image.load('images/characters/mage/attack/left/projectile2.png')

MageProjectileU1 = pygame.image.load('images/characters/mage/attack/up/projectile1.png')
MageProjectileU2 = pygame.image.load('images/characters/mage/attack/up/projectile2.png')

MageProjectileD1 = pygame.image.load('images/characters/mage/attack/down/projectile1.png')
MageProjectileD2 = pygame.image.load('images/characters/mage/attack/down/projectile2.png')

#######################################################################################################
#Map Images ###########################################################################################
#######################################################################################################

#wall images
WallImg = pygame.image.load('images/level1/wallbrickpattern.png')

#floor images
FloorImgCenter = pygame.image.load('images/level1/floors/floortile/floortile1.png')
FloorImgTop = pygame.image.load('images/level1/floors/floortile/floortile2.png')
FloorImgRight = pygame.image.load('images/level1/floors/floortile/floortile3.png')
FloorImgLeft = pygame.image.load('images/level1/floors/floortile/floortile5.png')
FloorImgTopRight = pygame.image.load('images/level1/floors/floortile/floortile6.png')
FloorImgTopLeft = pygame.image.load('images/level1/floors/floortile/floortile9.png')
FloorImgVerticalTunnel = pygame.image.load('images/level1/floors/floortile/floortile11.png')
FloorImgTopDeadEnd = pygame.image.load('images/level1/floors/floortile/floortile12.png')

#roof images
RoofImgCenter = pygame.image.load('images/level1/rooftile/roof1.png')
RoofImgCenterCenter = pygame.image.load('images/level1/rooftile/roof12.png')

#torch images
TorchImg1 = pygame.image.load('images/level1/wall_torch/walltorch1.png')
TorchImg2 = pygame.image.load('images/level1/wall_torch/walltorch2.png')
TorchImg3 = pygame.image.load('images/level1/wall_torch/walltorch3.png')
TorchImg4 = pygame.image.load('images/level1/wall_torch/walltorch2.png')
TorchImg5 = pygame.image.load('images/level1/wall_torch/walltorch1.png')
TorchImg6 = pygame.image.load('images/level1/wall_torch/walltorch4.png')
TorchImg7 = pygame.image.load('images/level1/wall_torch/walltorch5.png')
TorchImg8 = pygame.image.load('images/level1/wall_torch/walltorch4.png')

#chasm images
ChasmImgBottom = pygame.image.load('images/level1/chasm/chasmbottom.png')
ChasmImgTop = pygame.image.load('images/level1/chasm/chasmtop.png')

#lockeddoor images
LockDoorVImg = pygame.image.load('images/level1/lockeddoor/lockvertical.png')
LockDoorHImg = pygame.image.load('images/level1/lockeddoor/lockhorizontal.png')

#######################################################################################################
#Item Images ##########################################################################################
#######################################################################################################

#items
HealthPotion = pygame.image.load('images/items/potions/healthpotion.png')
SpecialPotion = pygame.image.load('images/items/potions/specialpotion.png')
KeyImg = pygame.image.load('images/items/key/key.png')

#######################################################################################################
#HUD Images ###########################################################################################
#######################################################################################################
InvImg = pygame.image.load('images/interface/inventory.png')
UiImg = pygame.image.load('images/interface/hud.png')
HealthBar = pygame.image.load('images/interface/healthbar.png')
SpecialBar = pygame.image.load('images/interface/specialbar.png')

#######################################################################################################
#Enemy Images #########################################################################################
#######################################################################################################

#shrimp walk images
ShrimpWalkU1 = pygame.image.load('images/mobs/shrimp/walk/up/walk1.png')
ShrimpWalkU2 = pygame.image.load('images/mobs/shrimp/walk/up/walk2.png')

ShrimpWalkD1 = pygame.image.load('images/mobs/shrimp/walk/down/walk1.png')
ShrimpWalkD2 = pygame.image.load('images/mobs/shrimp/walk/down/walk2.png')

ShrimpWalkL1 = pygame.image.load('images/mobs/shrimp/walk/left/walk1.png')
ShrimpWalkL2 = pygame.image.load('images/mobs/shrimp/walk/left/walk2.png')

ShrimpWalkR1 = pygame.image.load('images/mobs/shrimp/walk/right/walk1.png')
ShrimpWalkR2 = pygame.image.load('images/mobs/shrimp/walk/right/walk2.png')

#shrimp aggro images
ShrimpAggroLeft1 = pygame.image.load('images/mobs/shrimp/walk/left/aggro1.png')
ShrimpAggroLeft2 = pygame.image.load('images/mobs/shrimp/walk/left/aggro2.png')

ShrimpAggroRight1 = pygame.image.load('images/mobs/shrimp/walk/right/aggro1.png')
ShrimpAggroRight2 = pygame.image.load('images/mobs/shrimp/walk/right/aggro2.png')

#cant see eyebrows when moving up so no need to use another image

ShrimpAggroDown1 = pygame.image.load('images/mobs/shrimp/walk/down/aggro1.png')
ShrimpAggroDown2 = pygame.image.load('images/mobs/shrimp/walk/down/aggro2.png')

#shrimp attack images
ShrimpAttackU1 = pygame.image.load('images/mobs/shrimp/attack/up/attack1.png')
ShrimpAttackU2 = pygame.image.load('images/mobs/shrimp/attack/up/attack2.png')
ShrimpAttackU3 = pygame.image.load('images/mobs/shrimp/attack/up/attack3.png')

ShrimpAttackD1 = pygame.image.load('images/mobs/shrimp/attack/down/attack1.png')
ShrimpAttackD2 = pygame.image.load('images/mobs/shrimp/attack/down/attack2.png')
ShrimpAttackD3 = pygame.image.load('images/mobs/shrimp/attack/down/attack3.png')

ShrimpAttackL1 = pygame.image.load('images/mobs/shrimp/attack/left/attack1.png')
ShrimpAttackL2 = pygame.image.load('images/mobs/shrimp/attack/left/attack2.png')
ShrimpAttackL3 = pygame.image.load('images/mobs/shrimp/attack/left/attack3.png')

ShrimpAttackR1 = pygame.image.load('images/mobs/shrimp/attack/right/attack1.png')
ShrimpAttackR2 = pygame.image.load('images/mobs/shrimp/attack/right/attack2.png')
ShrimpAttackR3 = pygame.image.load('images/mobs/shrimp/attack/right/attack3.png')

#######################################################################################################
#Menu Images ##########################################################################################
#######################################################################################################

#logo and background
GameLogo = pygame.image.load('images/menu/splash/logo.png')

MenuSplash1 = pygame.image.load('images/menu/splash/bg1.png')
MenuSplash2 = pygame.image.load('images/menu/splash/bg2.png')
MenuSplash3 = pygame.image.load('images/menu/splash/bg3.png')
MenuSplash4 = pygame.image.load('images/menu/splash/bg4.png')
MenuSplash5 = pygame.image.load('images/menu/splash/bg5.png')
MenuSplash6 = pygame.image.load('images/menu/splash/bg6.png')

#buttons
SingleplayerButton = pygame.image.load('images/menu/buttons/single.png')
MultiplayerButton = pygame.image.load('images/menu/buttons/multi.png')

PlayButton = pygame.image.load('images/menu/buttons/play.png')
PlayButtonHover = pygame.image.load('images/menu/buttons/playhover.png')

MainMenuButton = pygame.image.load('images/menu/buttons/mainmenu.png')
QuitGameButton = pygame.image.load('images/menu/buttons/quitgame.png')
ResumeButton = pygame.image.load('images/menu/buttons/resume.png')

#portraits
PaladinPortrait = pygame.image.load('images/menu/portraits/paladin.png')
AssassinPortrait = pygame.image.load('images/menu/portraits/assassin.png')
WizardPortrait = pygame.image.load('images/menu/portraits/mage.png')
AlienPortrait = pygame.image.load('images/menu/portraits/alien.png')
PortraitSelector = pygame.image.load('images/menu/portraits/selector.png')
