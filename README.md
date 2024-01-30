# Image Text Detection
Automatically detect whether any text is present in an image

<p align="right"><sup><i><b>Original Author:</b> <a href="https://github.com/zyddnys/manga-image-translator">zyddnys</a></i></sup></p>

## Motivation
Originally, I wanted to separate images that contain texts from my dataset, specifically anime/manga images.
However, the text detection models/algorithms I found, such as [tesseract](https://github.com/tesseract-ocr/tesseract),
were mainly trained on printed texts, and thus always returned empty in my use cases.
That's when I stumbled upon this repo, [manga-image-translator](https://github.com/zyddnys/manga-image-translator).
Its detection model can properly detect the texts in my use cases.
Therefore, I strip it down to the bare mininum for detection.

## Getting Started
> Adapt the syntax for non-Windows system

0. Download this repo
    ```bash
    git clone https://github.com/Haoming02/image-text-detection
    cd image-text-detection
    ```
1. Using a Python virtual environment is recommended
    ```bash
    python -m venv venv
    venv\scripts\activate
    ```
2. Install the requirements
    - **Note:** If not using a Nvidia GPU, open the `requirements.txt` and remove the `--find-links` line
    ```bash
    (venv) pip install -r requirements.txt
    ```
3. Run the `main.py` script
    ```bash
    (venv) python main.py
    ```
4. Enter the desired path
    - When passing in an image, it will simply print out if any text is detected
    - When passing in a folder, it will first create a `text` subfolder, then move any image that contains texts into it
5. When running for the first time, it will automatically download the `.ckpt` model
    - I also backup the model in [Release](https://github.com/Haoming02/image-text-detection/releases), in case the original repo is gone for whatever reason

## Known Issue
The detection is not 100% accurate, it is overly sensitive in my experience. 
Though this still beats checking manually at least.
Play around with the parameters in the `main.py` script if you want more accurate results.

## To Do
- [ ] Convert the model into [TensorRT](https://github.com/NVIDIA/TensorRT) format for massive speedups

<hr>

***Special thanks to all the contributors of the original repository!***
