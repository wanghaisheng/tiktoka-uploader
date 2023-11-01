
import tkinter as tk
from tkinter import OptionMenu, filedialog,ttk,Message,Toplevel,messagebox
import pycountry
import os,re

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# 信息消息框
def showinfomsg(message,title='hints',DURATION = 500,parent=None):
    # msg1 = messagebox.showinfo(title="消息提示", message=message)
    # messagebox.after(2000,msg1.destroy)
    # parent.focus_force()
    top = Toplevel(parent)
    top.title(title)
    center_window(top)    
    # Update the Toplevel window's width to adapt to the message width

    message_widget=Message(top, text=message, padx=120, pady=120)
    message_widget.pack()
    message_widget.update_idletasks()
    window_width = message_widget.winfo_reqwidth() + 40  # Add padding      
    top.geometry(f"{window_width}x200")  # You can adjust the height as needed      
    top.after(DURATION, top.destroy)


# 疑问消息框

def askquestionmsg(message,title='hints',DURATION = 500,parent=None):
    top = Toplevel(parent)
    top.title(title)
    center_window(top)        
    msg4 = messagebox.askquestion(title="询问确认", message=message)
    print(msg4)


def askokcancelmsg(message,title='hints',DURATION = 500,parent=None):
    top = Toplevel(parent)
    top.title(title)
    center_window(top)        
    msg5 = messagebox.askokcancel(title="确定或取消", message=message)
    print(msg5)


def askretrycancelmsg(message,title='hints',DURATION = 500,parent=None):
    top = Toplevel(parent)
    top.title(title)
    center_window(top)        
    msg6 = messagebox.askretrycancel(title="重试或取消", message=message)
    print(msg6)


def askyesonmsg(message,title='hints',DURATION = 500,parent=None):
    top = Toplevel(parent)
    top.title(title)
    center_window(top)        
    msg7 = messagebox.askyesno(title="是或否", message="是否开启团战")
    print(msg7)


def askyesnocancelmsg(message,title='hints',DURATION = 500,parent=None):
    top = Toplevel(parent)
    top.title(title)
    center_window(top)           
    msg8 = messagebox.askyesnocancel(title="是或否或取消", message="是否打大龙", default=messagebox.CANCEL)
    print(msg8)
    
def find_key(input_dict, value):
    if type(input_dict)==list:
        input_dict=dict(input_dict)
    result = "None"
    for key,val in input_dict.items():
        if val == value:
            result = key
    return result

def _copy(event):
    try:
        string = event.widget.selection_get()
        clip.copy(string)
    except:
        pass


def language_from_browser(*pargs):
    """Attempts to determine the user's language based on information supplied by the user's web browser."""
    if len(pargs) > 0:
        restrict = True
        valid_options = [lang for lang in pargs]
    else:
        restrict = False
    if 'headers' in this_thread.current_info:
        langs = [entry.split(";")[0].strip() for entry in this_thread.current_info['headers'].get('Accept-Language', '').lower().split(",")]
    else:
        return None
    for lang in langs:
        if restrict:
            if lang in valid_options:
                return lang
            else:
                continue
        if len(lang) == 2:
            try:
                pycountry.languages.get(alpha_2=lang)
                return lang
            except:
                continue
        if len(lang) == 3:
            try:
                pycountry.languages.get(alpha_3=lang)
                return lang
            except:
                continue
    for lang in langs:
        if len(lang) <= 3:
            continue
        this_lang = re.sub(r'[\-\_].*', r'', lang)
        if restrict:
            if this_lang in valid_options:
                return this_lang
            else:
                continue
        if len(this_lang) == 2:
            try:
                pycountry.languages.get(alpha_2=this_lang)
                return this_lang
            except:
                continue
        if len(this_lang) == 3:
            try:
                pycountry.languages.get(alpha_3=this_lang)
                return this_lang
            except:
                continue
    return None

def country_name(country_code):
    """Given a two-digit country code, returns the country name."""
    return pycountry.countries.get(alpha_2=country_code).name

def state_name(state_code, country_code=None):
    """Given a two-digit U.S. state abbreviation or the abbreviation of a
    subdivision of another country, returns the state/subdivision
    name."""
    if country_code is None:
        country_code = 'US'
    for subdivision in pycountry.subdivisions.get(country_code=country_code):
        m = re.search(r'-([A-Z]+)$', subdivision.code)
        if m and m.group(1) == state_code:
            return subdivision.name
    return state_code
    #return us.states.lookup(state_code).name

def subdivision_type(country_code):
    """Returns the name of the most common country subdivision type for
    the given country code."""
    counts = dict()
    for subdivision in pycountry.subdivisions.get(country_code=country_code):
        if subdivision.parent_code is not None:
            continue
        if subdivision.name not in counts:
            counts[subdivision.type] = 1
        else:
            counts[subdivision.type] += 1
    counts_ordered = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    if len(counts_ordered) > 1 and counts[counts_ordered[1]] > 1:
        return counts_ordered[0] + '/' + counts_ordered[1]
    elif len(counts_ordered) > 0:
        return counts_ordered[0]
    else:
        return None
    
def countries_list():
    """Returns a list of countries, suitable for use in a multiple choice field."""
    return [{country.alpha_2: country.name} for country in sorted(pycountry.countries, key=lambda x: x.name)]

def states_list(country_code=None):
    """Returns a list of U.S. states or subdivisions of another country,
    suitable for use in a multiple choice field."""
    if country_code is None:
        country_code = 'US'
    mapping = dict()
    for subdivision in pycountry.subdivisions.get(country_code=country_code):
        if subdivision.parent_code is not None:
            continue
        m = re.search(r'-([A-Z0-9]+)$', subdivision.code)
        if m:
            mapping[m.group(1)] = subdivision.name
    return mapping
def city_list(state_code=None,country_code=None):
    pass
# https://github.com/dr5hn/countries-states-cities-database
# http://www.geonames.org/
# https://github.com/geopy/geopy
# https://gadm.org/
# https://area.site/world
# https://gitcode.com/mirrors/wizardcode/world-area/overview?utm_source=csdn_github_accelerator