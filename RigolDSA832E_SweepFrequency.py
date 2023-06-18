#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 12:56:58 2023

@author: Adam Czerniewski
Commands taken from https://rfmw.em.keysight.com/wireless/helpfiles/e5055a/Programming/GP-IB_Command_Finder/Sense/Frequency.htm
"""

import time, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.112', 5555)) # IP, port

s.sendall('*IDN?\n'.encode()) # Identifies equipment ID 

print(s.recv(4096)) # Returns equipment ID

# cmd_Center ='SENS:FREQ:CENT 100000000'+'\n'
# cmd_Sweep = 'SENS:SWEEP:TYPE CW' +'\n'

#s.sendall(cmd_Center.encode())
#s.sendall(cmd_Sweep.encode())

# Sets center frequency to 1 GHz
F = 1000000000

# Sweep Spectrum Analyzer center frequency from 1 GHz - 2 GHz in 100 MHz steps
for i in range(0,10):
    F += 100000000
    f = str(F)
    cmd = 'SENS:FREQ:CENT ' + f + '\n'
    print(cmd)
    s.sendall(cmd.encode())
    time.sleep(5)
    

# Close connection 
s.close()