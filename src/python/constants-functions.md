# Constants and Functions

[Jump to TL;DR (summary)](#too-long-didnt-read)

## Constants

Starting with some code from the introduction that draws a square

```python
{{#include constants-functions.py:2:10}}
```

We can see that our code is very repetitive. We call `turtle.forward` 4 times and `turtle.left` 3
times. We also give them all the same values to the functions over and over. We can start by getting
rid of the same value over and over and over again using constants, much like we have with scheme.

Constants in python are defined with all caps names and our constants would look something like

```python
{{#include constants-functions.py:16:17}}
```

Just like in scheme, we use all caps for our constants to show that they will never change. If we
wanted to have a constant with spaces in its name, we would write it like such

```python
{{#include constants-functions.py:32}}
```

And now that we have these constants defined, we can replace the numbers in our code with these
constants

```python
{{#include constants-functions.py:19:26}}
```

Now we just have one spot to change our size and angle if we want to draw a different shape or to
draw a different size. The code is still repetitive though. If we wanted to draw 2 squares, we would
have 14 lines of code. bruh :(. Instead, we can use

## Functions

Functions, which you are hopefully familiar with from scheme, are tools that allow us to group
blocks of code together which we can run and even give values to. In python, we follow the same
steps as in scheme when defining a function.

- Signature
- Purpose/Description
- ~~Tests~~
- Actual Function Body

Ok, we do all of them *except* tests. I know, it is so sad. They were my favorite part of
programming too.

Now that we have that out of the way, we can move our code into a function. We start with the
signature. Since this function is drawing a square, I think we should name it `draw_triangle`. No?
Ok... I guess we can call it `draw_square`. And we want our function to take in the size of the
square so that we can use it for <sub>small</sub> and **big** squares. Our function's signature
would look something like

```python
{{#include constants-functions.py:38}}
```

Although, yes, this function does not `return` an image per se, we will still put it down as such,
to clarify that the function will create an image on the screen. We will get into what it means for
a function to actually return a value later.

And now we can add our very, very complex description or purpose statement whatever you prefer.

```python
{{#include constants-functions.py:38:39}}
```

Now that we have the documentation out of the way, we can move onto the actual body of the function.
The function will basically be a copy and paste of our above code with some parts added to tell
python that it is a function.

```python
{{#include constants-functions.py:38:47}}
```

Here is a breakdown of the parts of a python function

```python
{{#include constants-functions.py:62:65}}
```

If we were to take in 2 inputs, we would put a comma in between them in the parenthesis

```python
{{#include constants-functions.py:68}}
```

Note that in the function, we have replaced `SIZE` with `size` since we are no longer using the
constant size that we defined before and instead are allowing us to specify the size of the square
when we call the function

> Python is what is called a "whitespace language" meaning that what the code means is heavily
dependant on the whitespace in the code.
>
> > Whitespace is a character that you can not see such as space or tab
>
> because of this, the indentation of your code matters. To specify that the code above is part of
the function, it needed to be indented one time. If we now wanted to write more code after, but not
inside of the function, we would have to un-indent the code which would look like so

```python
{{#include constants-functions.py:38:47}}

turtle.done() # This code is now not inside of the above function
```

To use our function that we have defined, we can now call it as such

```python
{{#include constants-functions.py:53:55}}
```

> Unlike in scheme where you can call/use a function from anywhere, in python, you must define a
function before you are able to use it, much like variables or constants. So the above code would
have to appear below the function we have made

## Designing a square root function

Now that we have designed a simple function, we get to do another one! yay!

This function we will define will find the square root of an inputted value

Lets walk down the steps of function definitions

- Signature

```python
{{#include constants-functions.py:74}}
```

- Purpose/Description

```python
{{#include constants-functions.py:75}}
```

- ~~Tests~~

No tests needed

- Actual Function Body

To make the function, we need to remember how to take a square root. If you remember from math
class, a square root is the same as raising something to the power of `1/2`, we can express that in
python with the following

```python
{{#include constants-functions.py:76}}
    n**(1/2)
```

If you remember back to the introduction, the `**` operator raises the number on the left to the
exponent on the right, so in this case, we are raising n to the power of `1/2` where n is the
inputted value to our function

Unlike scheme, python does not return anything from the function unless you explicitly tell it to
`return` the value. That is because in python, you can run multiple lines of code per function where
as scheme had you nest all of the function calls inside each other.

To be able to return the value, we need to add `return` before the value we want to return. Below is
the fully complete function

```python
{{#include constants-functions.py:74:77}}
```

Now we can use this function

```python
{{#include constants-functions.py:79}}
```

And we can assign the result to a variable as well

```python
{{#include constants-functions.py:80}}
```

But how to we show out this information to us? Im not too sure, but I have heard a bit about

## Printing Values to the Console

Python provides a function to us called print that will print out all of its arguments. This
function is a bit different than the ones that we have wrote so far in that it can take 0 or 100
inputs. Print will print out all of the inputs given to it. We use it like any other function that
we have before

```python
{{#include constants-functions.py:85:87}}
```

> Watch out! Although python is very google-able, there are 2 different versions of python: Python 2
and Python 3. There are a few syntax and other changes between these versions, one of these is the
layout of the print function. In Python 2, you would write `print "hello"` to print the string
hello. In the newer Python 3 that we use, we need to put parenthesis around the inputs to all
functions, so we would write `print("hello")`. **If you ever see the old way of printing, look
around for a newer source since the source you are using may be outdated, or just replace the old
style of prints with the new style.**

## Returning Nothing

When writing a function, we may want to not return anything from it since we might print to the
console or draw using a turtle. In that case, we need to mark the function as returning `(void)`.

We will use a simple function that prints a greeting to the name that is given ie.
`print_greeting("Zach")` would print `Hello Zach` to the console as an example for this.

The function signature and usage would look as follows

```python
{{#include constants-functions.py:94:99}}
```

> Make note of the un-indentation of the last line, meaning that it is not inside of the function
above it.

The main change we have made is the return type being `(void)` to tell us that this function returns
nothing.

Since this function returns nothing, we cannot get a value from it/assign it to a variable

```python
{{#include constants-functions.py:102:103}}
```

If we instead wanted to be able to use and manipulate the greeting before printing it out, we would
need to make our function return the greeting instead of printing it. Since it now returns the
greeting instead of printing it, we can rename it to `get_greeting`.

```python
{{#include constants-functions.py:111:116}}
```

Note that the last line does not print anything to the console, and instead just will return the
greeting for use to use later in our program. We can use the value like so

```python
{{#include constants-functions.py:119:120}}
```

## Mutation

This is a very common feature that scheme intentionally did not let us use, and that is because it
has a lot of quirks, but can also be very useful.

We can define variables like such

```python
{{#include constants-functions.py:125}}
```

And in python, we can now change that variable.

```python
{{#include constants-functions.py:125:127}}
```

So in the console, we will see the number 10, since `x` was changed from 7 to 10

Sometimes we don't want to change a variable to an exact value, but instead change it relatively
such as adding 5 to it. Python lets us to so in 2 ways. The obvious way would be to do something
like

```python
{{#include constants-functions.py:138}}
```

But python gives us the tool to do it a bit more concisely using

```python
{{#include constants-functions.py:142}}
```

Python lets us do this with all of the operators gone over in the introduction, here is an example
of a few of them.

```python
{{#include constants-functions.py:146:148}}
```

Weirdly, we can use these with strings too

```python
{{#include constants-functions.py:151:154}}
```

## Mutation Madness

Say we have this function

```python
{{#include constants-functions.py:162:165}}
```

And this code that deals with the function

```python
{{#include constants-functions.py:168:170}}
```

What do you think this would print?

<details>
<summary>Click for the answer</summary>

This would print out 10.

The x in the function and the x in the code outside of the function are not the same variable. Yes
they have the same name, but the one inside of the function could just as well be named `n` or
`jeff`.

The variables that are passed to a function cannot be modified by the function. But they can modify
the data in the function themselves.

If we wanted to actually give the changed value back to the code that called this function, we would
need to return it back out.

```python
{{#include constants-functions.py:180:184}}
```

And when we use the function, we would need to do the following:

```python
{{#include constants-functions.py:187:189}}
```

</details>

## Exercise

Given these functions

```python
{{#include constants-functions.py:194:203}}
```

And this code that uses the above functions

```python
{{#include constants-functions.py:206:214}}
```

What would be printed to the console

<details>
<summary>Solution</summary>

```python
{{#include constants-functions.py:216:229}}
```

</details>

## Too Long; Didn't Read

If you want an abridged version, you can look at just the code that I have gone over
[here][python-code]

- Functions are defined with the `def` keyword and look something like

```python
{{#include constants-functions.py:74:77}}
```

- Similarly to scheme, `CONSTANTS_LOOK_LIKE_THIS` and `variables_look_like_this` the only difference
is the underscores `_` versus the hyphen `-`
- Still follow the [help-sheet]'s rules for defining functions, just skip the test step for now
- Variable's values can be changed

```python
{{#include constants-functions.py:125:127}}
```

- Inside of a function, variables do not modify the variables that were passed in
(see [Mutation Madness](#mutation-madness))

[python-code]: https://github.com/DusterTheFirst/ecs-notes/tree/main/src/python/constants-functions.py
[help-sheet]: ../help-sheet.md
