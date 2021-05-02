let a = 0
basic.forever(function () {
    while (true) {
        a = 0
        for (let b = 0; b <= 9; b++) {
            basic.showNumber(b)
            for (let index = 0; index < 8; index++) {
                led.toggle(0, 0)
                basic.pause(200)
            }
        }
    }
})
basic.forever(function () {
	
})
