from datetime import datetime


# Converts a number of seconds into a timestamp of HH:MM:SS (HH is ignored unless > 0)
def convert_seconds_to_duration(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    duration = str(s)
    if s < 10:
        duration = "0" + duration
    duration = str(m) + ":" + duration
    if h > 0:
        if m < 10:
            duration = "0" + duration
        return str(h) + ":" + duration
    return duration


# Destroys all children of a frame.
def destroy_children(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Performs pack_forget for all children of a frame.
def pack_forget_children(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()


# Removes all whitespace, tab, newline, etc. from a string and returns.
def trim(text):
    return text.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")


# Returns date time in M/D/Y H:M:S format.
def get_date_time():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")
