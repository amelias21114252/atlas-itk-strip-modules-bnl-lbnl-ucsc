import re

text = """

================================================================================
Category A
IV current values above threshold.
================================================================================

SN20USBML1236980
----------------
1. SN20USBML1236980_21.json — HIGH CURRENT WARNING: maximum current = 613.05 nA (> 300 nA)

SN20USBML1237032
----------------
1. SN20USBML1237032_03.json — HIGH CURRENT WARNING: maximum current = 308.82 nA (> 300 nA)
2. SN20USBML1237032_05.json — HIGH CURRENT WARNING: maximum current = 303.33 nA (> 300 nA)
3. SN20USBML1237032_07.json — HIGH CURRENT WARNING: maximum current = 306.64 nA (> 300 nA)
4. SN20USBML1237032_13.json — HIGH CURRENT WARNING: maximum current = 309.93 nA (> 300 nA)
5. SN20USBML1237032_15.json — HIGH CURRENT WARNING: maximum current = 308.62 nA (> 300 nA)
6. SN20USBML1237032_23.json — HIGH CURRENT WARNING: maximum current = 300.67 nA (> 300 nA)

SN20USBML1237034
----------------
1. SN20USBML1237034_03.json — HIGH CURRENT WARNING: maximum current = 322.31 nA (> 300 nA)
2. SN20USBML1237034_05.json — HIGH CURRENT WARNING: maximum current = 324.00 nA (> 300 nA)
3. SN20USBML1237034_07.json — HIGH CURRENT WARNING: maximum current = 327.52 nA (> 300 nA)
4. SN20USBML1237034_09.json — HIGH CURRENT WARNING: maximum current = 318.09 nA (> 300 nA)
5. SN20USBML1237034_11.json — HIGH CURRENT WARNING: maximum current = 315.10 nA (> 300 nA)
6. SN20USBML1237034_13.json — HIGH CURRENT WARNING: maximum current = 319.14 nA (> 300 nA)
7. SN20USBML1237034_15.json — HIGH CURRENT WARNING: maximum current = 313.93 nA (> 300 nA)
8. SN20USBML1237034_17.json — HIGH CURRENT WARNING: maximum current = 318.30 nA (> 300 nA)
9. SN20USBML1237034_19.json — HIGH CURRENT WARNING: maximum current = 320.97 nA (> 300 nA)
10. SN20USBML1237034_21.json — HIGH CURRENT WARNING: maximum current = 331.63 nA (> 300 nA)
11. SN20USBML1237034_23.json — HIGH CURRENT WARNING: maximum current = 330.59 nA (> 300 nA)

SN20USBML1237155
----------------
1. SN20USBML1237155_01.json — HIGH CURRENT WARNING: maximum current = 2011.82 nA (> 300 nA)
2. SN20USBML1237155_10.json — HIGH CURRENT WARNING: maximum current = 379.60 nA (> 300 nA)
3. SN20USBML1237155_12.json — HIGH CURRENT WARNING: maximum current = 620.37 nA (> 300 nA)
4. SN20USBML1237155_14.json — HIGH CURRENT WARNING: maximum current = 872.02 nA (> 300 nA)
5. SN20USBML1237155_16.json — HIGH CURRENT WARNING: maximum current = 959.17 nA (> 300 nA)
6. SN20USBML1237155_18.json — HIGH CURRENT WARNING: maximum current = 1118.54 nA (> 300 nA)
7. SN20USBML1237155_20.json — HIGH CURRENT WARNING: maximum current = 1040.89 nA (> 300 nA)
8. SN20USBML1237155_22.json — HIGH CURRENT WARNING: maximum current = 3656.44 nA (> 300 nA)
9. SN20USBML1237155_24.json — HIGH CURRENT WARNING: maximum current = 6393.72 nA (> 300 nA)

SN20USBML1237571
----------------
1. SN20USBML1237571_01.json — HIGH CURRENT WARNING: maximum current = 393.23 nA (> 300 nA)
2. SN20USBML1237571_05.json — HIGH CURRENT WARNING: maximum current = 309.83 nA (> 300 nA)
3. SN20USBML1237571_07.json — HIGH CURRENT WARNING: maximum current = 307.60 nA (> 300 nA)
4. SN20USBML1237571_09.json — HIGH CURRENT WARNING: maximum current = 302.38 nA (> 300 nA)
5. SN20USBML1237571_15.json — HIGH CURRENT WARNING: maximum current = 300.00 nA (> 300 nA)
6. SN20USBML1237571_23.json — HIGH CURRENT WARNING: maximum current = 302.30 nA (> 300 nA)

SN20USBML1237578
----------------
1. SN20USBML1237578_01.json — HIGH CURRENT WARNING: maximum current = 3024.39 nA (> 300 nA)
2. SN20USBML1237578_03.json — HIGH CURRENT WARNING: maximum current = 2350.78 nA (> 300 nA)
3. SN20USBML1237578_04.json — HIGH CURRENT WARNING: maximum current = 327.49 nA (> 300 nA)
4. SN20USBML1237578_05.json — HIGH CURRENT WARNING: maximum current = 2314.87 nA (> 300 nA)
5. SN20USBML1237578_06.json — HIGH CURRENT WARNING: maximum current = 307.36 nA (> 300 nA)
6. SN20USBML1237578_07.json — HIGH CURRENT WARNING: maximum current = 2293.18 nA (> 300 nA)
7. SN20USBML1237578_08.json — HIGH CURRENT WARNING: maximum current = 319.28 nA (> 300 nA)
8. SN20USBML1237578_09.json — HIGH CURRENT WARNING: maximum current = 2258.93 nA (> 300 nA)
9. SN20USBML1237578_11.json — HIGH CURRENT WARNING: maximum current = 2236.94 nA (> 300 nA)
10. SN20USBML1237578_13.json — HIGH CURRENT WARNING: maximum current = 2211.75 nA (> 300 nA)
11. SN20USBML1237578_15.json — HIGH CURRENT WARNING: maximum current = 2168.89 nA (> 300 nA)
12. SN20USBML1237578_17.json — HIGH CURRENT WARNING: maximum current = 2183.65 nA (> 300 nA)
13. SN20USBML1237578_19.json — HIGH CURRENT WARNING: maximum current = 2141.59 nA (> 300 nA)
14. SN20USBML1237578_21.json — HIGH CURRENT WARNING: maximum current = 2117.53 nA (> 300 nA)
15. SN20USBML1237578_23.json — HIGH CURRENT WARNING: maximum current = 2104.81 nA (> 300 nA)
16. SN20USBML1237578_24.json — HIGH CURRENT WARNING: maximum current = 2833.54 nA (> 300 nA)

SN20USBML1237592
----------------
1. SN20USBML1237592_22.json — HIGH CURRENT WARNING: maximum current = 2054.55 nA (> 300 nA)

SN20USBML1237606
----------------
1. SN20USBML1237606_01.json — HIGH CURRENT WARNING: maximum current = 383.94 nA (> 300 nA)

SN20USBML1238008
----------------
1. SN20USBML1238008_01.json — HIGH CURRENT WARNING: maximum current = 9722.51 nA (> 300 nA)
2. SN20USBML1238008_02.json — HIGH CURRENT WARNING: maximum current = 3344.43 nA (> 300 nA)
3. SN20USBML1238008_10.json — HIGH CURRENT WARNING: maximum current = 586.21 nA (> 300 nA)
4. SN20USBML1238008_12.json — HIGH CURRENT WARNING: maximum current = 1268.00 nA (> 300 nA)
5. SN20USBML1238008_14.json — HIGH CURRENT WARNING: maximum current = 2629.20 nA (> 300 nA)
6. SN20USBML1238008_16.json — HIGH CURRENT WARNING: maximum current = 3420.40 nA (> 300 nA)
7. SN20USBML1238008_18.json — HIGH CURRENT WARNING: maximum current = 3267.66 nA (> 300 nA)
8. SN20USBML1238008_20.json — HIGH CURRENT WARNING: maximum current = 2812.66 nA (> 300 nA)
9. SN20USBML1238008_22.json — HIGH CURRENT WARNING: maximum current = 5616.12 nA (> 300 nA)
10. SN20USBML1238008_24.json — HIGH CURRENT WARNING: maximum current = 10056.19 nA (> 300 nA)

SN20USBML1238138
----------------
1. SN20USBML1238138_01.json — HIGH CURRENT WARNING: maximum current = 742.98 nA (> 300 nA)
2. SN20USBML1238138_03.json — HIGH CURRENT WARNING: maximum current = 476.20 nA (> 300 nA)
3. SN20USBML1238138_05.json — HIGH CURRENT WARNING: maximum current = 447.59 nA (> 300 nA)
4. SN20USBML1238138_07.json — HIGH CURRENT WARNING: maximum current = 422.82 nA (> 300 nA)
5. SN20USBML1238138_09.json — HIGH CURRENT WARNING: maximum current = 412.18 nA (> 300 nA)
6. SN20USBML1238138_11.json — HIGH CURRENT WARNING: maximum current = 422.10 nA (> 300 nA)
7. SN20USBML1238138_13.json — HIGH CURRENT WARNING: maximum current = 434.90 nA (> 300 nA)
8. SN20USBML1238138_15.json — HIGH CURRENT WARNING: maximum current = 443.82 nA (> 300 nA)
9. SN20USBML1238138_17.json — HIGH CURRENT WARNING: maximum current = 456.46 nA (> 300 nA)
10. SN20USBML1238138_19.json — HIGH CURRENT WARNING: maximum current = 487.62 nA (> 300 nA)
11. SN20USBML1238138_21.json — HIGH CURRENT WARNING: maximum current = 529.69 nA (> 300 nA)
12. SN20USBML1238138_23.json — HIGH CURRENT WARNING: maximum current = 542.78 nA (> 300 nA)
13. SN20USBML1238138_24.json — HIGH CURRENT WARNING: maximum current = 666.41 nA (> 300 nA)

SN20USBML1238408
----------------
1. SN20USBML1238408_01.json — HIGH CURRENT WARNING: maximum current = 7949.26 nA (> 300 nA)
2. SN20USBML1238408_03.json — HIGH CURRENT WARNING: maximum current = 436.77 nA (> 300 nA)
3. SN20USBML1238408_05.json — HIGH CURRENT WARNING: maximum current = 371.33 nA (> 300 nA)
4. SN20USBML1238408_07.json — HIGH CURRENT WARNING: maximum current = 321.79 nA (> 300 nA)
5. SN20USBML1238408_09.json — HIGH CURRENT WARNING: maximum current = 431.27 nA (> 300 nA)
6. SN20USBML1238408_11.json — HIGH CURRENT WARNING: maximum current = 368.02 nA (> 300 nA)
7. SN20USBML1238408_13.json — HIGH CURRENT WARNING: maximum current = 333.92 nA (> 300 nA)
8. SN20USBML1238408_24.json — HIGH CURRENT WARNING: maximum current = 1370.26 nA (> 300 nA)

SN20USBML1238778
----------------
1. SN20USBML1238778_22.json — HIGH CURRENT WARNING: maximum current = 1401.05 nA (> 300 nA)

SN20USBML1238811
----------------
1. SN20USBML1238811_23.json — HIGH CURRENT WARNING: maximum current = 412.16 nA (> 300 nA)
2. SN20USBML1238811_24.json — HIGH CURRENT WARNING: maximum current = 3689.70 nA (> 300 nA)

SN20USBML1238813
----------------
1. SN20USBML1238813_01.json — HIGH CURRENT WARNING: maximum current = 8391.03 nA (> 300 nA)
2. SN20USBML1238813_12.json — HIGH CURRENT WARNING: maximum current = 387.92 nA (> 300 nA)
3. SN20USBML1238813_14.json — HIGH CURRENT WARNING: maximum current = 620.11 nA (> 300 nA)
4. SN20USBML1238813_16.json — HIGH CURRENT WARNING: maximum current = 741.23 nA (> 300 nA)
5. SN20USBML1238813_18.json — HIGH CURRENT WARNING: maximum current = 1089.61 nA (> 300 nA)
6. SN20USBML1238813_20.json — HIGH CURRENT WARNING: maximum current = 1060.39 nA (> 300 nA)
7. SN20USBML1238813_22.json — HIGH CURRENT WARNING: maximum current = 3931.16 nA (> 300 nA)
8. SN20USBML1238813_24.json — HIGH CURRENT WARNING: maximum current = 10049.18 nA (> 300 nA)

"""

# Find serials like SN20USBML1236980, 20USBML1236980, SN20USBHX2004272, etc.
serials = re.findall(r'\bSN?(20USB(?:HX|ML)\d+)\b', text)

# Remove duplicates but keep original order
unique_serials = []
seen = set()

for serial in serials:
    if serial not in seen:
        unique_serials.append(serial)
        seen.add(serial)

# Print in requested format
for serial in unique_serials:
    print(f'"{serial}",')
    print()