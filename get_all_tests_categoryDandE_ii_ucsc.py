#python get_all_tests_categoryDandE_ii_ucsc.py


import subprocess

from pathlib import Path

import shutil

serial_numbers = [
    "20USBHX2003578",
    "20USBHX2003580",
    "20USBHX2003579",
    "20USBHX2003581",
    "20USBHX2003582",
    "20USBHX2003583",
    "20USBHX2003618",
    "20USBHX2003619",
    "20USBHX2003621",
    "20USBHX2003616",
    "20USBHX2003617",
    "20USBHX2003753",
    "20USBHX2003754",
    "20USBHX2003755",
    "20USBHX2003746",
    "20USBHX2003747",
    "20USBHX2003758",
    "20USBHX2003759",
    "20USBHX2003760",
    "20USBHX2003761",
    "20USBHX2003762",
    "20USBHX2003620",
    "20USBHX2003752",
    "20USBHX2003448",
    "20USBHX2003449",
    "20USBHX2003450",
    "20USBHX2003451",
    "20USBHX2003452",
    "20USBHX2003461",
    "20USBHX2003764",
    "20USBHX2003745",
    "20USBHX2003766",
    "20USBHX2003768",
    "20USBHX2003776",
    "20USBHX2003777",
    "20USBHX2003474",
    "20USBHX2003591",
    "20USBHX2003781",
    "20USBHX2003778",
    "20USBHX2003779",
    "20USBHX2003780",
    "20USBHX2003788",
    "20USBHX2003756",
    "20USBHX2003757",
    "20USBHX2003789",
    "20USBHX2003790",
    "20USBHX2003782",
    "20USBHX2003783",
    "20USBHX2003784",
    "20USBHX2003765",
    "20USBHX2003611",
    "20USBHX2003612",
    "20USBHX2003613",
    "20USBHX2003614",
    "20USBHX2003615",
    "20USBHX2003610",
    "20USBHX2003785",
    "20USBHX2003786",
    "20USBHX2003787",
    "20USBHX2003793",
    "20USBHX2004230",
    "20USBHX2004231",
    "20USBHX2004232",
    "20USBHX2004233",
    "20USBHX2004234",
    "20USBHX2004235",
    "20USBHX2004258",
    "20USBHX2004259",
    "20USBHX2004260",
    "20USBHX2004263",
    "20USBHX2004237",
    "20USBHX2004238",
    "20USBHX2004239",
    "20USBHX2004240",
    "20USBHX2004241",
    "20USBHX2004243",
    "20USBHX2004244",
    "20USBHX2004245",
    "20USBHX2004549",
    "20USBHX2004550",
    "20USBHX2004551",
    "20USBHX2004555",
    "20USBHX2004556",
    "20USBHX2004557",
    "20USBHX2004558",
    "20USBHX2004559",
    "20USBHX2004560",
    "20USBHX2004544",
    "20USBHX2004545",
    "20USBHX2004546",
    "20USBHX2004547",
    "20USBHX2004548",
    "20USBHX2004561",
    "20USBHX2004666",
    "20USBHX2004667",
    "20USBHX2004261",
    "20USBHX2004262",
    "20USBHX2004236",
    "20USBHX2004668",
    "20USBHX2004669",
    "20USBHX2004670",
    "20USBHX2004653",
    "20USBHX2004554",
    "20USBHX2004654",
    "20USBHX2004655",
    "20USBHX2004656",
    "20USBHX2004660",
    "20USBHX2004661",
    "20USBHX2004662",
    "20USBHX2004663",
    "20USBHX2004664",
    "20USBHX2004562",
    "20USBHX2004563",
    "20USBHX2004564",
    "20USBHX2004649",
    "20USBHX2004650",
    "20USBHX2004652",
    "20USBHX2004830",
    "20USBHX2004831",
    "20USBHX2004552",
    "20USBHX2004665",
    "20USBHX2004553",
    "20USBHX2004832",
    "20USBHX2004833",
    "20USBHX2004834",
    "20USBHX2004835",
    "20USBHX2004874",
    "20USBHX2004875",
    "20USBHX2004876",
    "20USBHX2004877",
    "20USBHX2004878",
    "20USBHX2004879",
    "20USBHX2004888",
    "20USBHX2004889",
    "20USBHX2004890",
    "20USBHX2004891",
    "20USBHX2004892",
    "20USBHX2004893",
    "20USBHX2004657",
    "20USBHX2004658",
    "20USBHX2004659",
    "20USBHX2004836",
    "20USBHX2004837",
    "20USBHX2004838",
    "20USBHX2004839",
    "20USBHX2004840",
    "20USBHX2004883",
    "20USBHX2004841",
    "20USBHX2004895",
    "20USBHX2004896",
    "20USBHX2004897",
    "20USBHX2004901",
    "20USBHX2004902",
    "20USBHX2004903",
    "20USBHX2004651",
    "20USBHX2004898",
    "20USBHX2004899",
    "20USBHX2004886",
    "20USBHX2004887",
    "20USBHX2004880",
    "20USBHX2004881",
    "20USBHX2004882",
    "20USBHX2004885",
    "20USBHX2004884",
    "20USBHX2004900",
    "20USBHX2005064",
    "20USBHX2005075",
    "20USBHX2005068",
    "20USBHX2005076",
    "20USBHX2005077",
    "20USBHX2005078",
    "20USBHX2005079",
    "20USBHX2005080",
    "20USBHX2005081",
    "20USBHX2004982",
    "20USBHX2004983",
    "20USBHX2004984",
    "20USBHX2004985",
    "20USBHX2004986",
    "20USBHX2004987",
    "20USBHX2005045",
    "20USBHX2005047",
    "20USBHX2005048",
    "20USBHX2005049",
    "20USBHX2005050",
    "20USBHX2005051",
    "20USBHX2005039",
    "20USBHX2005040",
    "20USBHX2005041",
    "20USBHX2005042",
    "20USBHX2005043",
    "20USBHX2005044",
    "20USBHX2005053",
    "20USBHX2005054",
    "20USBHX2005055",
    "20USBHX2005056",
    "20USBHX2005082",
    "20USBHX2005083",
    "20USBHX2005001",
    "20USBHX2005002",
    "20USBHX2005003",
    "20USBHX2005004",
    "20USBHX2005005",
    "20USBHX2005006",
    "20USBHX2004988",
    "20USBHX2004989",
    "20USBHX2004990",
    "20USBHX2004991",
    "20USBHX2004992",
    "20USBHX2004993",
    "20USBHX2004844",
    "20USBHX2004845",
    "20USBHX2004846",
    "20USBHX2004847",
    "20USBHX2004842",
    "20USBHX2004843",
    "20USBHX2004981",
    "20USBHX2004994",
    "20USBHX2005052",
    "20USBHX2004904",
    "20USBHX2004905",
    "20USBHX2004906",
    "20USBHX2005007",
    "20USBHX2005034",
    "20USBHX2005035",
    "20USBHX2005065",
    "20USBHX2005036",
    "20USBHX2005037",
    "20USBHX2005038",
    "20USBHX2005066",
    "20USBHX2005067",
    "20USBHX2005291",
    "20USBHX2005292",
    "20USBHX2005299",
    "20USBHX2005074",
    "20USBHX2005294",
    "20USBHX2005295",
    "20USBHX2005296",
    "20USBHX2005224",
    "20USBHX2005069",
    "20USBHX2005070",
    "20USBHX2005297",
    "20USBHX2005298",
    "20USBHX2005072",
    "20USBHX2005073",
    "20USBHX2005223",
    "20USBHX2005222",
    "20USBHX2005220",
    "20USBHX2005221",
    "20USBHX2005219",
    "20USBHX2005248",
    "20USBHX2005249",
    "20USBHX2005250",
    "20USBHX2005251",
    "20USBHX2005252",
    "20USBHX2005253",
    "20USBHX2005254",
    "20USBHX2005229",
    "20USBHX2005230",
    "20USBHX2005225",
    "20USBHX2005226",
    "20USBHX2005227",
    "20USBHX2005228",
    "20USBHX2005231",
    "20USBHX2005232",
    "20USBHX2005233",
    "20USBHX2005234",
    "20USBHX2005235",
    "20USBHX2005236",
    "20USBHX2005522",
    "20USBHX2005521",
    "20USBHX2005523",
    "20USBHX2005520",
    "20USBHX2005524",
    "20USBHX2005525",
    "20USBHX2005513",
    "20USBHX2005515",
    "20USBHX2005514",
    "20USBHX2005516",
    "20USBHX2005517",
    "20USBHX2005561",
    "20USBHX2005518",
    "20USBHX2005562",
    "20USBHX2005563",
    "20USBHX2005564",
    "20USBHX2005566",
    "20USBHX2005565",
    "20USBHX2005286",
    "20USBHX2005287",
    "20USBHX2005289",
    "20USBHX2005290",
    "20USBHX2005285",
    "20USBHX2005242",
    "20USBHX2005237",
    "20USBHX2005288",
    "20USBHX2005238",
    "20USBHX2005239",
    "20USBHX2005240",
    "20USBHX2005241",
    "20USBHX2005279",
    "20USBHX2005280",
    "20USBHX2005281",
    "20USBHX2005282",
    "20USBHX2005283",
    "20USBHX2005071",
    "20USBHX2004871",
    "20USBHX2004872",
    "20USBHX2004873",
    "20USBHX2004849",
    "20USBHX2004850",
    "20USBHX2004851",
    "20USBHX2005595",
    "20USBHX2005596",
    "20USBHX2005597",
    "20USBHX2005598",
    "20USBHX2005599",
    "20USBHX2005600",
    "20USBHX2005243",
    "20USBHX2005244",
    "20USBHX2005245",
    "20USBHX2005246",
    "20USBHX2005247",
    "20USBHX2005608",
    "20USBHX2004995",
    "20USBHX2004996",
    "20USBHX2004997",
    "20USBHX2004998",
    "20USBHX2004999",
    "20USBHX2005000",
    "20USBHX2005602",
    "20USBHX2005603",
    "20USBHX2005604",
    "20USBHX2005605",
    "20USBHX2005606",
    "20USBHX2005607",
    "20USBHX2005284",
]


