# Allscale Converter

*Unit converter and scaling tool that allows you to add your own units!*

![image](https://github.com/user-attachments/assets/88bf8112-2fff-44e5-bf59-162e99680cfd)


# Key features

- Create and convert any unit you want, get a sense of scale quickly
- Three cleanly designed themes to choose from + dark mode
- Offline friendly - you may download the site to use offline

[did you know, the average blue whale can fit around 81 passenger cars?] 
# Site:
https://fissionengine.pythonanywhere.com/

# About

General purpose unit converter that allows the user to add custom units, the units are then saved as cookies. The entire app is one front-end file that can be saved and ran locally.
The converter works by defining a unit as an amount of base unit, for example, 1kg is used as the base unit, it's conversion rate is defined as 1. 1g is defined as 1000, and 1 ton is defined as 0.001.

# Notes: 
some conversions may be incorrect, rounding errors may also be present. Feel free to give feedback or fix any code thank you!

# Hosting:
Made with Django. code for Css, Html and Js is all placed into the same file for simplicity. File can be located in the templates folder.

# Linux
```
git clone https://github.com/PianoPiston/AllscaleConverter.git
cd converter
python3 manage.py runserver
```
(requirements are git, Python3 and Django)
