# core_achievement_tracker.py - System osiągnięć FIROS

import json
from datetime import datetime

class Achievement:
    def __init__(self, id, title, description, reward_xp=0, reward_rfm=0):
        self.id = id
        self.title = title
        self.description = description
        self.reward_xp = reward_xp
        self.reward_rfm = reward_rfm

class AchievementTracker:
    def __init__(self, player_id):
        self.player_id = player_id
        self.unlocked = []
        self.filename = f"save/{player_id}_achievements.json"

    def unlock(self, achievement_id):
        if achievement_id not in self.unlocked:
            self.unlocked.append(achievement_id)
            print(f"[Osiągnięcie odblokowane] ID: {achievement_id}")

    def has_achievement(self, achievement_id):
        return achievement_id in self.unlocked

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.unlocked = data.get("unlocked", [])
        except FileNotFoundError:
            self.unlocked = []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump({
                "player_id": self.player_id,
                "unlocked": self.unlocked,
                "saved_at": datetime.utcnow().isoformat()
            }, f, indent=4)

class AchievementSystem:
    def __init__(self):
        self.achievements = self._load_achievements()

    def _load_achievements(self):
        return {
            1:  Achievement(1,  "Pierwsza Krew", "Wygraj swoją pierwszą bitwę", 100, 5),
            2:  Achievement(2,  "Pogromca Potworów", "Pokonaj 10 potworów", 200, 10),
            3:  Achievement(3,  "Uczeń Magii", "Użyj pierwszego zaklęcia", 50, 0),
            4:  Achievement(4,  "Zdobywca Ziem", "Odwiedź 5 różnych regionów", 150, 10),
            5:  Achievement(5,  "Zbieracz Artefaktów", "Zdobądź 3 unikalne artefakty", 250, 20),
            6:  Achievement(6,  "Mistrz Rzemiosła", "Wykonaj 5 mikstur", 100, 10),
            7:  Achievement(7,  "Handlarz", "Sprzedaj przedmiot na rynku", 50, 3),
            8:  Achievement(8,  "Bractwo Krwi", "Dołącz do Gildii", 100, 10),
            9:  Achievement(9,  "Elita PvP", "Wygraj 3 walki PvP", 300, 15),
            10: Achievement(10, "Odkrywca", "Odkryj sekretną lokację", 180, 0),
            11: Achievement(11, "Uczeń Run", "Pozyskaj runę", 70, 2),
            12: Achievement(12, "Zabójca Cieni", "Pokonaj przeciwnika frakcji Cieni", 160, 8),
            13: Achievement(13, "Tropiciel", "Zbadaj 3 ruiny", 120, 4),
            14: Achievement(14, "Szlachcic", "Zgromadź 1000 RFM", 0, 0),
            15: Achievement(15, "Mistrz Strategii", "Wygraj szachy magiczne", 300, 25),
            16: Achievement(16, "Władca Podziemi", "Pokonaj bossa w lochu", 400, 35),
            17: Achievement(17, "Zakon Wtajemniczonych", "Ukończ rytuał", 80, 10),
            18: Achievement(18, "Zguba Wilka", "Pokonaj wilka alfa", 90, 6),
            19: Achievement(19, "Oko Smoka", "Zdobądź łuskę smoka", 300, 50),
            20: Achievement(20, "Cichy Skrytobójca", "Wykonaj misję bez wykrycia", 200, 12),
            21: Achievement(21, "Wiedza to Potęga", "Odczytaj 10 ksiąg", 150, 0),
            22: Achievement(22, "Wódz", "Poprowadź drużynę w dungeonie", 220, 20),
            23: Achievement(23, "Błyskawiczna Śmierć", "Pokonaj przeciwnika w jednej turze", 250, 15),
            24: Achievement(24, "Kolekcjoner Kart", "Zdobądź 30 kart NFT", 100, 30),
            25: Achievement(25, "Weteran", "Spędź 20h w grze", 300, 0),
            26: Achievement(26, "Strażnik Balansu", "Zatrzymaj konflikt frakcji", 200, 10),
            27: Achievement(27, "Głos Gildii", "Weź udział w głosowaniu gildyjnym", 100, 8),
            28: Achievement(28, "Zasłużony", "Zdobądź 10 odznaczeń", 180, 15),
            29: Achievement(29, "Rytuał Zjednoczenia", "Zakończ misję frakcyjną", 300, 25),
            30: Achievement(30, "Legenda FIROS", "Zostań w Top 10 rankingu", 1000, 100),
        }

    def get_achievement(self, achievement_id):
        return self.achievements.get(achievement_id)

    def list_all(self):
        return list(self.achievements.values())

    def describe(self):
        print("🎖 Lista osiągnięć:")
        for ach in self.achievements.values():
            print(f"{ach.id}. {ach.title} - {ach.description} [+{ach.reward_xp}XP, +{ach.reward_rfm} RFM]")
