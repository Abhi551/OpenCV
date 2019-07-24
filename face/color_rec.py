import struct
import binascii
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import webcolors

import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name




NUM_CLUSTERS = 5

print ('reading image')
im = Image.open('MP000000000294819_437Wx649H_20160629020754.jpeg')
im = im.resize((150, 150))      # optional, to reduce time
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

print ('finding clusters')
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print ('cluster centres:\n', codes)
print ("\n")

for colour in codes:
	colour = colour.astype(int)
	requested_colour = tuple(colour)
	
	actual_name, closest_name = get_colour_name(requested_colour)
	if actual_name != None:
		print ('actual_name',actual_name)
	print ('closest_name',closest_name)	

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max]	
# colour = ''.join(chr(int(c)) for c in peak).encode('hex')
for c in peak:
	print (c)