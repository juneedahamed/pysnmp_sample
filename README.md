###pysnmp_sample

####How to use pysnmp  (ink to pysnmp http://pysnmp.sourceforge.net)

 1. Refer to installation.md on how to install dependencies and pysnmp itself
 
 2. The libsmi was installed at ~/snmp/apps,
       pyasn1 and pysnmp at python site-packages
 
 3. The libsmi is used to convert .mib files to .py files
 
 4. Convert using the command 

      ~/snmp/apps/bin/smidump -f python mibfile.mib | libsmi2pysnmp > filename.py
      
      Where mibfile.mib is the mib file and filename.py is the corresponding python file that will be used by pysnmp

 5. Note libsmi2pysnmp will be installed by pysnmp installation
 
 7. Example using the SAMPLEMIB.mib 

 	~/snmp/apps/bin/smidump -f python SAMPLEMIB.mib | > libsmi2pysnmp  SAMPLEMIB.py


