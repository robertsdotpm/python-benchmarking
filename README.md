# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
Based on average death probability except for lighting strike.
These sizes reflect the number of decimal places.

❤️ a heart disease (1)      🚗 b vehicle crash (2)      🌊 c drowning (3)      🛶 d canoe death (4)      🪂 e sky diving (5)      ⚡ f lightning strike (6)      ✈️ g plane crash (7)      🦈 h shark attack (8)
 1s 1000x > 1ms 1000x > 1µs 1000x > 1ns

 ■■■■■■■■ [⁰a 191 ❤️] ms: tcp echo client                             slow ❤️ a (8: like website RTT     ) 0.191322946549        [1⁰] heart disease    a:  O(1) = excellent
  ■■■■■■■ [¹b 85  🚗] ms: dns lookup google.com (cached prob)         slow 🚗 b (7: like gaming RTT      ) 0.0857495546341       [8¹] vehicle crash    b:  O(1) = excellent
  ■■■■■■■ [¹b 26  🚗] ms: tcp con to google                           slow 🚗 b (7: like gaming RTT      ) 0.0261753320694       [2¹] vehicle crash    b:  O(1) = excellent
     ■■■■ [⁴e 43  🪂] µs: send 10k udp packets                       brisk 🪂 e (4: like memory slice    ) 0.0000430078506472    [4⁴] sky diving       e:  O(1) = excellent
     ■■■■ [⁴e 27  🪂] µs: send 100 b udp packets                     brisk 🪂 e (4: like memory slice    ) 0.0000270204544067    [2⁴] sky diving       e:  O(1) = excellent
     ■■■■ [⁴e 26  🪂] µs: send 1k udp packets                        brisk 🪂 e (4: like memory slice    ) 0.0000265190601351    [2⁴] sky diving       e:  O(1) = excellent
     ■■■■ [⁴e 13  🪂] µs: n in list[1000]                            brisk 🪂 e (4: like memory slice    ) 0.0000130016803743    [1⁴] sky diving       e:      O(n) = fair
      ■■■ [⁵f 9   ⚡] µs: build stream sock                          brisk ⚡ f (3: like LAN send        ) 0.00000900626182555   [9⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 7   ⚡] µs: build dgram sock                           brisk ⚡ f (3: like LAN send        ) 0.00000799965858458   [7⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 4   ⚡] µs: bind dgram sock                            brisk ⚡ f (3: like LAN send        ) 0.00000499916076659   [4⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 2   ⚡] µs: ip bytes to ipaddress                      brisk ⚡ f (3: like LAN send        ) 0.00000232597374896   [2⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 1   ⚡] µs: n in list[100]                             brisk ⚡ f (3: like LAN send        ) 0.0000019692113398    [1⁵] lightning strike f:      O(n) = fair
      ■■■ [⁵f 1   ⚡] µs: create an async queue                      brisk ⚡ f (3: like LAN send        ) 0.00000146825790393   [1⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 1   ⚡] µs: time()                                     brisk ⚡ f (3: like LAN send        ) 0.00000124833917614   [1⁵] lightning strike f:  O(1) = excellent
      ■■■ [⁵f 1   ⚡] µs: str in list[100]                           brisk ⚡ f (3: like LAN send        ) 0.00000110484862322   [1⁵] lightning strike f:      O(n) = fair
      ■■■ [⁵f 1   ⚡] µs: add to an async queue                      brisk ⚡ f (3: like LAN send        ) 0.00000102562665936   [1⁵] lightning strike f:  O(1) = excellent
       ■■ [⁶g 958 ✈️] ns: get environmental variable                  fast ✈️ g (2: like 1KB compression ) 0.000000958602428441  [9⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 921 ✈️] ns: build async event                           fast ✈️ g (2: like 1KB compression ) 0.000000921277284618  [9⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 867 ✈️] ns: get from an async queue                     fast ✈️ g (2: like 1KB compression ) 0.000000867151975628  [8⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 820 ✈️] ns: 1k bytes to str                             fast ✈️ g (2: like 1KB compression ) 0.000000820256471628  [8⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 808 ✈️] ns: n in list[10]                               fast ✈️ g (2: like 1KB compression ) 0.000000808674812319  [8⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 766 ✈️] ns: set async event                             fast ✈️ g (2: like 1KB compression ) 0.000000766358137138  [7⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 742 ✈️] ns: n in list[5]                                fast ✈️ g (2: like 1KB compression ) 0.000000742086648952  [7⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 728 ✈️] ns: 1k str to bytes                             fast ✈️ g (2: like 1KB compression ) 0.000000728704214099  [7⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 711 ✈️] ns: str in list[10]                             fast ✈️ g (2: like 1KB compression ) 0.000000711788892747  [7⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 702 ✈️] ns: dict key lookup from single item dic        fast ✈️ g (2: like 1KB compression ) 0.000000702385663992  [7⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 698 ✈️] ns: make a dic with 4 items                     fast ✈️ g (2: like 1KB compression ) 0.000000698316097254  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 689 ✈️] ns: make a dic with one item                    fast ✈️ g (2: like 1KB compression ) 0.000000689263343808  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 682 ✈️] ns: overhead of a func call                     fast ✈️ g (2: like 1KB compression ) 0.000000682849168761  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 679 ✈️] ns: store ip tuple in dic                       fast ✈️ g (2: like 1KB compression ) 0.000000679244518276  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 662 ✈️] ns: str in list[5]                              fast ✈️ g (2: like 1KB compression ) 0.000000662681817996  [6⁶] plane crash      g:      O(n) = fair
       ■■ [⁶g 656 ✈️] ns: list append small int                       fast ✈️ g (2: like 1KB compression ) 0.000000656740188592  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 647 ✈️] ns: dict key lookup from 4 item dic             fast ✈️ g (2: like 1KB compression ) 0.000000647888660424  [6⁶] plane crash      g:  O(1) = excellent
       ■■ [⁶g 633 ✈️] ns: if x == n else ..                           fast ✈️ g (2: like 1KB compression ) 0.000000633290767653  [6⁶] plane crash      g:  O(1) = excellent
```

