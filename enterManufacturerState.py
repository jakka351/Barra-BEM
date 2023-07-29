#!/usr/bin/python3
#coding:utf-8
# license:
#################################################################################################################
# BA/BF Falcon - FoA Barra - Body Module - Component Manufacturer Level Access via CAN Calibration Protocol CCP #
#################################################################################################################
# Copyright (c) 2022 Benjamin Jack Leighton
# https://github.com/jakka351/FG-Falcon | https://github.com/jakka351/FG-Falcon-Hidden
# bjakkaleighton@gmail.com 
# All rights reserved.
#################################################################################################################
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that
# the following conditions are met:
# 1.    With the express written consent of the copyright holder.
# 2.    Redistributions of source code must retain the above copyright notice, this 
#       list of conditions and the following disclaimer.
# 3.    Redistributions in binary form must reproduce the above copyright notice, this 
#       list of conditions and the following disclaimer in the documentation and/or other 
#       materials provided with the distribution.
# 4.    Neither the name of the organization nor the names of its contributors may be used to
#       endorse or promote products derived from this software without specific prior written permission.
#################################################################################################################
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################################################
# Notes
#  1. This software can only be distributed with my written permission. It is for my own educational purposes and 
#     is potentially dangerous to ECU health and safety. 
#################################################################################################################
# import modules
import can, time, os, queue, sys, traceback
from threading import Thread
'''
   FOR SCRIPT TESTER'S TROUBLESHOOTING A FAILED MODULE IMPORT
       1) sudo apt update -y && sudo apt upgrade -y
       2) sudo apt install python3 python3-can 
       3) pip3 install time os queue sys traceback (NO SUDO)
'''
#os.system("sudo apt update -y") 

