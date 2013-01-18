#!/usr/bin/env python
# coding: utf-8

import os

from PIL import Image

THUMB_SIZE = 20
THRESHOLD = 60


def get_image_data(img_path):
    img = Image.open(img_path).resize((THUMB_SIZE, THUMB_SIZE), Image.BILINEAR)
    return set([sum(x) for x in img.getdata()])


def get_distance(data1, data2):
    return sum(1 for x in data1 - data2 if abs(x) > THRESHOLD)
