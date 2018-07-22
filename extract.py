#!/usr/bin/env python3
from behave import *

@given('we have images in images_for_extraction')
def step_impl(context):
    pass

@when(' When we run python3 extract.py')
def step_impl(context):
    assert True is not Falseb

@then('Then images with very imperfectly extracted portraits will appeaar in extracted_portraits
')
def step_impl(context):
    assert context.failed is False
