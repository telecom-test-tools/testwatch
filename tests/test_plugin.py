import pytest


def test_plugin_import():
    from testwatch.testwatch_plugin import TestWatchPlugin

    plugin = TestWatchPlugin()
    assert plugin.name == "testwatch"
