Mason's super awesome project :D

---How to use my project---

Paste the code into trinket.io. After running the program, it will ask you how large you would like your tubes to start out as.
It will then ask you for how many tubes you would like to generate. The user may input 2, 4, 6, or 8. 
If this number is not 2, 4, 6, or 8, the program will ask the user to renter a valid number.
The program will then generate the requested amount of tubes with a total amount of rings equal to double the size inputted. (If there are two tubes, total amount of rings are equal to size to keep pattern looking nice)
Once the pattern has generated, the program will tell you the amount of recursions that happened.
Run the program again to create a new pattern!

---Reasonable Recursion Depth Discussion---

For my project, I stopped the recursion once the size reached 0. This is because allowing the size to go into the negatives would reverse the tube's direction and cause overlapping, creating a pattern that didn't look so good. There is no limit set for a number that may be too high because although the design is really large and takes a long time to draw, it can still create a nice design with enough time and the right sizes.

---Test Cases---

![alt text](<Screenshot 2025-10-31 144133-1.png>)
    ![alt text](<Screenshot 2025-10-31 144243.png>)
    ![alt text](<Screenshot 2025-10-31 144306.png>)

---Debugging and Testing---

I ran into a lot of bugs in my program that needed to be debugged. The recursive function was the part that required the most testing. I ran into many bugs, such as the recursive function either looping infinitely or not looping at all. This required a lot of debugging, which included modifying my base case several times. 

I also had other issues that required debugging, but none of them were as large as the recursive function. An example of this is when I was coding the size subtraction from the tubes that are drawn. I had to figure out a way to create if statements so that if the amount of tubes was 2, the size would be subtracted by 1 rather than 0.5. This is because after testing, the tubes appeared fully black when there were only two tubes since subtracting by 0.5 placed the rings too close together with 2 tubes. This took less testing to figure out as I was able to create an if statement followed by elif statements specific to their situations. 

One last example is printing the correct number of recursions. Since the number of rings can be subtracted by 0.5, the total number of recursions can vary from 1x to 2x of the size inputted. I tried creating variables to track this, however it didn't work as planned. I decided to then use an if statement for the print statement which matched the previous if statement where if the number of tubes was equal to 2, the print statement would be size times 1. Otherwise, it would print size times 2 amount of recursions.

--Peer Review (Marko Trajkovic)---

The first thing I noticed that I liked was the code was very organized and neat, and the comments were dispersed well. I like how there can be more than 1 pattern, which is very creative and something many people did not do. I also like the implimentation of error control, like if you type a number besides 2, 4, 6 or 8 when asking for the number of tube, the program will tell the user that that input is invalid.  However, the Turtle code is quite simple and the pattern is just a bunch of Turtle circles going around eachother, which I feel could be expanded on.