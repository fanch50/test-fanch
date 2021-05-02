a = 0
"""

programme test fanch

"""

def on_forever():
    global a
    while True:
        a = 0
        for b in range(10):
            basic.show_number(b)
            for index in range(8):
                led.toggle(0, 0)
                basic.pause(200)
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
