

import os
import shutil
import random

    
for d in os.listdir('painting-contractor'):
    try:
        search_categories = open(f'painting-contractor/{d}/index.html', "r", encoding="utf8").read()
        
        op= search_categories.replace("﻿", '').replace('<span class="_fadeIn_4f9by_7">{</span><span class="_fadeIn_4f9by_7">Residential </span><span class="_fadeIn_4f9by_7">Painting </span><span class="_fadeIn_4f9by_7">Services</span><span class="_fadeIn_4f9by_7">|</span><span class="_fadeIn_4f9by_7">Home </span><span class="_fadeIn_4f9by_7">Painting </span><span class="_fadeIn_4f9by_7">Solutions</span><span class="_fadeIn_4f9by_7">|</span><span class="_fadeIn_4f9by_7">Expert </span><span class="_fadeIn_4f9by_7">House </span><span class="_fadeIn_4f9by_7">Painting </span><span class="_fadeIn_4f9by_7">Services</span><span class="_fadeIn_4f9by_7">}</span>', random.choice(['Residential Painting Services', 'Home Painting Solutions', 'Expert House Painting Services'])).replace('<span class="_fadeIn_4f9by_7">{</span><span class="_fadeIn_4f9by_7">Eco</span><span class="_fadeIn_4f9by_7">–</span><span class="_fadeIn_4f9by_7">Friendly</span><span class="_fadeIn_4f9by_7">|</span><span class="_fadeIn_4f9by_7">Green</span><span class="_fadeIn_4f9by_7">|</span><span class="_fadeIn_4f9by_7">Environmentally </span><span class="_fadeIn_4f9by_7">Conscious</span><span class="_fadeIn_4f9by_7">} </span><span class="_fadeIn_4f9by_7">Painting </span><span class="_fadeIn_4f9by_7">Solutions</span>', random.choice(['Eco–Friendly Painting Solutions', 'Green Painting Solutions', 'Environmentally Conscious Painting Solutions']))
        fp = open(f'painting-contractor/{d}/index.html', "w", encoding='utf-8-sig')
        fp.writelines(op)
        fp.close()
    except:
        pass


