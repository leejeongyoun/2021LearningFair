print("=====================")

print("커피를 주문해주세요.")

print("1. 아메리카노-3000원")

print("2. 바닐라라떼-5000원")

print("3. 에스프레소-4000원")


sum=0

ame=int(input("아메리카노를 몇 잔 주문하시겠습니까? :"))

vanilla=int(input("바닐라라떼를 몇 잔 주문하시겠습니까? :"))

espre=int(input("에스프레소를 몇 잔 주문하시겠습니까? :"))

if ame > 0 :
    sum=ame * 3000
    print("아메리카노", ame,"잔", end=" ")
    print()


if vanilla > 0 :
    sum=sum+(vanilla * 5000)
    print("바닐라라떼", vanilla,"잔", end=" ")
    print()


if espre > 0 :
    sum=sum+(espre * 4000)
    print("에스프레소", espre,"잔", end=" ")
    print()
    
print("=============================")
print("   s      s         s")
print('      s      s   s')
print('   s   s    s     s')
print()      
print('-----------------------')
print('`                     /==')
print(' `     =SMU cafe=    / //')
print('  `                 /==')
print("    ---------------        ")
print()
print("=============================")
print("          영 수 증           ")
print("=============================")
print("품명       /단가  /수량/금액 ")
print("=============================")
print(" 아메리카노/3000원/",ame,"/",ame*3000)
print(" 바닐라라떼/5000원/",vanilla,"/",vanilla*5000)
print(" 에스프레소/4000원/",espre,"/",espre*4000)
print("=============================")
print ("소계 :                 ", sum)
print("=============================")



