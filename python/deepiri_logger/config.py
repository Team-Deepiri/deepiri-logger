from __future__ import annotations

import logging
import sys
from typing import Optional

import structlog
from structlog import contextvars as structlog_contextvars

from .processors import deepiri_schema_processor


def init(
    service_name: str,
    version: str = "unknown",
    log_level: str = "INFO",
    log_file: Optional[str] = None,
) -> None:
    """Initialize Deepiri logger for Python services."""
    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format="%(message)s",
        handlers=handlers,
    )

    structlog_contextvars.clear_contextvars()
    structlog_contextvars.bind_contextvars(service_name=service_name, version=version)

    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_log_level,
            structlog_contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="iso"),
            deepiri_schema_processor,
            structlog.processors.JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )



def get_logger(name: str | None = None) -> structlog.BoundLogger:
    """Return a structlog logger instance, optionally bound to a name."""
    return structlog.get_logger(name) if name else structlog.get_logger()
