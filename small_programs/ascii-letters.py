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
"""
}

from pynput import keyboard

# Get immediate input and display the corresponding ASCII art
while True:
    with keyboard.Events() as events:
        event = events.get(1e6)
        if event.key == keyboard.KeyCode.from_char('a'):
            print(ascii_art['a'])
        elif event.key == keyboard.KeyCode.from_char('b'):
            print(ascii_art['b'])
        elif event.key == keyboard.KeyCode.from_char('c'):
            print(ascii_art['c'])
        


