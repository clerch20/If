import RoboPiLib as RPL
import setup
x = 1
RPL.pinMode(16,RPL.INPUT)
RPL.pinMode(17, RPL.INPUT)
while x == 1:
reading16 = RPL.digitalRead(16)
	RPL.servoWrite(0,1590)
elif reading16 == 1 and reading17 == 1:
	RPL.servoWrite(0,1500)