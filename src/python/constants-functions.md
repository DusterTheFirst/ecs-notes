# Constants and Functions

[Jump to TL;DR (summary)](#too-long-didnt-read)

## Constants

Starting with some code from the introduction that draws a square

```python
{{#include constants-functions.py:2:10}}
```

We can see that our code is very repetitive. We call `turtle.forward` 4 times and `turtle.left` 3 times.
We also give them all the same values to the functions over and over. We can start by getting rid of
the same value over and over and over again using constants, much like we have with scheme.

Constants in python are defined with all caps names and our constants would look something like

```python
{{#include constants-functions.py:16:17}}
```

Just like in scheme, we use all caps for our constants to show that they will never change. If we wanted
to have a constant with spaces in its name, we would write it like such

```python
{{#include constants-functions.py:32}}
```

And now that we have these constants defined, we can replace the numbers in our code with these constants

```python
{{#include constants-functions.py:19:26}}
```

Now we just have one spot to change our size and angle if we want to draw a different shape or to
draw a different size. The code is still repetitive though. If we wanted to draw 2 squares, we would
have 14 lines of code. bruh :(. Instead, we can use

## Functions

Functions, which you are hopefully familiar with from scheme, are tools that allow us to group blocks
of code together which we can run and even give values to. In python, we follow the same steps as in
scheme when defining a function.

- Signature
- Purpose/Description
- ~~Tests~~
- Actual Function Body

Ok, we do all of them *except* tests. I know, it is so sad. They were my favorite part of programming
too.

Now that we have that out of the way, we can move our code into a function. We start with the signature.
Since this function is drawing a square, I think we should name it `draw_triangle`. No? Ok... I guess
we can call it `draw_square`. And we want our function to take in the size of the square so that we
can use it for <sub>small</sub> and **big** squares. Our function's signature would look something like

```python
{{#include constants-functions.py:38}}
```

Although, yes, this function does not `return` an image per se, we will still put it down as such, to
clarify that the function will create an image on the screen. We will get into what it means for a function
to actually return a value later.

And now we can add our very, very complex description or purpose statement whatever you prefer.

```python
{{#include constants-functions.py:38:39}}
```


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

- Inside of a function, variables do not modify the variables that were passed in (see [Mutation Weirdness](#mutation-weirdness))

[python-code]: https://github.com/DusterTheFirst/ecs-notes/tree/main/src/python/constants-functions.py
[help-sheet]: ../help-sheet.md