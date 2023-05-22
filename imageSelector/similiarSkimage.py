from PIL import Image
import imagehash
import numpy as np

def find_similar(dir, similarity=80):
    hash_size = 8
    fnames = [1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31]
    threshold = 1 - similarity / 100
    diff_limit = int(threshold * (hash_size ** 2))
    img = Image.open(dir).convert('L')

    hash1 = imagehash.average_hash(img, hash_size).hash

    for image in fnames:
        img2 = Image.open("..\\Image_database\\{}.jpg".format(image)).convert('L')

        hash2 = imagehash.average_hash(img2, hash_size).hash

        if np.count_nonzero(hash1 != hash2) <= diff_limit:
            print("{} image found {}% similar to {}".format(image, similarity, dir))

find_similar("..\\Image_database\\29.jpg", 66)
