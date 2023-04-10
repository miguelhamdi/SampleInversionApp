"""Import Libraries"""
import librosa
import os
import soundfile as sf
import numpy as np

"""Load Audio File"""
audio_file = '/Users/miguelhamdi/Desktop/123.mp3'
y, sr = librosa.load(audio_file)

"""Determine how many beats there are"""
duration = librosa.get_duration(y=y, sr=sr)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
duration_in_minutes = duration / 60
beats_in_song = duration_in_minutes * tempo


"""Find the duration of each 8 bar segment"""
number_of_eight_bars = beats_in_song / 8
duration_per_eight_bar = duration / number_of_eight_bars

"""Split Audio into 8-Bar Clips"""
all_eight_bars = []
current_time = 0
while current_time < duration:
    eight_bar_end_time = current_time + duration_per_eight_bar
    if eight_bar_end_time > duration:
        eight_bar_end_time = duration
    all_eight_bars.append((current_time, eight_bar_end_time))
    current_time = eight_bar_end_time

"""Adding Each item from all_eight_bars to the Inverse Phase of the Previous item the inverse phase of the sum is then added to the next iteration of the loop and putting it into a seperate list called bar_list"""
bar_list =[]
bar_list.append(all_eight_bars[0])
all_eight_bars.pop(0)
for i in range(len(all_eight_bars)):
    prev_seg = -all_eight_bars[i-1]
    current_seg = all_eight_bars[i]
    if i != 0:
        sum = sum + prev_seg + current_seg
    else:
        sum = prev_seg + current_seg
    bar_list.append(sum)

"""Create a folder called Components"""
if not os.path.exists('Components'):
    os.mkdir('Components')

"""Save Each File into Folder"""
for i, segment in enumerate(bar_list):
    start_time = segment[0]
    end_time = segment[1]
    segment_audio = y[int(start_time * sr):int(end_time * sr)]
    sf.write(f'Components/segment_{i+1}.wav', segment_audio, sr, subtype='PCM_16')