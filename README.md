# PRODIGY_CS_02
A simple tool to encrypt/decrypt an image using the XOR method.

## Task
Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

## Preparation
Setting up the environment
```
python -m venv . && Scripts\src
```

Installing dependencies
```
pip install -r requirements.txt
```

## Running the program
Encrypting an image
```
python main.py -e <image> -k <key>
```

Example
```
python main.py -e img\orig.jpg -k 12345
```

Decrypting an image
```
python main.py -d <image> -k <key>
```

Example
```
python main.py -d orig_encrypted.png -k 12345
```