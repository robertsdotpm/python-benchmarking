# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
        atoms (1)      . soot (2)      , rice (3)      ; peas (4)      o marbles (5)      0 golf balls (6)      8 tennis balls (7)      # bowling balls (8)

      ■■■ time()                                   , (3)      0.0000012124707698822021484375 rice:                O(1) = excellent
       ■■ list append small int                    . (2)           0.00000064292144775390625 soot:                O(1) = excellent
       ■■ overhead of a func call                  . (2)       0.000000676333904266357421875 soot:                O(1) = excellent
       ■■ make a dic with one item                 . (2)      0.0000006476695537567138671875 soot:                O(1) = excellent
       ■■ dict key lookup from single item dic     . (2)      0.0000005924060344696044921875 soot:                O(1) = excellent
       ■■ make a dic with 4 items                  . (2)         0.0000006636943817138671875 soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic          . (2)      0.0000006385047435760498046875 soot:                O(1) = excellent
      ■■■ create an async queue                    , (3)        0.00000223334598541259765625 rice:                O(1) = excellent
      ■■■ add to an async queue                    , (3)      0.0000011282947063446044921875 rice:                O(1) = excellent
      ■■■ get from an async queue                  , (3)      0.0000010236947536468505859375 rice:                O(1) = excellent
      ■■■ build async event                        , (3)      0.0000011623046398162841796875 rice:                O(1) = excellent
       ■■ set async event                          . (2)        0.00000075884151458740234375 soot:                O(1) = excellent
       ■■ if x == n else ..                        . (2)      0.0000005978686809539794921875 soot:                O(1) = excellent
       ■■ n in list[5]                             . (2)      0.0000007034366130828857421875 soot:                     O(n) = fair
       ■■ n in list[10]                            . (2)        0.00000080967235565185546875 soot:                     O(n) = fair
      ■■■ n in list[100]                           , (3)      0.0000020832068920135498046875 rice:                     O(n) = fair
     ■■■■ n in list[1000]                          ; (4)        0.00001415097713470458984375 peas:                     O(n) = fair
       ■■ str in list[5]                           . (2)      0.0000006751410961151123046875 soot:                     O(n) = fair
       ■■ str in list[10]                          . (2)        0.00000069858837127685546875 soot:                     O(n) = fair
      ■■■ str in list[100]                         , (3)        0.00000128225803375244140625 rice:                     O(n) = fair
      ■■■ ip bytes to ipaddress                    , (3)      0.0000023830463886260986328125 rice:                O(1) = excellent
       ■■ store ip tuple in dic                    . (2)      0.0000005744183063507080078125 soot:                O(1) = excellent
       ■■ 1k str to bytes                          . (2)           0.00000072978973388671875 soot:                     O(n) = fair
       ■■ 1k bytes to str                          . (2)      0.0000008039672374725341796875 soot:                     O(n) = fair
      ■■■ build stream sock                        , (3)           0.00000598430633544921875 rice:                O(1) = excellent
      ■■■ build dgram sock                         , (3)         0.0000069768428802490234375 rice:                O(1) = excellent
     ■■■■ bind dgram sock                          ; (4)         0.0000109660625457763671875 peas:                O(1) = excellent
     ■■■■ send 100 b udp packets                   ; (4)         0.0000259225368499755859375 peas:                O(1) = excellent
     ■■■■ send 1k udp packets                      ; (4)         0.0000279071331024169921875 peas:                O(1) = excellent
     ■■■■ send 10k udp packets                     ; (4)           0.00004584789276123046875 peas:                O(1) = excellent
  ■■■■■■■ dns lookup google.com (cached prob)      8 (7)    0.0797923564910888671875 tennis balls:                O(1) = excellent
  ■■■■■■■ tcp con to google                        8 (7)    0.0221344470977783203125 tennis balls:                O(1) = excellent
 ■■■■■■■■ tcp echo client                          # (8)   0.1882301330566406250000 bowling balls:                O(1) = excellent
 ```

