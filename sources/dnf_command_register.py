class Foo(dnf.Plugin):
    name = "foo"
    def __init__(self, base, cli):
        super(Foo, self).__init__(base, cli)
        cli.register_command(FooCommand)
