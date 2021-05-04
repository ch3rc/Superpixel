###How to run
___
python3 slic.py [-h, --help] [-m, --manual] [-a, --algorithm] [-s, --size] [-r, --ruler]
___
- -h --help: brings up a help message
- -m --manual: to bring up a file explorer to choose your image and return the full path
- -a --algorithm: choose between [SLIC: 1, SLICO: 2, MSLIC: 3] [default: SLIC]
- -SLIC: segments image using a desired region size
- -SLICO: optimizes using an adaptive compactness factor
- -MSLICO: optimizes using manifold methods giving more context-sensitive superpixels
- -s --size: chooses and average superpixel size measured in pixels [default: 10]
- -r --ruler: chooses the enforcement of superpixel smoothness [default: 10.0]
___
###Known issues
___
no known issues at this time.
___
##links
___
- [github](www.https://github.com/ch3rc/Superpixel.git "github account") for code and logs under master branch
- contact me at my [UMSL email](ch3rc@mail.umsl.edu) if you have any questions