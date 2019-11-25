import everest

class TestCoordinator(everest.built.Built):

    def __init__(
            self,
            system
            ):
        inputs = locals().copy()
        self.observers = []
        super().__init__(
            inputs,
            __file__
            )

    def add_observer(observer):
        self.observers.append(observer)
        if self.anchored:
            observer.anchor(self.frameID, self.path)
