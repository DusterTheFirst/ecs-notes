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
; - (make-twothings Posn BalloonGame)
; and represents either a screen with no balloons, or a screen with at least one balloon

(define NO-BALLOONS false)
(define ONE-BALLOON (make-twothings (make-posn 10 20) NO-BALLOONS))
(define TWO-BALLOONS (make-twothings (make-posn 250 93) ONE-BALLOON))
(define THREE-BALLOONS (make-twothings (make-posn 200 200) TWO-BALLOONS))
(define FOUR-BALLOONS (make-twothings (make-posn 350 26) THREE-BALLOONS))


; BalloonGame -> ???
(define (balloon-game-template game)
  (cond [(boolean? game) ...]
        [(twothings? game)
         (... (posn-template (twothings-thing1 game))
              (balloon-game-template (twothings-thing2 game)))]))

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
; Draw the balloons if they exist, otherwise just the sky
(check-expect (draw-balloon-game NO-BALLOONS) BACKGROUND)
(check-expect
 (draw-balloon-game ONE-BALLOON)
 (place-image BALLOON-IMAGE 10 20 BACKGROUND))
(check-expect
 (draw-balloon-game TWO-BALLOONS)
 (place-image BALLOON-IMAGE 250 93
              (place-image BALLOON-IMAGE 10 20 BACKGROUND)))
(define (draw-balloon-game game)
  (cond [(boolean? game) BACKGROUND]
        [(twothings? game)
         (draw-balloon-on (twothings-thing1 game)
                          (draw-balloon-game (twothings-thing2 game)))]))

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
; Move the balloons if they exist
(check-expect (move-balloon-if-exists NO-BALLOONS) NO-BALLOONS)
(check-expect
 (move-balloon-if-exists ONE-BALLOON)
 (make-twothings (make-posn 10 15) NO-BALLOONS))
(check-expect
 (move-balloon-if-exists
  (make-twothings (make-posn 73 -12345677899634354) NO-BALLOONS))
  NO-BALLOONS)
(define (move-balloon-if-exists game)
  (cond [(boolean? game) game]
        [(twothings? game)
         (combine-move-or-remove
          (twothings-thing1 game)
          (move-balloon-if-exists (twothings-thing2 game)))]))

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
 (make-twothings (make-posn 1 5) NO-BALLOONS))
(check-expect
 (combine-move-or-remove (make-posn 100 85) ONE-BALLOON)
 (make-twothings (make-posn 100 80) ONE-BALLOON))
(check-expect
 (combine-move-or-remove
  (make-posn 42 -12345678123456789234567) NO-BALLOONS)
 NO-BALLOONS)
(define (combine-move-or-remove current-balloon other-balloons)
  (if (< (posn-y current-balloon) MIN-Y)
      other-balloons
      (make-twothings (move-or-remove current-balloon) other-balloons)))


; ON MOUSE FUNCTIONS
; add-balloon-if-you-can : BalloonGame Number Number MouseEvent -> BalloonGame
; Adds a balloon if you clicked
(check-expect
 (add-balloon-if-you-can NO-BALLOONS 42 73 "button-down")
 (make-twothings (make-posn 42 73) NO-BALLOONS))
(check-expect
 (add-balloon-if-you-can NO-BALLOONS 300 231 "move")
 NO-BALLOONS)
(check-expect
 (add-balloon-if-you-can ONE-BALLOON 82 36 "button-down")
 (make-twothings (make-posn 82 36) ONE-BALLOON))
(define (add-balloon-if-you-can game mouse-x mouse-y mouse-event)
  (if (mouse=? mouse-event "button-down")
      (make-twothings (make-posn mouse-x mouse-y) game)
      game))
