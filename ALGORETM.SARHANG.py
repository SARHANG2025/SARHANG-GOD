import random

bag= (f"/y//d/f/","/f//d/","/d//f/h/","/f//a/y/","/e////f.h/","/f/h.u//","/FIL//T/G/","/FK//B/","/D//CH/V/","/F/I/L/SH/","/S//M//A.R.N/","/M/T.X//","/f//h//g.h/","/g//d/","/f/h.g//","/r//g/h","/FIL//T/G/","/FK//B/","/D//CH/V/","/F/I/L/SH/","/S//M//A.R.N/","/M/T.X//","/C//S//S.X/","/GIF//SX/","/F/J.K//","/S//E/X","/C//O//D.X/","/GIF//SG/","/J/H.K//","/U//S/X","X/COD//ER/","yt/tr//k","HACK","FILTRING","YTTRK","COD/SEX")

bag_1= (random.choice(bag))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,0 ]

start_number = str(random.randint(0, 9))

result = start_number + '.' + '.'.join([str(random.choice(numbers)) for _ in range(32)])


print(f"\033[31m{bag_1}.\033[32m{result}")