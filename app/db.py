from deta import Deta

from .core.config import settings

deta = Deta(settings.DETA_PROJECT_KEY)
