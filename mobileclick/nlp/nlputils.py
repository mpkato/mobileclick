# -*- coding: utf-8 -*-

def normalize(tokens, key=lambda x: x):
    '''
    Convert tokens to lowercase
    '''
    return [key(token).lower() for token in tokens]
