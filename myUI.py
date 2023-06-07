import tkinter as tk
import variables
import customtkinter


# def create_ui():
#     window = customtkinter.CTk()
#     window.title("Mute Current Application")
#     window.geometry("1000x500")

#     global muteTextbox
#     muteTextbox = customtkinter.CTkTextbox(window)
#     muteTextbox.place(x="200", y="250")

#     button = customtkinter.CTkButton(window, text="Set Mute Key", command=SetMute)
#     button.place(x="250", y="350")

#     global UnmuteTextbox
#     UnmuteTextbox = customtkinter.CTkTextbox(window)
#     UnmuteTextbox.pack()

#     global EscapeTextbox
#     EscapeTextbox = customtkinter.CTkTextbox(window)
#     EscapeTextbox.pack()

#     window.mainloop()


def create_ui():
    customtkinter.set_appearance_mode(
        "dark"
    )  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme(
        "blue"
    )  # Themes: "blue" (standard), "green", "dark-blue"

    app = customtkinter.CTk()
    app.geometry("700x400")
    app.title("Mute Current Application")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(
        text="Mute Current Application", master=frame_1, justify=customtkinter.LEFT
    )
    label_1.pack(pady=10, padx=10)

    global muteTextbox
    muteTextbox = customtkinter.CTkEntry(
        height=10, width=50, master=frame_1, placeholder_text="..."
    )
    muteTextbox.pack()
    muteButton = customtkinter.CTkButton(
        text="Set Mute Button", master=frame_1, command=SetMute
    )
    muteButton.pack(pady=10, padx=10)

    # global unmuteTextbox
    # unmuteTextbox = customtkinter.CTkEntry(master=frame_1, placeholder_text="...")
    # unmuteTextbox.pack(pady=10, padx=10)
    # UnmuteButton = customtkinter.CTkButton(
    #     text="Set nmute Button", master=frame_1, command=SetUnmute
    # )
    # UnmuteButton.pack(pady=10, padx=10)

    # global exitTextbox
    # exitTextbox = customtkinter.CTkEntry(
    #     height="10", width="100", master=frame_1, placeholder_text="..."
    # )
    # exitTextbox.pack(pady=10, padx=10)
    # exitButton = customtkinter.CTkButton(
    #     text="Set Exit Button", master=frame_1, command=SetExit
    # )
    # exitButton.pack(pady=10, padx=10)

    # tabview_1 = customtkinter.CTkTabview(master=frame_1, width=200, height=70)
    # tabview_1.pack(pady=10, padx=10)
    # tabview_1.add("CTkTabview")
    # tabview_1.add("Tab 2")

    app.mainloop()


def SetMute():
    newMute = muteTextbox.get()
    variables.modify_MuteKey(newMute)


def SetUnmute():
    newUnmute = unmuteTextbox.get()
    variables.modify_UnmuteKey(newUnmute)


def SetExit():
    newExit = exitTextbox.get()
    variables.modify_UnmuteKey(newExit)
