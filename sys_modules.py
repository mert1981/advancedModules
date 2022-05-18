import sys 
"""
a = int(input("a: "))
b = int(input("b: "))

sys.exit() # no commands will be run after this
c = int(input("c: "))
"""
"""
sys.stderr.write("Bu bir hata mesajıdır.") #bir bufferin içine gidiyor
sys.stderr.flush() #flush bufferi boşaltır ve anında yazdırır. 
"""
"""
for i in sys.argv : 
    print(i)
"""

def kök_bulma(a,b,c):
    delta = b**2 - 4*a*c
    if(delta<0):
        print("Reel kök yoktur")
    else: 
        x1 = (-b -delta **0.5) / (2*a)
        x2 = (-b +delta **0.5) / (2*a)
        return (x1,x2)

if len(sys.argv) ==4 :
    print("Kökler",kök_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

else:
    sys.stderr.write("Lütfen değerleri doğru giriniz...")
    sys.stderr.flush()