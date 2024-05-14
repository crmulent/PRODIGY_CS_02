from PIL import Image
import numpy as np
import random
import os

def encrypt_image(path, key):
    img = Image.open(path)
    img = img.convert("RGB")
    img_array = np.array(img)
    imgrows=len(img_array)
    rowval=0
    pixval=0
    random.seed(key)
    random_key1 = random.randint(0, 255)
    random_key2 = random.randint(0, 255)
    
    encrypted_img_array = np.bitwise_xor(img_array, random_key1)
    encrypted_img_array = np.bitwise_xor(encrypted_img_array, random_key2)
    half_encryted_array = encrypted_img_array.copy()
    for x in half_encryted_array:
        for y in x:
            if(pixval>=imgrows):
                pixval=0
                rowval+=1
            encrypted_img_array[pixval][rowval]=y
            pixval+=1
    img_name = os.path.splitext(os.path.basename(path))[0]
    encrypted_img = Image.fromarray(encrypted_img_array)
    encrypted_img.save(f"{img_name}_encrypted.png")
    print("Image encrypted successfully!")