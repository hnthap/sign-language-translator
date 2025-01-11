import gc
import os
from typing import Union

import cv2
import matplotlib.pyplot as plt
import numpy as np

import torch


wlasl_path = r'd:\temp\cloned\word_level_slr\third_party\WLASL\start_kit'

assert os.path.isdir(wlasl_path)


def flush(*, verbose=True):
    x = gc.collect()
    if verbose:
        print('Garbage collector flushed %d objects' % x)
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats()


def get_torch_device(*, verbose=False):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    if verbose:
        print('[Device]: "%s"' % device)
        print('[Device name]:', torch.cuda.get_device_name(device))
    return torch.device(device)


def read_video(filename: str) -> np.ndarray:
    cap = cv2.VideoCapture(filename)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return np.array(frames)


def show_image(image: Union[str, np.ndarray]) -> None:
    if isinstance(image, str):
        image = cv2.imread(image)
    assert isinstance(image, np.ndarray), 'Invalid image format'
    plt.imshow(image[..., ::-1])
    plt.show()

    
def wlasl_video_path(video_id: int, *, checks_exist=True) -> str:
    path = os.path.join(wlasl_path, 'videos', f'{video_id}.mp4')
    if checks_exist:
        assert os.path.exists(path), f'Video not found: {path}'
    return path
