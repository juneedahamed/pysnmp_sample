## Dependencies 

1. libsmi
2. pyasn1


## Installing Dependencies


### 1. libsmi

  Download the latest `libsmi-0.4.8.tar` from http://www.ibr.cs.tu-bs.de/projects/libsmi/download/
  
  By default, `make install` will install all the files in `/usr/local/bin`, `/usr/local/lib` etc.
  
  Lets install this at `~/snmp/apps`
  
   `mkdir ~/snmp/apps`
   
   `tar xvf  libsmi-0.4.8.tar`
   
   `cd libsmi-0.4.8`
   
   `./configure --prefix ~/snmp/apps`
   
   `make`
   
   `make check`
   
   `make install`
   

### 2. pyasn1

  Download the latest `pyasn1-0.1.7.tar.gz` from https://pypi.python.org/packages/source/p/pyasn1/
  
  `tar xzvf pyasn1-0.1.7.tar.gz`
    
  `cd pyasn1-0.1.7`
    
  `sudo python setup.py install`
    
  `cd test`    [optional]
    
  `python suite.py` [ optional ]
  
  
## Installing pysnmp

  Download `pysnmp-4.2.5.tar.gz` from https://pypi.python.org/packages/source/p/pysnmp/
  
    `tar xzvf pysnmp-4.2.5.tar.gz`
    
    `sudo python setup.py install`
     
    ### Optional Test
      `python`
     
      `import pysnmp`
      
      The above import within python interactive console should not throw any error
      
      
