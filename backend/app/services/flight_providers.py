from abc import ABC, abstractmethod
class FlightScheduleProvider(ABC):
    @abstractmethod
    def routes_for_event(self, event, direction:str): ...
class MockFlightScheduleProvider(FlightScheduleProvider):
    def routes_for_event(self, event, direction:str):
        return [r for r in event.routes if r.direction == direction]
class OAGProvider(FlightScheduleProvider):
    """TODO: implement with OAG_API_KEY; return normalized route-risk intersections only."""
    def routes_for_event(self, event, direction:str): raise NotImplementedError("OAG integration pending")
class CiriumProvider(FlightScheduleProvider):
    """TODO: implement with CIRIUM_APP_ID/CIRIUM_APP_KEY."""
    def routes_for_event(self, event, direction:str): raise NotImplementedError("Cirium integration pending")
class FlightAwareProvider(FlightScheduleProvider):
    """TODO: implement with FLIGHTAWARE_API_KEY."""
    def routes_for_event(self, event, direction:str): raise NotImplementedError("FlightAware integration pending")
