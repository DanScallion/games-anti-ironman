# games-anti-ironman

Simple program in python that will backup your savegame.

To configure it add "settings.ini" to the same directory where the program is located.

in
[Settings]
currentgame = Stellaris

It it stores which game at this moment is it managing. 

Example of adding new game:
[Stellaris]
filepath = C:/Program Files (x86)/Steam/userdata/20000/22220/remote/save games/imperiumofgreatwater2_1549896605/
filename = ironman
filetype = .sav
lastsave = ironman_2023-03-21 21_10_51.sav

Example of use:
Backup newest savegame. 
"D:\users\danie\Documents\Scripts\games-anti-ironman.exe" -a backup 
"Program filepath" -a backup 

Load previous savegame. (Keep in mind it will erase current gamefile and load backup in its place.)
"Program filepath" -a load
"D:\users\danie\Documents\Scripts\games-anti-ironman.exe" -a load
