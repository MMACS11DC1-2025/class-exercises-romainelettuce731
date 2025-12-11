--Project Theme--

My project will determine if the art shown is considered pixel art or not. It will scan the art provided and look for the number of unique colours to determine whether it has a wider array of colours due to being digital art/paint art or whether it is a simpler design created out of larger pixels and less colours. 

Pixel art will be defined as art made digitally using pixels, and brush art will be defined as art made using digital/physical brushes or renders. This is because art created with brushes usually contain a greater range of colours due to discrepancies within the amount of paint ratios in brushes compared to pixels that have manually set colours.

A list will be created of a number of all the different colours detected within an image. If there is more than a certain number of colours, the image will be marked as an advanced image that will most likely have used rendering/brushes to have been made rather than a simple image made out of pixels.


--Performance Analaysis--

An example of the report can look like:
Image 1 took 0.78 seconds, Image 2 took 0.24 seconds, Image 3 took 0.12 seconds, Image 4 took 3.42 seconds, etc. In total, the program took 7.02 seconds to run.

Images 1, 3, 4, and 6 were determined to be pixel art as they had less than 100 000 unique colours. Images 2, 5, 7, 8, 9, and 10 were determined to be brush art as they had more than 100 000 pixels.

What parts take the longest?
Processing the unique colours within the images takes the longest. It is much faster as the program doesn't have to repeatedly process a nested for loop that handles a 300 000 item list, with each image now taking between 0.10 and 1.00 seconds (except for The Last Supper for some reason?? Which takes about 6.50 seconds on its own??? It's not even that big???). Loading the functions and the modules takes on average less than 0.05 seconds each time.

--Testing--

I tested my code by making sure each image was processed in a similar amount of time. I cleaned up errors and had to fix bugs that incorrectly printed the amount of unique colours within each image. I did this by running multiple tests and changing slight details within the code until I found the error that caused slight discrepancies within the number of unique colours. After this, I was able to fix what had caused the inconsistencies.

--Challenges Faced--

My biggest challenge was optimizing the code. The reason that I do not have nested for loops in my code is because when the code ran with nested for loops, it would take over 9 minutes to process 3 images. This was obivously a huge problem as running all 10 images would most likely take an hour as the images not tested had many more unique colours to test.

In order to fix this, I had to search the PIL library for a function that could help optimize this code by many times. After some research, I found the set function. The set() function creates a list of data that removes all duplicates. Using getdata() along with set() on an image can create a list of all unique RGB values in an image in less than one second. I was able to add this into my code to bring the time for 3 images from 9 minutes down to about 0.70 seconds. This greatly optimized by code and reduced the image processing time, with the only drawback being that I had to remove my nested for loops.