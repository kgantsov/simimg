#!/usr/bin/env python
# coding: utf-8

import glob
import os

from PIL import Image
import baker
import numpy

THUMB_SIZE = 20
THRESHOLD = 60
DISTANCE = 220


def get_image_data(img_path):
    '''
    Function takes path to image and return image data.
    '''
    img = Image.open(img_path).resize((THUMB_SIZE, THUMB_SIZE), Image.BILINEAR)
    return numpy.array([sum(x) for x in img.getdata()])


def get_distance(data1, data2):
    '''
    Function return distance between two file.
    '''
    return sum(1 for x in data1 - data2 if abs(x) > THRESHOLD)


@baker.command(shortopts={"dirname": "d"})
def find_similar(dirname):
    '''
    Takes path to dir and find similar images.
    '''
    files = glob.glob(os.path.join(dirname, '*.jpg'))
    images = [(f, get_image_data(f)) for f in files]
    similar_images = {}

    for fname, data in images:
        for fname1, data1 in images:
            if fname == fname1:
                continue

            if fname1 in similar_images:
                continue

            if get_distance(data, data1) < DISTANCE:
                similar_images[fname] = fname1
                print 'Images %s and %s very similar.' % (fname, fname1)

baker.run()
