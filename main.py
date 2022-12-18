import time
import random
import os
import platform
import psutil
import ipaddress
from decimal import Decimal as D
from decimal import getcontext
import asyncio
import socket

# Allow for very small measurements.
getcontext().prec = 12
os.environ['TEST_ENV_VAR'] = 'something'

# Enums used to describe how many tests to run.
FAST_TESTS = 0
VERY_SMALL_TEST = 1000000
SOMEWHAT_SMALL_TEST = 100000
SMALL_TEST = 10000
MEDIUM_TEST = 1000
LARGE_TEST = 100
if FAST_TESTS:
    MEDIUM_TEST = VERY_SMALL_TEST = SOMEWHAT_SMALL_TEST = SMALL_TEST = 1000
    LARGE_TEST = MEDIUM_TEST

COMPLEXITY = {
    "O(1)": "excellent",
    "O(log n)": "good",
    "O(n)": "fair",
    "O(n log n)": "bad",
    "O(n ^ 2)": "horrible",
    "O(2 ^ n)": "awful",
    "O(n!)": "painful"
}

# Human-friendly way to relate small decimal numbers.
SIZES = [
    "shark attack", # 8 decimals AND smaller
    "plane crash", # 7 decimals
    "lightning strike", # 6 decimals
    "sky diving", # 5 decimals
    "canoe death", # 4 decimals
    "drowning", # 3 decimals
    "vehicle crash", # 2 decimals
    "heart disease" # 1 decimal
][::-1]

# https://colin-scott.github.io/personal_website/research/interactive_latency.html
BALLPARK = [
    "memory reference", # 100 ns memory ref
    "1KB compression", # 1k with zippy = 4000 ns really
    "LAN send",
    "memory slice", # read 1,000,000 b from memory 151 us
    "datacenter RTT",
    "SSD read", # sequential read 1 ms
    "gaming RTT", # 10 ms
    "website RTT" # 100 ms
][::-1]

ICONS = [
    "🦈",
    "✈",
    "⚡", # smaller
    "🪂",
    "🛶",
    "💧",
    "🚗",
    "❤️"
][::-1]

# Lets also use the alphabet as a way to relate the magnitude between numbers.
ALPHA = "abcdefghijklmnopqrstuvwxyz"

# Will be used for showing number of zeros.
SUPERSCRIPT = "⁰¹²³⁴⁵⁶⁷⁸⁹"

ROUNDED = [
    # milli
    ["00", "ms"],
    ["0", "ms"],
    ["", "ms"],

    # micro
    ["00", "µs"],
    ["0", "µs"],
    ["", "µs"],

    # nano
    ["00", "ns"],
    ["0", "ns"],
    ["", "ns"]
]

T = lambda: D(time.time())

"""
Pin this Python process to core zero.
This disables the OS switching the process between
cores and making the benchmarking results less reliable.
"""
p = psutil.Process(os.getpid())
p.cpu_affinity([0])
p.nice(-20)
if platform.system() != "Windows":
    os.system("taskset -p -c 0 %d" % os.getpid())

def count_right_zeros(n):
    as_str = "{0:f}".format(n)
    i = None
    left = 1
    for ch in as_str:
        # Has whole number portion.
        if left and ch not in ['0', '.']:
            break

        # Left portion passing done.
        if ch == '.':
            i = 0
            left = 0
            continue

        # Process dec section.
        if not left:
            # Count zeros otherwise quit.
            if ch == '0':
                i += 1
            else:
                break

    return i

def get_sig_digit(n):
    as_str = "{0:f}".format(n)
    parts = as_str.split(".")
    if len(parts) == 2:
        dec_part = parts[-1]
        for ch in dec_part:
            if ch != "0":
                return ch
    else:
        return "0"

def format_dec(n):
    as_str = "{0:f}".format(n)
    i = count_right_zeros(n)
    if i is not None:
        # Format result with relatable size.
        sizes_last = len(SIZES) - 1
        i = i if i <= sizes_last else sizes_last
        # {: >45}
        #   0.00000134767293932 [1⁵] lightning strike f
        # "%s [%s%s] %s %s"
        out = "{: <21} [{: <1}{: <1}] {: <16} {: <1}".format(as_str, get_sig_digit(n), SUPERSCRIPT[i], SIZES[i], ALPHA[i])
    else:
        out = as_str

    return out

def format_speed(n):
    as_str = "{0:f}".format(n)
    i = count_right_zeros(n)
    if i >= 6:
        speed = "fast"
    elif i >= 3:
        speed = "brisk"
    else:
        speed = "slow"

    return speed

def format_rounded(n):
    as_str = "{0:f}".format(n)
    i = count_right_zeros(n)
    padding, units = ROUNDED[i]
    dec_p = as_str.split(".")[-1]
    if len(padding):
        padding = dec_p[i + 1:i + 1 + len(padding)]
    return [padding, units]

def visual_dec(n):
    sizes_last = len(SIZES) - 1
    i = count_right_zeros(n)
    if i == None:
        i = sizes_last

    i = i if i <= sizes_last else sizes_last
    return "■" * (((sizes_last - i) + 1))

