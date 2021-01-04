; CONSTANTS
(define BALLOON-IMAGE
  (above (circle 20 "solid" "red")
         (triangle 10 "solid" "red")
         (rectangle 2 30 "solid" "gray")))
(define MIN-Y (- (/ (image-height BALLOON-IMAGE) 2)))
(define BG-SIZE 500)
(define BACKGROUND (square BG-SIZE "solid" "light blue"))

; DATA DEFINITIONS
(define-struct twothings [thing1 thing2])

; A BalloonGame is one of:
; - false (no balloons)
; - Posn (balloon)
; - (make-twothings Posn Posn)
; and represents either a screen with no balloons, a screen with a balloon,
; or a screen with two balloons

(define NO-BALLOONS false)
(define BALLOON-CENTER (make-posn 250 250))
(define TWO-BALLOONS (make-twothings (make-posn 100 200) (make-posn 73 39)))

; BalloonGame -> ???
(define (balloon-game-template game)
  (cond [(boolean? game) ...]
        [(posn? game) (posn-template game)]
        [(twothings? game)
         (... (posn-template (twothings-thing1 game))
              (posn-template (twothings-thing2 game)))]))

; Posn -> ???
(define (posn-template p)
  (... (posn-x p) (posn-y p) ...))

; MAIN FUNCTION
; play : Any -> BalloonGame
; Play the balloon game (starting with no balloons)
(define (play _)
  (big-bang false
            [to-draw draw-balloon-game]
            [on-tick move-balloon-if-exists]
            [on-mouse add-balloon-if-you-can]))

; TO DRAW FUNCTIONS
; draw-balloon-game : BalloonGame -> Image
; Draw the balloon if it exists, otherwise just the sky
(check-expect (draw-balloon-game NO-BALLOONS) BACKGROUND)
(check-expect
 (draw-balloon-game BALLOON-CENTER)
 (place-image BALLOON-IMAGE 250 250 BACKGROUND))
(define (draw-balloon-game game)
  (cond [(boolean? game) BACKGROUND]
        [(posn? game) (draw-balloon-on game BACKGROUND)]
        [(twothings? game)
         (draw-balloon-on
          (twothings-thing1 game)
          (draw-balloon-on (twothings-thing2 game) BACKGROUND))]))

; draw-balloon-on : Posn Image -> Image
; Draw the balloon at the given position onto the given image
(check-expect
 (draw-balloon-on (make-posn 1 2) BACKGROUND)
 (place-image BALLOON-IMAGE 1 2 BACKGROUND))
(check-expect
 (draw-balloon-on (make-posn 700 32) (circle 300 "solid" "blue"))
 (place-image BALLOON-IMAGE 700 32 (circle 300 "solid" "blue")))
(define (draw-balloon-on p bg)
  (place-image BALLOON-IMAGE (posn-x p) (posn-y p) bg))

; ON TICK FUNCTIONS
; move-balloon-if-exists : BalloonGame -> BalloonGame
; Move the balloon if it exists
(check-expect (move-balloon-if-exists NO-BALLOONS) NO-BALLOONS)
(check-expect (move-balloon-if-exists (make-posn 100 200))
              (make-posn 100 195))
(check-expect (move-balloon-if-exists (make-posn 50 -2345678902345678))
              NO-BALLOONS)
(define (move-balloon-if-exists game)
  (cond [(boolean? game) game]
        [(posn? game) (move-or-remove game)]
        [(twothings? game)
         (combine-move-or-remove (twothings-thing1 game)
                                 (move-or-remove (twothings-thing2 game)))]))

; move-or-remove : Posn -> BalloonGame
; Move the balloon up if it is on the screen, otherwise remove it
(check-expect (move-or-remove (make-posn 10 20)) (make-posn 10 15))
(check-expect
 (move-or-remove (make-posn 73 -123456781234567892345678))
 NO-BALLOONS)
(define (move-or-remove p)
  (if (< (posn-y p) MIN-Y) NO-BALLOONS
      (make-posn (posn-x p) (- (posn-y p) 5))))

; combine-move-or-remove : Posn BalloonGame -> BalloonGame
; Move or remove the given balloon from the game
(check-expect
 (combine-move-or-remove (make-posn 1 10) NO-BALLOONS)
 (make-posn 1 5))
(check-expect
 (combine-move-or-remove (make-posn 100 85) (make-posn 10 70))
 (make-twothings (make-posn 100 80) (make-posn 10 70)))
(check-expect
 (combine-move-or-remove
  (make-posn 42 -12345678123456789234567) NO-BALLOONS)
 NO-BALLOONS)
(check-expect
 (combine-move-or-remove
  (make-posn 13 -2345678923467890234567) (make-posn 10 20))
 (make-posn 10 20))
(define (combine-move-or-remove current-balloon game)
  (cond [(boolean? game) (move-or-remove current-balloon)]
        [(posn? game)
         (if (< (posn-y current-balloon) MIN-Y)
             game
             (make-twothings (move-or-remove current-balloon) game))]
        [(twothings? game) game]))


; ON MOUSE FUNCTIONS
; add-balloon-if-you-can : BalloonGame Number Number MouseEvent -> BalloonGame
; Adds a balloon if there are no balloons or one balloon and you clicked
(check-expect
 (add-balloon-if-you-can NO-BALLOONS 42 73 "button-down")
 (make-posn 42 73))
(check-expect
 (add-balloon-if-you-can NO-BALLOONS 300 231 "move")
 NO-BALLOONS)
(check-expect
 (add-balloon-if-you-can BALLOON-CENTER 82 36 "button-down")
 (make-twothings BALLOON-CENTER (make-posn 82 36)))
(check-expect
 (add-balloon-if-you-can TWO-BALLOONS 12 300 "button-down") TWO-BALLOONS)
(define (add-balloon-if-you-can game mouse-x mouse-y mouse-event)
  (cond [(boolean? game)
         (if (mouse=? mouse-event "button-down")
             (make-posn mouse-x mouse-y)
             game)]
        [(posn? game)
         (if (mouse=? mouse-event "button-down")
             (make-twothings game (make-posn mouse-x mouse-y))
             game)]
        [(twothings? game) game]))
 