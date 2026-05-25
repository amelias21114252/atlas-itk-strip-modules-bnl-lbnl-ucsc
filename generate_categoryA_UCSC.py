import re

text = """

================================================================================
Category A
IV current values above threshold.
================================================================================

SN20USBML1236807
----------------
1. SN20USBML1236807_01.json — HIGH CURRENT WARNING: maximum current = 1526.61 nA (> 300 nA)
2. SN20USBML1236807_03.json — HIGH CURRENT WARNING: maximum current = 1055.64 nA (> 300 nA)
3. SN20USBML1236807_05.json — HIGH CURRENT WARNING: maximum current = 1021.22 nA (> 300 nA)
4. SN20USBML1236807_07.json — HIGH CURRENT WARNING: maximum current = 976.24 nA (> 300 nA)
5. SN20USBML1236807_09.json — HIGH CURRENT WARNING: maximum current = 941.65 nA (> 300 nA)
6. SN20USBML1236807_11.json — HIGH CURRENT WARNING: maximum current = 930.98 nA (> 300 nA)
7. SN20USBML1236807_13.json — HIGH CURRENT WARNING: maximum current = 900.93 nA (> 300 nA)
8. SN20USBML1236807_15.json — HIGH CURRENT WARNING: maximum current = 882.10 nA (> 300 nA)
9. SN20USBML1236807_17.json — HIGH CURRENT WARNING: maximum current = 871.32 nA (> 300 nA)
10. SN20USBML1236807_19.json — HIGH CURRENT WARNING: maximum current = 837.02 nA (> 300 nA)
11. SN20USBML1236807_21.json — HIGH CURRENT WARNING: maximum current = 839.35 nA (> 300 nA)
12. SN20USBML1236807_23.json — HIGH CURRENT WARNING: maximum current = 833.29 nA (> 300 nA)
13. SN20USBML1236807_24.json — HIGH CURRENT WARNING: maximum current = 948.38 nA (> 300 nA)

SN20USBML1236960
----------------
1. SN20USBML1236960_01.json — HIGH CURRENT WARNING: maximum current = 3194.74 nA (> 300 nA)
2. SN20USBML1236960_24.json — HIGH CURRENT WARNING: maximum current = 2926.29 nA (> 300 nA)

SN20USBML1237182
----------------
1. SN20USBML1237182_02.json — HIGH CURRENT WARNING: maximum current = 466.72 nA (> 300 nA)

SN20USBML1237480
----------------
1. SN20USBML1237480_01.json — HIGH CURRENT WARNING: maximum current = 414.21 nA (> 300 nA)
2. SN20USBML1237480_03.json — HIGH CURRENT WARNING: maximum current = 322.54 nA (> 300 nA)
3. SN20USBML1237480_05.json — HIGH CURRENT WARNING: maximum current = 330.55 nA (> 300 nA)
4. SN20USBML1237480_07.json — HIGH CURRENT WARNING: maximum current = 327.32 nA (> 300 nA)
5. SN20USBML1237480_09.json — HIGH CURRENT WARNING: maximum current = 313.41 nA (> 300 nA)
6. SN20USBML1237480_11.json — HIGH CURRENT WARNING: maximum current = 314.44 nA (> 300 nA)
7. SN20USBML1237480_13.json — HIGH CURRENT WARNING: maximum current = 309.04 nA (> 300 nA)
8. SN20USBML1237480_15.json — HIGH CURRENT WARNING: maximum current = 312.67 nA (> 300 nA)
9. SN20USBML1237480_17.json — HIGH CURRENT WARNING: maximum current = 304.78 nA (> 300 nA)
10. SN20USBML1237480_19.json — HIGH CURRENT WARNING: maximum current = 306.31 nA (> 300 nA)
11. SN20USBML1237480_21.json — HIGH CURRENT WARNING: maximum current = 307.07 nA (> 300 nA)
12. SN20USBML1237480_23.json — HIGH CURRENT WARNING: maximum current = 315.49 nA (> 300 nA)
13. SN20USBML1237480_24.json — HIGH CURRENT WARNING: maximum current = 353.95 nA (> 300 nA)

SN20USBML1237510
----------------
1. SN20USBML1237510_22.json — HIGH CURRENT WARNING: maximum current = 3475.00 nA (> 300 nA)

SN20USBML1237660
----------------
1. SN20USBML1237660_01.json — HIGH CURRENT WARNING: maximum current = 444.79 nA (> 300 nA)
2. SN20USBML1237660_03.json — HIGH CURRENT WARNING: maximum current = 347.17 nA (> 300 nA)
3. SN20USBML1237660_05.json — HIGH CURRENT WARNING: maximum current = 342.67 nA (> 300 nA)
4. SN20USBML1237660_07.json — HIGH CURRENT WARNING: maximum current = 325.47 nA (> 300 nA)
5. SN20USBML1237660_09.json — HIGH CURRENT WARNING: maximum current = 330.59 nA (> 300 nA)
6. SN20USBML1237660_11.json — HIGH CURRENT WARNING: maximum current = 332.26 nA (> 300 nA)
7. SN20USBML1237660_13.json — HIGH CURRENT WARNING: maximum current = 331.49 nA (> 300 nA)
8. SN20USBML1237660_15.json — HIGH CURRENT WARNING: maximum current = 316.22 nA (> 300 nA)
9. SN20USBML1237660_17.json — HIGH CURRENT WARNING: maximum current = 308.90 nA (> 300 nA)
10. SN20USBML1237660_19.json — HIGH CURRENT WARNING: maximum current = 314.41 nA (> 300 nA)
11. SN20USBML1237660_21.json — HIGH CURRENT WARNING: maximum current = 307.38 nA (> 300 nA)
12. SN20USBML1237660_24.json — HIGH CURRENT WARNING: maximum current = 433.05 nA (> 300 nA)

SN20USBML1237968
----------------
1. SN20USBML1237968_02.json — HIGH CURRENT WARNING: maximum current = 2562.91 nA (> 300 nA)
2. SN20USBML1237968_22.json — HIGH CURRENT WARNING: maximum current = 2555.28 nA (> 300 nA)

SN20USBML1237983
----------------
1. SN20USBML1237983_03.json — HIGH CURRENT WARNING: maximum current = 447.43 nA (> 300 nA)
2. SN20USBML1237983_05.json — HIGH CURRENT WARNING: maximum current = 444.75 nA (> 300 nA)
3. SN20USBML1237983_07.json — HIGH CURRENT WARNING: maximum current = 454.80 nA (> 300 nA)
4. SN20USBML1237983_09.json — HIGH CURRENT WARNING: maximum current = 447.38 nA (> 300 nA)
5. SN20USBML1237983_11.json — HIGH CURRENT WARNING: maximum current = 446.60 nA (> 300 nA)
6. SN20USBML1237983_13.json — HIGH CURRENT WARNING: maximum current = 460.32 nA (> 300 nA)
7. SN20USBML1237983_15.json — HIGH CURRENT WARNING: maximum current = 432.72 nA (> 300 nA)
8. SN20USBML1237983_17.json — HIGH CURRENT WARNING: maximum current = 468.72 nA (> 300 nA)
9. SN20USBML1237983_19.json — HIGH CURRENT WARNING: maximum current = 461.41 nA (> 300 nA)
10. SN20USBML1237983_21.json — HIGH CURRENT WARNING: maximum current = 441.07 nA (> 300 nA)
11. SN20USBML1237983_23.json — HIGH CURRENT WARNING: maximum current = 459.29 nA (> 300 nA)
12. SN20USBML1237983_24.json — HIGH CURRENT WARNING: maximum current = 303.47 nA (> 300 nA)

SN20USBML1237984
----------------
1. SN20USBML1237984_01.json — HIGH CURRENT WARNING: maximum current = 318.10 nA (> 300 nA)
2. SN20USBML1237984_03.json — HIGH CURRENT WARNING: maximum current = 411.17 nA (> 300 nA)
3. SN20USBML1237984_05.json — HIGH CURRENT WARNING: maximum current = 418.72 nA (> 300 nA)
4. SN20USBML1237984_07.json — HIGH CURRENT WARNING: maximum current = 426.82 nA (> 300 nA)
5. SN20USBML1237984_09.json — HIGH CURRENT WARNING: maximum current = 435.39 nA (> 300 nA)
6. SN20USBML1237984_11.json — HIGH CURRENT WARNING: maximum current = 420.85 nA (> 300 nA)
7. SN20USBML1237984_13.json — HIGH CURRENT WARNING: maximum current = 436.74 nA (> 300 nA)
8. SN20USBML1237984_15.json — HIGH CURRENT WARNING: maximum current = 441.17 nA (> 300 nA)
9. SN20USBML1237984_17.json — HIGH CURRENT WARNING: maximum current = 436.19 nA (> 300 nA)
10. SN20USBML1237984_19.json — HIGH CURRENT WARNING: maximum current = 437.65 nA (> 300 nA)
11. SN20USBML1237984_21.json — HIGH CURRENT WARNING: maximum current = 445.98 nA (> 300 nA)
12. SN20USBML1237984_23.json — HIGH CURRENT WARNING: maximum current = 434.95 nA (> 300 nA)
13. SN20USBML1237984_24.json — HIGH CURRENT WARNING: maximum current = 316.69 nA (> 300 nA)

SN20USBML1237991
----------------
1. SN20USBML1237991_02.json — HIGH CURRENT WARNING: maximum current = 332.86 nA (> 300 nA)
2. SN20USBML1237991_03.json — HIGH CURRENT WARNING: maximum current = 365.39 nA (> 300 nA)
3. SN20USBML1237991_05.json — HIGH CURRENT WARNING: maximum current = 364.43 nA (> 300 nA)
4. SN20USBML1237991_07.json — HIGH CURRENT WARNING: maximum current = 365.98 nA (> 300 nA)
5. SN20USBML1237991_09.json — HIGH CURRENT WARNING: maximum current = 364.02 nA (> 300 nA)
6. SN20USBML1237991_11.json — HIGH CURRENT WARNING: maximum current = 365.87 nA (> 300 nA)
7. SN20USBML1237991_13.json — HIGH CURRENT WARNING: maximum current = 368.32 nA (> 300 nA)
8. SN20USBML1237991_15.json — HIGH CURRENT WARNING: maximum current = 363.20 nA (> 300 nA)
9. SN20USBML1237991_17.json — HIGH CURRENT WARNING: maximum current = 364.94 nA (> 300 nA)
10. SN20USBML1237991_19.json — HIGH CURRENT WARNING: maximum current = 363.63 nA (> 300 nA)
11. SN20USBML1237991_21.json — HIGH CURRENT WARNING: maximum current = 367.73 nA (> 300 nA)
12. SN20USBML1237991_22.json — HIGH CURRENT WARNING: maximum current = 330.16 nA (> 300 nA)
13. SN20USBML1237991_23.json — HIGH CURRENT WARNING: maximum current = 362.86 nA (> 300 nA)
14. SN20USBML1237991_24.json — HIGH CURRENT WARNING: maximum current = 418.87 nA (> 300 nA)

SN20USBML1238366
----------------
1. SN20USBML1238366_02.json — HIGH CURRENT WARNING: maximum current = 1156.44 nA (> 300 nA)

SN20USBML1238399
----------------
1. SN20USBML1238399_02.json — HIGH CURRENT WARNING: maximum current = 709.40 nA (> 300 nA)

SN20USBML1238986
----------------
1. SN20USBML1238986_24.json — HIGH CURRENT WARNING: maximum current = 442.90 nA (> 300 nA)

SN20USBML1238991
----------------
1. SN20USBML1238991_10.json — HIGH CURRENT WARNING: maximum current = 346.27 nA (> 300 nA)
2. SN20USBML1238991_12.json — HIGH CURRENT WARNING: maximum current = 391.00 nA (> 300 nA)
3. SN20USBML1238991_14.json — HIGH CURRENT WARNING: maximum current = 436.80 nA (> 300 nA)
4. SN20USBML1238991_16.json — HIGH CURRENT WARNING: maximum current = 450.02 nA (> 300 nA)
5. SN20USBML1238991_18.json — HIGH CURRENT WARNING: maximum current = 528.41 nA (> 300 nA)
6. SN20USBML1238991_20.json — HIGH CURRENT WARNING: maximum current = 488.02 nA (> 300 nA)
7. SN20USBML1238991_22.json — HIGH CURRENT WARNING: maximum current = 479.34 nA (> 300 nA)

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