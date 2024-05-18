from src.encrypt import encrypt_image
from src.decrypt import decrypt_image
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Encrypt/decrypt an image using XOR method.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-e', type=str, metavar='image', help='image to encrypt')
    parser.add_argument('-d', type=str, metavar='image', help='image to decrypt')
    parser.add_argument('-k', type=str, metavar='key', help='key to use')
    image_to_encrypt = parser.parse_args().e
    image_to_decrypt = parser.parse_args().d
    key = parser.parse_args().k

    if not (image_to_encrypt or image_to_decrypt):
        print('usage: password_checker.py [-h] [-e image] [-d image] -k key')
        return 1
    
    if image_to_encrypt:
        encrypt_image(image_to_encrypt, key)
    elif image_to_decrypt:
        decrypt_image(image_to_decrypt, key)


if __name__ == '__main__':
    main()
