from nose.tools import *
from ex48 import parser


def test_sentence():
    sentence = parser.parse_sentence([('verb', 'run'),
                                     ('direction', 'north')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'run')
    assert_equal(sentence.object, 'north')

    sentence = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'),
                                     ('stop', 'the'), ('noun', 'honey')])
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'honey')
    assert_raises(parser.ParserError, parser.parse_sentence, [('noun', 'bear'), ('noun', 'honey'), ('noun', 'princess')])


# def test_verb():
#     assert_raises(parser.ParserError, parser.parse_verb, [('noun', 'bear'),
#                                                    ('noun', 'honey'),
#                                                    ('noun', 'princess')])
