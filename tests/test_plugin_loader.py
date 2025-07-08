from plugins.loader import load_plugins, discover_plugins


def test_load_plugins():
    modules = load_plugins('plugins.agents')
    assert any(hasattr(m, 'EchoAgent') for m in modules)


def test_discover_plugins():
    names = discover_plugins('plugins.agents')
    assert 'plugins.agents.echo' in names
