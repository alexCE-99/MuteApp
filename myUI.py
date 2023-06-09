# import dependencies
import tkinter as tk
import variables
import customtkinter


def create_ui():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    global app
    app = customtkinter.CTk()
    app.geometry("800x400")
    app.title("Mute Current Application")
    app.resizable(0, 0)

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    # using tkinter's grid geometry system instead of pack
    frame_1.columnconfigure(0, weight=1, pad=10)
    frame_1.columnconfigure(1, weight=1)
    frame_1.columnconfigure(2, weight=1)

    frame_1.rowconfigure(0, weight=1)
    frame_1.rowconfigure(1, weight=1)
    frame_1.rowconfigure(2, weight=1, pad=10)
    frame_1.rowconfigure(3, weight=1)

    label_1 = customtkinter.CTkLabel(text="Mute Current Application", master=frame_1)
    label_1.grid(row=0, column=1)

    global muteTextbox
    muteTextbox = customtkinter.CTkEntry(
        height=10, width=80, master=frame_1, placeholder_text=variables.muteKey
    )
    muteTextbox.grid(row=1, column=0, sticky="s")
    muteButton = customtkinter.CTkButton(
        text="Set Mute Button", master=frame_1, command=SetMute
    )
    muteButton.grid(row=2, column=0, sticky="n", pady=10)

    global unmuteTextbox
    unmuteTextbox = customtkinter.CTkEntry(
        height=10, width=80, master=frame_1, placeholder_text=variables.unmuteKey
    )
    unmuteTextbox.grid(row=1, column=1, sticky="s")
    UnmuteButton = customtkinter.CTkButton(
        text="Set Unmute Button", master=frame_1, command=SetUnmute
    )
    UnmuteButton.grid(row=2, column=1, sticky="n", pady=10)

    global exitTextbox
    exitTextbox = customtkinter.CTkEntry(
        height=10, width=80, master=frame_1, placeholder_text=variables.exitKey
    )
    exitTextbox.grid(row=1, column=2, sticky="s")
    exitButton = customtkinter.CTkButton(
        text="Set Exit Button", master=frame_1, command=SetExit
    )
    exitButton.grid(row=2, column=2, sticky="n", pady=10)

    StartScriptButton = customtkinter.CTkButton(
        text="Start Script", master=frame_1, command=StartScript
    )
    StartScriptButton.grid(row=3, column=1, pady=10)

    app.protocol("WM_DELETE_WINDOW", on_closing)

    app.mainloop()


def StartScript():
    variables.running = True
    app.destroy()


def on_closing():
    variables.running = False
    app.destroy()


def SetMute():
    newMute = muteTextbox.get()
    variables.modify_MuteKey(newMute)


def SetUnmute():
    newUnmute = unmuteTextbox.get()
    variables.modify_UnmuteKey(newUnmute)


def SetExit():
    newExit = exitTextbox.get()
    variables.modify_UnmuteKey(newExit)
