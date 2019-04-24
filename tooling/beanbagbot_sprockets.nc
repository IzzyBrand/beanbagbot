%
(beanbagbot_sprockets)
(T5  D=0.375 CR=0. - ZMIN=-0.4433 - flat end mill)
(T6  D=0.25 CR=0. TAPER=118deg - ZMIN=-0.5397 - drill)
G90 G54 G64 G50 G17 G40 G80 G94 G91.1 G49
G20 (Inch)
G30

N10(Drill3)
T6 G43 H6 M6
S3060 M3 M8
G54
G0 X-0.7778 Y-0.7778
G0 Z0.6
G0 Z0.2
G98 G73 X-0.7778 Y-0.7778 Z-0.5397 R0.002 Q0.0625 F5.
X0.7778
Y0.7778
X-0.7778
G80
G0 Z0.6
M5 M9
G30

N20(Drill2)
M1
T5 G43 H5 M6
S2546 M3 M8
G0 X0. Y0.
G0 Z0.7874
G0 Z0.3937
G0 X0.0641 Y-0.5528
G0 Z-0.0011
G1 Z-0.1979 F10.
G3 X-0.0641 Y0.5528 Z-0.2176 I-0.0641 J0.5528
G3 X0.0641 Y-0.5528 Z-0.2373 I0.0641 J-0.5528
G3 X-0.0641 Y0.5528 Z-0.257 I-0.0641 J0.5528
G3 X0.0641 Y-0.5528 Z-0.2767 I0.0641 J-0.5528
G3 X-0.0641 Y0.5528 Z-0.2964 I-0.0641 J0.5528
G3 X0.0641 Y-0.5528 Z-0.3161 I0.0641 J-0.5528
G3 X-0.0641 Y0.5528 Z-0.3357 I-0.0641 J0.5528
G3 X0.0641 Y-0.5528 Z-0.3554 I0.0641 J-0.5528
G3 X-0.0641 Y0.5528 Z-0.3751 I-0.0641 J0.5528
G3 X0.0641 Y-0.5528 Z-0.3948 I0.0641 J-0.5528
G3 X-0.0641 Y0.5528 Z-0.4145 I-0.0641 J0.5528
G3 X0.0641 Y-0.5528 Z-0.4342 I0.0641 J-0.5528
G3 X0.5565 Y0. Z-0.4433 I-0.0641 J0.5528
G3 X-0.5565 I-0.5565 J0.
G3 X0.5565 I0.5565 J0.
G3 X0. I-0.2783 J0.
G0 Z0.3937
G0 Z0.7874
M5 M9

G30
M30
%