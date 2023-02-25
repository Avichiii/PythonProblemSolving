import re

_PAT = re.compile(r'(\d{4})\.img(\d+)')
_KEY = lambda pic: tuple(map(int, _PAT.match(pic).groups()))
def _Key(pic):
    int_ = map(int,pic)
    match = _PAT.match(pic)
    group = match.group()
    return group
def sort_photos(pics):
    sorted_pics = sorted(pics, key=_Key)[-5:]
    # year, idx = _KEY(pics[-1])
    for i in pics[-1:]:
        extra = ''
        extra = i
        strip = extra.split(extra[-1])
        print(strip)
        join = f'{int(extra[-1]) + 1}'.join(strip)
    return sorted_pics + [join]


print(sort_photos(["2012.img2","2016.img1","2016.img3","2016.img4","2016.img5"]))

'''
    ['2013.img3', '2013.img5', '2015.img3', '2016.img1', '2016.img2', '2016.img4', '2016.img5'] should equal 
    ['2013.img5', '2015.img3', '2016.img1', '2016.img2', '2016.img4', '2016.img5']


    ['2015.img19', '2016.img14', '2016.img16', '2016.img19', '2016.img20', '2116.img21'] should equal 
    ['2015.img19', '2016.img14', '2016.img16', '2016.img19', '2016.img20', '2016.img21']
    

    ['2014.img7', '2014.img8', '2015.img14', '2016.img18', '2016.img7', '2119.img21'] should equal 
    ['2014.img7', '2014.img8', '2015.img14', '2016.img7', '2016.img18', '2016.img19']

    ['2015.img4', '2015.img6', '2016.img14', '2016.img20', '2016.img5', '2016.img6'] should equal 
    ['2015.img4', '2015.img6', '2016.img5', '2016.img14', '2016.img20', '2016.img21']


    ['2010.img19', '2013.img7', '2013.img16', '2014.img10', '2016.img1', '2026.img2'] should equal 
    ['2010.img19', '2013.img7', '2013.img16', '2014.img10', '2016.img1', '2016.img2']
        result = []
        for i in pics[-1:]:
        extra = ''
        extra = i
        strip = extra.split(extra[-1:])
        join = f'{int(extra[-1]) + 1}'.join(strip)
        result.append(join)
    return result
    
'''