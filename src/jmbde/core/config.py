from pathlib import Path


class Config:
    """Application configuration."""

    # Default paths
    BASE_DIR = Path(__file__).parent.parent.parent.parent
    DATA_DIR = BASE_DIR / "data"
    DATABASE_PATH = DATA_DIR / "jmbde.db"

    @classmethod
    def initialize(cls):
        """Initialize configuration."""
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
