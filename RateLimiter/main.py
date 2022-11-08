from abc import ABC, abstractmethod
import threading
import time
lock = threading.Lock()

class Limiter(ABC):
    @abstractmethod
    def rate_limit(self):
        pass

class TokenBucket(Limiter):
    def __init__(self, bucket_size, req_per_minute) -> None:
        self.bucket = [False for _ in range(bucket_size)]
        self.bucket_size = bucket_size
        self.req_per_minute = req_per_minute
        self.req_counter = 0
        self.first_request_time = time.time()
        self.refill()
    
    def check_limit(self):
        now = time.time()
        if int(now - self.first_request_time) >= self.bucket_size:
            self.refill()
            print("Refilling bucket")
        

    def refill(self):
        self.bucket = [False for _ in range(self.bucket_size)]
        self.req_counter = 0

    def rate_limit(self):
        self.check_limit()
        if self.bucket[-1]:
            print("Rate Limit occur")
            return
        self.bucket[self.req_counter] = True
        self.req_counter += 1
        print(f"Req serverd: {self.req_counter}")

class RateLimiter:
    def __init__(self) -> None:
        self.user_store = {}

    def init(self, ip):
        if ip in self.user_store:
            return self.user_store[ip]
        self.user_store[ip] = TokenBucket(10, 10)
        return self.user_store[ip]

    def limit(self, ip):
        limiter = self.init(ip)
        limiter.rate_limit()


rl = RateLimiter()
while True:
    rl.limit('10.0.0.1')
    time.sleep(0.2)