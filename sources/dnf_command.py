import dnf
class FooCommand(dnf.cli.Command):
    aliases = ["foo"]
    def run(self, args):
        print "Called `dnf foo {}`".format(" ".join(args))

