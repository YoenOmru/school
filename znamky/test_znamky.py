"""Testy k úloze Známky studenta.

Testuje funkce ze souboru znamky.py (tvoje řešení), který musí ležet
ve stejné složce. Spusť:

    python test_znamky.py        # vypíše OK / CHYBA pro každý krok
    python -m pytest             # funguje i s pytestem

Testy jsou po krocích - dokud funkci pro daný krok nemáš, jeho test
selže, ale ostatní kroky se otestují normálně. U chyby test vypíše,
co volal, co čekal, co dostal a čeho si všimnout.
"""

import os
import re
import tempfile
import traceback

STUDENT_FILE = "znamky.py"


# ---------------------------------------------------------------------------
# Pomocné funkce testů
# ---------------------------------------------------------------------------

def _tmp_file(text):
    """Vytvoří dočasný soubor s daným obsahem a vrátí jeho cestu."""
    fd, path = tempfile.mkstemp(suffix=".txt", text=True)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def _equal(a, b):
    """Porovnání, které u desetinných čísel toleruje drobnou nepřesnost."""
    if isinstance(a, float) or isinstance(b, float):
        return (isinstance(a, (int, float)) and isinstance(b, (int, float))
                and not isinstance(a, bool) and abs(a - b) < 1e-9)
    if type(a) != type(b):
        return False
    if isinstance(a, (list, tuple)):
        return len(a) == len(b) and all(_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(_equal(a[k], b[k]) for k in a)
    return a == b


def _type_name(value):
    return type(value).__name__


def _generic_hints(actual, expected):
    """Obecné nápovědy podle toho, jak se výsledek liší."""
    hints = []
    if actual is None and expected is not None:
        hints.append("Funkce vrátila None - nechybí na konci 'return'?")
    elif type(actual) != type(expected) and not (
            isinstance(actual, (int, float)) and isinstance(expected, (int, float))):
        hints.append(f"Funkce má vracet {_type_name(expected)}, "
                     f"ale vrátila {_type_name(actual)}.")
    elif isinstance(expected, (list, tuple, dict)) and len(actual) != len(expected):
        hints.append(f"Očekávaný počet prvků je {len(expected)}, vrácený {len(actual)}.")
    return hints


def check(actual, expected, call, hints=(), file_text=None):
    """Když se actual liší od expected, vyhodí AssertionError se srozumitelnou zprávou.

    call      - jak byla funkce zavolána (text pro výpis)
    hints     - seznam dvojic (podmínka(actual) -> bool, text nápovědy)
    file_text - obsah testovacího souboru, pokud funkce četla soubor
    """
    if _equal(actual, expected):
        return
    lines = [f"Volání:    {call}"]
    if file_text is not None:
        lines.append("Soubor obsahoval (řádek po řádku):")
        for line in file_text.splitlines():
            lines.append(f"             {line!r}")
    lines.append(f"Očekáváno: {expected!r}")
    lines.append(f"Vráceno:   {actual!r}")
    found = _generic_hints(actual, expected)
    for condition, text in hints:
        try:
            if condition(actual):
                found.append(text)
        except Exception:
            pass
    for text in found:
        lines.append(f"Nápověda:  {text}")
    raise AssertionError("\n".join(lines))


def check_text_file(actual, expected, what):
    """Porovná obsah dvou textových souborů a ukáže první rozdílný řádek."""
    if actual == expected:
        return
    act_lines = actual.split("\n")
    exp_lines = expected.split("\n")
    lines = [f"{what} se liší od očekávaného."]
    if actual.rstrip("\n") == expected.rstrip("\n"):
        lines.append("Obsah sedí, liší se jen '\\n' na konci souboru - "
                     "každý řádek (i poslední) má končit '\\n'.")
        raise AssertionError("\n".join(lines))
    if sorted(act_lines) == sorted(exp_lines):
        lines.append("Nápověda:  všechny řádky jsou správně, jen v jiném pořadí "
                     "- nezapomněl jsi seřadit (sorted)?")
    for i in range(max(len(act_lines), len(exp_lines))):
        a = act_lines[i] if i < len(act_lines) else "<konec souboru>"
        e = exp_lines[i] if i < len(exp_lines) else "<konec souboru>"
        if a != e:
            lines.append(f"První rozdíl je na řádku {i + 1}:")
            lines.append(f"  očekáváno: {e!r}")
            lines.append(f"  zapsáno:   {a!r}")
            if a.strip() == e.strip():
                lines.append("Nápověda:  liší se jen mezery nebo konec řádku ('\\n').")
            elif a == "<konec souboru>":
                lines.append("Nápověda:  soubor je kratší - nezapsal jsi všechno (nebo chybí '\\n')?")
            if i > 0:
                lines.append("Řádky před rozdílem (shodné):")
                lines += ["  " + line for line in exp_lines[max(0, i - 3):i]]
            break
    if len(exp_lines) <= 15:
        lines.append("Celý očekávaný obsah:")
        lines += ["  " + line for line in expected.rstrip("\n").split("\n")]
        lines.append("Celý zapsaný obsah:")
        if actual == "":
            lines.append("  <prázdný soubor>")
        else:
            lines += ["  " + line for line in actual.rstrip("\n").split("\n")]
    raise AssertionError("\n".join(lines))


# ---------------------------------------------------------------------------
# Testy
# ---------------------------------------------------------------------------

def test_krok1_read_lines():
    from znamky import read_lines
    text = "Math:1,2\n\n  Physics:3  \n\n"
    path = _tmp_file(text)
    try:
        actual = read_lines(path)
    finally:
        os.remove(path)
    check(actual, ["Math:1,2", "Physics:3"], "read_lines(soubor)", [
        (lambda r: any(s.endswith("\n") for s in r),
         "Řádky končí znakem '\\n' - použij strip()."),
        (lambda r: any(s != s.strip() for s in r),
         "Některý řádek má mezery na začátku/konci - použij strip()."),
        (lambda r: "" in r,
         "Seznam obsahuje prázdné řetězce - prázdné řádky nepřidávej."),
    ], file_text=text)


def test_krok2_parse_line():
    from znamky import parse_line
    hints = [
        (lambda r: isinstance(r[1][0], str),
         "Známky jsou řetězce ('1'), ne čísla (1) - převeď je pomocí int()."),
        (lambda r: isinstance(r, list),
         "Vracej dvojici (tuple): return subject, grades"),
        (lambda r: ":" in r[0],
         "V názvu předmětu zůstala dvojtečka - použij split(':')."),
    ]
    check(parse_line("Math:1,2,1,3"), ("Math", [1, 2, 1, 3]),
          'parse_line("Math:1,2,1,3")', hints)
    check(parse_line("PE:1"), ("PE", [1]), 'parse_line("PE:1")', hints)


def test_krok3_average():
    from znamky import average
    check(average([1, 2, 3]), 2.0, "average([1, 2, 3])")
    check(average([1, 2]), 1.5, "average([1, 2])", [
        (lambda r: r == 1, "Vyšlo celé číslo - nepoužil jsi // místo / ?"),
    ])
    check(average([4]), 4.0, "average([4])")
    try:
        result = average([])
    except ZeroDivisionError:
        raise AssertionError(
            "Volání:    average([])\n"
            "Očekáváno: None\n"
            "Vráceno:   pád programu ZeroDivisionError (dělení nulou)\n"
            "Nápověda:  prázdný seznam ošetři před dělením: if len(values) == 0: return None")
    check(result, None, "average([])", [
        (lambda r: r == 0, "Pro prázdný seznam vracej None, ne 0."),
    ])


def test_krok4_load_grades():
    from znamky import load_grades
    text = "Math:1,2\nPhysics:3,3\n\nMath:5\n"
    path = _tmp_file(text)
    try:
        actual = load_grades(path)
    finally:
        os.remove(path)
    check(actual, {"Math": [1, 2, 5], "Physics": [3, 3]}, "load_grades(soubor)", [
        (lambda r: r.get("Math") == [5],
         "Druhý řádek Math přepsal první - známky k existujícímu seznamu přidej (extend)."),
        (lambda r: r.get("Math") == [[1, 2], [5]],
         "Místo extend jsi použil append - vznikl seznam seznamů."),
    ], file_text=text)


def test_krok5_averages():
    from znamky import compute_averages, overall_average
    grades = {"Math": [1, 2], "PE": [1, 1, 1], "Czech": [3]}
    call = f"compute_averages({grades})"
    check(compute_averages(grades), {"Math": 1.5, "PE": 1.0, "Czech": 3.0}, call)
    check(grades, {"Math": [1, 2], "PE": [1, 1, 1], "Czech": [3]},
          call + "  # obsah vstupního slovníku po volání", [
              (lambda r: True, "Funkce změnila vstupní slovník - vytvoř a vrať NOVÝ slovník."),
          ])
    averages = {"Math": 1.5, "PE": 1.0, "Czech": 3.0}
    check(overall_average(averages), 5.5 / 3, f"overall_average({averages})")


def test_krok6_write_report():
    from znamky import write_report
    fd, path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    try:
        averages = {"PE": 1.0, "Math": 1.5, "Czech": 3.0}
        result = write_report(path, averages, 5.5 / 3)
        with open(path, encoding="utf-8") as f:
            content = f.read()
    finally:
        os.remove(path)
    check_text_file(content,
                    "Czech: 3.00\n"
                    "Math: 1.50\n"
                    "PE: 1.00\n"
                    "Overall: 1.83\n",
                    f"Soubor zapsaný voláním write_report(soubor, {averages}, 1.8333...)")


def test_cely_program():
    """Porovná výstup pro znamky.txt se souborem vysledky_ocekavane.txt."""
    from znamky import main
    here = os.path.dirname(os.path.abspath(__file__))
    fd, out = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    try:
        main(os.path.join(here, "znamky.txt"), out)
        with open(out, encoding="utf-8") as f:
            actual = f.read()
    finally:
        os.remove(out)
    with open(os.path.join(here, "vysledky_ocekavane.txt"), encoding="utf-8") as f:
        expected = f.read()
    check_text_file(actual, expected,
                    "Výstup main('znamky.txt', ...) porovnaný s vysledky_ocekavane.txt")


# ---------------------------------------------------------------------------
# Spouštění bez pytestu
# ---------------------------------------------------------------------------

def _student_frames(exc):
    """Řádky tracebacku, které leží ve studentově souboru."""
    frames = traceback.extract_tb(exc.__traceback__)
    return [f"{os.path.basename(fr.filename)}, řádek {fr.lineno}: {fr.line}"
            for fr in frames if os.path.basename(fr.filename) == STUDENT_FILE]


def _test_call(exc):
    """Poslední řádek testu, který vedl k pádu (co test zrovna volal)."""
    this_file = os.path.basename(__file__)
    frames = [fr for fr in traceback.extract_tb(exc.__traceback__)
              if os.path.basename(fr.filename) == this_file]
    return frames[-1].line if frames else None


def _indent(text):
    return "\n".join("       " + line for line in str(text).split("\n"))


if __name__ == "__main__":
    tests = [value for name, value in list(globals().items())
             if name.startswith("test_") and callable(value)]
    passed = 0
    for test in tests:
        try:
            test()
            print(f"OK     {test.__name__}")
            passed += 1
            continue
        except ModuleNotFoundError as e:
            print(f"CHYBÍ  {test.__name__}")
            print(_indent(f"Soubor {e.name}.py nebyl nalezen - musí ležet ve stejné složce jako testy."))
        except ImportError as e:
            match = re.search(r"cannot import name '(\w+)' from '(\w+)'", str(e))
            print(f"CHYBÍ  {test.__name__}")
            if match:
                print(_indent(f"V souboru {match.group(2)}.py není funkce {match.group(1)} "
                              "- ještě jsi ji nenapsal, nebo se jmenuje jinak."))
            else:
                print(_indent(e))
        except AssertionError as e:
            print(f"CHYBA  {test.__name__}")
            print(_indent(e))
        except Exception as e:
            print(f"PÁD    {test.__name__}")
            print(_indent(f"Tvůj kód spadl s chybou {type(e).__name__}: {e}"))
            call = _test_call(e)
            if call:
                print(_indent(f"Test právě volal:  {call}"))
            for line in _student_frames(e):
                print(_indent(f"  v {line}"))
        print()
    print(f"{passed}/{len(tests)} testů prošlo")
