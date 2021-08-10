class BasePath(object):
    def __init__(self, mask) -> None:
        pass


class EPWTPath(BasePath):
    def get_path(self):
        pass


class RBEPWTPath(BasePath):
    def __init__(self, *args, **kargs) -> None:
        super().__init__(self, args, kargs)

    def get_path(self):
        pass
