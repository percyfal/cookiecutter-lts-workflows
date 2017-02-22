# -*- coding: utf-8 -*-
import os

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

WORKFLOW=os.path.join(os.path.normpath(os.path.dirname(__file__)), "workflow.sm")
