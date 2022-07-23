# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

```
       ■■ list append small int                         0.0000006465117931365966796875 soot:                O(1) = excellent
       ■■ overhead of a func call                       0.0000006759536266326904296875 soot:                O(1) = excellent
       ■■ make a dic with one item                        0.00000068517589569091796875 soot:                O(1) = excellent
       ■■ dict key lookup from single item dic           0.000000657023906707763671875 soot:                O(1) = excellent
       ■■ make a dic with 4 items                       0.0000006766397953033447265625 soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic                0.000000629467487335205078125 soot:                O(1) = excellent
      ■■■ create an async queue                           0.00000223837757110595703125 sand:                O(1) = excellent
      ■■■ add to an async queue                         0.0000010849487781524658203125 sand:                O(1) = excellent
      ■■■ get from an async queue                       0.0000010221984386444091796875 sand:                O(1) = excellent
      ■■■ build async event                               0.00000114129924774169921875 sand:                O(1) = excellent
       ■■ set async event                                 0.00000075875186920166015625 soot:                O(1) = excellent
       ■■ if x == n else ..                              0.000000630827426910400390625 soot:                O(1) = excellent
       ■■ n in list[5]                                  0.0000007194516658782958984375 soot:                     O(n) = fair
       ■■ n in list[10]                                  0.000000831948757171630859375 soot:                     O(n) = fair
      ■■■ n in list[100]                                0.0000020643889904022216796875 sand:                     O(n) = fair
     ■■■■ n in list[1000]                                   0.000014973545074462890625 peas:                     O(n) = fair
       ■■ str in list[5]                                  0.00000064152431488037109375 soot:                     O(n) = fair
       ■■ str in list[10]                                0.000000677704334259033203125 soot:                     O(n) = fair
      ■■■ str in list[100]                              0.0000012035639286041259765625 sand:                     O(n) = fair
      ■■■ ip bytes to ipaddress                           0.00000244194889068603515625 sand:                O(1) = excellent
       ■■ store ip tuple in dic                          0.000000645173549652099609375 soot:                O(1) = excellent
       ■■ 1k str to bytes                                0.000000780634403228759765625 soot:                     O(n) = fair
       ■■ 1k bytes to str                                 0.00000088452053070068359375 soot:                     O(n) = fair
      ■■■ build stream sock                                0.0000099399089813232421875 sand:                O(1) = excellent
      ■■■ build dgram sock                                 0.0000079867839813232421875 sand:                O(1) = excellent
     ■■■■ bind dgram sock                                  0.0000119812488555908203125 peas:                O(1) = excellent
     ■■■■ send 100 b udp packets                           0.0000282576084136962890625 peas:                O(1) = excellent
     ■■■■ send 1kb udp packets                              0.0000359408855438232421875 peas:                O(1) = excellent
     ■■■■ send 10kb udp packets                                0.0000559024810791015625 peas:                O(1) = excellent
    ■■■■■ dns lookup google.com (cached prob)             0.00051505565643310546875 marbles:                O(1) = excellent
  ■■■■■■■ tcp con to google                          0.05662667751312255859375 tennis balls:                O(1) = excellent
 ■■■■■■■■ tcp echo client                            0.1860095024108886718750 bowling balls:                O(1) = excellent
 ```

