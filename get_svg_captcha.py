#-*- coding:utf-8 -*-
from fractions import Fraction
from re import compile
allxy=compile(r"[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}(?:\.[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}){0,1}")
first_movey=compile(r"[\x4d\x6d][\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}(?:\.[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}){0,1}\x20[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}(?:\.[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}){0,1}").search
path=compile(r"\x64\x3d\x22[^\x22]{1,}\x22").finditer
first_number=allxy.search
allxy=allxy.finditer
def get_miny(data):
    a=False
    b=allxy(data)
    b.next()
    c=Fraction(b.next().group())
    for d in b:
        if a:
            d=Fraction(d.group())
            if d<c:
                c=d
        a=False if a else True
    return c
def get_width(data):
    a=False
    b=allxy(data)
    c=d=Fraction(b.next().group())
    for e in b:
        if a:
            e=Fraction(e.group())
            if e<c:
                c=e
            elif d<e:
                d=e
        a=False if a else True
    return d-c
#验证码识别仅可用于默认字体,其他字体需要改表,https://github.com/haua/svg-captcha-recognize
length_map={
998:"1",
1081:"1",
1082:"v",
1130:"Y",
1134:"Y",
1172:"v",
1224:"Y",
1298:"V",
1311:"V",
1360:"i",
1406:"V",
1473:"i",
1478:"T",
1491:"r",
1601:"T",
1604:"X",
1613:"x",
1614:"N",
1616:"N",
1617:"N",
1618:"N",
1634:"k",
1637:"k",
1706:"K",
1709:"K",
1754:"F",
1770:"k",
1838:"u",
1840:"A",
1844:"A",
1848:"K",
1850:"Z",
1853:"Z",
1886:"h",
1900:"F",
1922:"H",
1928:"H",
1960:"P",
1991:"u",
1993:"A",
1996:"D",
2004:"Z",
2018:"w",
2035:"w",
2042:"7",
2043:"h",
2080:"j",
2082:"H",
2104:"R",
2107:"R",
2123:"P",
2140:"4",
2162:"D",
2164:"O",
2183:"w",
2199:"C",
2200:"C",
2201:"C",
2202:"C",
2210:"f",
2212:"7",
2246:"E",
2253:"j",
2260:"o",
2272:"d",
2282:"M",
2294:"U",
2301:"U",
2310:"W",
2321:"M",
2332:"a",
2344:"O",
2345:"W",
2346:"W",
2366:"s",
2380:"b",
2382:"0",
2394:"f",
2433:"E",
2448:"o",
2461:"d",
2464:"p",
2466:"M",
2485:"U",
2498:"c",
2501:"e",
2503:"W",
2512:"q",
2526:"a",
2546:"2",
2563:"s",
2578:"b",
2580:"0",
2606:"5",
2632:"6",
2669:"p",
2706:"c",
2709:"e",
2721:"q",
2758:"2",
2800:"9",
2823:"5",
2851:"6",
3033:"9",
3038:"S",
3054:"B",
3160:"g",
3244:"Q",
3254:"Q",
3266:"G",
3291:"S",
3308:"B",
3414:"8",
3423:"g",
3514:"Q",
3538:"G",
3663:"m",
3667:"m",
3698:"8",
3878:"3",
3968:"m",
4201:"3"}
miny_map={
986:lambda data:"I" if 13<get_miny(data) else "l",
1068:lambda data:"I" if 13<get_miny(data) else "l",
1610:lambda data:"x" if 19<get_miny(data) else "J",
1744:lambda data:"x" if 19<get_miny(data) else "J",
1615:lambda data:"r" if 18<get_miny(data) else "N",
2198:lambda data:"n" if 19<get_miny(data) else "C",
2381:lambda data:"n" if 19<get_miny(data) else "C",
1598:lambda data:"X" if 13<get_miny(data) else "N",
1731:lambda data:"X" if 13<get_miny(data) else "N",
1694:lambda data:"z" if 22<get_miny(data) else "t",
1835:lambda data:"z" if 22<get_miny(data) else "t",
2279:lambda data:"R" if 13<get_miny(data) else "M"}
first_movey_map={
1274:lambda data:"y" if 30<first_movey(data).group().split(" ")[1] else "L",
1380:lambda data:"y" if 30<first_movey(data).group().split(" ")[1] else "L"}
width_map={
2318:lambda data:"W" if 30<get_width(data) else "4"}
def get_svg_captcha(svg):
    a={}
    for b in path(svg):
        b=b.group()[3:-1:]
        svg=len(b)
        if svg in length_map:
            a[Fraction(first_number(b).group())]=length_map[svg]
        elif svg in miny_map:
            a[Fraction(first_number(b).group())]=miny_map[svg](b)
        elif svg in first_movey_map:
            a[Fraction(first_number(b).group())]=first_movey_map[svg](b)
        elif svg in width_map:
            a[Fraction(first_number(b).group())]=width_map[svg](b)
    return "".join((a[b] for b in sorted(a)))