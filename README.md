# Individuell uppgift - Hälsostudie

Ett skolprojekt med syftet att analysera och visualisera data från en fiktiv hälsostudie. 

## Beskrivning

Jag, en fiktiv dataanalytiker på ett forskningsinstitut, Fejk Forskning<sup>™</sup>, har fått i uppdrag att analysera data från en hälsostudie som institutet har bedrivit. 

Studien har sammanställt 800 deltagares ålder, kön, vikt, längd, blodtryck, kolesterolnivå, rökvanor och om de har en viss sjukdom. 

Mitt uppdrag är att undersöka relationen mellan blodtryck och rökning. 

Uppgiften är indelad i två delar: Del 1 Grundläggande analys och statistik och Del 2 Fördjupning och pipeline. 

VIKTIGT: ALLT ARBETE LIGGER I BRANCH del1, inte i main.

Del 1 består av:

* Dataförberedelse och "Rengöring"
* Beskrivande analys
* Simulering kopplad till caset
* Beräkning av konfidensintervall
* Hypotesprövning: "Rökare har högre medel-blodtryck än icke-rökare"
* Statistical Power

## Innehåll i Notebook:en 

### Dataförberedelse och "Rengöring" 

* Importerar de bibliotek som behövs 
* Läser in datasetet health_study_dataset.csv 
* Undersöker om datasetet saknar värden, har dubbletter, vilka dtypes det kommer med 
* Ändrar dtypes 

### Beskrivande analys

* Sammanställer nyckeltal (min, max, medel, median för ålder, längd, vikt, blodtryck och kolesterol)
* Skapar diverse relevanta plottar (histogram, boxplot, stapeldiagram och spridningsdiagram) med både matplotlib och seaborn 

### Simulering kopplad till caset

* Slumpar fram 1000 personer med samma risk för sjukdom som deltagarna i studien 
* Detta görs med numpy.random.choice()

### Beräkning av konfidensintervall

* Med normalapproximation 
* Med bootstrap: använder bl.a. numpy.random.choice och numpy.empty för att skapa en "slumpgenerator-fabrik" 

### Hypotesprövning 

* Standard t-test och Welch-style t-test
    * Beräknar t-statistik och p-värde med scipy.stats.ttest_ind()
* Permutationstest
    * Använder numpy.random.permutation() i "slumpgenerator-fabriken" och numpy.concatenate() för att skapa ett gemensamt urval

### Statistical Power 

* Skapar en funktion för att beräkna power vid olika hypotetiska skillnader 
* Funktionen beräknar styrka utifrån en kombination av numpy.random.normal() och scipy.stats.ttest_ind() i en for-loop. 

## Installation

Python version 3.13.7 

1. Klona projektet från Github: 

git clone https://github.com/josefinoleryd/Individuell-uppgift-Health_Study.git

2. Installera nödvändiga paket: 

pip install -r requirements.twt

## Hur man kör 

När du har installerat alla paket enligt installationsavsnittet:

1. Öppna projektet i VS Code 

2. Byt till branch del1

git checkout del1 

3. Öppna rapport.ipynb 

4. Klicka på "Run All"

5. Bob's your uncle! 

## Teknikstack

* Dataanalys och beräkningar: pandas, numpy och scipy
* Visualisering: matplotlib och seaborn
* Rapport: Jupyter Notebook