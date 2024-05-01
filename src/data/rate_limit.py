import requests
from conn import url, headers

def check_rate_limit():
        # Check limitof API calls
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        daily_limits = response.headers.get('x-Ratelimit-request-limt')
        daily_remaining = response.headers.get('X-Ratelimit-requests-remaining')
        calls_per_min_allowed = response.headers.get('X-RateLimit-Limit')
        calls_per_min_remaining = response.headers.get('X-RateLimit-Remaining')
        
        rate_limit = {
                'daily_limits': daily_limits,
                'daily_remaining': daily_remaining,
                'minute_limit': calls_per_min_allowed,
                'minute_remaining': calls_per_min_remaining
                
        }
        
        return rate_limit

check = check_rate_limit()

print(check)