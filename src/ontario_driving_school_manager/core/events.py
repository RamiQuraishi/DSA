"""
Event handling system for the Ontario Driving School Manager.
"""

from typing import Any, Callable, Dict, List, Type
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    """Base class for all events."""
    timestamp: datetime = datetime.now()
    event_type: str = ""

class EventHandler:
    """Handler for processing events."""
    def __init__(self):
        self.handlers: Dict[str, List[Callable]] = {}

    def register(self, event_type: str, handler: Callable) -> None:
        """Register a handler for an event type."""
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)

    def unregister(self, event_type: str, handler: Callable) -> None:
        """Unregister a handler for an event type."""
        if event_type in self.handlers:
            self.handlers[event_type].remove(handler)

    def handle(self, event: Event) -> None:
        """Handle an event by calling all registered handlers."""
        if event.event_type in self.handlers:
            for handler in self.handlers[event.event_type]:
                handler(event)

class EventBus:
    """Central event bus for the application."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.handler = EventHandler()
        return cls._instance

    def publish(self, event: Event) -> None:
        """Publish an event to all registered handlers."""
        self.handler.handle(event)

    def subscribe(self, event_type: str, handler: Callable) -> None:
        """Subscribe a handler to an event type."""
        self.handler.register(event_type, handler)

    def unsubscribe(self, event_type: str, handler: Callable) -> None:
        """Unsubscribe a handler from an event type."""
        self.handler.unregister(event_type, handler) 