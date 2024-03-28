# CS50P Final Project Habit Tracker
## Description
A simple CLI Habit Tracker built in python

### `project.py`
The project has 6 functions.
* The `main()` function is used for navigating to the other functions and operations through switch case.
* The `createcsv()` function creates a Habits.csv file if it doesn't already exist which is used to store all user data. This function was very difficult as early iterations of it did not work on linux but did work on windows, any way I tried to create a file was met with a sad and swift error but finally in the end through the divine hand of god the function started to work. I have no idea why it didn't work previously. I looked at documentations for hours and consulted many an AI bot all which made me believe that my implementation was correct but it still refused to work, maybe it got a joy out of my suffering I don't know. there were points where I wanted to give up on this functionality but I knew that the UX tradeoff that would come with that decision would be far too great too bear so with a heavy hand I struggled through but in the end I did it.
* The `clear()` method clears the screen to make the output prettier and more usable. It checks the operating system and uses relevant shell command to clear the screen. seeing all the functions previously performed would get annoying to look at and served no purpose so this function was born.
* The `create()` method is used to create new habits. it queries the user for the name of the habit and it's frequency in a week and asks you the days of week the habit should be repeated. it automatically fills in the day the habit was started. Initially the day was supposed to calculate how many days until today should have been logged but I realised that updating that every time the program is launched would be unecessary and the date already does a fine job of displaying how long it has been since the start of the habit. Including the amount of would be logs would also lead to focusing on missed days demotivating the user from continuing the habit whereas the log motivates them further.
* The `log()` method displays the user all the habits that need to be done on the day and queries them for the ones they have done upon receiving thee input it updates the logs for it. the method copies the entire file as a list modifies it and then overwrites the original. This was done because I discovered that you can't modify csv objects, you can add but you can't modify.
* The `view()` method generates pretty tables to view all your habits and relevant info using tabulate.
* the `tod()` method expects a list of days and a date and verifies if the date's day is in the list.

### `test_project.py`
The tests for this might just have been the most difficult thing I've ever done. The tests started to feel harder than the project during some points but then i remembered the `createcsv()` function and all such thoughts disappeared. The tests emulate normal usage. 
* First it creates a file and checks it's existence.
* It then creates a habit and checks the csv file for it
* Then it logs a habit and checks if it worked
* It then views the habit to check if it works properly
* There's also a test for `tod()`

There was no difficulty in figuring out what to test the difficulty was in the how. I used unittest.patch to simulate human input. It was hard to learn how to do this as the python documentation is abhorent and could possibly lead to someone unlearning the language. After I figured out how to do that I started to get `StopIteration` error which occurs when you don't have enough inputs. I checked again and again counting all the calls for input and their exact order to make sure I wasn't messing anything up. I learned that i needed to use `itertools.cycle` to load the inputs. And after all that suffering it was finally done

## How to use
```
pip install -r requirements.txt
python project.py
```

[Youtube Video](https://youtu.be/rBtb075Zbw8)
