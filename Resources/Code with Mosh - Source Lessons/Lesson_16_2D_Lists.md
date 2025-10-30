# Lesson 16: 2D Lists

**Video Timestamp:** 2:01:44–2:05:04  
**Week:** Week 11  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

In this tutorial I'm going to show you how to use y loops in python. We use y loops to execute a block of code multiple times and there are often useful in building interactive programs and games. In a future tutorial I'm going to show you how to build a simple game using a y loop. So, let's get started with the basics, we write a y statement and right after that, we type a condition followed by a colon as long as this condition is true the quote that we write in this block will be repeatedly executed. Here is an example. We can define a variable like i, as in short for index and set it to 1. Now we set our condition to i less than or equal to 5, so as long as I is less then or equal to 5, we can print i, on the terminal. And then we need to increment i, by 1. So we set i to i plus 1. The reason we do this is that if we don't do this I will be 1 forever so we'll end up with an infinite loop. Because this condition will always be true. One is always less then 5, so in every iteration of this loop, we increment i by 1, so at some point, i is gonna be six and then that is when this condition will be false and then we'll jump out of this loop, okay? Now to demonstrate how everything works after this loop I'm going to add a print statement say done. So note that these two lines are indented so they are part of the y block. Okay, now let's go ahead and run this program and see what happens. So, take a look, we get the numbers 1-5 followed by done. So heres how this program gets executed first we set i to 1 now python interpreter executes line 2, this condition is true because i is less then 5, so i is printed on the terminal and then incremented by 1. Then the control moves back to the beginning of the y loop. So it doesn't go to the next statement. So, we come back here and now we are in the second iteration. In the second iteration i is 2, and because 2 is less then 5, our condition is still true, so i will be printed on the terminal, and once again it will be incremented by 1, so at some point i is going to be 6, and that's when this condition will be false so our look will be terminated and this done message will be printed on the terminal. So this is the basics of y loops. Now let's make this program a little bit more interesting. Here we can write an expression like this. We add a string, and in this string we add an asterisk and then we multiply this string by i. So with this expression, we can repeat a string, when we multiply a string by a number, that string will be repeated. For example, if i is two, this expression will produce a string with two asterisks. Now let's run the program and see what we get. So we see this little triangle shape here. Because in the first iteration i is 1, so, 1 times an asterisk produces 1 asterisk. In the second iteration i is 2, so when we multiply 2 Building a Guessing Game by 1 asterisks, we'll get 2 asterisks. In this tutorial I'm going to show you how to use a y loop to build a guessing game like this. So we have this secret number which is currently set to 9. Now the computer is asking me to make a guess. So, let's say 1 is not right because the secret number is 9, okay, try again, 2, no it's not right, let's try again, so I only have three chances to make a guess. If I can't guess the number the program tells me that I failed. let's run the program one more time, this time I'm going to guess the number, it's 9, there you go, it says you in. So let's go ahead and build this program using a y loop. Alright, let's start by defining a variable to store our secret number so, we call the secret underline number and set it to 9. Now we need a while loop to repeatedly ask a user to make a guess. So while condition colon What is our condition here? Well we want to give our user a maximum of three guesses. So similar to the last tutorial, we can define a variable like I, set it to 0, and assume this represents the number of guesses the user has made. And then we write our condition as i less then 3. Note that here I'm not using less then or equal to operator, because with this condition our loop will be executed 4 times, while i is 0, one, two, and three, so here we should use the less then operator. Now if we give this code to someone else it's unclear what does i represent here, it's only in our head that i represents the number of guesses the user has made. So as a best practice, always use meaningful and descriptive names for your variables. So it's better to rename this variable to guess, count. Let me show you how to rename. So right click on i variable, and then go to refactor and rename it. Look at the shortcut. On a Mac computer it's shift and f 6. Now in this dialogue box we can easily rename your variable and pycharm will update all the references to that variable so we don't have to manually update each instance, okay? Let's change this to guess\_count enter, there you go, now that is better, also it's better to store 3 in a separate variable to make our code more readable, because it's not quite clear what does 3 represent here. So, let's define a variable called guess limit say to 3, and then we can change 3 to guess underline limit, now our code is more readable while guess count is less then guess limit, see it reads like a story this is how you should write code. Okay, so while this condition is true, we want toast the user to make a guess. So here we use our input function, guess Now whatever the user enters comes out as a string so we need to convert it to an integer. So right here, we pass the result to the end function and then get it and store it in a separate variable called guess. So at this point the user made a guess, now we need to increment guess count so guess count we set it to plus equal 1 or okay, now we need to check to see if the user will make the right guess. So here we need an if statement. If what the user guessed equals our secret number, again see our code is so readable. It's like a story you can read it like plain English. So if this condition is true we want to tell the user they won. So print you won now lets go ahead and run our program up to this point. So okay it's asking me to make a guess, I'm going to make the wrong guess so one it asked me again, 2 one more time, 3, okay, what is missing in this implementation is the message that tells me that I failed. We're going to take care of it momentarily, but let's run the program one more time and make the right guess. So, 9 okay it says you won, but it's still asking me to make a guess, because our while loop is going to get executed 3 times. Look 1 and 2. So we need to change our program such that if the user makes the right guess, we need to terminate our while loop, we need to jump out of it. How do we do that? So, over here if the user makes the right guess, after we print this message we can use the brick statement to terminate terminate a loop, when python interpreter sees this, it's going to immediately terminate our loop, it's not going to evaluate this condition again. Now let's run our program and see what happens. So, I'm going to guess the right number, you won and look, you are now asked to make two more guesses, beautiful. Now the last thing we need to add here is the message that tells the user that they failed if they could not guess the right number. How do we do that? Well in Python our while loops can optionally have an else part. similar to the if statements. So earlier you learned that our if statements can optionally happen else part. Here, so if this condition is true, do this, otherwise do something else. In this case our if statement doesn't have an else part. Now, similar to the if statements Our while loops, our while statements can also have an else part. So, right at this level we can add an else block, so else colon. And the code that we write here will get executed if this while loop completes successfully without an immediate break. In other words. If the user guesses the right number, you break this loop, you jump out of it so the code that we write in the else block will not get executed. But if the user cannot guess this number, you're never going to break out of this loop, so this loop will be executed to completion untill this condition become false. In that case, the code that we write in the else block will get executed, and this is the perfect opportunity for us to tell the user hey, you made three guesses but none of them were right. So, print, sorry you failed. Now, let's test the program one more time. So, guess 1, 2, 3, sorry you failed, let's run it one more time. This time I'm going to make a wrong guess, and then the right guess, we won and our loop terminated immediately. Building the Car Game Alright, now it's time for you to practice what you have learned so far. So once again we're going to build a game this game is a simulation card game. Now our game doesn't have a graphical user interface or gooey and it doesn't really matter for now, our focus is entirely on building the engine for this game. So let's see how this works. When we run this, we get this little symbol here, and our program is waiting for us to enter a command. If you type help either a lower case or upper case we get the list of commands that our program or our game currently supports. So we can type the start command to start our car, we can type stop command to stop our car, and quit to terminate the game. Any other commands that we type our program is going to tell us hey I don't understand that. For example, if I type asd here, it's going to say I don't understand that.If you type start, we get this message, car started, ready to go, if you type stop it says car stopped, and finally if we hit quit our program terminates, this is a fantastic exercise for you to practice wha you have learned, so pause the video and spend 5-10 minutes to build this program. Alright, we're going to start with a while loop with a condition What is our condition here? We want to run this loop until the user types quit. So we can define a variable or a story to command what the user enters, and then we can run this loop as long as the command does not equal to quit. So right before the loop, we define a variable, command, and initially we set it to an empty string. An empty string is a string that has no characters in it. We only have the quotes. So then we type out our condition as while command does not equal to quit then do something. Now immediately we have a problem here because we're assuming that the user types the command in lower case, so if they type this in upper case they our program is not going to behave properly, so to fix this problem, you need to call the lower method of the string object and then compare the results. With this quit. You could also call this upper and then type quit in upper case. It's about our personal preference in this demo I'm going to use lower case characters. So, okay, now in this loop we need to ask the user to enter a command. So once again we're going to use our input function, we're going to add a greater then symbol followed by a space, whatever the user enters, we get it and store it in our command variable. Now apart from quit command, there are three other commands that we need to support. Start, stop, and help. So here we need an if statement to compare what the user enters with one of the supported commands. So, if command.lower equals start then you want to print the message like the car started. So print the car started. Ready to go, it doesn't matter, now the second condition. What if its not start, maybe it's stop? So, el if command.lower equals stop, there you go, then we print a different message car stopped. Now look at our code. We have repeated this lower lower lower multiple times. This is bad, in programming we have a term called dry, which is short for don't repeat yourself. So whenever you have duplicate your code that means you're doing something wrong. So how can we solve this problem. Well, instead of calling the lower method in each condition, we can call it right here when we get the input from the user, so this input function as you know returns a string, we can immediately call the lower method on this string, and with this command will always be in lowercase, so we don't need to call this method in every condition. Look, we remove the duplication and also our conditions are shorter and easier to read. There is also one more place we need to modify so, it's right here. That is better. Now, the third command. We need one more el if. If the command equals help, then, we want to show the commands that we support. So, here we're going to print a multi line string. So we use triple quotes like this, and give the user a guideline like this. So start to start the car stop to stop the car, and quit to quit. Now finally we need an else part, so if what the user enters is none of these commands, we're going to tell them, hey we don't understand these, else, colon print sorry I don't understand that. And by the way note that here becomes I'm using double quotes, I can easily use a single quote as an apostrophe, okay? So let's run our program up to this point and see what happens. Alright, let's type start car is started, beautiful, stop, car is stopped, help, we get this guideline, but there's so much indentation before our commands, we'll fix that in a second. And finally let's test the quit command, oops, our program didn't work properly. Here is the reason. With these if statements, we're comparing the command with start stop, and help. Anything else will end up here, so that's why our program says it doesn't understand that. So that's why our program says it doesn't understand that command. However, after this el statement the control will be moved to the beginning of the loop. At this point our command is quit, so our loop will complete and the program terminates. In other words when we run this program and type quit, our program actually quits but we still see this message which shouldn't appear here. How can we solve this problem? Well, we can come back here and just before the else block, add another el if, something like this. el if command equals quit then you can immediately break. This will solve our problem, but note that we have kind of repeated this expression in two places. The reality is that we don't really need this condition on the top, because with these if statements well more accurately with this el if we can jump out of this loop and terminate our program. So, we can simplify our condition to something like this. True. So while true means this block of code is going to get executed repeatedly, until we explicitly break out of it, okay? Now let's test our program one more time. So, quit now our program terminates and we don't see that message beautiful. So let's fix the last problem. You saw that when we typed help, these guidelines appeared with so much in indentation, and here's the reason, look, right here in our code, they are already indented. So when we use triple quotes, what we type here will be printed exactly as is. So, because we have an indentation here, this indentation will also be printed on the terminal. So, let's delete these okay, run the program one more time, type help, the indentation is gone. Beautiful. Now here's a challenge for you. I want you to take this program to the next level. So right now if we type start we get this message car started. And if we type start again we get the same message. It would be better if we got a message like car is already started so it doesn't make sense to start a car twice. Similarly, if we type stop it says car stopped, if we type it again we get the exact same message, it doesn't make sense to stop the car twice. So here's what I need you to do if the car is stopped and the user tries to stop it again, the program should say hey, the car is already stopped, what are you doing? And similarly if the car is already started and the user tries to start it again, the program should yell at the user. So go ahead and make the necessary changes to implement this scenario. Alright to add this to our program, we need to know if the car is started or not. So there is one more piece of information we need to store in the memory. What is the kind of data we need to store here? A boolean. Is the car started or not, it's a matter of yes or no. True or false. So on the top, here we can define another variable like started and initially we set it to false. So the car is not started, right? Now when the user types the start command, here we need to check to see if the car is already started. If not the we'll start it or otherwise we'll yell at the user. So in this block we'll write another if statement, if it's already started and we print car is already started. Otherwise, so if you add an el statement here. And at this point, you set started to true. So we start the car and we print this message, okay? Now we need to make a similar change for the stop command. So if the car is already stopped we need to print a different message. If not started, so here we're using the not operator to see if the car is stopped. So if it's not started that means it's stopped, okay? So if it stopped we print car is already stopped with double p's, otherwise so else we need to stop the car, how do we do that? We set started to false. And then we'll print this message. As easy as that. Let's go ahead and run our program. So, initially our car is stopped. So I'm going to type stop, it says the car is already stopped, so lets start it, okay, now our car is started, let's start it one more time. The program is yelling at us. So we can not start the car twice. Beautiful. Now let's stop it it says the car is stopped, let's stop it one more time, we get this message



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand 2D list structure**
- Define a **2D list** as a list containing other lists (a list of lists)
- Recognize that 2D lists represent tabular data like matrices or grids
- Visualize 2D lists as rows and columns

