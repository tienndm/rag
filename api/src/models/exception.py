class RagError(Exception):
    pass

class RagNotFound(RagError):
    pass


class RagAlreadyExists(RagError):
    pass

class RagUnknownError(RagError):
    pass
