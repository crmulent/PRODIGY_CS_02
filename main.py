from src.encrypt import encrypt_image
from src.decrypt import decrypt_image

if __name__=="__main__":
    image = "orig.jpg"
    key = 12345
    encrypt_image(image, key)
    decrypt_image("orig_encrypted.png", key)
