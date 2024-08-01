#!/usr/bin/env python3

"""
Module for encrypting passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function that hashes the password
    using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Function that validates the password against
    the hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
