# raffik v.1.0
This minimal python tool will help you to increase your site/blog/profile view traffic with differnet IP and User-Agent for each request.

# Requirements 

1) tor
2) stem
3) pysocks
3) python 3.x

# Tested on Linux

This tool has only been tested and works on Linux

# Installation

## Install Tor
```console
> sudo apt install tor
```
## Configuring Tor
Locate and open torrc file in ```/etc/tor/torrc ``` 

Uncomment the following lines
```
ControlPort 9051
...
CookieAuthentication 1
```
Save the file and exit.

## Installing requirements
Install ```stem``` and ```pysocks``` and restart Tor.

```console
> pip install stem pysocks

> sudo service tor restart
```

# How to use

```console
> sudo python3 -m raffik.py

    Enter blog address:

    Enter number of views you want:
```
# Disclaimer

Author will not take any responsibility of your activity using this tool.
For Educational purpose only.

# License

GNU v3.0 License