########################################################################################################
def scroll():
    '''
        WHAT ARE WE IF WE DONT INCLUDE ASCII ART????
    '''
    ########################################################################################################
    print('                                                                                                    ')
    print('    |==============================================================================================|')
    time.sleep(0.0125)
    print('    |             ,777I77II??~++++=~::,,,,::::::::::~~~==+~                           jakka351     |')
    time.sleep(0.0125)
    print('    |           ,IIIIII,IIII+~.p.o.w.e.r.e.d.,.b.y,~,:::~+?+?=                                     |')
    time.sleep(0.0125)
    print('    |         :=I7777I=IIIIII~...:===,:,=~:,,,,,,::=,,,:::~~:=?===                                 |')
    time.sleep(0.0125)
    print('    |      ~=,?I?777II7IIIII=~,.r a s p b e r r y . p i ,~:~~:~+:~:~                               |')
    time.sleep(0.0125)
    print('    |      I=I?IIIIII~IIIIIII+:..,,,,,,,,,,,,.,.,,::.,,,,:::~~=~:=+~?~~                            |')
    time.sleep(0.0125)
    print('    |      I77?+?IIIIIIIII7I7=~,.,,,..,,,,.,.,.......,.,.,.,..,,,:~=~:==~~                         |')
    time.sleep(0.0125)
    print('    |     +=I7777I?+???IIIIII+=:..,,,,,,,,,,,...,,,,,,,,,,,,..,,,:..:?I7+...,,                     |')
    time.sleep(0.0125)
    print('    |     +=+=I7777I=~~+~:~IIII~,..,,,,,,,,,,..,,,,,...~+II?I?+?III7IIII777I7=.....                |')
    time.sleep(0.0125)
    print('    |      ==++++III=~~~::~+I:+?~:.........:+IIIIIIII+=?IIIIIII???????????III7II7I....             |')
    time.sleep(0.0125)
    print('    |     ?+=======::,,,,...,,:=?==~?+?????????????+==~~~~~===+++++++++++++++???II?III....         |')
    time.sleep(0.0125)
    print('    |     ?+=======+=~=I7III~:~~I??++??IIIIII??+??++++==~~~~:::~~~~============++?II?+7II.         |')
    time.sleep(0.0125)
    print('    |     ??+=====~~~=~~~+III~~=III??++++=+++?II??+=+?+====~~~:::::~~~~~~~~~~======+???++II.       |')
    time.sleep(0.0125)
    print('    |     ??+=?=~~~~~~~~~~=~I=77I7III??++==~++++=+I??+?~?+===~~~~::::::~~~~~~~~~~~===++++=II,      |')
    time.sleep(0.0125)
    print('    |     I??+=++=~~~~~~~~~~~?I777IIII??++====~======????+==+==~~~~:::::::::~~~~~~~~~====+==I,     |')
    time.sleep(0.0125)
    print('    |      ?I+=~~=++~~~~~~~~=?=:+IIIII??++++===~:~~~~~~~=???=?:=~~~~~::::::::~~~~~~~~~~=~=+?7~:    |')
    time.sleep(0.0125)
    print('    |       ?+=~~~~=++~~~~~+???~=?7II??+++++++==~~:~~~~~~:~~???=+:~~~~~~:::::::::~~~~=++:,.,+=,,   |')
    time.sleep(0.0125)
    print('    |        =?I+~~~==++~~:+??~====+I?+===+++++==~~~::::::::::~????~~~~~:::::~:~==+:,,,,?..::+=:   |')
    time.sleep(0.0125)
    print('    |          =?I=~~~==++=+++~==:,~~=+====+++++:,,...:,::~:::::~~~~+~:~~:~~==,.,,.?I~,..::~~=,:   |')
    time.sleep(0.0125)
    print('    |           ~=+I?=~~=~+++~~=...,~:=+====++?:~+=?I~,I=I??..~III7I:==~,.,,.,,.,,,...::~~++~:~:   |')
    time.sleep(0.0125)
    print('    |              ~?I+=~~~~+~~~.:+,,,:=+===+++~+==~=+:III=?I?77777I~~~===,,,,.,.,,~~~~=+=~::,,:   |')
    time.sleep(0.0125)
    print('    |                ~?I+=:~~~~~~,,+:,,+==~+++++,:~~:==,??,:,,=??I++,,,:~===,,,::~~=++=:::~=..,,   |')
    time.sleep(0.0125)
    print('    |             ,,,,:=+?==~~~~.=:~~,..,=+++++=~:=+=~:.,:,,,,::?=I=:::::+~====++++=~:::?I+?,..,   |')
    time.sleep(0.0125)
    print('    |              :,,,,~+====~:,,,:=,.,,,~~===~~~,:==~~~~~~:..,,,,,,..,,,~==+++~:,~++I++II?...    |')
    time.sleep(0.0125)
    print('    |               :,,,,,,+==+,:..:==.:,,~:~~~~~:,,,,:~~~~~~~~=========~++++~,....II+II+?...,:    |')
    time.sleep(0.0125)
    print('    |                 ,,,,,,,++.,,.,,,,=:,,~:::~:::,,,,,,,,,::~~~=====~====~.......?I=I.....,:~    |')
    time.sleep(0.0125)
    print('    |                   ::,,,,,,:~::,~+I+,..~::::::,,,,,,,,,,,,,,,,,~==~~~.........+.......,:,,    |')
    time.sleep(0.0125)
    print('    |                        :,,,,,,:~::,~+I+     BARRA BEM CCP                 ..+.......,:,,     |') 
    time.sleep(0.0125)
    print('    |==============================================================================================|')
    time.sleep(0.0125)
    print('    |   BA/BF Falcon - FoA Barra - Body Module systemSupplierSpecific - CAN Calibration Protocol   |')
    time.sleep(0.0125)
    print('    |      This software can only be distributed with my express written permission.               |')
    time.sleep(0.0125)
    print('    |==============================================================================================|')
    #############################################################################################################
    return
