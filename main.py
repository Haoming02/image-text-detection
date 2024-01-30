from detection import dispatch as dispatch_detection
from torch.cuda import is_available
import asyncio
import numpy as np
import cv2
import os

def detect(img: np.array) -> bool:
    textlines, mask_raw, mask = asyncio.run(
        dispatch_detection(
            "default",
            img,
            1536, 0.5, 0.7, 2.3,
            False, False,
            False, False,
            ("cuda" if is_available() else "cpu"),
            True
        )
    )
    return bool(textlines)

def recursive(path:str, target_folder:str):
    for FILE in os.listdir(path):
        f = os.path.join(path, FILE)
        if os.path.isfile(f):
            img = cv2.imread(f)
            if img is None:
                continue
            if detect(img):
                os.rename(f, os.path.join(target_folder, FILE))
        else:
            recursive(f, target_folder)

def single_check(path:str):
    img = cv2.imread(path)
    if img is None:
        print('Invalid File...')
        raise SystemExit

    if detect(img):
        print(f'"{os.path.basename(path)}" contains text')
    else:
        print(f'"{os.path.basename(path)}" contains no text')

def process(path:str):
    if os.path.isfile(path):
        single_check(path)
    else:
        excl = os.path.join(path, 'text')
        os.makedirs(excl, exist_ok=True)
        recursive(path, excl)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = input('Enter Path: ')

    process(path.strip())
