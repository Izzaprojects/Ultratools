# UltraTools Full Version

import os
import time
import random
import urllib.parse
import platform
import functools
import math
import sys

# ==========================
# Basic Tools
# ==========================

def quick_print(*args, sep=" ", end="\n"):
    print(sep.join(map(str, args)), end=end)

def repeat_string(s, times):
    return s * times

# ==========================
# Timer Tools
# ==========================

_timer_start = 0

def timer_start():
    global _timer_start
    _timer_start = time.time()

def timer_stop():
    return round(time.time() - _timer_start, 4)

def wait(seconds):
    time.sleep(seconds)

# ==========================
# List Tools
# ==========================

def gen_list(length, value=None):
    return [value] * length

def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def unique_list(lst):
    return list(dict.fromkeys(lst))

def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

# ==========================
# String Tools
# ==========================

def capitalize_all(text):
    return " ".join(word.capitalize() for word in text.split())

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    clean = ''.join(filter(str.isalnum, text.lower()))
    return clean == clean[::-1]

def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")

# ==========================
# File Tools
# ==========================

def save_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def read_file(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def file_exists(filename):
    return os.path.isfile(filename)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return True
    return False

# ==========================
# Math Tools
# ==========================

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return math.factorial(n)

def fibonacci(n):
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

# ==========================
# System Tools
# ==========================

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_os_info():
    return platform.system(), platform.release()

def get_python_version():
    return sys.version

# ==========================
# Decorators
# ==========================

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {result}")
        return result
    return wrapper

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[TIMEIT] {func.__name__} executed in {duration:.4f} seconds")
        return result
    return wrapper

# ==========================
# Randomizer Tools
# ==========================

def random_choice(seq):
    return random.choice(seq) if seq else None

def random_int(a, b):
    return random.randint(a, b)

def random_float(a=0.0, b=1.0):
    return random.uniform(a, b)

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# ==========================
# Web Tools
# ==========================

def url_encode(text):
    return urllib.parse.quote(text)

def url_decode(text):
    return urllib.parse.unquote(text)

def create_query(params):
    return urllib.parse.urlencode(params)

def parse_query(query):
    return dict(urllib.parse.parse_qsl(query))
    