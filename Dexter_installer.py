#! /usr/bin/python
# coding=utf-8 

import sys
import os
import pygtk
import gtk

sino = gtk.MessageDialog(type=gtk.MESSAGE_QUESTION,buttons=gtk.BUTTONS_YES_NO, message_format="¿Quiere agregar Dexter a fuentes ppa del centro de software de ubuntu?")
duda=sino.run()
if duda==gtk.RESPONSE_NO:
	sino.destroy()
	sys.end()
elif duda==gtk.RESPONSE_YES:
	os.system('gksudo add-apt-repository ppa:elementaryart/elementary-dev')
	os.system('sudo apt-get update')
	sino.destroy()
sino = gtk.MessageDialog(type=gtk.MESSAGE_QUESTION,buttons=gtk.BUTTONS_YES_NO, message_format="Muy bien. ¿Ahora quiere Instalar Dexter? Si pulsa Si por favor tenga en cuenta que tal vez deba pulsar 'S' o 'Y' en la consola para finalizar")
duda=sino.run()
if duda==gtk.RESPONSE_NO:
	sino.destroy()
	sys.end()
elif duda==gtk.RESPONSE_YES:
	os.system('sudo apt-get install dexter')
	sino.destroy()
sys.end()
