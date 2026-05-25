import re

text = """

================================================================================
Category D
Incomplete dataset or missing generated files.
================================================================================

SN20USBML1237972
----------------
1. SN20USBML1237972_24.json — empty

SN20USBML1237979
----------------
1. SN20USBML1237979_24.json — empty

SN20USBML1237987
----------------
1. SN20USBML1237987_24.json — empty

SN20USBML1237988
----------------
1. SN20USBML1237988_23.json — empty
2. SN20USBML1237988_24.json — empty

SN20USBML1237989
----------------
1. SN20USBML1237989_23.json — empty
2. SN20USBML1237989_24.json — empty

SN20USBML1237992
----------------
1. SN20USBML1237992_23.json — empty
2. SN20USBML1237992_24.json — empty

SN20USBML1237994
----------------
1. SN20USBML1237994_23.json — empty
2. SN20USBML1237994_24.json — empty

SN20USBML1237999
----------------
1. SN20USBML1237999_09.json — empty
2. SN20USBML1237999_10.json — empty
3. SN20USBML1237999_11.json — empty
4. SN20USBML1237999_12.json — empty
5. SN20USBML1237999_13.json — empty
6. SN20USBML1237999_14.json — empty
7. SN20USBML1237999_15.json — empty
8. SN20USBML1237999_16.json — empty
9. SN20USBML1237999_17.json — empty
10. SN20USBML1237999_18.json — empty
11. SN20USBML1237999_19.json — empty
12. SN20USBML1237999_20.json — empty
13. SN20USBML1237999_21.json — empty
14. SN20USBML1237999_22.json — empty
15. SN20USBML1237999_23.json — empty
16. SN20USBML1237999_24.json — empty

SN20USBML1238000
----------------
1. SN20USBML1238000_09.json — empty
2. SN20USBML1238000_10.json — empty
3. SN20USBML1238000_11.json — empty
4. SN20USBML1238000_12.json — empty
5. SN20USBML1238000_13.json — empty
6. SN20USBML1238000_14.json — empty
7. SN20USBML1238000_15.json — empty
8. SN20USBML1238000_16.json — empty
9. SN20USBML1238000_17.json — empty
10. SN20USBML1238000_18.json — empty
11. SN20USBML1238000_19.json — empty
12. SN20USBML1238000_20.json — empty
13. SN20USBML1238000_21.json — empty
14. SN20USBML1238000_22.json — empty
15. SN20USBML1238000_23.json — empty
16. SN20USBML1238000_24.json — empty

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