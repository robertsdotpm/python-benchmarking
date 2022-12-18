# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
Based on average death probability except for lighting strike.
These sizes reflect the number of decimal places.

❤️ a heart disease (1)      🚗 b vehicle crash (2)      💧 c drowning (3)      🛶 d canoe death (4)      🪂 e sky diving (5)      ⚡ f lightning strike (6)      ✈ g plane crash (7)      🦈 h shark attack (8)
 1s 1000x > 1ms 1000x > 1µs 1000x > 1ns

 ■■■■■■■■ [⁰a 192 ❤️] ms: tcp echo client                             slow ❤️ a (8: like website RTT     ) 0.192783308029        [1⁰] heart disease    a:  O(1) = excellent
 ■■■■■■■■ [⁰a 112 ❤️] ms: dns lookup google.com (cached prob)         slow ❤️ a (8: like website RTT     ) 0.112471532821        [1⁰] heart disease    a:  O(1) = excellent
  ■■■■■■■ [¹b 64  🚗] ms: tcp con to google                           slow 🚗 b (7: like gaming RTT      ) 0.0640018939972       [6¹] vehicle crash    b:  O(1) = excellent
     ■■■■ [⁴e 38  🪂] µs: send 10k udp packets                       brisk 🪂 e (4: like memory slice    ) 0.0000381512641909    [3⁴] sky diving       e:  O(1) = excellent
     ■■■■ [⁴e 24  🪂] µs: send 100 b udp packets                     brisk 🪂 e (4: like memory slice    ) 0.0000249960422518    [2⁴] sky diving       e:  O(1) = excellent
     ■■■■ [⁴e 19  🪂] µs: send 1k udp packets                        brisk 🪂 e (4: like memory slice    ) 0.0000190134048462    [1⁴] sky diving       e:  O(1) = excellent
     ■■■■ [⁴e 13  🪂] µs: n in list[1000]                            brisk 🪂 e (4: like memory slice    ) 0.0000137040615082    [1⁴] sky diving       e:      O(n) = fair
      ■■■ [⁵f 8   ⚡] µs: build stream sock                          brisk ⚡ f (3: like LAN send        ) 0.0000080006122589    [8⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 6   ⚡] µs: bind dgram sock                            brisk ⚡ f (3: like LAN send        ) 0.00000699925422667   [6⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 5   ⚡] µs: build dgram sock                           brisk ⚡ f (3: like LAN send        ) 0.00000599980354308   [5⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 2   ⚡] µs: ip bytes to ipaddress                      brisk ⚡ f (3: like LAN send        ) 0.00000241759252532   [2⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 1   ⚡] µs: n in list[100]                             brisk ⚡ f (3: like LAN send        ) 0.00000198112964627   [1⁵] lightning strike f:      O(n) = fair
      ■■■ [⁵f 1   ⚡] µs: create an async queue                      brisk ⚡ f (3: like LAN send        ) 0.00000150759077064   [1⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 1   ⚡] µs: time()                                     brisk ⚡ f (3: like LAN send        ) 0.000001198502779     [1⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 1   ⚡] µs: str in list[100]                           brisk ⚡ f (3: like LAN send        ) 0.00000108184647561   [1⁵] lightning strike f:      O(n) = fair
       ■■ [⁶g 970 ✈] ns: make a dic with 4 items                     fast ✈ g (2: like 1KB compression ) 0.000000970860242832  [9⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 965 ✈] ns: add to an async queue                       fast ✈ g (2: like 1KB compression ) 0.000000965698719029  [9⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 930 ✈] ns: build async event                           fast ✈ g (2: like 1KB compression ) 0.000000930807113633  [9⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 928 ✈] ns: get environmental variable                  fast ✈ g (2: like 1KB compression ) 0.000000928055763237  [9⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 923 ✈] ns: dict key lookup from single item dic        fast ✈ g (2: like 1KB compression ) 0.00000092379164694   [9⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 875 ✈] ns: get from an async queue                     fast ✈ g (2: like 1KB compression ) 0.000000875832319241  [8⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 820 ✈] ns: 1k bytes to str                             fast ✈ g (2: like 1KB compression ) 0.000000820837020867  [8⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 795 ✈] ns: n in list[10]                               fast ✈ g (2: like 1KB compression ) 0.000000795756816851  [7⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 759 ✈] ns: 1k str to bytes                             fast ✈ g (2: like 1KB compression ) 0.000000759049415577  [7⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 754 ✈] ns: n in list[5]                                fast ✈ g (2: like 1KB compression ) 0.000000754710197454  [7⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 742 ✈] ns: dict key lookup from 4 item dic             fast ✈ g (2: like 1KB compression ) 0.000000742240667334  [7⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 741 ✈] ns: set async event                             fast ✈ g (2: like 1KB compression ) 0.000000741263389591  [7⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 728 ✈] ns: str in list[10]                             fast ✈ g (2: like 1KB compression ) 0.000000728814840318  [7⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 717 ✈] ns: make a dic with one item                    fast ✈ g (2: like 1KB compression ) 0.000000717132329931  [7⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 684 ✈] ns: store ip tuple in dic                       fast ✈ g (2: like 1KB compression ) 0.000000684214353567  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 680 ✈] ns: overhead of a func call                     fast ✈ g (2: like 1KB compression ) 0.000000680716991418  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 678 ✈] ns: str in list[5]                              fast ✈ g (2: like 1KB compression ) 0.000000678245306009  [6⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 667 ✈] ns: list append small int                       fast ✈ g (2: like 1KB compression ) 0.000000667293071744  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 651 ✈] ns: if x == n else ..                           fast ✈ g (2: like 1KB compression ) 0.000000651389598842  [6⁶] plane crash      g:  O(1) = excellent
```

