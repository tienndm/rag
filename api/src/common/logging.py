import logging
from logging.handlers import TimedRotatingFileHandler
import os
from typing import Optional, Union, Literal
import sys


class SingletonLogger:
    """
    Singleton logger class that provides a centralized logging system.
    
    This logger supports both file and console logging with automatic log rotation.
    """
    _instance = None

    @staticmethod
    def getLogger(
        logDir: str = "./data/api/logs",
        logFile: str = "api.log",
        when: Literal["S", "M", "H", "D", "midnight"] = "midnight",
        backupCount: int = 7,
        logLevel: Union[int, str] = logging.INFO,
        format_string: str = "%(asctime)s - %(levelname)s - %(message)s",
    ) -> logging.Logger:
        """
        Get or create a logger instance.
        
        Args:
            logDir: Directory where log files are stored
            logFile: Name of the log file
            when: Log rotation interval (S=second, M=minute, H=hour, D=day, midnight)
            backupCount: Number of backup logs to keep
            logLevel: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            format_string: Format of log messages
            
        Returns:
            Logger instance
        """
        if SingletonLogger._instance is None:
            SingletonLogger._instance = SingletonLogger._initializeLogger(
                logDir, logFile, when, backupCount, logLevel, format_string
            )
        return SingletonLogger._instance

    @staticmethod
    def _initializeLogger(
        logDir: str, 
        logFile: str, 
        when: str, 
        backupCount: int, 
        logLevel: Union[int, str] = logging.INFO,
        format_string: str = "%(asctime)s - %(levelname)s - %(message)s"
    ) -> logging.Logger:
        """
        Initialize a new logger instance.
        
        This method configures both file and console handlers.
        """
        os.makedirs(logDir, exist_ok=True)

        logger = logging.getLogger(logFile)
        
        if isinstance(logLevel, str):
            logLevel = getattr(logging, logLevel.upper(), logging.INFO)
            
        logger.setLevel(logLevel)
        
        if logger.handlers:
            logger.handlers.clear()

        logPath = os.path.join(logDir, logFile)
        fileHandler = TimedRotatingFileHandler(
            logPath, when=when, interval=1, backupCount=backupCount
        )
        fileHandler.setLevel(logLevel)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setLevel(logLevel)

        formatter = logging.Formatter(format_string)
        fileHandler.setFormatter(formatter)
        consoleHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.addHandler(consoleHandler)

        return logger
    
    @staticmethod
    def setLogLevel(level: Union[int, str]) -> None:
        """
        Dynamically change the log level of the existing logger.
        
        Args:
            level: New log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        if SingletonLogger._instance is not None:
            if isinstance(level, str):
                level = getattr(logging, level.upper(), logging.INFO)
                
            SingletonLogger._instance.setLevel(level)
            for handler in SingletonLogger._instance.handlers:
                handler.setLevel(level)