def write_python_list(f, title, values):

    f.write(f"{title} = [\n")

    for serial in values:

        f.write(f'    "{serial}",\n')

    f.write("]\n\n")

passed = []

category_d_failed = []

category_e_ii_failed = []

# ============================================================

# Output directories

# ============================================================

base_output_dir = Path("UCSC")

hx_output_dir = base_output_dir / "HX"

hx_output_dir.mkdir(parents=True, exist_ok=True)

script_path = Path("get_test_run2.py").resolve()

# ============================================================

# Run modules

# ============================================================

for i, serial in enumerate(serial_numbers, start=1):

    print("=" * 80)

    print(f"[{i}/{len(serial_numbers)}] Running for {serial}")

    sn_serial = serial if serial.startswith("SN") else f"SN{serial}"

    final_module_dir = hx_output_dir / sn_serial

    temp_dir = hx_output_dir / f"temp_{sn_serial}"

    if temp_dir.exists():

        shutil.rmtree(temp_dir)

    temp_dir.mkdir(parents=True, exist_ok=True)

    try:

        result = subprocess.run(

            [

                "python",

                str(script_path),

                "--serial_number",

                serial,

                "--test_name",

                "Response Curve TC",

            ],

            check=False,

            capture_output=True,

            text=True,

            cwd=temp_dir,

        )

        print(result.stdout)

        if result.stderr:

            print(result.stderr)

        json_files = sorted(temp_dir.rglob("*.json"))

        if json_files:

            final_module_dir.mkdir(parents=True, exist_ok=True)

            moved_count = 0

            for item in json_files:

                target = final_module_dir / item.name

                if target.exists():

                    target.unlink()

                shutil.move(str(item), str(target))

                moved_count += 1

            if moved_count == 25:

                passed.append(serial)

                print(

                    f"✅ PASSED: {serial} — all 25 JSON files saved to {final_module_dir}"

                )

            else:

                category_d_failed.append(serial)

                print(

                    f"⚠️ CATEGORY D FAILURE: {serial} — incomplete data "

                    f"({moved_count}/25 JSON files), but folder was still saved to {final_module_dir}"

                )

        else:

            category_e_ii_failed.append(serial)

            print(

                f"❌ CATEGORY E(ii) FAILURE: {serial} — no JSON files were created"

            )

    except Exception as e:

        category_e_ii_failed.append(serial)

        print(

            f"❌ CATEGORY E(ii) FAILURE: {serial} — script crashed or could not be processed"

        )

        print(f"Error: {e}")

    finally:

        if temp_dir.exists():

            shutil.rmtree(temp_dir)

