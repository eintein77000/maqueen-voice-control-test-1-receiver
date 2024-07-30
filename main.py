def on_received_number(receivedNumber):
    global cmd
    cmd = receivedNumber
    if cmd == 62:
        basic.show_icon(IconNames.HAPPY)
    elif cmd == 65:
        basic.clear_screen()
    elif cmd == 103:
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    elif cmd == 104:
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    elif cmd == 5:
        maqueen.motor_stop(maqueen.Motors.ALL)
        basic.show_icon(IconNames.NO)
    elif cmd == 22:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 40)
        basic.show_string("F")
    elif cmd == 23:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 40)
        basic.show_string("R")
    elif cmd == 6:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 30)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 30)
        basic.show_string("L")
    elif cmd == 7:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 30)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 30)
        basic.show_string("R")
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
input.on_button_pressed(Button.B, on_button_pressed_b)

cmd = 0
radio.set_group(42)
maqueen.motor_stop(maqueen.Motors.ALL)
cmd = 999
basic.show_icon(IconNames.CHESSBOARD)

def on_forever():
    pass
basic.forever(on_forever)
