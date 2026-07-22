<div align="center">
<h1>Pixora: A Python Library for Pixel Art Conversion</h1>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/sepandhaghighi/pixora"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/sepandhaghighi/pixora"></a>
<a href="https://badge.fury.io/py/pixora"><img src="https://badge.fury.io/py/pixora.svg" alt="PyPI version"></a>
<a href="https://codecov.io/gh/sepandhaghighi/pixora"><img src="https://codecov.io/gh/sepandhaghighi/pixora/graph/badge.svg?token=Bxwiv64q4n"></a>
</div>			
				
## Overview	

<p align="justify">
Pixora is a lightweight Python library and command-line tool for converting ordinary images into retro-style pixel art. Built on top of Pillow, it provides a simple API for pixelizing images with customizable pixel sizes while supporting both file paths and in-memory objects. Whether you are creating game assets, generating pixelated avatars, or adding a nostalgic visual effect to your images, Pixora offers a fast, and easy-to-use solution for both scripts and terminal workflows.
</p>

<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/pixora"><img src="http://pepy.tech/badge/pixora"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/pixora"><img src="https://img.shields.io/github/stars/sepandhaghighi/pixora.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">main</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/pixora/actions/workflows/test.yml/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/pixora/actions/workflows/test.yml/badge.svg?branch=dev"></td>
	</tr>
</table>
<table>
    <tr> 
        <td align="center">Code Quality</td>
        <td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/pixora"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/pixora/badge" alt="CodeFactor"></a></td>
        <td align="center"><a href="https://app.codacy.com/gh/sepandhaghighi/pixora/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/50dc58daa2c94c16b823b8fb406d2283"></a></td>
    </tr>
</table>

## Installation		

### Source Code
- Download [Version 0.1](https://github.com/sepandhaghighi/pixora/archive/v0.1.zip) or [Latest Source](https://github.com/sepandhaghighi/pixora/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install pixora==0.1`						


## Usage

### Library

```python
from pixora import NearestNeighbor, Lanczos
from pixora import pixelize
pixelize("input.png", output="output.png", algorithm=NearestNeighbor(pixel_size=12))
image = pixelize("input.png", algorithm=Lanczos(pixel_size=12))
image.show()
```

### CLI

```bash
pixora input.png output.png

pixora input.png output.png --pixel-size=12
```

### Available Algorithms


| Algorithm         | Description                                 |
| ----------------- | ------------------------------------------- |
| `NearestNeighbor` | Pixelate using nearest-neighbor resampling  |
| `Bilinear`        | Pixelate using bilinear resampling          |
| `Bicubic`         | Pixelate using bicubic resampling           |
| `Lanczos`         | Pixelate using Lanczos resampling           |


## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template

## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>		
GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL
<h4>Zilliqa</h4>
zil1knmz8zj88cf0exr2ry7nav9elehxfcgqu3c5e5
<h4>Coffeete</h4>
<a href="http://www.coffeete.ir/opensource">
<img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>

