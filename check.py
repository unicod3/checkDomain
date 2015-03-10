#!/usr/bin/env python
"""
    A simple domain checker written with python with pygtk
    Check Domain Information
    author = 'unicod3'
"""
# example check.py
__author__ = 'unicod3'
import pygtk
pygtk.require('2.0')
import gtk
import pythonwhois

class checkDomain:
    def enter_callback(self, widget, entry, lblResult):
        try:
            entry_text = entry.get_text()
            lblResult.set_text("Checking...")
            w = pythonwhois.get_whois(entry_text)
            result = "Domain : %s \n" % entry_text
            if w["contacts"]["registrant"] is None:
                result += "\nDomain Is Available"
            else:
                result += "Registrant : %s \n" % w["contacts"]["registrant"]["name"]
                result += "Created at : %s \n" % w["creation_date"][0].strftime("%d/%m/%Y")
                result += "Expired at : %s \n" % w["expiration_date"][0].strftime("%d/%m/%Y")
        except pythonwhois.shared.WhoisException:
            lblResult.set_text("Please check the domain!")
        else:
            lblResult.set_text(result)

    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(300, 150)
        window.set_title("Check Domain")
        window.connect("delete_event", lambda w,e: gtk.main_quit())
        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        lblResult = gtk.Label()
        entry = gtk.Entry()
        entry.set_max_length(50)
        entry.connect("activate", self.enter_callback, entry, lblResult)
        entry.select_region(0, len(entry.get_text()))

        label = gtk.Label("_Domain")
        label.set_use_underline(True)
        label.set_mnemonic_widget(entry)
        vbox.pack_start(label, True, True, 0)
        label.show()
        vbox.pack_start(entry, True, True, 0)
        entry.show()

        vbox.pack_start(lblResult,True,True,0)
        lblResult.show()

        button = gtk.Button(label="Check", stock=None)
        button.connect("clicked", self.enter_callback, entry, lblResult)
        vbox.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    checkDomain()
    main()