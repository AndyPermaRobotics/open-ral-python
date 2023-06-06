class Container:
    def __init__(self, uid: str):
        self.uid = uid

    def to_map(self):
        return {
            'UID': self.uid,
        }
