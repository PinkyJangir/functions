def speed1(speed):
    speed2=speed-70
    point=speed2//5
    if speed<=70:
        print('ok')
    elif point>12:
        print('licence suspended')
    elif speed>70:
        print('point',point)
speed=int(input('enter:'))
speed1(speed)