from django.test import TestCase

# Create your tests here.

# plan your stupid ideas here

idea1=""" #lets see if i can use one unit as the base for all conversions, now without needing to define n! 
amount of stupid HARDCODED results.

convert_distance():

m = 1 #one meter used as base
mile = 1600
km = 1000

if forwards:
    if unit1 == meter: 
        return input1*unit2_const
    else if unit1 != meter:
        return input1*unit2_const/unit1_const

if backwards: #wip
    if unit2 == meter:
        return input2*unit1_const
    else if unit2 != meter:
        return input2*unit1_const/unit2_const

# THE IF CLAUSE WASNT NEEDED, SOMETHING DIVIDED BY ITSELF IS ALWAYS 1, SO IF THE TWO UNITS WERE SAME,
IT WOULD HAVE GOTTEN SAME RESULT, TIME WASTED!

# current system (thanks alot chatgpt)

    let conversionFactor = 1;
    if (unit1 === "meters" && unit2 === "kilometers") conversionFactor = 0.001;
    else if (unit1 === "meters" && unit2 === "miles") conversionFactor = 0.000621371;
    else if (unit1 === "kilometers" && unit2 === "meters") conversionFactor = 1000;
    else if (unit1 === "kilometers" && unit2 === "miles") conversionFactor = 0.621371;
    else if (unit1 === "miles" && unit2 === "meters") conversionFactor = 1609.34;
    else if (unit1 === "miles" && unit2 === "kilometers") conversionFactor = 1.60934;

    
    // Check if the first input is filled, calculate the second input
    if (direction == "forw") {
        document.getElementById('distance-input2').value = (input1 * conversionFactor).toFixed(2);
    }
    // If the second input is filled, calculate the first input
    else if (direction == "back") {
        document.getElementById('distance-input1').value = (input2 / conversionFactor).toFixed(2);
    }

# solution should scale better

(a/m) / (b/m) = a/b #True

should reduce lines of code from O(n!) to O(n)+x, x=two extra conditionals (idk if thats the proper use of that term but
it probably doesnt matter.)

"""

og_function_by_me="""

        function convertSpeed(direction) {
            const unit1 = document.getElementById('speed-unit1').value;
            const unit2 = document.getElementById('speed-unit2').value;
            const input1 = parseFloat(document.getElementById('speed-input1').value);
            const input2 = parseFloat(document.getElementById('speed-input2').value);

            let conversionFactor = 1;
            if (unit1 === "mps" && unit2 === "kph") conversionFactor = 3.6;
            else if (unit1 === "mps" && unit2 === "mph") conversionFactor = 2.23694;
            else if (unit1 === "kph" && unit2 === "mps") conversionFactor = 0.277778;
            else if (unit1 === "kph" && unit2 === "mph") conversionFactor = 0.621371;
            else if (unit1 === "mph" && unit2 === "mps") conversionFactor = 0.44704;
            else if (unit1 === "mph" && unit2 === "kph") conversionFactor = 1.60934;

            // Check if the first input is filled, calculate the second input
            if (direction == "forw") {
                document.getElementById('speed-input2').value = (input1 * conversionFactor).toFixed(2);
            }
            // If the second input is filled, calculate the first input
            else if (direction == "back") {
                document.getElementById('speed-input1').value = (input2 / conversionFactor).toFixed(2);
            }
        }
"""

convert_from_input="""
input
type

result = 1/input*type.conversion_ratio
createcookie(result)

# genius algorithm, i know

"""

adsfafds = """
test:

if cookies respond the correct theme type, 

i

[edkj
for elif is_backwards=
=true:
)
Colorscheme cmyr
gb

if color == blue;
    basecolor=color[0]
    shade=color[:5]
    eli
    
/()=`
"""

changes = """

algorithm optimised with testing/legacy code removed

file restructuring

+Unit and clear buttons redesigned

UI fixed

- overlay added and missing code bug fixed.

better user guide

mobile version friendly! 

- working unit adder

- new fonts added

new units

_____________________

The Allscale Converter has undergone significant improvements for enhanced usability and performance. 
The algorithm has been optimized, legacy code removed, and CSS structures reorganized. 
The Unit and Clear buttons have been redesigned, alongside UI fixes, 
including a new overlay feature and a bug fix for missing code and app-breaking feature. 
The user guides littered around have been revamped for clarity, and the app is now fully mobile-friendly 
and no longer has un-equal sizing (this took an unfortunate amount of time to figure out). 
The now fully functional unit adder on mobile is complemented by stylish new fonts and several 
humorous and practical units added for a better user experience. 


"""

