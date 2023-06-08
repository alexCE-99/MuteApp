muteKey = "["
exitKey = "escape"
unmuteKey = "]"


# functions to modify variables called from ui
def modify_MuteKey(newMute):
    global muteKey
    muteKey = newMute


def modify_UnmuteKey(newUnmute):
    global unmuteKey
    unmuteKey = newUnmute


def modify_ExitKey(newExit):
    global exitKey
    exitKey = newExit
