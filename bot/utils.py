from datetime import datetime, timezone


def getTimeDelta(futureTimeString: str, currentTime = datetime.now(timezone.utc)):
    futureTime = datetime.fromisoformat(futureTimeString.replace("Z", "+00:00"))
    difference = futureTime-currentTime
    return {'days':difference.days, 
            'hours':difference.seconds // 3600, 
            'minutes':(difference.seconds % 3600) // 60, 
            'seconds':difference.seconds}

def collectionToLower(collection: list | tuple | set) -> list[str] | None:
    if collection:
        return [str(elm).casefold() for elm in collection]
    return None
    