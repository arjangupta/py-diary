# Define the ASCII art for each letter in Doh font
ascii_art = {
'a': r"""
              AAA               
              A:::A              
             A:::::A             
            A:::::::A            
           A:::::::::A           
          A:::::A:::::A          
         A:::::A A:::::A         
        A:::::A   A:::::A        
       A:::::A     A:::::A       
      A:::::AAAAAAAAA:::::A      
     A:::::::::::::::::::::A     
    A:::::AAAAAAAAAAAAA:::::A    
   A:::::A             A:::::A   
  A:::::A               A:::::A  
 A:::::A                 A:::::A 
AAAAAAA                   AAAAAAA
    """,
'b': r""" 
BBBBBBBBBBBBBBBBB   
B::::::::::::::::B  
B::::::BBBBBB:::::B 
BB:::::B     B:::::B
  B::::B     B:::::B
  B::::B     B:::::B
  B::::BBBBBB:::::B 
  B:::::::::::::BB  
  B::::BBBBBB:::::B 
  B::::B     B:::::B
  B::::B     B:::::B
  B::::B     B:::::B
BB:::::BBBBBB::::::B
B:::::::::::::::::B 
B::::::::::::::::B  
BBBBBBBBBBBBBBBBB
""",
'c': r"""
        CCCCCCCCCCCCC
     CCC::::::::::::C
   CC:::::::::::::::C
  C:::::CCCCCCCC::::C
 C:::::C       CCCCCC
C:::::C              
C:::::C              
C:::::C              
C:::::C              
C:::::C              
C:::::C              
 C:::::C       CCCCCC
  C:::::CCCCCCCC::::C
   CC:::::::::::::::C
     CCC::::::::::::C
        CCCCCCCCCCCCC
""",
'd': r"""
DDDDDDDDDDDDD        
D::::::::::::DDD     
D:::::::::::::::DD   
DDD:::::DDDDD:::::D  
  D:::::D    D:::::D 
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D    D:::::D 
DDD:::::DDDDD:::::D  
D:::::::::::::::DD   
D::::::::::::DDD     
DDDDDDDDDDDDD        
""",
'e': r"""
EEEEEEEEEEEEEEEEEEEEEE
E::::::::::::::::::::E
E::::::::::::::::::::E
EE::::::EEEEEEEEE::::E
  E:::::E       EEEEEE
  E:::::E             
  E::::::EEEEEEEEEE   
  E:::::::::::::::E   
  E:::::::::::::::E   
  E::::::EEEEEEEEEE   
  E:::::E             
  E:::::E       EEEEEE
EE::::::EEEEEEEE:::::E
E::::::::::::::::::::E
E::::::::::::::::::::E
EEEEEEEEEEEEEEEEEEEEEE
""",
'f': r"""
FFFFFFFFFFFFFFFFFFFFFF
F::::::::::::::::::::F
F::::::::::::::::::::F
FF::::::FFFFFFFFF::::F
  F:::::F       FFFFFF
  F:::::F             
  F::::::FFFFFFFFFF   
  F:::::::::::::::F   
  F:::::::::::::::F   
  F::::::FFFFFFFFFF   
  F:::::F             
  F:::::F             
FF:::::::FF           
F::::::::FF           
F::::::::FF           
FFFFFFFFFFF           
""",
'g': r"""
        GGGGGGGGGGGGG
     GGG::::::::::::G
   GG:::::::::::::::G
  G:::::GGGGGGGG::::G
 G:::::G       GGGGGG
G:::::G              
G:::::G              
G:::::G    GGGGGGGGGG
G:::::G    G::::::::G
G:::::G    GGGGG::::G
G:::::G        G::::G
 G:::::G       G::::G
  G:::::GGGGGGGG::::G
   GG:::::::::::::::G
     GGG::::::GGG:::G
        GGGGGG   GGGG
""",
'h': r"""
HHHHHHHHH     HHHHHHHHH
H:::::::H     H:::::::H
H:::::::H     H:::::::H
HH::::::H     H::::::HH
  H:::::H     H:::::H  
  H:::::H     H:::::H  
  H::::::HHHHH::::::H  
  H:::::::::::::::::H  
  H:::::::::::::::::H  
  H::::::HHHHH::::::H  
  H:::::H     H:::::H  
  H:::::H     H:::::H  
HH::::::H     H::::::HH
H:::::::H     H:::::::H
H:::::::H     H:::::::H
HHHHHHHHH     HHHHHHHHH
""",
'i': r"""
IIIIIIIIII
I::::::::I
I::::::::I
II::::::II
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
II::::::II
I::::::::I
I::::::::I
IIIIIIIIII
""",
'j': r"""
                     
          JJJJJJJJJJJ
          J:::::::::J
          J:::::::::J
          JJ:::::::JJ
            J:::::J  
            J:::::J  
            J:::::J  
            J:::::j  
            J:::::J  
JJJJJJJ     J:::::J  
J:::::J     J:::::J  
J::::::J   J::::::J  
J:::::::JJJ:::::::J  
 JJ:::::::::::::JJ   
   JJ:::::::::JJ     
     JJJJJJJJJ                        
""",
'k': r"""
KKKKKKKKK    KKKKKKK
K:::::::K    K:::::K
K:::::::K    K:::::K
K:::::::K   K::::::K
KK::::::K  K:::::KKK
  K:::::K K:::::K   
  K::::::K:::::K    
  K:::::::::::K     
  K:::::::::::K     
  K::::::K:::::K    
  K:::::K K:::::K   
KK::::::K  K:::::KKK
K:::::::K   K::::::K
K:::::::K    K:::::K
K:::::::K    K:::::K
KKKKKKKKK    KKKKKKK
""",
'l': r"""
LLLLLLLLLLL             
L:::::::::L             
L:::::::::L             
LL:::::::LL             
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L         LLLLLL
LL:::::::LLLLLLLLL:::::L
L::::::::::::::::::::::L
L::::::::::::::::::::::L
LLLLLLLLLLLLLLLLLLLLLLLL
""",
'm': r"""                      
MMMMMMMM               MMMMMMMM
M:::::::M             M:::::::M
M::::::::M           M::::::::M
M:::::::::M         M:::::::::M
M::::::::::M       M::::::::::M
M:::::::::::M     M:::::::::::M
M:::::::M::::M   M::::M:::::::M
M::::::M M::::M M::::M M::::::M
M::::::M  M::::M::::M  M::::::M
M::::::M   M:::::::M   M::::::M
M::::::M    M:::::M    M::::::M
M::::::M     MMMMM     M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
MMMMMMMM               MMMMMMMM
""",
'n': r"""
NNNNNNNN        NNNNNNNN
N:::::::N       N::::::N
N::::::::N      N::::::N
N:::::::::N     N::::::N
N::::::::::N    N::::::N
N:::::::::::N   N::::::N
N:::::::N::::N  N::::::N
N::::::N N::::N N::::::N
N::::::N  N::::N:::::::N
N::::::N   N:::::::::::N
N::::::N    N::::::::::N
N::::::N     N:::::::::N
N::::::N      N::::::::N
N::::::N       N:::::::N
N::::::N        N::::::N
NNNNNNNN         NNNNNNN
""",
'o': r"""
     OOOOOOOOO     
   OO:::::::::OO   
 OO:::::::::::::OO 
O:::::::OOO:::::::O
O::::::O   O::::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O::::::O   O::::::O
O:::::::OOO:::::::O
 OO:::::::::::::OO 
   OO:::::::::OO   
     OOOOOOOOO     
""",
'p': r"""
PPPPPPPPPPPPPPPPP   
P::::::::::::::::P  
P::::::PPPPPP:::::P 
PP:::::P     P:::::P
  P::::P     P:::::P
  P::::P     P:::::P
  P::::PPPPPP:::::P 
  P:::::::::::::PP  
  P::::PPPPPPPPP    
  P::::P            
  P::::P            
  P::::P            
PP::::::PP          
P::::::::P          
P::::::::P          
PPPPPPPPPP 
""",
'q': r"""
     QQQQQQQQQ      
   QQ:::::::::QQ    
 QQ:::::::::::::QQ  
Q:::::::QQQ:::::::Q 
Q::::::O   Q::::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O  QQQQ:::::Q 
Q::::::O Q::::::::Q 
Q:::::::QQ::::::::Q 
 QQ::::::::::::::Q  
   QQ:::::::::::Q   
     QQQQQQQQ::::QQ 
             Q:::::Q
              QQQQQQ
""",
'r': r"""
RRRRRRRRRRRRRRRRR   
R::::::::::::::::R  
R::::::RRRRRR:::::R 
RR:::::R     R:::::R
  R::::R     R:::::R
  R::::R     R:::::R
  R::::RRRRRR:::::R 
  R:::::::::::::RR  
  R::::RRRRRR:::::R 
  R::::R     R:::::R
  R::::R     R:::::R
  R::::R     R:::::R
RR:::::R     R:::::R
R::::::R     R:::::R
R::::::R     R:::::R
RRRRRRRR     RRRRRRR
""",
's': r"""
   SSSSSSSSSSSSSSS 
 SS:::::::::::::::S
S:::::SSSSSS::::::S
S:::::S     SSSSSSS
S:::::S
S:::::S
 S::::SSSS
  SS::::::SSSSS
    SSS::::::::SS
       SSSSSS::::S
            S:::::S
            S:::::S
SSSSSSS     S:::::S
S::::::SSSSSS:::::S
S:::::::::::::::SS 
 SSSSSSSSSSSSSSS   
""",
't': r"""
TTTTTTTTTTTTTTTTTTTTTTT
T:::::::::::::::::::::T
T:::::::::::::::::::::T
T:::::TT:::::::TT:::::T
TTTTTT  T:::::T  TTTTTT
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
      TT:::::::TT      
      T:::::::::T      
      T:::::::::T      
      TTTTTTTTTTT  
""",
'u': r"""
UUUUUUUU     UUUUUUUU
U::::::U     U::::::U
U::::::U     U::::::U
UU:::::U     U:::::UU
 U:::::U     U:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U::::::U   U::::::U 
 U:::::::UUU:::::::U 
  UU:::::::::::::UU  
    UU:::::::::UU    
      UUUUUUUUU      
""",
'v': r"""
VVVVVVVV           VVVVVVVV
V::::::V           V::::::V
V::::::V           V::::::V
V::::::V           V::::::V
 V:::::V           V:::::V 
  V:::::V         V:::::V  
   V:::::V       V:::::V   
    V:::::V     V:::::V    
     V:::::V   V:::::V     
      V:::::V V:::::V      
       V:::::V:::::V       
        V:::::::::V        
         V:::::::V         
          V:::::V          
           V:::V           
            VVV
""",
'w': r"""
WWWWWWWW                           WWWWWWWW
W::::::W                           W::::::W
W::::::W                           W::::::W
W::::::W                           W::::::W
 W:::::W           WWWWW           W:::::W 
  W:::::W         W:::::W         W:::::W  
   W:::::W       W:::::::W       W:::::W   
    W:::::W     W:::::::::W     W:::::W    
     W:::::W   W:::::W:::::W   W:::::W     
      W:::::W W:::::W W:::::W W:::::W      
       W:::::W:::::W   W:::::W:::::W       
        W:::::::::W     W:::::::::W        
         W:::::::W       W:::::::W         
          W:::::W         W:::::W          
           W:::W           W:::W           
            WWW             WWW       
""",
'x': r"""
XXXXXXX       XXXXXXX
X:::::X       X:::::X
X:::::X       X:::::X
X::::::X     X::::::X
XXX:::::X   X:::::XXX
   X:::::X X:::::X   
    X:::::X:::::X    
     X:::::::::X     
     X:::::::::X     
    X:::::X:::::X    
   X:::::X X:::::X   
XXX:::::X   X:::::XXX
X::::::X     X::::::X
X:::::X       X:::::X
X:::::X       X:::::X
XXXXXXX       XXXXXXX
""",
'y': r"""
YYYYYYY       YYYYYYY
Y:::::Y       Y:::::Y
Y:::::Y       Y:::::Y
Y::::::Y     Y::::::Y
YYY:::::Y   Y:::::YYY
   Y:::::Y Y:::::Y   
    Y:::::Y:::::Y    
     Y:::::::::Y     
      Y:::::::Y      
       Y:::::Y       
       Y:::::Y       
       Y:::::Y       
       Y:::::Y       
    YYYY:::::YYYY    
    Y:::::::::::Y    
    YYYYYYYYYYYYY    
""",
'z': r"""
ZZZZZZZZZZZZZZZZZZZ
Z:::::::::::::::::Z
Z:::::::::::::::::Z
Z:::ZZZZZZZZ:::::Z 
ZZZZZ     Z:::::Z  
        Z:::::Z    
       Z:::::Z     
      Z:::::Z      
     Z:::::Z       
    Z:::::Z        
   Z:::::Z         
ZZZ:::::Z     ZZZZZ
Z::::::ZZZZZZZZ:::Z
Z:::::::::::::::::Z
Z:::::::::::::::::Z
ZZZZZZZZZZZZZZZZZZZ
"""
}

