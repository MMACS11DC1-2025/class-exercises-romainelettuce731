funky tube generator

by mason

so funky

---How to use my project---

Paste the code into trinket.io. After running the program, it will ask you how large you would like your tubes to start out as.
It will then ask you for how many tubes you would like to generate. The user may input 2, 4, 6, or 8. 
If this number is not 2, 4, 6, or 8, the program will ask the user to re-enter a valid number.
The program will then generate the requested amount of tubes with a total amount of rings equal to double the size inputted. (If there are two tubes, total amount of rings are equal to size to keep pattern looking nice)
Once the pattern has generated, the program will tell you the amount of recursions that happened.
Run the program again to create a new pattern!

---Reasonable Recursion and Depth Discussion---

For my project, I stopped the recursion once the size reached 0. This is because allowing the size to go into the negatives would reverse the tube's direction and cause overlapping, creating a pattern that didn't look so good. I set the limit to 300 as a maximum because any larger creates a shape you can't see and the program takes an extremely long time to draw it. My recursive approach was to have a program that had two input questions that branched into multiple results. This can be demonstrated by  the ring spacing being different for the amount of tubes that would be printed. These inputs also affect the output as it changes the pattern produced by the overlapping of tubes, if present, as well as the general size and number of tubes in the first place.

---Test Cases---

![alt text](<Screenshot 2025-10-31 144133-1.png>)
    ![alt text](<Screenshot 2025-10-31 144243.png>)
    ![alt text](<Screenshot 2025-10-31 144306.png>)

---Debugging and Testing---

I ran into a lot of bugs in my program that needed to be debugged. The recursive function was the part that required the most testing. I ran into many bugs, such as the recursive function either looping infinitely or not looping at all. This required a lot of debugging, which included modifying my base case several times. 

I also had other issues that required debugging, but none of them were as large as the recursive function. An example of this is when I was coding the size subtraction from the tubes that are drawn. I had to figure out a way to create if statements so that if the amount of tubes was 2, the size would be subtracted by 1 rather than 0.5. This is because after testing, the tubes appeared fully black when there were only two tubes since subtracting by 0.5 placed the rings too close together with 2 tubes. This took less testing to figure out as I was able to create an if statement followed by elif statements specific to their situations. 

One last example is printing the correct number of recursions. Since the number of rings can be subtracted by 0.5, the total number of recursions can vary from 1x to 2x of the size inputted. I tried creating variables to track this, however it didn't work as planned. I decided to then use an if statement for the print statement which matched the previous if statement where if the number of tubes was equal to 2, the print statement would be size times 1. Otherwise, it would print size times 2 amount of recursions.

--Peer Review (Marko Trajkovic)---

The first thing I noticed that I liked was the code was very organized and neat, and the comments were dispersed well. I like how there can be more than 1 pattern, which is very creative and something many people did not do. I also like this implimentation of error control, like if you type a number besides 2, 4, 6 or 8 when asking for the number of tube, the program will tell the user that that input is invalid.  However, the Turtle code is quite simple and the pattern is just a bunch of Turtle circles going around eachother, which I feel could be expanded on.

--Challenges--

The biggest challenge that I had to overcome was creating the error handling for my input statements. I had to figure out how to create a while loop that would only break if the input was an integer and not a string. This way, the user could re-enter their input without having the program crash. This was even harder in my second input statement as I needed only specific integers, while also not allowing the program to crash for incorrect input. I was able to solve this for the first statement by creating a list with integers between 0 and 300, and if the user input was not one of these numbers, it would ask them to retry. I solved the second statement by creating a list where if the user input was not a number in the list, it would ask them to retry. Both of these inputs would then be converted to an integer afterwards.