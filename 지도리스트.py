while True:
    print('\n ========위치기반 지도리스트=======')
    print('1,휴지통')
    print('2,공중화장실')
    print('3, 나가기')

    c = int(input('메뉴번호를 입력하시오 : '))
    if c == 1:
        #파일 불러오기
        import huge

    if c == 2:
        #파일 불러오기
        import pt
    if c == 3:
        print('프로그램을 종료합니다.')
        exit()