@echo off

echo ==Extract audio from video
set dir=%~dp0
set input=%~n1
set ext=%~x1

Python %dir%\video_audio\extract_audio.py %input% %ext%