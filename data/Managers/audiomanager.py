import pygame
import sys
from mutagen.mp3 import MP3
import os
import time
import data.Managers.univars as univars


pygame.mixer.init()



class Music_Manager:
    def __init__(self):
        self.current_song = None
        self.mp3data = None
        self.song_prog = 0
        self.sounds = {}
        self.song_pos = 0
    
    def update(self,dt):
        if not self.current_song == None:
            self.song_pos += dt/60
            self.song_prog = self.song_pos/(self.mp3data.info.length)
            if round(self.song_prog,2) >= 1:
                self.play_song(self.current_song)
            
    def init_sounds(self):
        for sfx in os.listdir("data/audio/SFX"):
            self.sounds[sfx] = pygame.mixer.Sound(f"data/audio/SFX/{sfx}")
            
        
            
    def play_song(self,song,start_seconds=0):
        
        if (not self.current_song == song) or (round(self.song_prog,2) >= 1 ):
            self.song_pos = start_seconds
            self.current_song = song
            pygame.mixer.music.load(f"data/audio/{song}.mp3")
            self.mp3data = MP3(f"data/audio/{song}.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.rewind()
            pygame.mixer.music.set_pos(start_seconds)
            
    def move_needle(self,seconds):
        
        pygame.mixer.music.rewind()
        pygame.mixer.music.set_pos(seconds)
        
        self.song_pos = seconds
            
        
    def play_sound(self,name,ntimes = 1,ext = ".wav"):
        name = f"{name}{ext}"
        self.sounds[name].play(ntimes -1)
        
        
    def swapcont(self,song):
        if (not self.current_song == song):
            self.play_song(song,start_seconds=self.song_pos)
            
            
            
            
am = Music_Manager()