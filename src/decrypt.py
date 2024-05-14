from PIL import Image
import numpy as np
import random
import os

def decrypt_image(path, key):
    encrypted_img = Image.open(path)
    encrypted_img = encrypted_img.convert("RGB")
    encrypted_img_array = np.array(encrypted_img)
    imgrows=len(encrypted_img_array)
    imgpixperrow=len(encrypted_img_array[0])
    rowval=0
    pixval=0
    random.seed(key)
    random_key1 = random.randint(0, 255)
    random_key2 = random.randint(0, 255)
    
    half_decrypted_array=encrypted_img_array.copy()
    for x in range(imgpixperrow):
        for y in range(imgrows):
            if(pixval>=imgpixperrow):
                pixval=0
                rowval+=1
            half_decrypted_array[rowval][pixval]=encrypted_img_array[y][x]
            pixval+=1
    decrypted_array = np.bitwise_xor(half_decrypted_array, random_key2)
    decrypted_array = np.bitwise_xor(decrypted_array, random_key1)    
    
    img_name = os.path.splitext(os.path.basename(path))[0]
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(f"{img_name.replace("encrypted", "decrypted")}.png")
    print("Image decrypted successfully!")