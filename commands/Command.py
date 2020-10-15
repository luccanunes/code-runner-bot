class Command:
    def __init__(self, settings: dict):
        self.name = settings.get('name', None)
        self.aliases = settings.get('aliases', None)
        self.description = settings.get('description', None)
