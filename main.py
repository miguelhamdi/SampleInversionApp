"""Import Libraries"""
import librosa
import os

"""Load Audio File"""
audio_file = '/Users/miguelhamdi/Desktop/123.mp3'
y, sr = librosa.load(audio_file)

"""Determine how many beats there are"""
duration = librosa.get_duration(y=y, sr=sr)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
duration_in_minutes = duration / 60
beats_in_song = duration_in_minutes * tempo
number_of_eight_bars = beats_in_song / 8
"""Find the duration of each 8 bar segment"""
duration_per_eight_bar = duration / number_of_eight_bars

"""Split Audio into 8-Bar Clips"""
all_eight_bars = []
current_time = 0



"""Adding Each Bar to the Inverse Phase of the Previous Bar"""

"""Create a folder called Components"""

"""Save Each File into Folder"""
