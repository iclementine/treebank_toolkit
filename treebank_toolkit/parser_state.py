"""
Parser state of transition-based parsers.
Note
"""

from copy import copy

class State(object):
    def __init__(self, sent, stack=None, buf=None, seen_the_end=False, tags=None, arcs=None):
        self.sent = sent
        self.stack = copy(stack)
        self.buf = copy(buf)
        self.seen_the_end = seen_the_end # added for the Arc-Eager system with tree constraint
        self.tags = copy(tags)
        self.arcs = copy(arcs)
        
    @classmethod
    def init_from_sent(cls, sent):
        stack = [0]
        buf = list(reversed(range(1, len(sent) + 1))) # mind that len doesn't include <root>
        tags = {}
        arcs = {}
        seen_the_end = False
        return cls(sent, stack, buf, seen_the_end, tags, arcs)
   
    @classmethod
    def copy(cls, state):
        res = cls(state.sent, state.stack, state.buf, state.seen_the_end, state.tags, state.arcs)
        return res
    
    def is_final(self):
        return len(self.stack) ==1 and len(self.buf) == 0
    
    def __repr__(self):
        return "State({},\nstack={},\nbuf={},\nseen_the_end={},\ntags={},\narcs={})".format(
            repr(self.sent),
            repr(self.stack),
            repr(self.buf),
            repr(self.seen_the_end),
            repr(self.tags),
            repr(self.arcs))
    
    def __str__(self):
        return "State\nsent_form: {}\nstack: {}\nbuffer: {}\nseen_the_end: {}\ntags: {}\narcs: {}".format(
            str(self.sent.form),
            str([self.sent.form[idx] for idx in self.stack]),
            str([self.sent.form[idx] for idx in self.buf]),
            str(self.seen_the_end),
            str(self.tags),
            str(self.arcs))
