import csv
from operator import attrgetter

class Strumenti:
    def __init__(self, idStr, tipo, marca, anno_acquisto, valore):
        self.idStr = idStr
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"{self.idStr}, {self.tipo}, {self.marca}, {self.anno_acquisto}, {self.valore}"


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumentiMagazzino = []
        self.strumentiPrestati = {}

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        with open(file_path) as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            next(csvReader)
            for righe in csvReader:
                self.aggiungi_strumento(righe[0], righe[1], righe[2], righe[3], righe[4])

    def aggiungi_strumento(self, idStr, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        strumenti = Strumenti(idStr, tipo, marca, anno_acquisto, valore)
        self.strumentiMagazzino.append(strumenti)
        return strumenti


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        strumenti_ordinati = sorted(self.strumentiMagazzino, key=attrgetter("marca"))
        return strumenti_ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        if str(id_strumento) in self.strumentiPrestati:
            return "Strumento non disponibile"
        for s in self.strumentiMagazzino:
            if str(s.idStr) == str(id_strumento):
                self.strumentiPrestati[str(id_strumento)] = [cognome_allievo, data]
                return f"Prestito avvenuto con successo per {str(id_strumento)}, {self.strumentiPrestati[str(id_strumento)][0]}"
        return "Id non valido"


    def termina_prestito(self, id_prestato):
        """Termina un prestito in atto"""
        # TODO
        if str(id_prestato) in self.strumentiPrestati:
            self.strumentiPrestati.pop(str(id_prestato))
            return f"Prestito terminato per {id_prestato}"
        return "Id non valido"
