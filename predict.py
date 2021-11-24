import argparse

import torch
import cv2
import numpy as np
import os

from model import Generator
import config
import ipdb

torch.backends.cudnn.enabled = False
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True
    
net = Generator()
net.load_state_dict(torch.load(config.checkpoint, map_location="cpu"))


def load_image(image_path, x32=False):
    img = cv2.imread(image_path).astype(np.float32)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w = img.shape[:2]

    if x32: # 是否将图片resize成32的整数倍
        def to_32s(x):
            return 256 if x < 256 else x - x%32
        img = cv2.resize(img, (to_32s(w), to_32s(h)))

    # img = cv2.resize(img, (1080, int(1080/h*w)))
    img = torch.from_numpy(img)
    img = img/127.5 - 1.0
    return img


def predict(image_name):
        
    net.to(config.device).eval()
    print(f"model loaded: {config.checkpoint}")
            
    image = load_image(os.path.join(config.input_dir, image_name), config.x32)

    with torch.no_grad():
        input = image.permute(2, 0, 1).unsqueeze(0).to(config.device)
        out = net(input, config.upsample_align).squeeze(0).permute(1, 2, 0).cpu().numpy()
        out = (out + 1)*127.5
        out = np.clip(out, 0, 255).astype(np.uint8)
            
    os.makedirs(config.output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(config.output_dir, image_name), cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
    print(f"image saved: {image_name}")
    
    return out

    
if __name__ == '__main__':
    predict('1.jpg')
    
