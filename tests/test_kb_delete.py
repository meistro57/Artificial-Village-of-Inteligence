from knowledge_base.local_kb import KnowledgeBase


def test_delete_fact():
    kb = KnowledgeBase()
    kb.add_fact('a', '1')
    assert kb.query('a') == '1'
    kb.delete_fact('a')
    assert kb.query('a') == ''
