# Splatoon 3 Canvas Printer
## 1. Intro
This repo is a hardware development based on Pro Micro MCU integrated Atmega32u4 chip.<br>
[Splatoon3](https://en.wikipedia.org/wiki/Splatoon_3)(喷射战士 in Chinese language) or 'penpen(喷喷) called between chinese fans, have a wonderful part for paint lover,draw a scrawl in the blank canvas with resolution 320x120 and post for viewing by others.<br>
However,it's hard to draw with Nintendo Controller,even if some straight line.We can consider to use a simple Micro control unit(MCU) replace controller and convert image you want to draw into a `.c` file and compile it into a `.hex` file,finally upload this file to your device.
## 2.Device and Accessories
* [Pro Micro](https://www.sparkfun.com/products/12640)(I recommend 5v/16MHz)
* Two jumpers and a switch button
* Bread Board (Depend on your type of jumpers)
* A computer with Windows OS and have install [Arduino IDE](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE)
## 3.Step
* 1.Resize your image into resolution 320x120 with `resize.py` file in Resize folder,code `python resize.py image.jpg(.png)` in terminal upon Resize folder.
* 2.Convert your image to `.c` file in Printer folder,move your resized `.png` file to Printer folder and code `python png2c.py Resized.png` in terminal.
* 3.Configure `.cmd` file start with `.txt` file.Create a `.txt` file and type:<br> Make sure these folder's location you typed correctly then code `ren avrgccstart.txt avrgccstart.cmd` in terminal thus we create `.cmd` file for uploading later.
* 4.Generate `.hex` in `.cmd`file you just created,double tap this this file and code `make` then some files about `Joystick` will generated including `Joystick.hex` file.
* Open Arduino IDE and put your Pro Micro plug into computer,open preferences and input `https://raw.githubusercontent.com/sparkfun/Arduino_Boards/main/IDE_Board_Manager/package_sparkfun_index.json` into Additional boards manager URLs for configuration of Pro Micro device,then check upload in show verbose output during,finally click OK.
* 
  

