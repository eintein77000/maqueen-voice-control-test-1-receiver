radio.onReceivedNumber(function (receivedNumber) {
    cmd = receivedNumber
    if (cmd == 62) {
        basic.showIcon(IconNames.Happy)
    } else if (cmd == 65) {
        basic.clearScreen()
    } else if (cmd == 103) {
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    } else if (cmd == 104) {
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    } else if (cmd == 5) {
        maqueen.motorStop(maqueen.Motors.All)
        basic.showIcon(IconNames.No)
    } else if (cmd == 22) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 40)
        basic.showString("F")
    } else if (cmd == 23) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 40)
        basic.showString("R")
    } else if (cmd == 6) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 30)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 30)
        basic.showString("L")
    } else if (cmd == 7) {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 30)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 30)
        basic.showString("R")
    }
})
input.onButtonPressed(Button.A, function () {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
})
input.onButtonPressed(Button.B, function () {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
})
let cmd = 0
radio.setGroup(42)
maqueen.motorStop(maqueen.Motors.All)
cmd = 999
basic.showIcon(IconNames.Chessboard)
basic.forever(function () {
	
})
