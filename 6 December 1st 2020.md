# Recursion and balloon game
[Jump to TL;DR (summary)](#too-long-didnt-read-december-1-2020)\
[Jump to Table Of Contents](#file-1-ecs-notes-md)\
[Starting code for this lesson on wescheme](https://www.wescheme.org/openEditor?publicId=5L8j5dHY5S)

# Starting with the balloon game
We left off writing a game where the user can make balloons which will fly upwards.
Our game worked and was great, but there is a slight problem, we can only have 2
balloons at a time, and that sucks. We want all the balloons!!!

Currently our Balloon game type is as follows:
```scheme
; A BalloonGame is one of:
; - false (no balloons)
; - Posn (balloon)
; - (make-twothings Posn Posn)
; and represents either a screen with no balloons, a screen with a balloon,
; or a screen with two balloons
```

As we can see, there are the 3 variants, no balloons, one balloon and 2 balloons.
If we wanted 3 balloons what could we do? One option would be to make a 4th variant
and make it something like:
```scheme
; - (make-threethings Posn Posn Posn)
```

But that method has a problem. First off, we need to make another whole data type `threethings`
and making data types is *so **not** lit*. Another problem with this method is every single time
we want to add another balloon, we have to make another variant, and a whole new data type. ***UGH***.

What if I told you ~~that you lived in a simulation~~ that there is a way to make a data definition that
can hole *infinite* amounts of data.

# Recursive data structures
You saw this coming if you read the title, but what you might not have known is what in the gosh darn
is this fandangled recursion thing? Well, I can hit you with what my friend Merriam Webster says:
```
recursion (noun)
re·​cur·​sion | ri-ˈkər-zhən
    
    a computer programming technique involving the use of a procedure,
    subroutine, function, or algorithm that calls itself one or more
    times until a specified condition is met at which time the rest
    of each repetition is processed from the last one called to the
    first 
```

Ok webster, that's cool and all, but like ***HUH?*** what do all those words mean. *Procedures*?
*Subroutines*?

It looks like Mr. Webster is a bit too verbose for us, let be break it down.

Recursion is when some *thing* does itself multiple times. In terms of scheme and our programming
knowledge, there are 2 places where we can use recursion. Functions and structures.

A data structure is recursive when one of the parts of it is the data structure itself. A way to
visualize it is to think of russian nesting dolls. Each doll has its outer shell with the paint and
the nice artwork, but if you look inside of them, they have a whole new doll inside. 

# Too Long; Didn't Read (December 1 2020)
- [Final Product](https://www.wescheme.org/openEditor?publicId=4CXe2en4jH)
- Recursion is the method of nesting something inside of another of that same thing
    - We can have recursive data structures (A structure that contains itself) (think of a russian nesting doll)
    - We can have recursive functions (A function that calls itself)
- With all recursive things, you ***MUST*** have an 'escape'
    - Recursive data structures must have a variant to signal that the recursion is finished (our false case above)
    - Recursive functions must have a way to not call themselves again, so they must contain a cond/if with at least one branch not calling themselves
- If you do not have this escape from recursion
    - Your data structure would be infinitely large since it would forever contain 1 more of itself which would contain 1 more of itself which ....
    - You function would never be done running since it would forever call itself which would call itself which would call itself which would ....

[Jump to Table Of Contents](#file-1-ecs-notes-md)