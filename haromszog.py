import math

class HaromszogSzamitasok:
    def haromszog_terulet(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            print("Hiba: A háromszög nem érvényes.")
            return None

        s = (a + b + c) / 2

        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def haromszog_kerulet(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            print("Hiba: A háromszög nem érvényes.")
            return None

        return a + b + c

    def feladatmegoldo(self, a, b, c):
        print(f"A háromszög oldalai: a = {a}, b = {b}, c = {c}")

        perimeter = self.haromszog_kerulet(a, b, c)
        area = self.haromszog_terulet(a, b, c)

        if perimeter is not None and area is not None:
            print(f"A háromszög kerülete: {perimeter:.2f}")
            print(f"A háromszög területe: {area:.2f}")
        else:
            print("A háromszög adatai nem helyesek, a számítás sikertelen.")

if __name__ == "__main__":
    szamitas = HaromszogSzamitasok
    a, b, c = 3, 4, 5  # Itt adhatsz meg más értékeket is
    szamitas.feladatmegoldo(a, b, c)