def icon_dec(n):
    sizes_last = len(SIZES) - 1
    i = count_right_zeros(n)
    if i == None:
        i = sizes_last
    return ICONS[i]

def format_complexity(c):
    out = "{} = {}".format(c, COMPLEXITY[c])
    return out

def format_ballpark(n):
    sizes_last = len(SIZES) - 1
    i = count_right_zeros(n)
    if i == None:
        i = sizes_last
    return BALLPARK[i]

def size_chart():
    out = ""
    for i in range(0, len(SIZES)):
        if i:
            out += "      "

        out += "{} {} {} ({})".format(
            ICONS[i],
            ALPHA[i],
            SIZES[i],
            i + 1
        )
    return out

def units_chart():
    info = [
        " 1s 1000x > 1ms 1000x > 1µs 1000x > 1ns",
        "1s = 1000ms",
        "1ms = 1000µs",
        "1µs = 1000ns",
        "1s = 1,000,000,000ns",
    ]
    out = ""
    i = 0
    for s in [info[0]]:
        if i:
            out += "      "

        out += s
        i += 1

    return out

A_LIST = []
def list_append():
    start = T()
    A_LIST.append(1000)
    return T() - start

def overhead(p):
    pass
def func_overhead():
    buf = "1" * 1024
    start = T()
    overhead(buf)
    return T() - start

def single_dic_build():
    x = random.random()
    start = T()
    a_dic = {
        "this is a key": x
    }
    return T() - start

def single_dic_lookup():
    x = random.random()
    a_dic = {
        "this is a key": x
    }
    start = T()
    y = a_dic["this is a key"]
    return T() - start

def four_dic_build():
    a = random.random()
    b = random.random()
    c = random.random()
    d = random.random()
    start = T()
    a_dic = {
        "this is a key": a,
        "another key": b,
        "some thing": c,
        "wser23w4r234r234234": d
    }
    return T() - start

def single_dic_lookup():
    a = random.random()
    b = random.random()
    c = random.random()
    d = random.random()
    a_dic = {
        "this is a key": a,
        "another key": b,
        "some thing": c,
        "wser23w4r234r234234": d
    }
    start = T()
    n = a_dic["wser23w4r234r234234"]
    return T() - start

def async_queue_build():
    start = T()
    x = asyncio.Queue()
    return T() - start

def async_queue_append():
    x = asyncio.Queue()
    start = T()
    x.put_nowait(1000)
    return T() - start

def async_queue_get():
    x = asyncio.Queue()
    x.put_nowait(1000)
    start = T()
    a = x.get_nowait()
    return T() - start

def build_stream_sock():
    start = T()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end = T() - start
    s.close()
    return end

def build_dgram_sock():
    start = T()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end = T() - start
    s.close()
    return end

def bind_dgram_sock():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start = T()
    s.bind(("", 0))
    end = T() - start
    s.close()
    return end

def time_time():
    start = T()
    x = T()
    return T() - start

def send_udp_packets(n):
    def closure():
        buf = b"1" * n
        dest = ("192.0.2.1", 31337) # 'TEST-NET-1' IP = unroutable
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setblocking(0)

        """
        Make the socket 'non-blocking.'
        Try to simulate some of the more common behaviour with async code.
        """
        start = T()
        s.sendto(buf, dest)
        end = T() - start
        s.close()
        return end

    return closure

def kstr_to_bytes():
    kstr = "1" * 1024
    start = T()
    x = kstr.encode("ascii")
    return T() - start

def kbytes_to_str():
    kb = b"1" * 1024
    start = T()
    x = kb.decode("utf-8")
    return T() - start

def build_async_event():
    start = T()
    e = asyncio.Event()
    return T() - start

def set_async_event():
    e = asyncio.Event()
    start = T()
    e.set()
    return T() - start

def if_equ_n():
    start = T()
    if 100 == 1000:
        pass
    else:
        pass
    return T() - start

def n_in_list(list_size):
    my_list = []
    x = random.random()
    for i in range(0, list_size):
        my_list.append(x)

    def closure():
        start = T()
        if 1000 in my_list:
            pass
        return T() - start

    return closure

def s_in_list(list_size):
    my_list = []
    x = "test"
    for i in range(0, list_size):
        my_list.append(x)

    def closure():
        start = T()
        if "x" in my_list:
            pass
        return T() - start

    return closure

def ip_str_to_ipaddr():
    start = T()
    x = ipaddress.ip_address("8.8.8.8")
    return T() - start

def store_ip_tup_dic():
    d = {}
    start = T()
    d[("8.8.8.8", 80)] = 1
    return T() - start

def res_google():
    start = T()
    socket.getaddrinfo("www.google.com", 80, family=socket.AF_INET, type=socket.SOCK_STREAM)
    return T() - start

def google_tcp_con():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start = T()
    s.connect(("www.google.com", 80))
    end = T() - start
    s.close()
    return end