# ============================================================

# Summary page

# ============================================================

summary_path = hx_output_dir / "summary_page_ucsc_HX.txt"

with open(summary_path, "w") as f:

    f.write("=" * 80 + "\n")

    f.write("UCSC HX FINAL SUMMARY\n")

    f.write("=" * 80 + "\n\n")

    f.write(f"TOTAL MODULES CHECKED: {len(serial_numbers)}\n")

    f.write(f"PASSED MODULES 25/25 JSON FILES: {len(passed)}\n")

    f.write(f"CATEGORY D MODULES 1-24/25 JSON FILES: {len(category_d_failed)}\n")

    f.write(f"CATEGORY E(ii) MODULES 0/25 JSON FILES: {len(category_e_ii_failed)}\n\n")

    write_python_list(f, "passed_modules", passed)

    write_python_list(f, "category_d_modules", category_d_failed)

    write_python_list(f, "category_e_ii_modules", category_e_ii_failed)

print("\n" + "=" * 80)

print("UCSC HX FINAL SUMMARY")

print("=" * 80)

print(f"\n✅ PASSED MODULES 25/25 JSON FILES ({len(passed)}):")

for serial in passed:

    print(f"  ✅ {serial}")

print(f"\n⚠️ CATEGORY D MODULES 1-24/25 JSON FILES ({len(category_d_failed)}):")

for serial in category_d_failed:

    print(f"  ⚠️ {serial}")

print(f"\n❌ CATEGORY E(ii) MODULES 0/25 JSON FILES ({len(category_e_ii_failed)}):")

for serial in category_e_ii_failed:

    print(f"  ❌ {serial}")

print(f"\n📄 Summary saved to: {summary_path}")

print(f"📁 HX modules saved inside: {hx_output_dir}")