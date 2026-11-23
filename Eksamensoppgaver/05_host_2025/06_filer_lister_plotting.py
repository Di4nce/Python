# Gitt en serie med målinger fra en strøm-måler lagret på følgende format: MålerID; Dato; Klokkeslett; Verdi
# M1; 2025-11-20; 01.00.00; 7.3
# M1; 2025-11-20; 01.10.00; 8.9
# M1; 2025-11-20; 01.20.00; 12.3
# M1; 2025-11-20; 01.30.00; 11.8
# M1; 2025-11-20; 01.40.00; 13.7

# Merk at ditt script skal lese ei fil som er betydelig lengre enn denne, dette er bare et lite utdrag slik
# at du ser formatet

# Du kan anta at fila heter "strommalinger.txt" og ligger i samme mappe som ditt Python script.
# Oppgaven som helhet går ut på å lese inn, regne ut gjennomsnitt, og plotte verdiene på y-aksen
# med tidspunkt (dato og klokkeslett) på x-aksen. Du kan anta at alle målingene har samme målerID
# og derfor ignorere denne kolonnen i CSV-fila.

# Skriv et Python-script som gjør følgende:
# 1. Leser inn dato, klokkeslett og verdi for alle linjene. Lag datetime objekter for dato og
# klokkeslett. Legg datetime objektene og verdiene i hver sine lister. (5%)
# 2. Regner ut maksimal, minimal og gjennomsnittlig verdi og skriver dette ut. (3%)
# 3. Plott tidspunkt og verdi med Matplotlib. (3%)
# 4. Håndter feil som kan skje når man leser fila: feil filnavn og andre feil i selve fillesingen skal
# håndteres ved å skrive ut en forståelig feilmelding, feil dataformat i ei linje skal håndteres
# ved å hoppe over linja og skrive ut at det er en feil i den linja. (3%)

# Skriv svaret ditt her. Endringer blir lagret automatisk.