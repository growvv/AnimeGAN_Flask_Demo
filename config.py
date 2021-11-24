import torch
from torch._C import device

checkpoint = './weights/face_paint_512_v2_add.pt'
input_dir = './static/inputs'
output_dir = './static/outputs'
upsample_align = False
x32 = False
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
