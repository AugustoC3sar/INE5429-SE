class Data:
    def __init__(self, keyword: str, content: bytes):
        self._keyword = keyword
        self._content = content
    
    def keyword(self) -> str:
        return self._keyword
    
    def content(self) -> bytes:
        return self._content
