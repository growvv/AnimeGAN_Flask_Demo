## Demo of AnimeGAN

based on [PyTorch Implementation of AnimeGANv2](https://github.com/bryandlee/animegan2-pytorch)

Go To Experience!!! **[click here](http://tongchen.dynv6.net:8080/)**


<details>
<summary>samples</summary>

<br>
Results from converted `Anime` style model (input image, generate result, pytorch result from left to right)

<div align="center">
<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/2021112318053244.jpeg"   width=50%><img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/2021112318472212.jpeg" width=50% > &nbsp;
</div>

<div align="center">
<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/2021112323220052.jpg"   width=50%><img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/2021112323182333.jpg" width=50% > &nbsp;
</div>

<div align="center">
<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/QQ20211123-1.jpg" width=50%><img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/2021112323082795.jpg" width=50%> &nbsp; 
</div>

<div align="center">
<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/QQ20211123-0.jpg" width=50%><img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/1.jpg" width=50%> &nbsp; 
</div>
</details>

<details>
<summary>UI</summary>
<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/20211123232213.png"   width=100%>

<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/20211123232411.png" width=100%>
</details>
 
 
## Basic Usage

**Run**
```
git clone https://github.com/growvv/AnimeGAN_Flask_Demo.git
python app.py
or gunicorn app:app -c gunicorn.conf.py (recommend)
```
 
**Note:** Default use CPU to run, if you want to use GPU, please change `device` to `cuda`, Use GPU maybe occur out of memory error.

