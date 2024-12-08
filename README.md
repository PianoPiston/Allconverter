# Allscale Converter

Convert any unit to any other, add your own units for scale and customizability! 

![image](https://github.com/user-attachments/assets/0ede8e87-d22d-4519-808b-2aa8ce4266d7)

# Site:
https://fissionengine.pythonanywhere.com/

# About

General purpose unit converter that allows the user to add custom units, the units are then saved as cookies. The entire app is one front-end file that can be saved and ran locally.
The converter works by defining a unit as an amount of base unit, for example, 1kg is used as the base unit, it's conversion rate is defined as 1. 1g is defined as 1000, and 1 ton is defined as 0.001.

# Notes: 
some conversions may be incorrect, rounding errors may also be present so this is not a scientific calculator (currently). Feel free to message with any feedback, or fix any conversion rates that are wrong, thank you!

# Hosting:
Made with Django. code for Css, Html and Js is all placed into the same file for simplicity (this is generally considered bad practice, though). File can be located in the templates folder.

# Linux
```
git clone https://github.com/PianoPiston/AllscaleConverter.git
cd converter
python3 manage.py runserver
```
(requirements are git, Python3 and Django)
