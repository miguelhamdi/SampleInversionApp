# SampleInversionApp
An app that takes a audio source and returns different clips of each individual component of the audio source.

USER GUIDE
1. User opens app.
2. Imports an audio file (song).
3. Presses convert button.
4. App returns a folder which includes short audio clips of each individual component named Sample1, Sample2, etc...

DEVELOPER GUIDE
1. Take imported audio file.
2. Split into 8 bar clips.
    1. By finding the tempo of the song (bpm) & the lenght of the song (in minutes).
    2. By counting the beats with the librosa library.
3. Put each 8 bar clip into a list called bars.
4. Take the sum of bar[1] & the phase inverse of bar[0] (previous bar).
5. Put the sum into a seperate combined clip called Sample1.
6. Add Sample1 to another list called Samples.
7. Repeat tasks 5, 6, & 7 but add 1 to the index of every bar. 
8. Call the iterations of each sum Sample1, Sample2, etc...
9. Put all the contents of the list Samples, into a folder where the initial file was imported from. Called the folder Components.
