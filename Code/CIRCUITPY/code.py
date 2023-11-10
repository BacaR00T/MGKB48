print("MGKB48")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.hid import HIDModes


keyboard = KMKKeyboard()
layers_ext = Layers()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

                                                                                                #right
keyboard.col_pins = (board.P0_17, board.P0_20, board.P0_22, board.P0_24, board.P1_00, board.P0_11, board.P0_09, board.P0_10, board.P1_11, board.P1_13, board.P1_15, board.P0_02, )
keyboard.row_pins = (board.P1_04, board.P1_06, board.P1_01, board.P1_02,)                           
keyboard.diode_orientation = DiodeOrientation.COL2ROW

LOWER = KC.MO(1)
RAISE = KC.MO(2)
EXTRA = KC.MO(3)

keyboard.keymap = [
    #KEYS
    [
        KC.ESC,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,           KC.BSLS,  
        KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,           KC.H,       KC.J,       KC.K,       KC.L,       KC.SCOLON,      KC.QUOT,    
        KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,           KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLASH,       KC.EQL,    
        KC.LCTRL,   KC.LGUI,    KC.LALT,    KC.TAB,     KC.BSPC,    KC.SPC,         KC.TRNS,    KC.ENT,     KC.MINS,    LOWER,      EXTRA,          RAISE,    
    
    ],
    #LOWER
    [
       KC.TILD,     KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,        KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,        KC.UNDS,
       KC.TRNS,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.TRNS,
       KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.LBRC,     KC.RBRC,        KC.MPLY,     KC.MPRV,    KC.MNXT,    KC.VOLD,   KC.VOLU,     KC.MUTE,
       KC.MB_RMB,   KC.MB_MMB,  KC.MB_LMB,  KC.LGUI,   KC.MW_UP,     KC.MW_DN,      KC.TRNS,     KC.BT_CLEAR_BONDS,    KC.TRNS,    KC.TRNS,   KC.TRNS,     KC.TRNS,
    
    ],
    #RAISE  
    [
        KC.F1,       KC.F2,      KC.F3,      KC.F4,     KC.F5,       KC.F6,          KC.F7,       KC.F8,      KC.F9,      KC.F10,    KC.F11,      KC.F12,
        KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.SLCK,     KC.PSCR,        KC.LEFT,     KC.RIGHT,   KC.UP,      KC.DOWN,   KC.TRNS,     KC.TRNS,
        KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.TRNS,     KC.TRNS,
        KC.RESET,     KC.TRNS,    KC.TRNS,  KC.TRNS,   KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.TRNS,     KC.TRNS,

    ],
    #EXTRA
    [
        KC.F1,       KC.F2,      KC.F3,      KC.F4,     KC.F5,       KC.F6,          KC.F7,       KC.F8,      KC.F9,      KC.F10,    KC.F11,      KC.F12,
        KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.SLCK,     KC.PSCR,        KC.LEFT,     KC.RIGHT,   KC.UP,      KC.DOWN,   KC.TRNS,     KC.TRNS,
        KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.TRNS,     KC.TRNS,
        KC.RESET,     KC.TRNS,    KC.TRNS,  KC.TRNS,   KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,    KC.TRNS,    KC.TRNS,   KC.TRNS,     KC.TRNS,
        
    ],
]
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode
import busio as io

i2c0 = io.I2C(scl=board.P0_31, sda=board.P0_29)
trackball = Trackball(i2c0, mode=TrackballMode.MOUSE_MODE)
keyboard.modules.append(trackball)
trackball.set_rgbw(255, 255, 255, 255)
trackball.set_red(0)
trackball.set_green(100)
trackball.set_blue(100)
trackball.set_white(0)


keyboard.debug_enabled = True
from kmk.hid import HIDModes

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='MGKB48')
    
