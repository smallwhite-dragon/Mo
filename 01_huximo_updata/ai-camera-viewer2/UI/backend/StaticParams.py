#PLC
0x09
TMP_SELECTED    =0x10    #选中模板
AUTO            =0x0C    #自动模式
0x0E    #手动模式
0x14    #手动模式下，进入打标位置
0x15    #手动模式下，进入DPM位置
AUTO_OK     =0x07    #自动模式下，合格退出
AUTO_NOK    =0x08    #自动模式下，不合格退出
AUTO_CFM    =0x0A    #自动模式确认发送

ISPOSITION  =    0x04060D    #到位
EMCSTOP     =    0x04110D    #急停
RESET       =    0x04120D    #复位
SETAUTOOK   =    0x040B0D    #自动模式确认接收

#打标机协议
SOH = 0x001
STX = 0x002
ETX = 0x003
CR  = 0x00D
ACK = 0x006
NAK = 0x015

#打标机状态
OFFLINE     = '00000000'
ABORTED     = '00000001'
ONLINE      = '00000010'
TARGET      = '00000100'
HOMING      = '00000200'
PRINTING    = '00000400'
DRYRUN      = '00000800'
PAUSED      = '00001000'
PARKING     = '00002000'
BATCH       = '00003000'
REPEAT      = '00008000'
PREVIEW     = '00010000'
PREPOSITION = '00020000'
INPUT       = '00040000'
SERIALTOOL  = '00080000'
SELECTED    = '00100000'
PULSE       = '00010000'
FLY         = '00010000'
FLY_TRIGGER = '00010000'
FLY_AUTO_GO = '00010000'
FLY_TRIGGER_LASER   = '00010000'
FLY_AXIS_RESET      = '00010000'