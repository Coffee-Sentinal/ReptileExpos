from datetime import timedelta
def monitoring_windows(start, end=None):
    end = end or start
    return {
        "pre_event_online": {"start": start - timedelta(weeks=8), "end": start - timedelta(weeks=2)},
        "inbound_route_risk": {"start": start - timedelta(days=14), "end": start},
        "event_weekend": {"start": start, "end": end},
        "outbound_route_risk": {"start": start, "end": start + timedelta(days=7)},
        "post_event_online": {"start": start + timedelta(days=1), "end": start + timedelta(days=30)},
    }
