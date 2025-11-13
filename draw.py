import random

# ANSI escape codes for colors
BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
RESET = "\033[0m" # Resets the color to default

def draw_d4(value: int, color: str = RESET) -> None:
    print(color + """
          ;;
        ,;  ;,
       ,;    ;,
      ,;      ;,
     ,;        ;,
    ,;          ;, 
   ,;     {}      ;,
  ,;              ;,
 ,;                ;, 
,;                  ;,
::::::::::::::::::::::
    """.format(value) + RESET)

def draw_d6(value: int, color: str = RESET) -> None:
    print(color + """
 ::::::::::::::
 ::          ::  
 ::          ::
 ::    {}     ::
 ::          ::
 ::          ::                
 :::::::::::::: 
    """.format(value))


def draw_d20(value: int, color: str = RESET) -> None:
    # Account for single and double digit numbers moving parts of the dice
    if value > 9:
        d20_art = color + """             
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;    ;   ;  {}  ;   ;   ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
    """.format(value) + RESET
    else: 
        d20_art = color + """             
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;    {}    ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
    """.format(value) + RESET
    print(d20_art)

# Example usage:
# draw_d4(3, GREEN)
# draw_d6(5, RED)
# draw_d20(17, BLUE)
# draw_d20(8, YELLOW)