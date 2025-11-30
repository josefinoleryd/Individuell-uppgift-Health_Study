# Individuell uppgift - Hälsostudie

Ett skolprojekt med syftet att analysera och visualisera data från en fiktiv hälsostudie. 

## Beskrivning

Jag, en fiktiv dataanalytiker på ett forskningsinstitut, Fejk Forskning<sup>™</sup>, har fått i uppdrag att analysera data från en hälsostudie som institutet har bedrivit. 

Studien har sammanställt 800 deltagares ålder, kön, vikt, längd, blodtryck, kolesterolnivå, rökvanor och om de har en viss sjukdom. 

Mitt uppdrag är att undersöka relationen mellan blodtryck och rökning. 

Uppgiften är indelad i två delar: Del 1 Grundläggande analys och statistik och Del 2 Fördjupning och pipeline. 

VIKTIGT: ALLT ARBETE MED DEL 1 LIGGER I BRANCH del1 och ALLT ARBETE MED DEL 2 LIGGER I BRANCH del2. 

Det som är exakt likadant som i Del 1 är märkt EXAKT LIKADANT SOM I DEL 1

* i kodblock: <span style="color: green;"># EXAKT LIKADANT SOM I DEL 1:</span>
* i markdown: <mark>EXAKT LIKADANT SOM I DEL 1:</mark>

Denna README gäller främst Del 2

Del 2 består, utöver tidigare arbete med Del 1, av:

* Funktioner och moduler
* Fördjupad analys (linjär regression)
* Förbättringsförslag och vidare arbete 

## Funktioner

### Modulen health_utils.py

Här ligger funktionen load_and_prep_data som, mycket riktigt, läser in datan från en csv-fil och städar den 

Här ligger också klassen HealthAnalyzer som har följande metoder: 

* get_stats: beräknar min, max, medel och median för valfria kolumner 
* plot_ hist: ritar ett histogram över valfri kolumn
* plot_bar: ritar ett stapeldiagram över valfri kolumn 
    * kan hantera namnbyte (från 1 och 0 till Yes och No) och procent istället för antal
* calc_confidence_interval: beräknar konfidensintervall med Bootstrap-metoden för given kolumn (endast numerisk)
    * antal simuleringar och 95% konfidensintervall är default, men kan ändras vid behov

## Fördjupad analys (linjär regression)

* En modell som ska förutsäga blodtryck med hjälp av multipel linjär regression (scikit-learn och LinearRegression)
* En visuell presentation av modellens prognos jämfört med stuidens faktiska data

## Slutsats 

* Modellen sög

## Förbättringsförslag & Vidare Arbete

* Lägga in koden för den linjära regressionen i en funktion så det går att beräkna med andra variabler än vikt och rökvanor 
* Testa hur bra modellen är: 
    * sklearn.model_selection.train_test_split
    * sklearn.model_selection.cross_val_score
* PCA (Principal Component Analysis)

## Installation och hur man kör

Python version 3.13.7 

1. Klona projektet från Github: 

git clone https://github.com/josefinoleryd/Individuell-uppgift-Health_Study.git

2. Byt till branch del2 

git checkout del2

3. Installera nödvändiga paket: 

pip install -r requirements.txt

4. Öppna rapport.ipynb 

5. Klicka på "Run All"

6. Easy as pie

## Teknikstack

* Dataanalys och beräkningar: pandas, numpy, scipy, scikit-learn
* Visualisering: matplotlib och seaborn
* Rapport: Jupyter Notebook