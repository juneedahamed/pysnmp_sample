The following are dependencies 

1. libsmi
2. pyasn1


Installing Dependencies


1. libsmi

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
   

