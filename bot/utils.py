from datetime import datetime, timezone

def getTimeDelta(futureTimeString, currentTime = datetime.now(timezone.utc)):
    futureTime = datetime.fromisoformat(futureTimeString.replace("Z", "+00:00"))
    difference = futureTime-currentTime
    return {'days':difference.days, 
            'hours':difference.seconds // 3600, 
            'minutes':(difference.seconds % 3600) // 60, 
            'seconds':difference.seconds}
    