from operator import add

from pico2d import *
import ball
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()

    global grass
    grass = Grass()

    global balls
    balls = [Ball(random.randint(100, 1700), 60, 0) for _ in range(30)]
    
    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)  
    
    game_world.add_objects(balls, 1)
    game_world.add_oject(grass, 0)
    game_world.add_oject(boy)

    # 소년과 볼 사이의 충돌 페어를 등록
    game_world.add_collision_pair("boy:ball",boy, None)
    for ball in balls:
        game_world.add_collision_pair("boy:ball", None, ball)

    # 좀비와 볼 사이 충돌 페어 등록
    game_world.add_collision_pair("zombie:ball",zombies, None)

    #좀비 / 소년 충돌 페어 등록
    game_world.add_collision_pair("boy:zombie", boy, None)
    for zombie in zombies:
        game_world.add_collision_pair("boy:zombie", None, zombie)



def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()
    game_world.handle_collision()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()









