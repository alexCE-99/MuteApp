muteKey = "["
exitKey = "escape"
unmuteKey = "]"
running = False


# functions to modify variables called from ui
def modify_MuteKey(newMute):
    global muteKey
    if newMute == "":
        muteKey = muteKey
    else:
        muteKey = newMute


def modify_UnmuteKey(newUnmute):
    global unmuteKey
    if newUnmute == "":
        unmuteKey = unmuteKey
    else:
        unmuteKey = newUnmute


def modify_ExitKey(newExit):
    global exitKey
    if newExit == "":
        exitKey = exitKey
    else:
        exitKey = newExit
