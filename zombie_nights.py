#Zombie Nights
import pygame

class TelePort(pygame.sprite.Sprite):
    def __init__(self, x, y, zn):
        # initialize the super class Sprite
        super().__init__()
        # Tile level initializations
        self.image = pygame.transform.scale(pygame.image.load(zn.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[zn.level][0] + 'teleport.png'), (64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x  # left
        self.rect.y = y  # top

class Crate(pygame.sprite.Sprite):
    def __init__(self, x, y, zn):
        #initialize the super class Sprite
        super().__init__()
        #initialize the Crate
        self.image = pygame.transform.scale(pygame.image.load(zn.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[zn.level][0] + 'Crate.png'), (32,32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.zn = zn

class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y, zn):
        #initialize the super class Sprite
        super().__init__()
        #initilaize the Gem
        self.gem_frames = []
        for i in range(8): #0-7
            self.gem_frames.append(pygame.transform.scale(pygame.image.load(zn.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[zn.level][0] + 'crystals/yellow_crystal_' + str(i) + '.png' ), (64,64)))

        self.image = self.gem_frames[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.current_frame_index = 0
        self.zn = zn

    def update(self):
        self.current_frame_index = (self.current_frame_index + 0.1) % len(self.gem_frames)
        self.image = self.gem_frames[int(self.current_frame_index)]


class Fruits(pygame.sprite.Sprite):
    def __init__(self, x, y, fruit_code, zn):
        # initialize the super class Sprite
        super().__init__()
        # Tile level initializations
        self.image = pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/'+ Zombie_Nights.game_levels[zn.level][0] +'fruits/fruit_' + str(fruit_code) + '.png'), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x  # left
        self.rect.y = y  # top
        self.fruit_nutrition = fruit_code + 1

class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y, zn):
        # initialize the super class Sprite
        super().__init__()
        # Tile level initializations
        self.image = pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/'+ Zombie_Nights.game_levels[zn.level][0] +'sword.png'), (32, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x  # left
        self.rect.y = y  # top

class Snowman(pygame.sprite.Sprite):
    def __init__(self, x, y, zn):
        # initialize the super class Sprite
        super().__init__()
        # Tile level initializations
        self.image = pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/'+ Zombie_Nights.game_levels[zn.level][0] +'SnowMan.png'), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.left = x  # left
        self.rect.bottom = y+32  # bottom


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_code, zn):
        # initialize the super class Sprite
        super().__init__()
        # Tile level initializations
        if tile_code == 7:
            self.image = pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/'+ Zombie_Nights.game_levels[zn.level][0] +'tiles/Tile (' + str(tile_code) + ').png'), (28, 32))
            x = x+4
        else:
            self.image = pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/'+ Zombie_Nights.game_levels[zn.level][0] +'tiles/Tile (' + str(tile_code) + ').png'), (32, 32))

        self.rect = self.image.get_rect()
        self.rect.x = x  # left
        self.rect.y = y  # top

class Water(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_code, zn):
        # initialize the super class Sprite
        super().__init__()
        # Tile level initializations
        self.image = pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/'+ Zombie_Nights.game_levels[zn.level][0] +'tiles/Tile (' + str(tile_code) + ').png'), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x  # left
        self.rect.y = y  # top

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, zombie_flag, zn):
        # initialize the Sprite
        super().__init__()
        # Player initializations
        self.zn = zn
        y = y+33
        self.gender = 'male' if zombie_flag == 1 else 'female'

        self.zombie_right_walk = []
        self.zombie_left_walk = []
        for i in range(1,11):  # 1-10
            self.zombie_right_walk.append(pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[zn.level][0] +'zombie/'+ self.gender+'/walk/Walk (' + str(i) + ').png'), (32, 64)))
            self.zombie_left_walk.append(pygame.transform.flip(self.zombie_right_walk[i-1], True, False))

        self.zombie_right_attack = []
        self.zombie_left_attack = []
        for i in range(1,9): #1-8
            self.zombie_right_attack.append(pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[zn.level][0] +'zombie/'+ self.gender+'/attack/Attack (' + str(i) + ').png'), (32, 64)))
            self.zombie_left_attack.append(pygame.transform.flip(self.zombie_right_attack[i-1], True, False))

        self.zombie_right_dead = []
        self.zombie_left_dead = []
        for i in range(1,13): # 1-12
            self.zombie_right_dead.append(pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[zn.level][0] +'zombie/'+ self.gender+'/dead/Dead (' + str(i) + ').png'), (32, 64)))
            self.zombie_left_dead.append(pygame.transform.flip(self.zombie_right_dead[i-1], True, False))

        # a default image
        if self.gender == 'male':
            self.image = self.zombie_right_walk[0]
        else:
            self.image = self.zombie_left_walk[0]

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)


        # state
        self.state = 1  # walk
        if self.gender == 'male':
            self.dx = 1  # right
            self.state_frames = self.zombie_right_walk  # default
        else:
            self.dx = -1  # left
            self.state_frames = self.zombie_left_walk  # default

        self.current_frame_index = 0

        # motion
        self.HORIZONTAL_ACCELERATION = 0.01
        self.HORIZONTAL_FRICTION = 0.001
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.default_position = pygame.math.Vector2(x, y)


    def update(self):
        self.animate()

    def animate(self):
        self.current_frame_index = (self.current_frame_index + 0.1) % len(self.state_frames)
        self.image = self.state_frames[int(self.current_frame_index)]

        if self.state == 1:
            self.acceleration.x = self.dx * self.HORIZONTAL_ACCELERATION - self.HORIZONTAL_FRICTION * self.velocity.x
            self.velocity += self.acceleration
            # displacement = velocity * time + 0.5 * acceleration * time * time
            # consider, time = 1
            # displacement = velocity + 0.5 * acceleration
            self.position += self.velocity + 0.5 * self.acceleration
            self.rect.bottomleft = self.position

            if self.gender == 'male':
                #fruit collide
                if pygame.sprite.spritecollide(self, self.zn.fruits_group, False):
                    self.dx = -1
                    self.state_frames = self.zombie_left_walk
                    self.velocity.x = 0
                elif self.position.x < self.default_position.x:
                    self.dx = 1
                    self.state_frames = self.zombie_right_walk
                    self.velocity.x = 0
            elif self.gender == 'female':
                #fruit collide
                if pygame.sprite.spritecollide(self, self.zn.fruits_group, False):
                    self.dx = 1
                    self.state_frames = self.zombie_right_walk
                    self.velocity.x = 0
                elif self.position.x > self.default_position.x:
                    self.dx = -1
                    self.state_frames = self.zombie_left_walk
                    self.velocity.x = 0

            #zombie player collision
            if pygame.sprite.spritecollide(self, self.zn.player_group, False):
                self.state = 2
                if self.dx == -1:
                    self.state_frames = self.zombie_left_attack
                elif self.dx == 1:
                    self.state_frames = self.zombie_right_attack

                self.attack_time = self.zn.FPS * 2

            # zombie zombie collision
            collided = pygame.sprite.spritecollide(self, self.zn.zombie_group, False)
            if len(collided) > 1:
                print('zombies collided')
                self.state = 3
                if self.dx == 1:
                    self.state_frames = self.zombie_right_dead
                elif self.dx == -1:
                    self.state_frames = self.zombie_left_dead
                self.attack_time = self.zn.FPS * 2

        elif self.state == 2:
            self.zn.player.power = 0  # PLAYER DIES
            self.attack_time -=1
            if self.attack_time == 0:
                self.state = 1
                if self.dx == -1:
                    self.state_frames = self.zombie_left_walk
                elif self.dx == 1:
                    self.state_frames = self.zombie_right_walk

        elif self.state == 3:
            print('zombie state 3')

            self.attack_time -= 1
            if self.attack_time == 0:
                self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, zn):
        # initialize the Sprite
        super().__init__()
        # Player initializations
        self.zn = zn

        self.player_right_idle = []
        self.player_left_idle = []

        for i in range(10):  # 0-9
            self.player_right_idle.append(pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/player/idle/Idle__00' + str(i) + '.png'), (32, 64)))
            self.player_left_idle.append(pygame.transform.flip(self.player_right_idle[i], True, False))

        self.player_right_running = []
        self.player_left_running = []
        for i in range(10):  # 0-9
            self.player_right_running.append(pygame.transform.scale( pygame.image.load(zn.GAME_FOLDER + 'images/player/running/Run__00' + str(i) + '.png'), (32, 64)))
            self.player_left_running.append(pygame.transform.flip(self.player_right_running[i], True, False))

        self.player_right_attack = []
        self.player_left_attack = []
        for i in range(10):
            self.player_right_attack.append(pygame.transform.scale( pygame.image.load( zn.GAME_FOLDER + 'images/player/attack/Attack__00'+ str(i)+'.png'), (64,64)))
            self.player_left_attack.append(pygame.transform.flip(self.player_right_attack[i], True, False))

        self.player_right_dieing = []
        self.player_left_dieing = []
        for i in range(5):
            self.player_right_dieing.append(pygame.transform.scale( pygame.image.load(self.zn.GAME_FOLDER + 'images/player/dieing/Dead__00' + str(i) + '.png') , (64,64)))
            self.player_left_dieing.append(pygame.transform.flip(self.player_right_dieing[i], True, False))

        self.player_right_dead = []
        self.player_left_dead = []
        for i in range(4):
            self.player_right_dead.append(pygame.transform.scale( pygame.image.load(self.zn.GAME_FOLDER + 'images/player/dead/Dead__00' + str(i) + '.png') , (64,64)))
            self.player_left_dead.append(pygame.transform.flip(self.player_right_dead[i], True, False))

        # a default image
        self.image = self.player_right_idle[0]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        # state
        self.state = 0  # idle
        self.dx = 1  # right
        self.state_frames = self.player_right_idle  # default
        self.current_frame_index = 0

        # player attributes
        self.power = 10
        self.MAX_POWER = 20
        self.RUN_POWER_LOSS = 0.01
        self.JUMP_POWER_LOSS = 0.1
        self.hasSword = False

        #sounds
        self.fruit_picked = pygame.mixer.Sound(zn.GAME_FOLDER  + 'sounds/pickup.wav')
        self.fruit_picked.set_volume(0.2)

        self.dead = pygame.mixer.Sound(zn.GAME_FOLDER + 'sounds/dead.wav')
        self.dead.set_volume(0.1)

        self.bad_fruit_picked = pygame.mixer.Sound(zn.GAME_FOLDER + 'sounds/bad_pickup.wav')
        self.bad_fruit_picked.set_volume(0.1)

        self.jump_sound = pygame.mixer.Sound(zn.GAME_FOLDER + 'sounds/jump.wav')
        self.jump_sound.set_volume(0.1)

        self.teleport = pygame.mixer.Sound(zn.GAME_FOLDER + 'sounds/teleport.wav')
        self.teleport.set_volume(0.1)

        # motion
        self.HORIZONTAL_FRICTION = 0.1
        self.GRAVITY = 0.02

        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.GRAVITY)


    def jump(self):
        if self.power > 0:
            # is grounded
            grounded = pygame.sprite.spritecollide(self, self.zn.tile_group, False)
            if grounded:
                self.jump_height = self.power * 0.15
                self.velocity.y = -1 * self.jump_height
                self.power -= self.JUMP_POWER_LOSS
                self.jump_sound.play()


    def update(self):
        if self.power > 0:
            self.horizontal_acceleration = self.power * 0.05
            self.state = 0  # idle
            if self.dx == 1:
                self.state_frames = self.player_right_idle
            elif self.dx == -1:
                self.state_frames = self.player_left_idle

            # get the keys pressed
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT] and self.rect.right < self.zn.WINDOW_WIDTH:
                # run right
                self.state = 1  # running
                self.dx = 1  # right
                self.state_frames = self.player_right_running
                self.power -= self.RUN_POWER_LOSS

            elif keys[pygame.K_LEFT] and self.rect.left:
                # run left
                self.state = 1  # running
                self.dx = -1  # left
                self.state_frames = self.player_left_running
                self.power -= self.RUN_POWER_LOSS

            elif keys[pygame.K_LALT] and self.hasSword:
                self.state = 2  # attack
                if self.dx == 1:  # right
                    self.state_frames = self.player_right_attack
                elif self.dx == -1:  # left
                    self.state_frames = self.player_left_attack
                self.power -= self.RUN_POWER_LOSS

        elif self.power <= 0 and self.state >= 0:
            self.dead.play()
            self.state = -1 #dieing
            if self.dx == 1:
                self.state_frames = self.player_right_dieing
            elif self.dx == -1:
                self.state_frames = self.player_left_dieing

        self.animate()

    def animate(self):
        self.current_frame_index = (self.current_frame_index + 0.1) % len(self.state_frames)
        self.image = self.state_frames[int(self.current_frame_index)]

        if self.state >=0: #alive
            if self.state == 1:
                #running
                if pygame.sprite.spritecollide(self, self.zn.snowman_group, False):
                    self.acceleration.x = 0
                    self.velocity.x = 0
                elif pygame.sprite.spritecollide(self, self.zn.crate_group, False):
                    self.acceleration.x = 0
                    self.velocity.x = 0
                    if self.dx == -1:
                        self.position.x +=30
                    elif self.dx == 1:
                        self.position.x -=30
                else:
                    self.acceleration.x = self.dx * self.horizontal_acceleration - self.HORIZONTAL_FRICTION * self.velocity.x
            else:
                self.acceleration.x = 0
                self.velocity.x = 0

            self.velocity += self.acceleration
            # displacement = velocity * time + 0.5 * acceleration * time * time
            # consider, time = 1
            # displacement = velocity + 0.5 * acceleration
            self.position += self.velocity + 0.5 * self.acceleration

            if self.position.x > self.zn.WINDOW_WIDTH - self.rect.width:
                self.position.x = self.zn.WINDOW_WIDTH - self.rect.width
            elif self.position.x < 0:
                self.position.x = 0

            if self.position.y < self.rect.height:
                self.position.y = self.rect.height

            # is grounded?
            collided = pygame.sprite.spritecollide(self, self.zn.tile_group, False)
            if collided and self.velocity.y > 0:  # moving down
                # player and tile group are in conact (collide)
                self.position.y = collided[0].rect.top + 1
                self.velocity.y = 0
            elif collided and self.velocity.y < 0 and self.rect.top > collided[0].rect.top:  # moving up
                # player and tile group are in contact (collide)
                self.velocity.y = 0
                self.position.y += 4

            collided = pygame.sprite.spritecollide(self, self.zn.water_group, False)
            if collided:
                # player and water group are in conact (collide) => death
                self.power =0
                self.velocity.y = 0
                self.position.y = collided[0].rect.bottom

            collided = pygame.sprite.spritecollide(self, self.zn.water_base_group, False)
            if collided and self.velocity.y < 0 :  # moving up
                # player and water group are in contact (collide)
                self.velocity.y = 0
                self.position.y += 6

            self.rect.bottomleft = self.position

            # Has taken a fruits
            collided = pygame.sprite.spritecollide(self, self.zn.fruits_group, True)
            if collided:
                for x in collided:
                    self.power += x.fruit_nutrition
                    if x.fruit_nutrition > 0:
                        self.fruit_picked.play()
                    else:
                        self.bad_fruit_picked.play()
                if self.zn.level == 3:
                    if len(self.zn.fruits_group) == 0:
                        self.zn.crate_group.empty()


            if self.state == 2: #attacking
                pygame.sprite.spritecollide(self, self.zn.snowman_group, True)

            #Has taken sword?
            if pygame.sprite.spritecollide(self, self.zn.sword_group, True):
                self.hasSword = True

            #level change?
            collided = pygame.sprite.spritecollide(self, self.zn.teleport_group, False)
            if collided:
                self.teleport.play()
                if self.zn.level == 1:
                    self.zn.game_status = 3 # level 2 to start
                elif self.zn.level == 2:
                    self.hasSword = False
                    self.zn.game_status = 4 # level 3 to start
                elif self.zn.level == 3:
                    self.zn.game_status = 5 # game ends

        elif self.state ==-1:
            #dieing
            if self.current_frame_index > 4.5:
                self.state = -2 #dead
                if self.dx == 1:
                    self.state_frames = self.player_right_dead
                elif self.dx == -1:
                    self.state_frames = self.player_left_dead
        elif self.state == -2:
            self.zn.game_status = 6
            print('player dead, game over (lost)')

