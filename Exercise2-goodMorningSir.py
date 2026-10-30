
import time
from greeting import get_greeting


if __name__ == "__main__":
    current_hour = time.localtime().tm_hour
    print(get_greeting(current_hour))
