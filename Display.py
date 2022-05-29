from  ST7735 import Display, color565, sysfont as sysfont
from machine import SPI,ADC
from time import sleep_ms


def circleBall():
    sck = Pin(18)
    miso= Pin(19)
    mosi= Pin(23)
    SPI_CS = 26
    SPI_DC = 5
    spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
    display=Display(spi,SPI_CS,SPI_DC)
    #display.draw_text(0, 0, 'Hello World!', sysfont, color565(255, 0, 0))
    display.clear()
    display.draw_filledCircle(6,6,4,color565(0,0,255))

def adcRead():
    x=ADC(Pin(33))
    y=ADC(Pin(34))
    val_x=x.read_u16()
    val_y=y.read_u16()
    return [val_x,val_y]
def adcConvert(x,y):
      sck = Pin(18)
    miso= Pin(19)
    mosi= Pin(23)
    SPI_CS = 26
    SPI_DC = 5
    spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
    display=Display(spi,SPI_CS,SPI_DC)
    #display.draw_text(0, 0, 'Hello World!', sysfont, color565(255, 0, 0))
    display.clear()
    display.draw_filledCircle(x,y,4,color565(0,0,255))
    

adcRead()
    