**Create 2D lists**
- Create 2D lists using nested square brackets
- Initialize 2D lists with specific dimensions and values
- Understand that each inner list represents a row

**Access 2D list elements**
- Use double indexing `matrix[row][column]` to access specific elements
- Understand that the first index selects the row, the second selects the column
- Use negative indices to count from the end in either dimension

**Iterate over 2D lists**
- Use nested `for` loops to process all elements
- Use an outer loop for rows and an inner loop for columns
- Access both row and individual element values during iteration

**Recognize common pitfalls**
- Remember that `matrix[i][j]` accesses row `i`, column `j`
- Avoid index errors by staying within valid row and column bounds
- Understand that modifying one row doesn't affect other rows (unless they share references)
- Be cautious when creating 2D lists with repetition (e.g., `[[0] * 3] * 3` creates shared references)

## Key Terms

- **2D List (Two-Dimensional List)** — A list that contains other lists, forming a grid or matrix structure
- **Matrix** — A mathematical term for a 2D array of numbers; represented by 2D lists in Python
- **Row** — A horizontal sequence of elements in a 2D list (each inner list)
- **Column** — A vertical sequence of elements across multiple rows
- **Nested List** — A list inside another list
- **Double Indexing** — Using two indices to access elements in a 2D structure (e.g., `matrix[row][column]`)
- **Nested Loop** — A loop inside another loop, commonly used to traverse 2D lists
- **Multidimensional Array** — A general term for arrays with more than one dimension
- **Grid** — A visual representation of data arranged in rows and columns, like a 2D list
- **Element Access** — Retrieving a specific value from a data structure using its position


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Create a 2D List (Matrix)

**Description:** Create a 2D list representing a 3x3 matrix.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
print(matrix[1][2])
```

**Expected Output:**
```
2
6
```

### Task 2: Modify 2D List Elements

**Description:** Change an element in a 2D list and print the row.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0])
```

**Expected Output:**
```
[1, 20, 3]
```

### Task 3: Iterate Over 2D List

**Description:** Use nested loops to print all elements in a 2D list.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
```

**Expected Output:**
```
1
2
3
4
5
6
7
8
9
```

---

## Teaching Notes

### Key Concepts
- [To be added by instructor]

### Learning Objectives
- [To be added by instructor]

### Common Student Mistakes
- [To be added by instructor]

### Practice Exercises
- [To be added by instructor]

---

*This transcript is sourced from Code with Mosh's "Python for Beginners" video tutorial.*  
*Video link: https://www.youtube.com/watch?v=_uQrJ0TkZlc*
