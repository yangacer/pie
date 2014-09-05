import re

class builder(object):

    def __init__(self, debug=False):
        nbPattern = r'<!-- \[(?P<name>[\w-]*)\] -->\s*' \
            r'(?P<content>.*?)(?=\<!-- -->)\<!-- -->'
        refPattern = r'\[#@\]\(([\w-]*)\)'
        self.debug = debug
        self.named_blocks_ = None
        self.nbMatcher = re.compile(nbPattern, re.DOTALL)
        self.refMatcher = re.compile(refPattern)
        pass

    def compile(self, content):
        """
        Find inline named blocks in given content and save found
        blocks.

        Raise RuntimeError if found multiple definitions of a named
        block.
        """
        results = self.nbMatcher.findall(content)
        # Check multiple definitions
        results.sort()
        for i in xrange(1, len(results)):
            if results[i-1][0] == results[i][0]:
                raise RuntimeError('error: %s is specified multiple times.' %
                                   results[i][0])
            pass
        self.named_blocks_ = dict(results)


    def _replace_aux(self, matchObj):
        """
        Auxiliary replacement callback which returns replacement
        string.

        Raise RuntimeError if referenced block was not defined.
        """
        name = matchObj.group(1)
        if name in self.named_blocks_:
            return self.named_blocks_[name]
        raise RuntimeError('error: Undefined reference; %s ' %
                           matchObj.group(0))

    def replace(self, content):
        """
        Substitute reference with named blocks.
        """
        return self.refMatcher.sub(self._replace_aux, content)

