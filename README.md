## Demo of AnimeGAN

based on [PyTorch Implementation of AnimeGANv2](https://github.com/bryandlee/animegan2-pytorch)

Go To Experience!!! **[click here](http://tongchen.dynv6.net:8080/)**


<details>
<summary>samples</summary>

<br>
Results from converted <code>Anime</code> style model (input image, generate result, from left to right)

<div align="center">
<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/2021112318053244.jpeg"   width=50%><img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/2021112400134355.jpeg" width=50% > &nbsp;
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

<font color=red size=2>注：图片来自互联网，侵权立删</font>

</details>


<details>
<summary>UI</summary>
<p>1. Upload picture</p>
<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/20211123232213.png"   width=100%>

<p>2. Generate style picture</p>
<img src="https://cdn.jsdelivr.net/gh/growvv/image-bed//mac-m1/20211124151834.png" width=100%>
</details>
 
 
## Basic Usage

**Run**
```
git clone https://github.com/growvv/AnimeGAN_Flask_Demo.git
python app.py
or gunicorn app:app -c gunicorn.conf.py (recommend)
```
 
**Note:** Default use CPU to run, if you want to use GPU, please change `device` to `cuda`, Use GPU maybe occur out of memory error.

