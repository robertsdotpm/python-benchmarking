# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
        atoms (8)      . soot (7)      , rice (6)      ; peas (5)      o marbles (4)      0 golf balls (3)      8 tennis balls (2)      # bowling balls (1)

      ■■■ time()                                   , (6)       0.000001133844852447509765625 rice:                O(1) = excellent
       ■■ list append small int                    . (7)      0.0000006549060344696044921875 soot:                O(1) = excellent
       ■■ overhead of a func call                  . (7)           0.00000063968658447265625 soot:                O(1) = excellent
       ■■ make a dic with one item                 . (7)       0.000000640670299530029296875 soot:                O(1) = excellent
       ■■ dict key lookup from single item dic     . (7)      0.0000005808231830596923828125 soot:                O(1) = excellent
       ■■ make a dic with 4 items                  . (7)       0.000000700885295867919921875 soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic          . (7)         0.0000006542034149169921875 soot:                O(1) = excellent
      ■■■ create an async queue                    , (6)        0.00000225407314300537109375 rice:                O(1) = excellent
      ■■■ add to an async queue                    , (6)      0.0000011473515033721923828125 rice:                O(1) = excellent
       ■■ get from an async queue                  . (7)       0.000000974569797515869140625 soot:                O(1) = excellent
      ■■■ build async event                        , (6)      0.0000011861693859100341796875 rice:                O(1) = excellent
       ■■ set async event                          . (7)      0.0000007742741107940673828125 soot:                O(1) = excellent
       ■■ if x == n else ..                        . (7)      0.0000006243879795074462890625 soot:                O(1) = excellent
       ■■ n in list[5]                             . (7)         0.0000007259769439697265625 soot:                     O(n) = fair
       ■■ n in list[10]                            . (7)      0.0000008201549053192138671875 soot:                     O(n) = fair
      ■■■ n in list[100]                           , (6)      0.0000020562536716461181640625 rice:                     O(n) = fair
     ■■■■ n in list[1000]                          ; (5)        0.00001435301303863525390625 peas:                     O(n) = fair
       ■■ str in list[5]                           . (7)      0.0000006662924289703369140625 soot:                     O(n) = fair
       ■■ str in list[10]                          . (7)      0.0000006705758571624755859375 soot:                     O(n) = fair
      ■■■ str in list[100]                         , (6)         0.0000012338657379150390625 rice:                     O(n) = fair
      ■■■ ip bytes to ipaddress                    , (6)        0.00000237593364715576171875 rice:                O(1) = excellent
       ■■ store ip tuple in dic                    . (7)      0.0000006900088787078857421875 soot:                O(1) = excellent
       ■■ 1k str to bytes                          . (7)      0.0000007505128383636474609375 soot:                     O(n) = fair
       ■■ 1k bytes to str                          . (7)      0.0000007974388599395751953125 soot:                     O(n) = fair
      ■■■ build stream sock                        , (6)            0.0000069770812988281250 rice:                O(1) = excellent
      ■■■ build dgram sock                         , (6)          0.000004977703094482421875 rice:                O(1) = excellent
     ■■■■ bind dgram sock                          ; (5)          0.000010970592498779296875 peas:                O(1) = excellent
     ■■■■ send 100 b udp packets                   ; (5)           0.00002990627288818359375 peas:                O(1) = excellent
     ■■■■ send 1k udp packets                      ; (5)         0.0000308907032012939453125 peas:                O(1) = excellent
     ■■■■ send 10k udp packets                     ; (5)            0.0000558166503906250000 peas:                O(1) = excellent
  ■■■■■■■ dns lookup google.com (cached prob)      8 (2)   0.07659800052642822265625 tennis balls:                O(1) = excellent
  ■■■■■■■ tcp con to google                        8 (2)   0.02273490428924560546875 tennis balls:                O(1) = excellent
 ■■■■■■■■ tcp echo client                          # (1)   0.1883389949798583984375 bowling balls:                O(1) = excellent
 ```