def displayLicense():
    print('''
        #################################################################################################################
        # BA/BF Falcon - FoA Barra - Body Module - Component Manufacturer Level Access via CAN Calibration Protocol CCP #
        #################################################################################################################
        # Copyright (c) 2022 Benjamin Jack Leighton
        # https://github.com/jakka351/FG-Falcon | https://github.com/jakka351/FG-Falcon-Hidden
        # bjakkaleighton@gmail.com 
        # All rights reserved.
        #################################################################################################################
        # Redistribution and use in source and binary forms, with or without modification, are permitted provided that
        # the following conditions are met:
        # 1.    With the express written consent of the copyright holder.
        # 2.    Redistributions of source code must retain the above copyright notice, this 
        #       list of conditions and the following disclaimer.
        # 3.    Redistributions in binary form must reproduce the above copyright notice, this 
        #       list of conditions and the following disclaimer in the documentation and/or other 
        #       materials provided with the distribution.
        # 4.    Neither the name of the organization nor the names of its contributors may be used to
        #       endorse or promote products derived from this software without specific prior written permission.
        #################################################################################################################
        # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
        # INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
        # DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
        # SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
        # SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
        # WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
        # USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
        #################################################################################################################
        # Notes
        #  1. This software can only be distributed with my written permission. It is for my own educational purposes and 
        #     is potentially dangerous to ECU health and safety. 
        #################################################################################################################
        ''')

########################################################################################################
def setup():
    """
    can0 is default network but it can be whatever you want
    DOCS: linux socketcan, python-can
    Hardware notes - Raspberry Pi + MCP2515 via SPI will work fine.
    Python-CAN hardware interfaces: https://python-can.readthedocs.io/en/master/interfaces.html
    this script will work on windows under a USB-CAN interface - see above url
    """
    global highSpeedCan
    try:
       highSpeedCan = can.interface.Bus(channel='can0', bustype='socketcan_native')
       '''
           vcan0 is a virtual can interface, handy for testing without needing any hardware
       '''
    except OSError:
        print("    the can interface is not up...")
        cleanscreen()
        displayLicense()                                            # quit if ctl + c is hit
        time.sleep(3)
        sys.exit()
        '''
           quits if there is no socketcan interface found
           troubleshoot with 'sudo ifconfig', 'dmesg | grep can'  
           check that MCP2515 initialized
           and then check your darn wiring sally.
        '''
    time.sleep(0.25)
    print("   ")
    time.sleep(0.25)
    print("    CANbus active on", highSpeedCan)  
    time.sleep(0.25)
    return

########################################################################################################
# GLOBAL VARIABLES
########################################################################################################
c                      = ''
count                  = 0  
R1                     = 0
R2                     = 0
R3                     = 0
R4                     = 0
K1                     = 0
K2                     = 0
K3                     = 0
K3                     = 0
K4                     = 0
RR                     = 0x00
SS                     = 0x00
UU                     = 0x00
WW                     = 0x00
XX                     = 0x00
YY                     = 0x00
ZZ                     = 0x00
########################################################################################################
''' CAN RX & TX IDENTIFIERS '''
BEM_DiagSig_Rx         = 0x726
BEM_DiagSig_Tx         = 0x72E
BEM_CCP_Rx             = 0x706
BEM_CCP_Tx             = 0x712
########################################################################################################
''' CCP ENCRYPTION ALGORITHM '''
challenge0_ubl         = 0
challenge1_ubl         = 0 
challenge2_ubl         = 0
challenge3_ubl         = 0
result0_ubl            = 0
result1_ubl            = 0
result2_ubl            = 0
result3_ubl            = 0
reply_cnt_ubl          = 0
adden_a_uil            = 0
adden_b_uil            = 0
sum_uil                = 0
temp1_ubl              = 0
temp2_ubl              = 0
temp3_ubl              = 0

''' CCP ENCRYPTION ALGORITHM FUNCTION'''