class Zombie_Nights:

    game_levels = {
        1 : ['level1/', 'Greenlands'],
        2 : ['level2/', 'Crossing the Arctic'],
        3 : ['level3/', 'Ultimate Challenge']

    }

    def __init__(self):
        self.GAME_FOLDER = 'D:/python project/game dev/art_of_game_development/game_7/'
        self.level = 1
        # create a window and set its attributes
        self.WINDOW_WIDTH = 1280  # multiples of 32
        self.WINDOW_HEIGHT = 800  # multiples of 32
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('ZOMBIE NIGHTS')
        pygame.display.set_icon(pygame.image.load(self.GAME_FOLDER + 'images/game_icon.ico'))

        # a tile group (a bag to hold and process (update, draw, ...) the Sprites)
        self.tile_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.fruits_group = pygame.sprite.Group()
        self.teleport_group = pygame.sprite.Group()
        self.water_group = pygame.sprite.Group()
        self.water_base_group = pygame.sprite.Group()
        self.snowman_group = pygame.sprite.Group()
        self.sword_group = pygame.sprite.Group()
        self.zombie_group = pygame.sprite.Group()
        self.crate_group = pygame.sprite.Group()

        self.FPS = 60
        #game_status
        self.game_status =1 #starting slide

    def tile_map_level1(self):
        # game_background
        self.game_background_image = pygame.transform.scale(pygame.image.load( self.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[self.level][0] + 'background.png'), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # tile_map
        tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 7, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5, -5, -5, 6, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5,-5,-5, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 6, 6, 6, 0, 0, 0, 0, 0, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 7, 7, -5, -5, 6, -5, -5, -5,-5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        for r in range(25):
            for c in range(40):
                if tile_map[r][c] == 1:
                    t = Tile(c * 32, r * 32, 1, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 2:
                    t = Tile(c * 32, r * 32, 2, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 3:
                    t = Tile(c * 32, r * 32, 3, self)
                    self.tile_group.add(t)

                elif tile_map[r][c] == 4:
                    t = Tile(c * 32, r * 32, 4, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 5:
                    t = Tile(c * 32, r * 32, 5, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 6:
                    f = Fruits(c * 32, r * 32, 0, self)
                    self.fruits_group.add(f)
                elif tile_map[r][c] == 7:
                    f = Fruits(c * 32, r * 32, 1, self)
                    self.fruits_group.add(f)
                elif tile_map[r][c] == -5:
                    f = Fruits(c * 32, r * 32, -5, self)
                    self.fruits_group.add(f)

                elif tile_map[r][c] == 8:
                    tp = TelePort(c * 32, r * 32, self)
                    self.teleport_group.add(tp)

                elif tile_map[r][c] == 9:  # player
                    self.player = Player(c * 32, r * 32 + 32, self)
                    self.player_group.add(self.player)



    def tile_map_level2(self):
        # game_background
        self.game_background_image = pygame.transform.scale(pygame.image.load( self.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[self.level][0] + 'background.png'), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # tile_map
        tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,11,11,11,11,11,11,11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 5, 5, 5, 5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10,10,10,10,10,10,10, 0, 0, 0, 0, 0, 0, 0, 0, 0,13, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,11,11,11,11,11,11,11,11,11,11,11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10,10,10,10,10,10,10,10,10,10,10, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 5, 5, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [11,11,11,11,11,11,11,11,11,11,11,0, 0,11,11,11,11,11,11,11,11,11,11,11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [10,10,10,10,10,10,10,10,10,10,10, 0, 0,10,10,10,10,10,10,10,10,10,10,10,0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [12,0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 5, 5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2,11,11,11,11,11,11,11,11, 2, 2, 2, 2,11,11,11, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10,10,10,10,10,10,10,10, 1, 1, 1, 1,10,10,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        for r in range(25):
            for c in range(40):
                if tile_map[r][c] == 1:
                    t = Tile(c * 32, r * 32, 1, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 2:
                    t = Tile(c * 32, r * 32, 2, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 3:
                    t = Tile(c * 32, r * 32, 3, self)
                    self.tile_group.add(t)

                elif tile_map[r][c] == 4:
                    t = Tile(c * 32, r * 32, 4, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 5:
                    t = Tile(c * 32, r * 32, 5, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 6:
                    t = Tile(c * 32, r * 32, 6, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 7:
                    t = Tile(c * 32, r * 32, 7, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 8:
                    s = Snowman(c * 32, r * 32,  self)
                    self.snowman_group.add(s)
                elif tile_map[r][c] == 9:
                    self.player.position = (c*32, r*32)
                    self.player.rect.bottomleft = self.player.position

                elif tile_map[r][c] == 10:
                    w = Water(c * 32, r * 32, 10, self)
                    self.water_base_group.add(w)
                elif tile_map[r][c] == 11:
                    w = Water(c * 32, r * 32, 11, self)
                    self.water_group.add(w)
                elif tile_map[r][c] == 12:
                    s = Sword(c * 32, (r-1) * 32, self)
                    self.sword_group.add(s)

                elif tile_map[r][c] == 13:
                    t = TelePort(c * 32, r * 32, self)
                    self.teleport_group.add(t)
                elif tile_map[r][c] == 14:
                    f = Fruits(c * 32, r * 32, 1,self)
                    self.fruits_group.add(f)



    def tile_map_level3(self):
        # game_background
        self.game_background_image = pygame.transform.scale(pygame.image.load( self.GAME_FOLDER + 'images/' + Zombie_Nights.game_levels[self.level][0] + 'background.png'), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # tile_map
        tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10,10,10,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10, 8, 0,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10, 0, 0,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 4, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 7, 0, 0,-2, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 7, 0, 0,-2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 4, 4, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 4, 4, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-1,0, 0, 7, 0, 0,-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 7, 0, 0,-2],
            [4, 4, 4, 4, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 7, 0, 0,-2, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 7, 0, 0,-2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 4, 4, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 4, 4, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 7, 0, 0,-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 4, 4, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        for r in range(25):
            for c in range(40):
                if tile_map[r][c] == 1:
                    t = Tile(c * 32, r * 32, 1, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 2:
                    t = Tile(c * 32, r * 32, 2, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 3:
                    t = Tile(c * 32, r * 32, 3, self)
                    self.tile_group.add(t)

                elif tile_map[r][c] == 4:
                    t = Tile(c * 32, r * 32, 4, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 5:
                    t = Tile(c * 32, r * 32, 5, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 6:
                    t = Tile(c * 32, r * 32, 6, self)
                    self.tile_group.add(t)
                elif tile_map[r][c] == 7:
                    f = Fruits(c * 32, r * 32, 1, self)
                    self.fruits_group.add(f)
                elif tile_map[r][c] == 8:
                    g = Gem(c * 32, r * 32, self)
                    self.teleport_group.add(g)
                elif tile_map[r][c] == 10:
                    c = Crate(c * 32, r * 32, self)
                    self.crate_group.add(c)

                elif tile_map[r][c] == -1:
                    z = Zombie(c * 32, r * 32, 1, self)
                    self.zombie_group.add(z)

                elif tile_map[r][c] == -2:
                    z = Zombie(c * 32, r * 32, 2, self)
                    self.zombie_group.add(z)

                elif tile_map[r][c] == 9:  # player
                    self.player.position = (c*32, r*32)
                    self.player.rect.bottomleft = self.player.position



    def main_loop(self):
        #Colors
        GREY = pygame.Color(127,127,127)
        YELLOW = pygame.Color(255,255,0)
        BLACK = pygame.Color(0,0,0)
        ORANGE = pygame.Color(255,127,0)
        WHITE = pygame.Color(255,255,255)

        #Power lines
        HORIZONTAL_POWER_LINE_X = 10
        HORIZONTAL_POWER_LINE_Y = self.WINDOW_HEIGHT-2
        HORIZONTAL_POWER_LINE_WIDTH = 20

        #music
        slide_music = pygame.mixer.Sound(self.GAME_FOLDER + 'sounds/level_music.wav')
        slide_music.set_volume(0.1)

        pygame.mixer.music.load(self.GAME_FOLDER + 'sounds/background_music.mp3')
        pygame.mixer.music.set_volume(0.1)

        assets_loaded = False

        #game fonts
        slide_font = pygame.font.Font(self.GAME_FOLDER + 'fonts/Poultrygeist.ttf', 60)
        general_font_big = pygame.font.Font(self.GAME_FOLDER + 'fonts/SunnyspellsRegular.otf', 60)
        general_font = pygame.font.Font(self.GAME_FOLDER + 'fonts/SunnyspellsRegular.otf', 40)

        #texts
        welcome_text = slide_font.render('Zombie Nights', True, ORANGE)
        welcome_text_rect = welcome_text.get_rect()
        welcome_text_rect.center = (self.WINDOW_WIDTH//2, self.WINDOW_HEIGHT//2- 100)

        level_text = general_font_big.render(Zombie_Nights.game_levels[self.level][1], True, WHITE)
        level_text_rect = level_text.get_rect()
        level_text_rect.center = (self.WINDOW_WIDTH//2, self.WINDOW_HEIGHT//2)

        start_text = general_font.render('Press ENTER to start...', True, WHITE)
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (self.WINDOW_WIDTH//2, self.WINDOW_HEIGHT//2 + 100)

        # game_loop control variables

        clock = pygame.time.Clock()
        running = True
        while running:
            # read the events (user actions)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_SPACE and self.game_status == 2:
                        self.player.jump()
                    elif ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER and self.game_status in [1,3,4]:
                        self.game_status = 2
                        assets_loaded = False
                        slide_music.stop()
                        pygame.mixer.music.play(-1)
                    elif ev.key == pygame.K_q and self.game_status >=5:
                        running = False
                    elif ev.key == pygame.K_r and self.game_status >=5:
                        self.level = 1
                        self.game_status = 1
                        self.tile_group.empty()
                        self.player_group.empty()
                        self.fruits_group.empty()
                        self.teleport_group.empty()
                        self.water_group.empty()
                        self.water_base_group.empty()
                        self.snowman_group.empty()
                        self.sword_group.empty()
                        self.zombie_group.empty()
                        self.crate_group.empty()
                        assets_loaded = False
                        slide_music.stop()

            if self.game_status == 1: #Press enter to start the game
                level_text = general_font_big.render(Zombie_Nights.game_levels[self.level][1], True, WHITE)
                level_text_rect = level_text.get_rect()
                level_text_rect.center = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2)

                start_text = general_font.render('Press ENTER to start...', True, WHITE)
                start_text_rect = start_text.get_rect()
                start_text_rect.center = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2 + 100)

                self.window.fill(BLACK)
                self.window.blit(welcome_text, welcome_text_rect)
                self.window.blit(level_text, level_text_rect)
                self.window.blit(start_text, start_text_rect)
                if assets_loaded == False:
                    pygame.mixer.music.stop()
                    self.tile_map_level1()
                    slide_music.play(-1)
                    assets_loaded = True

            elif self.game_status == 2: #Active
                # apply the background image
                self.window.blit(self.game_background_image, (0, 0))

                # blit the tiles
                self.tile_group.draw(self.window)

                if self.level == 2:
                    #blit the water bodies
                    self.water_group.draw(self.window)
                    self.water_base_group.draw(self.window)
                    # blit the snowman
                    self.snowman_group.draw(self.window)
                elif self.level == 3:
                    # blit the zombies
                    self.crate_group.draw(self.window)
                    self.zombie_group.update()
                    self.zombie_group.draw(self.window)

                # blit the fruits
                self.fruits_group.draw(self.window)

                # blit the sword
                self.sword_group.draw(self.window)
                # blit the teleport
                self.teleport_group.update()
                self.teleport_group.draw(self.window)
                # blit the player
                self.player_group.update()
                self.player_group.draw(self.window)


                #draw the power indicator
                power_lines = self.player.power * 100 / self.player.MAX_POWER
                for i in range(10):
                    if power_lines > 0:
                        pygame.draw.line(self.window, YELLOW, (HORIZONTAL_POWER_LINE_X, HORIZONTAL_POWER_LINE_Y -i * 5), (HORIZONTAL_POWER_LINE_X + HORIZONTAL_POWER_LINE_WIDTH, HORIZONTAL_POWER_LINE_Y - i*5), 2)
                        power_lines -= 10
                    else:
                        pygame.draw.line(self.window, GREY, (HORIZONTAL_POWER_LINE_X, HORIZONTAL_POWER_LINE_Y - i * 5), ( HORIZONTAL_POWER_LINE_X + HORIZONTAL_POWER_LINE_WIDTH, HORIZONTAL_POWER_LINE_Y - i * 5), 2)

            elif self.game_status == 3:
                if self.level == 1:
                    self.tile_group.empty()
                    self.fruits_group.empty()
                    self.teleport_group.empty()
                    self.water_group.empty()
                    self.water_base_group.empty()
                    self.snowman_group.empty()
                    self.sword_group.empty()
                    self.zombie_group.empty()
                    self.crate_group.empty()
                    self.level = 2
                    if assets_loaded == False:
                        level_text = general_font_big.render(Zombie_Nights.game_levels[self.level][1], True, WHITE)
                        level_text_rect = level_text.get_rect()
                        level_text_rect.center = (self.WINDOW_WIDTH//2, self.WINDOW_HEIGHT//2)
                        pygame.mixer.music.stop()
                        self.tile_map_level2()
                        slide_music.play(-1)
                        assets_loaded = True

                self.window.fill(BLACK)
                self.window.blit(welcome_text, welcome_text_rect)
                self.window.blit(level_text, level_text_rect)
                self.window.blit(start_text, start_text_rect)


            elif self.game_status == 4 :
                if self.level == 2:
                    self.tile_group.empty()
                    self.fruits_group.empty()
                    self.teleport_group.empty()
                    self.water_group.empty()
                    self.water_base_group.empty()
                    self.snowman_group.empty()
                    self.sword_group.empty()
                    self.zombie_group.empty()
                    self.crate_group.empty()

                    self.level = 3
                    if assets_loaded == False:
                        level_text = general_font_big.render(Zombie_Nights.game_levels[self.level][1], True, WHITE)
                        level_text_rect = level_text.get_rect()
                        level_text_rect.center = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2)
                        pygame.mixer.music.stop()
                        self.tile_map_level3()
                        slide_music.play(-1)
                        assets_loaded = True

                self.window.fill(BLACK)
                self.window.blit(welcome_text, welcome_text_rect)
                self.window.blit(level_text, level_text_rect)
                self.window.blit(start_text, start_text_rect)
            elif self.game_status == 5 :
                self.tile_group.empty()
                self.player_group.empty()
                self.fruits_group.empty()
                self.teleport_group.empty()
                self.water_group.empty()
                self.water_base_group.empty()
                self.snowman_group.empty()
                self.sword_group.empty()
                self.zombie_group.empty()
                self.crate_group.empty()

                level_text = general_font_big.render('You are a Real Champion!!!', True, WHITE)
                level_text_rect = level_text.get_rect()
                level_text_rect.center = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2)
                start_text = general_font_big.render('Press R to restart, Q to quit', True, WHITE)
                start_text_rect = level_text.get_rect()
                start_text_rect.center = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2+ 100)

                pygame.mixer.music.stop()
                slide_music.play(-1)

                self.window.fill(BLACK)
                self.window.blit(welcome_text, welcome_text_rect)
                self.window.blit(level_text, level_text_rect)
                self.window.blit(start_text, start_text_rect)

            elif self.game_status == 6:
                self.tile_group.empty()
                self.player_group.empty()
                self.fruits_group.empty()
                self.teleport_group.empty()
                self.water_group.empty()
                self.water_base_group.empty()
                self.snowman_group.empty()
                self.sword_group.empty()
                self.zombie_group.empty()
                self.crate_group.empty()

                level_text = general_font_big.render('You lose the Championship!!!', True, WHITE)
                level_text_rect = level_text.get_rect()
                level_text_rect.center = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2)
                start_text = general_font_big.render('Press R to restart, Q to quit', True, WHITE)
                start_text_rect = level_text.get_rect()
                start_text_rect.center = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2 + 100)

                pygame.mixer.music.stop()
                slide_music.play(-1)

                self.window.fill(BLACK)
                self.window.blit(welcome_text, welcome_text_rect)
                self.window.blit(level_text, level_text_rect)
                self.window.blit(start_text, start_text_rect)

            # update the display surface
            pygame.display.update()
            # moderate the rate of iteration to 60 FPS
            # makes the game run at the same speed over different CPU's
            clock.tick(self.FPS)

def main():
    # initialize the pygame framework
    pygame.init()
    zn = Zombie_Nights()
    zn.main_loop()
    # deallocate
    pygame.quit()

main()