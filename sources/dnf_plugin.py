class Bar(dnf.Plugin):
    name = "foo"
    def __init__(self, base, cli):
        super(Bar, self).__init__(base, cli)
        self.base = base

    def transaction(self):
        print [p.name for p in self.base.transaction.install_set]

