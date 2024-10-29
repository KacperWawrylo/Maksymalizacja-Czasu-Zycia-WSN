# Maksymalizacja Żywotności WSN

Projekt ten implementuje narzędzie do zarządzania i symulacji Bezprzewodowych Sieci Sensorowych (WSN), którego celem jest maksymalizacja żywotności sieci poprzez optymalizację aktywnych sensorów. Aplikacja zawiera interfejs graficzny do wizualizacji sieci sensorów i celów, a także funkcje generowania sieci, optymalizacji aktywności sensorów i symulacji działania sieci w czasie.

## Funkcje

- **Interfejs Graficzny**: Zbudowany przy użyciu `tkinter`, umożliwiający interaktywną wizualizację sensorów i celów w obrębie zdefiniowanego obszaru.
- **Zarządzanie Sensorami i Celami**: Umieszczanie sensorów i celów w konfigurowalnym obszarze, gdzie każdy sensor ma określony zasięg i żywotność baterii.
- **Optymalizacja Sieci**: Automatyczna optymalizacja aktywnych sensorów w celu maksymalizacji pokrycia i wydłużenia żywotności sieci.
- **Symulacja**: Symulacja działania sieci w czasie, z wizualizacją aktywnych sensorów oraz pokrycia sieci, wraz z analizą graficzną.
- **Wykresy**: Generowanie wykresów, które pokazują liczbę aktywnych sensorów oraz procent pokrycia celów w czasie za pomocą `matplotlib`.

## Struktura Projektu

- **`main.py`**: Inicjalizuje interfejs GUI, zarządza generowaniem sieci, optymalizacją oraz symulacją.
- **`sensor.py`**: Definiuje klasę `Sensor`, z atrybutami jak współrzędne `x`, `y`, zasięg, żywotność oraz metodami do monitorowania celów i zmniejszania żywotności.
- **`target.py`**: Definiuje klasę `Target`, reprezentującą punkty, które mają być monitorowane przez sensory.
- **`region.py`**: Definiuje klasę `Region`, przechowującą sensory i cele oraz optymalizującą ich użycie dla maksymalnego pokrycia.
- **`simulation_data.py`**: Zbiera i przechowuje dane symulacji, takie jak kroki czasowe, liczba aktywnych sensorów oraz procent pokrycia.

## Instalacja

### Wymagania

Upewnij się, że masz zainstalowany `matplotlib` do generowania wykresów:

```bash
pip install -r requirements.txt
