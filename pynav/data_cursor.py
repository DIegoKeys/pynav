class DataCursor:
    def __init__(self, data, headers=None):
        self.data = data
        self.position = -1
        self.headers = headers if headers is not None else self._get_headers()

    def _get_headers(self):
        if len(self.data) > 0:
            if isinstance(self.data[0], dict):
                return list(self.data[0].keys())
            elif hasattr(self.data[0], 'cursor_description'):
                return [desc[0] for desc in self.data[0].cursor_description]
            elif isinstance(self.data[0], tuple) and hasattr(self.data[0], '_fields'):
                return self.data[0]._fields
            else:
                return [f"Field_{i}" for i in range(len(self.data[0]))]
        return []

    def move_next(self):
        if self.position < len(self.data) - 1:
            self.position += 1
            return True
        return False

    def move_previous(self):
        if self.position > 0:
            self.position -= 1
            return True
        return False

    def move_first(self):
        if len(self.data) > 0:
            self.position = 0
            return True
        return False

    def move_last(self):
        if len(self.data) > 0:
            self.position = len(self.data) - 1
            return True
        return False

    def get_current(self):
        if 0 <= self.position < len(self.data):
            return self.data[self.position]
        return None

    def has_next(self):
        return self.position < len(self.data) - 1

    def has_previous(self):
        return self.position > 0

    def get_headers(self):
        return self.headers
