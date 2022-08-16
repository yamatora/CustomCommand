@echo off

echo ==Extract audio from video
set input=%~n1
set ext=%~x1

Python C:\Users\yamatora\CustomCommand\video_audio\extract_audio.py %input% %ext%