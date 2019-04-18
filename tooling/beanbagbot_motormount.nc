%
(beanbagbot_motormount)
(T3  D=0.323 CR=0. TAPER=118deg - ZMIN=-0.647 - drill)
(T5  D=0.375 CR=0. - ZMIN=-0.55 - flat end mill)
(T8  D=0.3125 CR=0. TAPER=118deg - ZMIN=-0.25 - center drill)
G90 G54 G64 G50 G17 G40 G80 G94 G91.1 G49
G20 (Inch)
G30

N10(Drill7)
T5 G43 H5 M6
S5140 M3 M8
G54
G0 X2.875 Y0.75
G0 Z2.
G0 Z0.5
G0 Y0.875
G0 Z0.2
G1 Z0. F5.
G3 Y0.625 Z-0.02 I0. J-0.125
G3 Y0.875 Z-0.04 I0. J0.125
G3 Y0.625 Z-0.06 I0. J-0.125
G3 Y0.875 Z-0.08 I0. J0.125
G3 Y0.625 Z-0.1 I0. J-0.125
G3 Y0.875 Z-0.12 I0. J0.125
G3 Y0.625 Z-0.14 I0. J-0.125
G3 Y0.875 Z-0.16 I0. J0.125
G3 Y0.625 Z-0.18 I0. J-0.125
G3 Y0.875 Z-0.2 I0. J0.125
G3 Y0.625 Z-0.22 I0. J-0.125
G3 Y0.875 Z-0.24 I0. J0.125
G3 Y0.625 Z-0.26 I0. J-0.125
G3 Y0.875 Z-0.28 I0. J0.125
G3 Y0.625 Z-0.3 I0. J-0.125
G3 Y0.875 Z-0.32 I0. J0.125
G3 Y0.625 Z-0.34 I0. J-0.125
G3 Y0.875 Z-0.36 I0. J0.125
G3 Y0.625 Z-0.38 I0. J-0.125
G3 Y0.875 Z-0.4 I0. J0.125
G3 Y0.625 Z-0.42 I0. J-0.125
G3 Y0.875 Z-0.44 I0. J0.125
G3 Y0.625 Z-0.46 I0. J-0.125
G3 Y0.875 Z-0.48 I0. J0.125
G3 Y0.625 Z-0.5 I0. J-0.125
G3 Y0.875 Z-0.52 I0. J0.125
G3 Y0.625 Z-0.54 I0. J-0.125
G3 X3. Y0.75 Z-0.55 I0. J0.125
G3 X2.75 I-0.125 J0.
G3 X3. I0.125 J0.
G3 X2.875 I-0.0625 J0.
G0 Z0.5
G0 Z2.
M5 M9
G30

N20(Drill8)
M1
T8 G43 H8 M6
S3670 M3 M8
G0 X0.4635 Y0.75
G0 Z0.8
G0 Z0.2
G98 G81 X0.4635 Y0.75 Z-0.25 R0.2 F2.
X1.9635
X3.7865
X5.2865
G80
G0 Z0.8
M5 M9
G30

N30(Drill6)
M1
T3 G43 H3 M6
S3550 M3 M8
G0 X0.4635 Y0.75
G0 Z2.
G0 Z0.5
G98 G73 X0.4635 Y0.75 Z-0.647 R0.2 Q0.0807 F2.
X1.9635
X3.7865
X5.2865
G80
G0 Z2.
M5 M9

G30
M30
%
