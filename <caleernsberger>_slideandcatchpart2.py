#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:15:08 2024

@author: caleernsberger
"""
import pygame
import random
import simpleGE

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Bubbie.png")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.scene.screen.get_width())
        self.dy = random.randint(4, 8)
        
    def checkBounds(self):
        if self.bottom > self.scene.screen.get_height():
            self.reset()


class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Bucket.png")
        self.setSize(100, 100)
        self.position = (320, 400)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("desert.jpg")
        self.score = 0
        self.high_score = 0
        self.timer = 15  
        self.frame_rate = 60  
        self.frame_counter = 0  
        self.timer_font = pygame.font.Font(None, 36)  
        self.game_over_font = pygame.font.Font(None, 72)  
        
        self.andCoin = simpleGE.Sound("bloop.mp3")
        
        self.charlie = Charlie(self)
        self.coins = []
        for i in range(10):
            self.coins.append(Coin(self))
        
        self.sprites = [self.charlie, self.coins]
        
        self.font = pygame.font.Font(None, 36)  
        
    def process(self):
        if self.timer <= 0: 
            self.stop()
            return
        
        for coin in self.coins:
            if self.charlie.collidesWith(coin):
                self.andCoin.play()
                coin.reset()
                self.score += 1 
        
        
        if self.score > self.high_score:
            self.high_score = self.score
        
     
        if self.timer > 0:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_rate:
                self.timer -= 1
                self.frame_counter = 0
        
        
        timer_text = "Time: {:.1f}".format(max(0, self.timer))
        timer_surface = self.timer_font.render(timer_text, True, (255, 255, 255))
        self.screen.fill((0, 0, 0), (self.screen.get_width() - 150, 20, 150, 36)) 
        self.screen.blit(timer_surface, (self.screen.get_width() - 150, 20))
        
    
        score_text = "Score: " + str(self.score)
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        self.screen.fill((0, 0, 0), (20, 20, 150, 36))  
        self.screen.blit(score_surface, (20, 20))
        
    def stop(self):
        
        game_over_text = "Game Over"
        game_over_surface = self.game_over_font.render(game_over_text, True, (255, 0, 0))
        self.screen.blit(game_over_surface, (self.screen.get_width() // 2 - 140, self.screen.get_height() // 2 - 50))
        
        high_score_text = "Your Score: " + str(self.high_score)
        high_score_surface = self.font.render(high_score_text, True, (255, 255, 255))
        self.screen.blit(high_score_surface, (self.screen.get_width() // 2 - 90, self.screen.get_height() // 2 + 50))
  
   
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()