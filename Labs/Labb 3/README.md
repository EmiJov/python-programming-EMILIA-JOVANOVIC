# Labb 3 - Linjär klassificering

Detta program läser in punkter från 'unlabelled_data.csv', klassificerar dem med hjälp av en linjär gräns, och sparar resultatet i en ny fil 'labelled_data.csv'. Programmet ritar även en graf där punkterna färgas efter klass och den valda linjen visas.

## Vad programmet gör
- Läser in punkter från en CSV-fil
- Testar olika m‑värden
- Klassificerar punkterna som 0 eller 1 beroende på om de ligger ovanför eller under linjen
- Skapar en ny fil 'labelled_data.csv' med tre kolumner: 'x', 'y', 'label'
- Visar en graf där punkterna färgas efter klass och linjen ritas ut

## Val av linje
Jag testade flera olika m‑värden och valde till slut linjen **y = -x** (k = -1, m = 0).  
Motiveringen är att punkterna i datamängden ligger i två tydliga kluster, ungefär symmetriskt kring diagonalen. Linjen 'y = -x' delar dessa kluster på ett naturligt sätt och ger en jämn fördelning av punkterna på vardera sida.

## Användning
1. Placera filen 'unlabelled_data.csv' i mappen 'Labs/Labb 3/'.
2. Kör programmet i terminalen: python labb3.py
3. Programmet skapar en ny fil 'labelled_data.csv' med en extra kolumn 'label'.
4. En graf öppnas där punkterna färgas efter klass och linjen ritas ut.