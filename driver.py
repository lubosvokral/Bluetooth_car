from machine import Pin,PWM,UART #importing PIN and PWM
import time #importing time

#OUT1  and OUT2
In1=Pin(6,Pin.OUT)  #IN1`
In2=Pin(7,Pin.OUT)  #IN2


#OUT3  and OUT4
In3=Pin(4,Pin.OUT)  #IN3
In4=Pin(3,Pin.OUT)  #IN4

#OUT5  and OUT6
In5=Pin(17,Pin.OUT)  #IN1`
In6=Pin(16,Pin.OUT)  #IN2

#OUT7  and OUT8
In7=Pin(15,Pin.OUT)
In8=Pin(14,Pin.OUT)

EN_A=PWM(Pin(8))
EN_B=PWM(Pin(2))
EN_C=PWM(Pin(9))
EN_D=PWM(Pin(18))
# Defining frequency for enable pins
EN_A.freq(1500)
EN_B.freq(1500)
EN_C.freq(1500)
EN_D.freq(1500)
# Setting maximum duty cycle for maximum speed (0 to 65025)
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)
EN_C.duty_u16(65025)
EN_D.duty_u16(65025)

# Left
def turn_left():
    In1.low()
    In2.high()
    In3.low()
    In4.high()
    In5.high()
    In6.low()
    In7.high()
    In8.low()
    
# Right
def turn_right():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    In5.low()
    In6.high()
    In7.low()
    In8.high()
# Backward
def move_backward():
    In1.low()
    In2.high()
    In3.high()
    In4.low()
    In5.low()
    In6.high()
    In7.high()
    In8.low()
# Forward
def move_forward():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    In5.high()
    In6.low()
    In7.low()
    In8.high()

def step_left():
    In1.low()
    In2.high()
    In3.low()
    In4.high()
    In5.low()
    In6.high()
    In7.low()
    In8.high()

def step_right():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    In5.high()
    In6.low()
    In7.high()
    In8.low()
# Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    In5.low()
    In6.low()
    In7.low()
    In8.low()