def calculateResult(challenge0_ubl, challenge1_ubl, challenge2_ubl, challenge3_ubl):

    '''
    THE FOLLOWING IS THE CODE USED IN BARRA BEM FOR CALCULATING VALUES USED IN THE CCP UNLOCK COMMAND
    '''
    SECURITY_ID0 = 0x41
    SECURITY_ID1 = 0x55
    SECURITY_ID2 = 0x36
    SECURITY_ID3 = 0x74
    print("    Calculating Response Key...")
    adden_a_uil  = (SECURITY_ID2 << 8) + (SECURITY_ID0)
    adden_b_uil  = (challenge2_ubl << 8) + (challenge3_ubl)
    sum_uil      = adden_a_uil + adden_b_uil

    result2_ubl  = (sum_uil >> 8)
    result3_ubl  = (sum_uil & 0xFF)

    adden_a_uil  = (SECURITY_ID0 << 8) + SECURITY_ID1
    adden_a_uil  = (challenge2_ubl << 8) + challenge3_ubl
    sum_uil      = adden_a_uil + adden_b_uil

    result0_ubl  = (sum_uil >> 8)
    result1_ubl  = (sum_uil & 0xFF)

    result3_ubl  = result3_ubl * 13
    result2_ubl  = result2_ubl * 11
    result1_ubl  = result1_ubl * 19
    result0_ubl  = result0_ubl * 17

    result3_ubl  = (((temp1_ubl == result3_ubl) << 6) | ((temp2_ubl == result3_ubl) >> 2))
    result2_ubl  = (((temp1_ubl == result2_ubl) << 6) | ((temp2_ubl == result2_ubl) >> 2))
    result1_ubl  = (((temp1_ubl == result1_ubl) << 6) | ((temp2_ubl == result1_ubl) >> 2))
    result0_ubl  = (((temp1_ubl == result0_ubl) << 6) | ((temp2_ubl == result0_ubl) >> 2))

    result3_ubl  =  result3_ubl ^ 17
    result2_ubl  = result2_ubl ^ 86
    result1_ubl  = result1_ubl ^ 75
    result0_ubl  = result0_ubl ^ 52

    if result2_ubl & 0x04:
        temp3_ubl = (temp1_ubl == (result3_ubl >> 4)) | (temp2_ubl == (result3_ubl << 4))
        temp2_ubl = (temp1_ubl == (result2_ubl >> 4)) | (temp2_ubl == (result2_ubl << 4))
        result3_ubl = temp2_ubl
        result2_ubl = temp3_ubl

    else:
        temp3_ubl = (temp1_ubl == (result1_ubl >> 4)) | (temp2_ubl == (result1_ubl << 4))
        temp2_ubl = (temp1_ubl == (result0_ubl >> 4)) | (temp2_ubl == (result0_ubl << 4))
        result1_ubl = temp2_ubl
        result0_ubl = temp3_ubl

    print("    Key Calculated.")
    R1 = result0_ubl
    R2 = result1_ubl
    R3 = result2_ubl
    R4 = result3_ubl
    print("    ", R1, R2, R3, R4)
    return R1, R2, R3, R4

########################################################################################################
'''
    DST ENCRYPTION ALGORITHM 
        CONVERT SERIAL NUMBER TO 4 BYTE HEXADECIMAL FORM PERFORM ROTATES ON THE 4 SERIAL NUMBER BYTES
        AS FOLLOWS - ROTATE RIGHT, PUTTING LEAST SIGNIFICANT BIT INTO THE MOST SIGNIFICANT BIT.
        1. SN[0] DO NOT ROTATE
        2. SN[1] ROTATE RIGHT ONCE
        3. SN[3] ROTATE RIGHT 5 TIMES
        4. SN[4] ROTATE RIGHT 3 TIMES
        CALCULATE BYTES AS FOLLOWS:
        1. BYTE[0] = 02(EBEM2 WAS 00, GBEM 01)
        2. BYTE[1] = ((SN[1] & 0F) << 4) +(SN[3] & 0F ^ 3A)
        3. BYTE[2] = ((SN[3] & F0) + )...
        WIP
        SN = 0x01234567
        SN[0] = 0
        SN[1] = 0
        SN[2] = 0
        SN[3] = 0
'''
########################################################################################################
'''
    DIAGNOSTIC SERVICE 0X10 DIAGNOSTIC SESSION CONTROL - ecuAdjustmentSession
'''
ECUADJ_REQ              = [0x02, 0x10, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00]
ECUADJ_MSG = can.Message(
    arbitration_id = BEM_DiagSig_Rx, 
    data           = ECUADJ_REQ, 
    is_extended_id = False
        )    
