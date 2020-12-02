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
visualize it is to think of russian nesting dolls (also called Matryoshka):

<details>
<summary>Click To Expand Images</summary>

![Image 1](https://m.media-amazon.com/images/S/aplus-media/sc/d88c17bc-2edd-430f-8786-fe2569db8f3a.__CR0,171,1716,1061_PT0_SX970_V1___.jpg)
![Image 2](https://cdn.shopify.com/s/files/1/1659/7413/products/Authentic-Russian-Nesting-Doll-Apples-2-947841_1200x1200.jpg?v=1571439509)

</details>

Each doll has its outer shell with the paint and
the nice artwork, but if you look inside of them, they have a whole new doll inside.

This outer doll can be thought of as the structure and the paint could be a property of it, much like the
positions in our `twothings` structure and the doll on the inside would be a whole new two things struct.
Lets try to change our `BalloonGame` into a recursive structure so that we can have infinite balloons and
it may help to see a concrete example.

## Making a recursive structure
Back to our `BalloonGame` structure:
```scheme
; A BalloonGame is one of:
; - false (no balloons)
; - Posn (balloon)
; - (make-twothings Posn Posn)
; and represents either a screen with no balloons, a screen with a balloon,
; or a screen with two balloons
```

We can join the single and double data structure variants into one recursive data variant.

```scheme
; A BalloonGame is one of:
; - false (no balloons)
; - (make-twothings Posn BalloonGame)
; and represents either a screen with no balloons, or a screen with at least one balloon
```

In the above definition, we replaced the second Posn in the `twothings` struct with a Balloon,
but what does that entail exactly? Well, now `chain` our `Balloon Gme`s together.

We can start with the inside most `BalloonGame`, the false variant.
```scheme
(define NO-BALLOONS false)
```

Since the false variant of our data type has no `BalloonGame` inside of it, it is the end of
the recursion, the center most Matryoshka. But we can now put another doll around it:

```scheme
(define ONE-BALLOON (make-twothings (make-posn 10 20) NO-BALLOONS))
```

Now our `ONE-BALLOON` constant is a `BalloonGame` with one balloon. If we unravel it, or replace
the constants with their actual value so its a bit easier to picture, it will look as such:
```scheme
(define ONE-BALLOON (make-twothings (make-posn 10 20) false))
```

The false at the end signals that that is the end of our recursion. Now if we have 2 balloons, we can show
that like so:
```scheme
(define TWO-BALLOONS (make-twothings (make-posn 250 93) ONE-BALLOON))
```

or unwrapped:
```scheme
(define TWO-BALLOONS (make-twothings (make-posn 250 93) (make-twothings (make-posn 10 20) false)))
```

Once again, we have that false at the end to signal that our recursion is done.

Recursion is a lot to wrap your head around, so this could take multiple reads through
(and definitely should), but here are a few more examples of the `BalloonGame` data structure
for you to gander at

```scheme
(define NO-BALLOONS false)
(define ONE-BALLOON (make-twothings (make-posn 10 20) NO-BALLOONS))
(define TWO-BALLOONS (make-twothings (make-posn 250 93) ONE-BALLOON))
(define THREE-BALLOONS (make-twothings (make-posn 200 200) TWO-BALLOONS))
(define FOUR-BALLOONS (make-twothings (make-posn 350 26) THREE-BALLOONS))
```

And them "unraveled"
```scheme
(define NO-BALLOONS false)

(define ONE-BALLOON (make-twothings (make-posn 10 20)
                                    false))

(define TWO-BALLOONS (make-twothings (make-posn 250 93)
                                     (make-twothings (make-posn 10 20)
                                                     false)))

(define THREE-BALLOONS (make-twothings (make-posn 200 200)
                                       (make-twothings (make-posn 250 93)
                                                       (make-twothings (make-posn 10 20)
                                                                       false))))
(define FOUR-BALLOONS (make-twothings (make-posn 350 26)
                                      (make-twothings (make-posn 200 200)
                                                      (make-twothings (make-posn 250 93)
                                                                      (make-twothings (make-posn 10 20)
                                                                                      false)))))
```

In the "unraveled" version &mdash; which by the way you should almost never type out by hand,
always use the method shown above it, where you have each nested one get defined before it
&mdash; it becomes a bit clearer to see the "nesting" of the structure inside of itself.
It is worthy to note that all of them end in false. If there not a second, non recursive variant
of our data type, we would never to be able to stop recursing, but since we have that second false
variant, we are allowed to stop our data type with the false variant.

Since we have now updated the data definition and its samples (the NO-BALLOONS - FOUR-BALLOONS above)
we can move to the final step of the data defining process, which is to make our template. In our case,
we just need to update our template.

Currently we have this:
```scheme
; BalloonGame -> ???
(define (balloon-game-template game)
  (cond [(boolean? game) ...]
        [(posn? game) (posn-template game)]
        [(twothings? game)
         (... (posn-template (twothings-thing1 game))
              (posn-template (twothings-thing2 game)))]))
```

And that template worked for our 3 variants, the no balloons (false), the one Posn, or the 2 Posns.
Since we no longer have 3 variants we have to change the template. We can begin by removing the one
posn template, since although we do use only 1 posn, we still use the `twothings` struct.

```diff
; BalloonGame -> ???
(define (balloon-game-template game)
  (cond [(boolean? game) ...]
-       [(posn? game) (posn-template game)]
        [(twothings? game)
         (... (posn-template (twothings-thing1 game))
              (posn-template (twothings-thing2 game)))]))
```

Now its all fine and dandy? Right? Well not yet... We also changed the data that is
stored in the two things structure. Since we changed our *definition*, we also need
to change the code that uses it, or the *implementation*.

In our new data definition for the two things variant, we changed from 2 Posns to a
Posn and another BalloonGame. In our above template, we call the `posn-template` on the
`thing1` and the `thing2` from twothings since they both used to be posns, Now the second
one is another `BalloonGame` so we have to call this same `baloon-game-template` on that
baloon game

```diff
; BalloonGame -> ???
(define (balloon-game-template game)
  (cond [(boolean? game) ...]
        [(twothings? game)
         (... (posn-template (twothings-thing1 game))
-             (posn-template (twothings-thing2 game)))]))
+             (balloon-game-template (twothings-thing2 game)))]))
```

As you can see, we now have our template calling that same template. This is very similar
to our **recursive data structure** in a lot of ways, I wonder what it would be called?

# Recursive functions
Recursive functions are very much the same as recursive data definitions. But instead of
containing themselves, as recursive structures do, they call (or run) themselves.

We can see that in practice in our new and updated `balloon-game-template`:
```scheme
; BalloonGame -> ???
(define (balloon-game-template game)
  (cond [(boolean? game) ...]
        [(twothings? game)
         (... (posn-template (twothings-thing1 game))
              (balloon-game-template (twothings-thing2 game)))]))
``` 

Since the function calls itself, it needs a path to take that could not call itself or else
it would be stuck calling itself which would call itself which would....

Just like how a recursive structure needs a second variant a recursive function needs a cond
or if with *one or more* of the paths **not** calling itself.

This escape can be seen in our template with the boolean? cond case which will run when we get
to the end of our "nested dolls".


\# TODO: FUNCTION HANDLING THEM
\# TODO: REST

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