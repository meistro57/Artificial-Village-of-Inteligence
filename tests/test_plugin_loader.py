from plugins.loader import load_plugins


def test_load_plugins():
    modules = load_plugins('plugins.agents')
    assert any(hasattr(m, 'EchoAgent') for m in modules)
