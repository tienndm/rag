from urllib.parse import urlparse

from settings import DATABASE_URI

IS_RELATIONAL_DB = False
IS_DOCUMENT_DB = False
IS_KEY_VALUE_DB = False

DATABASE_TYPE, _, _ = urlparse(DATABASE_URI).scheme.partition("+")
if DATABASE_TYPE == "postgresql":
    from .postgre import AsyncPostgreSQLEngine as AsyncRelationalDBEngine
    from .postgre import AsyncPostgreSQLScopedSession as AsyncScopedSession
    from .postgre import getAsyncPostgreSqlSession as getAsyncSession
    from .postgre import initializePostgreDB as initializeDB

    IS_RELATIONAL_DB = True

else:
    raise RuntimeError(
        f"Invalid databasetype \'{DATABASE_TYPE}\' provided in DATABASE_URI: {DATABASE_URI}"
    )