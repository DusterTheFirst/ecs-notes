# Introduction

[Jump to TL;DR (summary)](#too-long-didnt-read)

Welcome to the wonderful world of python.
Python is a very different language than scheme/racket which we have used so far.
Almost all of the syntax (or the structure of the language) will be different than how
we have done previous.

Below is a more in depth dive into each aspect of the language

## Math

Unlike scheme which uses prefix notation for mathematical operations such as `(+ 6 8)` which would
add 6 and 8 together. Python on the other hand uses infix notation such as `6 + 8`
which is much more similar to the mathematical notation you have learned before.

To add, subtract, multiply, and divide in python you would do the following:

```python
{{#include introduction.py:3:17}}
```

As well as the usual operators, python has a few others.

In math class or when using a calculator, it is common to represent an exponent with the `^`
character ex: `2^6` would represent 2 to the power of 6, but that is not the case in python. The `^`
character already has a meaning as the [XOR] operator, which does not matter for this class yet, but
is important to note that python will not throw out code that uses the `^` character but will just
produce a weird value. Instead, python uses 2 multiplication symbols to denote exponentiation: `**`.
Some more examples are below.

```python
{{#include introduction.py:20:21}}
```

Sometimes when you divide, you might not care about the decimal or fractional portion of the result
and for that use case, python has the double division `//` operator for "integer division" or
division without decimals

```python
{{#include introduction.py:24:25}}
```

And when dividing you might only care about the remainder and for that, python has the modulo `%`
operator.

```python
{{#include introduction.py:28:29}}
```

### More Math

Sometimes you need more than just the simple operations and for that, python has the math library.
The documentation for the math library can be found [on the official python docs][python-math-docs]
but python is a very popular language and is very easily google-able. Do not hesitate to use the
internet whenever you need to reference some docs or look something up.

In order to use libraries, you need to `import` them. To import the math library you would do as
such:

```python
{{#include introduction.py:34}}
```

Functions from a library can be used by putting the library name, a dot, and then the name of the
function. ex: `math.sin()` would be the sin function in the math library

Here are a few useful but non-exhaustive list of the functions available from the math library.

```python
{{#include introduction.py:36:55}}
```

Once again, the [docs][python-math-docs] have an exhaustive list of all methods available from the
library.

## Booleans

Just like in scheme, we can also deal with true/false conditions or booleans. These are also used
in python, although their names are capitalized:

```python
{{#include introduction.py:60:61}}
```

Just like in scheme, we can also do logical operations with the booleans, such as `and` and `or`
which are used much like they are in scheme, just in infix notation instead of prefix notation.

```python
{{#include introduction.py:63:77}}
```

There is also a less common logical operation called `xor` or `eXclusive OR` which you may never
have to use, but is good to know. It will return `True` if one and only one of the inputs is `True`
which can be seen below.

```python
{{#include introduction.py:80:83}}
```

## Conditionals

When dealing with numbers, we may want to check if some *condition* holds true. There are 2
different types of conditionals, equality and inequality. You may remember these from your math
class, but if not here is a refresher.

Equality is the comparison of 2 exact numbers, such as `_ is equal to _` or `_ is not equal to _`.
Equality can be expressed in python as such:

```python
{{#include introduction.py:88:92}}
```

Inequality is checking the relation of 1 number with respect to another or `_ is greater than _` or
`_ is less than _`. These operations can be expressed in python as such:

```python
{{#include introduction.py:95:105}}
```

## Strings

Similarly to scheme, strings, which are just text, can be created using quotation marks (`"`) aka
double quotes. But unlike scheme python also lets you use apostrophes (`'`) aka single quotes to
surround your text. Both act exactly the same.

```python
{{#include introduction.py:110:111}}
```

When using double quotes, you are allowed to use apostrophes in the text as usual

```python
{{#include introduction.py:113}}
```

And when using single quotes, you can use double quotes inside of the text with no problem

```python
{{#include introduction.py:114}}
```

When you want to use both in one string, things get a bit more complex. The quotes that you write
around your string, signal to the language that everything inside of it is text, but when the text
contains the same quote you used to tell the language about the text, the language will mistakenly
see it as you ending the string.

You can see this in the syntax highlighting (coloring) of the code below changing after that quote,
meaning that python would not read this how we wanted.

```python
"They're having a lot of fun and yelling "yippee""
'They're having a lot of fun and yelling "yippee"'
```

To get around this issue, we can use what is called "escaping quotes". If you want to use the
character that you used to make a string (ie. `'` inside a single quoted string or `"` inside a
double quoted string) you can put a backslash `\` character in front of it to tell the language to
treat it as part of the string.

```python
{{#include introduction.py:117:118}}
```

Note the colors staying the same throughout the string. Both strings above are exactly equal, the
only difference is what quote we are using.

Sometimes it is useful to combine 2 strings, and python allows us to do so using the `+` operator.

```python
{{#include introduction.py:121}}
```

We may also want to create a string that has multiple lines of text. We can do so using a multiline
strings which are defined using 3 double quotes

```python
{{#include introduction.py:124:127}}
```

You can also use the newline character `\n` instead to denote multiple lines in a string

```python
{{#include introduction.py:129}}
```

The above 2 strings are exactly equal, they are just different ways of writing them

## Comments

A lot of the time, code is complicated.
[Reading code is 2x harder than writing that same code.][harder-to-read-than-write]
To help ourselves with our programming, programming languages have comments, or lines/sections of
code that are not read by the language, but instead by the programmer. I have been using comments in
these notes with notes and information on what is in the code that I am showing you. These comments
are denoted by a different, dimmer color than the rest of the code.

Comments in python are denoted using the pound sign `#` aka hash or hashtag.

```python
{{#include introduction.py:133}}
```

Comments can appear after code, but any text after the `#` is interpreted as a comment.

```python
{{#include introduction.py:135}}
```

If you want a comment that spans multiple lines, you can use a multiline comment which will just get
ignored when you run the program since you do nothing with it

```python
{{#include introduction.py:137:140}}
```

But it is probably better to just use multiple comments, one per line <sup>like a sane person</sup>

```python
{{#include introduction.py:142:144}}
```

## Turtle

You cant have a programming lesson without a bit of fun, so here is our fun for this lesson. We get
to draw! yaay woot woot.... Just me? ok...

In python, we can use the turtle library. The documentation for the turtle library can be found
[on the official python docs][python-turtle-docs] Just like with the math library, we have to
`import` the library to use it.

```python
{{#include introduction.py:149}}
```

With all good art, we need color, so we can go ahead and set the color of the turtle with the color
method

```python
{{#include introduction.py:152}}
```

To move the turtle, we have 2 options. We can either move in a direction, ie `forward`, `backward`,
or we could move to an exact position.

```python
{{#include introduction.py:154:160}}
```

The coordinates of the canvas that we can draw on are on the x axis, -180 to 180 and on the y axis,
-200 to 200. The center of the screen being 0,0.

We can also stop the turtle from drawing a path, or change its color mid stroke using the functions
below.

```python
{{#include introduction.py:162:165}}
```

Once again, the [docs][python-math-docs] have an exhaustive list of all methods available from the
library.

Remember, python is very google-able, please feel free to google to your heart's content.

## Too Long; Didn't Read

If you want an abridged version, you can look at just the code that I have gone over
[here][python-code]

[python-code]: https://github.com/DusterTheFirst/ecs-notes/tree/main/src/python/introduction.py
[XOR]: https://en.wikipedia.org/wiki/Exclusive_or
[harder-to-read-than-write]: https://www.quora.com/Why-is-reading-code-much-harder-than-writing-it-How-can-I-read-code-and-understand-what-the-code-actually-is-doing-in-Python-to-be-precise
[python-math-docs]: https://docs.python.org/3/library/math.html
[python-turtle-docs]: https://docs.python.org/3/library/turtle.html
