from provider_types.provider import Provider


class IConfig:
    def __init__(self):
        self.provider = Provider()
        print(self.provider)
        print('IConfig')
