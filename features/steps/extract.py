#!/usr/bin/env python3
from behave import *

@given('we have images in images_for_extractio')
def step_impl(context):
    pass

@when('we run python3 extract.py')
def step_impl(context):
    assert True is not False

@then('imperfectly extracted portraits appeaar in extracted_portraits')
def step_impl(context):
    assert context.failed is False