'''
    DIAGNOSTIC SERVICE 0X2F INPUTOUTPUTCONTROLBYLOCALINDENTIFIER - CALL ROUTINE 0XF2A9
'''
IOBCI_REQ              = [0x07, 0x2F, 0xF2, 0xA9, 0x07, 0x97, 0x6A, 0x65]
IOBCI_MSG = can.Message(
    arbitration_id = BEM_DiagSig_Rx, 
    data           = IOBCI_REQ, 
    is_extended_id = False
        )    
'''
    CONNECT TO BEM CCP REQUEST
'''
CCPCTB_REQ              = [0x01, 0x01, 0xBE, 0xBE, 0x00, 0x00, 0x00, 0x00]
CCPCTB_MSG = can.Message(
    arbitration_id = BEM_CCP_Rx, 
    data           = CCPCTB_REQ, 
    is_extended_id = False
        )    
'''
    GET SECURITY SEED REQUEST
'''
CCPGSS_REQ              = [0x12, 0x02, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00]
CCPGSS_MSG = can.Message(
    arbitration_id = BEM_CCP_Rx, 
    data           = CCPGSS_REQ, 
    is_extended_id = False
        )    
'''
    CALCULATED KEY RESPONSE TO UNLOCK
'''
CCPSKR_REQ              = [0x13, 0x03, R1, R2, R3, R4, 0x00, 0x00]
CCPSKR_MSG = can.Message(
    arbitration_id = BEM_CCP_Rx, 
    data           = CCPSKR_REQ, 
    is_extended_id = False
        )    
'''
    DISCONNECT FROM BEM CCP SESSION
'''
#CCPSKR_REQ              = [0x13, 0x03, R1, R2, R3, 0x00, 0x00, 0x00]
#CCPSKR_MSG = can.Message(
#    arbitration_id = BEM_CCP_Rx, 
#    data           = [CCPSKR_REQ], 
#    is_extended_id = False
#        )    
'''
'''
CCP_SET_MTA          = [0x02, 0x04, 0x00, 0x00, WW, XX, YY, ZZ]
CCPSKR_MSG = can.Message(
    arbitration_id = BEM_CCP_Rx, 
    data           = CCPSKR_REQ, 
    is_extended_id = False
        )    
'''
    DOWNLOAD TO EEPROM
'''
CCP_DLD_E2P          = [0x03, 0x05, SS, UU, UU, UU, UU, 0x00]
CCP_DLD_E2P_MSG = can.Message(
    arbitration_id = BEM_CCP_Rx, 
    data           = CCP_DLD_E2P, 
    is_extended_id = False
        )    
