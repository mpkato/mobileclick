# -*- coding: utf-8 -*-

def safe_filename(name):
    return remove_breaks(name).replace(' ', '_').lower()

def remove_breaks(name):
    return name.replace('\r', '').replace('\n', '')
