import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

tm.show("HELLO")
tm.scroll("1234567890 CAFE")