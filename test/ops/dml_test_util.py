"""
Helpers used by the tensorflow-directml-plugin python tests
"""
import re


def should_skip_test(pattern, args):
    """
    Returns whether the test should be skipped based on a regex that should match the
    adapter name
    """
    return any(re.match(pattern, arg) is not None for arg in args)
