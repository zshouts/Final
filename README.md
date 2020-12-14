# Final
CIS1415 Final Project
# How to use the program
My program works like any other calculator, you input your numbers by using the buttons on the GUI then press one of the operators, enter a second number and press equals. You will get an error if trying to divide by 0 or if you try to press an operator button before entering an input. After completing an expression like 2+2, you do not need to input the result if you want to use it. The result would show up as 4 on the display and the program automatically converts the result into the first input of a new expression if an operator button is pressed. If you do not wish to use the result of the previous expression in a new expression you will have to press the clear button to reset the inputs back to 0. A history log of the past use can be stored if you click the save button located to the left of the display before ending the program. 

# Requirements
1 and 2 are straightforward, #3 is met in my themes list located on line 18. #4 is met on line 21 with my information dictionary. #5, I imported breezypythongui, random, and I believe I covered using tkinter in the breezypythongui file when I had to research and insert parameters in order to customize the background and foreground of my buttons. #6, is covered on line 29 where I open the file for writing, followed by inside my execute function where the text is written to the file and also within the save function where the file is closed. #7 is covered inside the execute function within the division portion since you cannot divide by 0, I made sure the program would still function if it were tried. #8 if/elif were used inside every function. #9, Again I think I covered this portion within breezypythongui when I had to learn some tkinter and implement it so I could change the colors. 

# Screenshots
![SS1](https://user-images.githubusercontent.com/75189383/102127461-266dde00-3e12-11eb-917e-0511c876d378.png)
![SS2](https://user-images.githubusercontent.com/75189383/102127633-5cab5d80-3e12-11eb-88fc-75fc4468f16e.png)
![SS3](https://user-images.githubusercontent.com/75189383/102127684-6765f280-3e12-11eb-9635-01d701e27d39.png)
![SS4](https://user-images.githubusercontent.com/75189383/102127719-73ea4b00-3e12-11eb-88ab-d8d0b6222c85.png)
![SS5](https://user-images.githubusercontent.com/75189383/102127737-7d73b300-3e12-11eb-95b5-eac7b824ff3b.png)
![SS6](https://user-images.githubusercontent.com/75189383/102127747-7fd60d00-3e12-11eb-8577-11e8a9c89430.png)
![SS7](https://user-images.githubusercontent.com/75189383/102127756-819fd080-3e12-11eb-93c2-e0ff82bc43ef.png)
![SS8](https://user-images.githubusercontent.com/75189383/102127764-82d0fd80-3e12-11eb-844b-563b758ea42d.png)
![SS9](https://user-images.githubusercontent.com/75189383/102127765-84022a80-3e12-11eb-9f77-ac5bfaba2e60.png)
![SS10](https://user-images.githubusercontent.com/75189383/102127773-86648480-3e12-11eb-8072-5eb11ae77eaf.png)
![SS11](https://user-images.githubusercontent.com/75189383/102127776-8795b180-3e12-11eb-8e57-d7aaf97ec737.png)

# Personal Reflection
I had a lot of fun with this project at first, but once I got into the middle of it I was starting to have troubles and things weren't working the way I thought they were going to in my head so I got stuck. I ended up spending a lot of time just trying to figure out how to the change the colors on my buttons because that wasn't included in the base breezypythongui module. I got to a point where I was just trying different things to see if they worked and eventually I found a way to get everything to come full circle and I ended up really enjoying myself. It turned out the way I wanted it to even after doubting my knowledge. 
