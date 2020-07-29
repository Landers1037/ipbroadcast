# -*- coding: utf-8 -*-
# Time: 2020-04-02 11:38
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py.py

from .verify_token import httpauth,verify_token,verify_auth_token
from .easy_auth import check_password,generate_token

"""
verify_token 校验token返回bool
verify_auth_token 校验token返回用户
"""