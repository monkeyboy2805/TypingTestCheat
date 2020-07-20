import tkinter
pc = tkinter.Tk()
pc.withdraw()
pc.clipboard_clear()
pc.clipboard_append(" ") #push some garbage onto the clipboard to stop it crashing
previous_clip = pc.clipboard_get()
pc.update()
pc.destroy()
current_clip = ""
while True:
    cc = tkinter.Tk()
    cc.withdraw()
    current_clip = cc.clipboard_get()
    cc.update()
    cc.destroy()
    if current_clip != previous_clip:
        r = tkinter.Tk()
        r.withdraw()
        out = ""
        for i in range(0, len(current_clip)):
            if ord(current_clip[i]) <= 120483 and ord(current_clip[i]) >= 120458:
                out = out + chr(ord(current_clip[i]) - 120361)
            elif ord(current_clip[i]) <= 8200 and ord(current_clip[i]) >= 8192:
                out = out + " "
            else:
                out = out + current_clip[i]
        out = out.replace("   ", " ")
        out = out.replace("  ", " ")
        r.clipboard_clear()
        r.clipboard_append(out)
        r.update()
        r.destroy()
    previous_clip = current_clip
