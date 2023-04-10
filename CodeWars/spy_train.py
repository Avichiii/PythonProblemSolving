'''
"呜呜呜" (1) = Full speed ahead! "哐当" = 20
"呜呜呜" (2) = Slow speed ahead! "哐当" = 10


'''


def length_of_railway(sounds):
    sounds = sounds.replace('呜呜呜', 'a').replace('哐当', 'b')
    
    result = 0
    speed = 10

    for sound in sounds:
        if sound == 'a':
            speed == 20 if sound != 20 else 10
        elif sound == 'b':
            result += speed
    
    return result

print(length_of_railway('呜呜呜呜呜呜哐当哐当哐当我密码！人心散了，队伍不好带啊。此刻我呜呜呜哐当哐当呜呜呜哐当哐当茶叶蛋了啊，请出哐当哐当哐当！其实，我是一个演员。my哐当哐当呜呜呜呜呜呜呜呜呜哐当'))

    # valid_sounds = ['呜', '哐', '当']
    # S = ''
    # print(S)
    # for sound in sounds:
    #     if sound in valid_sounds:
    #         S += sound