'''
    UPLOAD FROM EEPROM 
'''
CCP_UPL_E2P          = [0x04, 0x06, SS, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_UPL_E2P_MSG = can.Message(
    arbitration_id = BEM_CCP_Rx, 
    data           = CCP_UPL_E2P, 
    is_extended_id = False
        )    
'''
    SHORT DOWNLOAD TO EEPROM
'''
CCP_DLD_E1P          = [0x0F, 0x07, SS, 0x00, WW, XX, YY, ZZ]
CCP_DLD_E1P_MSG = can.Message(
    arbitration_id = BEM_CCP_Rx, 
    data           = CCP_DLD_E1P, 
    is_extended_id = False
        )    
'''
    RESPONSES
'''
BEM_PSR              = [0x04, 0x6F, 0xF2, 0xA9, 0x00, 0x00, 0x00, 0x00]
BEM_CNC              = [0x03, 0x7F, 0x2F, 0x12, 0x00, 0x00, 0x00, 0x00]
CCP_PSR              = [0xFF, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_NRC              = [0xFF, 0x32, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_GSS              = [0xFF, 0x00, 0x02, 0x01, K1, K2, K3, K4]
#CCP_AOK              = [0xFF, 0x00, 0x02, 0x00, K1, K2, K3, K4]
CCP_SAG              = [0xFF, 0x00, 0x03, 0x02, 0x00, 0x00, 0x00, 0x00]
CCP_SAD              = [0xFF, 0x35, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_DIS              = [0xFF, 0x00, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_OOR              = [0xFF, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_MTA_SET          = [0xFF, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_ACC_LKD          = [0xFF, 0x35, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_MTA_OOR          = [0xFF, 0x32, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_E2P_DSD          = [0xFF, 0x00, 0x05, 0x00, 0x00, 0x00, 0x40, 0x04]
CCP_MTA_OOR          = [0xFF, RR, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_DAT_REQ          = [0xFF, 0x00, 0x06, UU, UU, UU, UU, UU]
CCP_DAT_NRC          = [0xFF, RR, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00]
CCP_E1P_REQ          = [0xFF, RR, 0x07, UU, UU, UU, UU, UU]
CCP_E1P_NRC          = [0xFF, RR, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00]

def testerPresentTask():
    '''
        TESTERPRESENT SEND PERIODIC TASK NEEDED
    '''
    pass

########################################################################################################
def sendCANmessage(msgToSend):
    '''
    msgToSend options = IOBCI_MSG, CCPCTB_MSG 
    '''    
    global highSpeedCan
    highSpeedCan.send(msgToSend)
    '''
        print(f"Message sent on {MidSpeedCan.channel_info}")
        error handling goes here bruh
    '''
    return

########################################################################################################
def cleanline():                      # CLEANS THE LAST OUTPUT LINE FROM THE CONSOLE
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def cleanscreen():                    # cleans the whole console screen
    os.system("clear")

########################################################################################################
def msgbuffer():
    global message, q, BEM_CCP_Rx, BEM_CCP_Tx, BEM_DiagSig_Rx, BEM_DiagSig_Tx                            
    while True:
        message = highSpeedCan.recv()         
        '''
            IF RECIEVING CAN FRAMES THEN PUT THESE CAN ARB ID'S INTO A QUEUE
        '''
        if message.arbitration_id   == BEM_DiagSig_Rx:                        
            q.put(message)
            print("    0x726 BEM_DiagSig_Rx:")
            print("   ", message)        
        elif message.arbitration_id == BEM_DiagSig_Tx:                        
            q.put(message)
            print("    0x72E BEM_DiagSig_Tx:")
            print("   ", message)        
        elif message.arbitration_id == BEM_CCP_Rx:                        
            q.put(message)
            print("    0x706 BEM_CCP_Rx:")
            print("   ", message)            
        elif message.arbitration_id == BEM_CCP_Tx:                        
            q.put(message)
            print("    0x712 BEM_CCP_Tx:") 
            print("   ", message) 
        else:
            pass

########################################################################################################
def main():
    global highSpeedCan, message, q 
    """
        CAN message printer
    """
    try:
        while True:
            for i in range(8):
                while(q.empty() == True): 
                    ''' pass in a loop if there are no can messages queued '''
                    sendCANmessage(ECUADJ_MSG)
                    pass
                message = q.get()   
                c = '{0:f},{1:d},'.format(message.timestamp,count)
                print("    0x2F inputOutputControlByCommonIdentifier routine request sent. ")
                sendCANmessage(IOBCI_MSG)    
                if message.arbitration_id == BEM_DiagSig_Tx and message.data == BEM_PSR:
                    print("    0x2F inputOutputControlByCommonIdentifier routine request accepted - BEM entering into CCP State.")
                    time.sleep(0.25)                    
                    sendCanMessage(CCPCTB_MSG)
                    if message.arbitration_id == BEM_CCP_Tx and message.data == CCP_PSR:
                        print("    Can Calibration Protocol is active | Rx 0x706 | Tx 0x712 |")
                        time.sleep(0.25)                    
                        sendCANmessage(CCPGSS_MSG)
                        time.sleep(0.25)                    
                        print("    Requesting CCP Security Seed.")
                        time.sleep(0.25)                    
                        if message.arbitration_id == BEM_CCP_Tx and message.data[0:3] == CCP_GS1:
                            K1 = message.data[4] 
                            K2 = message.data[5] 
                            K3 = message.data[6] 
                            K4 = message.data[7] 
                            calculateResult(K1, K2, K3, K4)
                            R1 = result0_ubl
                            R2 = result1_ubl
                            R3 = result2_ubl
                            R4 = result3_ubl
                            sendCANmessage(CCPSKR_MSG)
                            if message.arbitration_id   == BEM_CCP_Tx and message.data == CCP_SAG: 
                                print("    CCP SECURITY ACCESS GRANTED. ")
                                time.sleep(0.25) 
                                ''' start testerPresent task '''    
                                ''' would you like a slice of EEPROM cake? '''               
                            elif message.arbitration_id == BEM_CCP_Tx and message.data == CCP_SAD: 
                                print("    CCP SECURITY ACCESS DENIED.  ")
                                time.sleep(0.25)                    
                        else:
                            pass
                    else:
                        pass
                elif message.arbitration_id == BEM_DiagSig_Tx and (message.data == BEM_CNC or message.data[1] == 0x7F):
                    ####################
                    '''
                        Negative Response Codes { 0x7F }
                    '''
                    ####################
                    print("""    0x7F Negative Response Recieved | Hex Codes: 
                                    postiveResponse                                       = 0x00
                                    generalReject                                         = 0x10
                                    serviceNotSupported                                   = 0x11
                                    subFunctionNotSupported                               = 0x12
                                    responseTooLong                                       = 0x14
                                    busyRepeatRequest                                     = 0x21
                                    conditionsNotCorrect                                  = 0x22
                                    requestSequenceError                                  = 0x24
                                    requestOutOfRange                                     = 0x31
                                    securityAccessDenied                                  = 0x33
                                    invalidKey                                            = 0x35
                                    exceedNumberOfAttempts                                = 0x36
                                    requiredTimeDelayNotExpired                           = 0x37
                                    uploadDownloadNotAccepted                             = 0x70
                                    generalProgrammingFailure                             = 0x72
                                    requestCorrectlyReceived_ResponsePending              = 0x78
                                    subFuncionNotSupportedInActiveSession                 = 0x7E
                                    serviceNotSupportedInActiveSession                    = 0x7F
                                    rpmTooHigh                                            = 0x81
                                    rpmTooLow                                             = 0x82
                                    engineIsRunning                                       = 0x83
                                    engineIsNotRunning                                    = 0x84
                                    shifterLeverNotInPark                                 = 0x90
                        """)
                else:
                    pass                
    except KeyboardInterrupt:
        displayLicense()                                            # quit if ctl + c is hit
        sys.exit(0)  
    except Exception:
        displayLicense()                                            # quit if ctl + c is hit
        traceback.print_exc(file=sys.stdout)                     # quit if there is a python problem
        sys.exit()
    except OSError:
        displayLicense()                                            # quit if ctl + c is hit
        sys.exit()                                               # quit if there is a system issue
    return 
########################################################################################################

########################################################################################################
if __name__ == "__main__":                                     
    '''
        MAIN SCRIPT - 
        REQUESTS THE ROUTINE VIA STANDARD DIANGOSTICS
        SETS THE BEM INTO UNLOCKED CCP STATE
        NO TESTER PRESENT TASK YET SO WILL TIME OUT AFTER 2000 MS
    '''
    cleanscreen()
    displayLicense()
    time.sleep(3)
    cleanscreen()
    scroll()    
    setup()    
    q                      = queue.Queue()                       
    rx                     = Thread(target = msgbuffer)          
    rx.start()

########################################################################################################