def tcp_echo_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("tcpbin.com", 4242))
    start = T()
    s.send(b"hello, world\r\n")
    buf = s.recv(1024)
    end = T() - start
    s.close()
    return end

def env_lookup():
    start = T()
    x = os.getenv('test_env_var')
    return T() - start

TESTS = [
    [
        "get environmental variable",
        env_lookup,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "time()",
        time_time,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "list append small int",
        list_append,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "overhead of a func call",
        func_overhead,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "make a dic with one item",
        single_dic_build,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "dict key lookup from single item dic",
        single_dic_lookup,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "make a dic with 4 items",
        four_dic_build,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "dict key lookup from 4 item dic",
        single_dic_lookup,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "create an async queue",
        async_queue_build,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "add to an async queue",
        async_queue_append,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "get from an async queue",
        async_queue_get,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "build async event",
        build_async_event,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "set async event",
        set_async_event,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "if x == n else ..",
        if_equ_n,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "n in list[5]",
        n_in_list(5),
        VERY_SMALL_TEST,
        "O(n)"
    ],
    [
        "n in list[10]",
        n_in_list(10),
        VERY_SMALL_TEST,
        "O(n)"
    ],
    [
        "n in list[100]",
        n_in_list(100),
        VERY_SMALL_TEST,
        "O(n)"
    ],
    [
        "n in list[1000]",
        n_in_list(1000),
        SMALL_TEST,
        "O(n)"
    ],
    [
        "str in list[5]",
        s_in_list(5),
        VERY_SMALL_TEST,
        "O(n)"
    ],
    [
        "str in list[10]",
        s_in_list(10),
        VERY_SMALL_TEST,
        "O(n)"
    ],
    [
        "str in list[100]",
        s_in_list(100),
        VERY_SMALL_TEST,
        "O(n)"
    ],
    [
        "ip bytes to ipaddress",
        ip_str_to_ipaddr,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "store ip tuple in dic",
        store_ip_tup_dic,
        VERY_SMALL_TEST,
        "O(1)"
    ],
    [
        "1k str to bytes",
        kstr_to_bytes,
        VERY_SMALL_TEST,
        "O(n)"
    ],
    [
        "1k bytes to str",
        kbytes_to_str,
        VERY_SMALL_TEST,
        "O(n)"
    ],
    [
        "build stream sock",
        build_stream_sock,
        MEDIUM_TEST,
        "O(1)"
    ],
    [
        "build dgram sock",
        build_dgram_sock,
        MEDIUM_TEST,
        "O(1)"
    ],
    [
        "bind dgram sock",
        bind_dgram_sock,
        MEDIUM_TEST,
        "O(1)"
    ],
    [
        "send 100 b udp packets",
        send_udp_packets(100),
        MEDIUM_TEST,
        "O(1)"
    ],
    [
        "send 1k udp packets",
        send_udp_packets(1024),
        MEDIUM_TEST,
        "O(1)"
    ],
    [
        "send 10k udp packets",
        send_udp_packets(10240),
        MEDIUM_TEST,
        "O(1)"
    ],
    [
        "dns lookup google.com (cached prob)",
        res_google,
        10,
        "O(1)"
    ],
    [
        "tcp con to google",
        google_tcp_con,
        10,
        "O(1)"
    ],
    [
        "tcp echo client",
        tcp_echo_client,
        5,
        "O(1)"
    ],
]

# Sort by zero no
def zsort(sub_li):
    return(sorted(sub_li, key=lambda x: x[1], reverse=True))  

print("Running tests -- they are ordered so please wait a while . . .")
print()

# Profile all tests N times.
# List average run time.
results = []
for test in TESTS:
    total = 0
    test_name, test_func, test_no, test_complex = test

    # Measure single test run-time.
    for i in range(0, test_no):
        total += test_func()

    # Format result.
    avg = total / D(test_no)
    z = count_right_zeros(avg)
    z = (len(SIZES)) - min(z, len(SIZES))
    out = "{: >9} [{: <1}{: <1} {: <1}{: <2} {: <1}] {: <2}: {: <42} {: >5} {: <1} {: <1} ({: <1}: like {: <16}) {: >45}:  {: >15}".format(
        visual_dec(avg),
        SUPERSCRIPT[count_right_zeros(avg)],
        ALPHA[count_right_zeros(avg)],
        get_sig_digit(avg),
        format_rounded(avg)[0],
        icon_dec(avg),
        format_rounded(avg)[1],
        test_name,
        format_speed(avg),
        icon_dec(avg),
        ALPHA[count_right_zeros(avg)],
        z,
        format_ballpark(avg),
        format_dec(avg),
        format_complexity(test_complex)
    )

    # Store result.
    results.append([out, avg])

# Sizes chart.
print("Based on average death probability except for lighting strike.")
print("These sizes reflect the number of decimal places.")
print()
print(size_chart())
print(units_chart())
print()


# Show output.
results = zsort(results)
for result in results:
    out, _ = result
    print(out)


"""
open file time
"""