from pynput import keyboard

# Get immediate input and display the corresponding ASCII art
while True:
  with keyboard.Events() as events:
    event = events.get(1e6)
    if event.key == keyboard.KeyCode.from_char('a'):
      print(ascii_art['a'])
      print(ascii_art['a'])
    elif event.key == keyboard.KeyCode.from_char('b'):
      print(ascii_art['b'])
      print(ascii_art['b'])
    elif event.key == keyboard.KeyCode.from_char('c'):
      print(ascii_art['c'])
      print(ascii_art['c'])
    elif event.key == keyboard.KeyCode.from_char('d'):
      print(ascii_art['d'])
      print(ascii_art['d'])
    elif event.key == keyboard.KeyCode.from_char('e'):
      print(ascii_art['e'])
      print(ascii_art['e'])
    elif event.key == keyboard.KeyCode.from_char('f'):
      print(ascii_art['f'])
      print(ascii_art['f'])
    elif event.key == keyboard.KeyCode.from_char('g'):
      print(ascii_art['g'])
      print(ascii_art['g'])
    elif event.key == keyboard.KeyCode.from_char('h'):
      print(ascii_art['h'])
      print(ascii_art['h'])
    elif event.key == keyboard.KeyCode.from_char('i'):
      print(ascii_art['i'])
      print(ascii_art['i'])
    elif event.key == keyboard.KeyCode.from_char('j'):
      print(ascii_art['j'])
      print(ascii_art['j'])
    elif event.key == keyboard.KeyCode.from_char('k'):
      print(ascii_art['k'])
      print(ascii_art['k'])
    elif event.key == keyboard.KeyCode.from_char('l'):
      print(ascii_art['l'])
      print(ascii_art['l'])
    elif event.key == keyboard.KeyCode.from_char('m'):
      print(ascii_art['m'])
      print(ascii_art['m'])
    elif event.key == keyboard.KeyCode.from_char('n'):
      print(ascii_art['n'])
      print(ascii_art['n'])
    elif event.key == keyboard.KeyCode.from_char('o'):
      print(ascii_art['o'])
      print(ascii_art['o'])
    elif event.key == keyboard.KeyCode.from_char('p'):
      print(ascii_art['p'])
      print(ascii_art['p'])
    elif event.key == keyboard.KeyCode.from_char('q'):
      print(ascii_art['q'])
      print(ascii_art['q'])
    elif event.key == keyboard.KeyCode.from_char('r'):
      print(ascii_art['r'])
      print(ascii_art['r'])
    elif event.key == keyboard.KeyCode.from_char('s'):
      print(ascii_art['s'])
      print(ascii_art['s'])
    elif event.key == keyboard.KeyCode.from_char('t'):
      print(ascii_art['t'])
      print(ascii_art['t'])
    elif event.key == keyboard.KeyCode.from_char('u'):
      print(ascii_art['u'])
      print(ascii_art['u'])
    elif event.key == keyboard.KeyCode.from_char('v'):
      print(ascii_art['v'])
      print(ascii_art['v'])
    elif event.key == keyboard.KeyCode.from_char('w'):
      print(ascii_art['w'])
      print(ascii_art['w'])
    elif event.key == keyboard.KeyCode.from_char('x'):
      print(ascii_art['x'])
      print(ascii_art['x'])
    elif event.key == keyboard.KeyCode.from_char('y'):
      print(ascii_art['y'])
      print(ascii_art['y'])
    elif event.key == keyboard.KeyCode.from_char('z'):
      print(ascii_art['z'])
      print(ascii_art['z'])
    elif event.key == keyboard.Key.esc:
        break
    else:
        pass



