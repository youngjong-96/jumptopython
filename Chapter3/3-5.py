menu=['김밥','돈까스','피자','치킨']
menu_count=[0,0,0,0]

while True:
    menupan="""메뉴를 선택하세요. (0을 누르면 종료)
         1. 김밥(4,000원)
         2. 돈까스(8,000원)
         3. 피자(15,000원)
         4. 치킨(20,000원)
    """
    menu_pick=int(input(menupan))
    if menu_pick==0:
        break
    elif menu_pick==1:
        menu_count[0]+=1
    elif menu_pick==2:
        menu_count[1]+=1
    elif menu_pick==3:
        menu_count[2]+=1
    elif menu_pick==4:
        menu_count[3]+=1

print(menu_count)    