## HTTP to HTTPS Proxy Tunnel
### SSL Mocker.

This is a very simple proxy implimented in Python. Which has the follwoing advantegs (which actually forced me to write it)

- Can take any HTTPS request and convert it into normal HTTP and serve the client.
- Can handle gzip compression.

## Creation reason

Mainly the following prompted me to code it

- Selenium+IE's inherent inability to properly accept self-signed certificates.
- Self-imposed Restriction of various free tools which only allow normall http scanning in their free versions.


## Procedure

- Configure clinet to use 127.0.0.1:8080
- Run this python script.(It will start a proxy server on port 127.0.0.1:8080)
- Enter any site as http instead of https

## Work in progress

- Optimizing the speed.
- Adding ability to intelligently parse secure and non-secure sites.

In case of any issues drop me a note 

Licence
=======
This software is licenced under **BEER WARE** licence 

**"THE BEER-WARE LICENSE" (Revision 42):**


![Alt text](http://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/BeerWare_Logo.svg/170px-BeerWare_Logo.svg.png)


**Rabimba Karanjai** <rabimba [at] outlook.com> wrote this file. As long as you retain this notice you can do whatever you want with this stuff. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return.

