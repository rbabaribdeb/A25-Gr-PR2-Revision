import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QApplication, QLineEdit, QHBoxLayout, QPushButton

class ListeJoueur(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste de joueur")
        self.setMinimumWidth(600)

        # Layout
        main_fenetre = QVBoxLayout()
        grid = QGridLayout()

        # Titre
        titre = QLabel("Liste de joueurs")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titre.setStyleSheet("font-size: 42px; font-weight: bold; background-color: grey; color: red; border-radius: 12px;")

        main_fenetre.addWidget(titre)
        main_fenetre.addSpacing(20)

        # Joueur Edits
        self.nom_edits = []
        self.point_edits = []

        for i in range(4):
            label_joueur = QLabel(f"Joueur #{i+1}")

            nom_edit = QLineEdit()
            nom_edit.setPlaceholderText("Nom du joueur")

            point_edit = QLineEdit()
            point_edit.setFixedWidth(80)
            point_edit.setPlaceholderText("0")

            self.nom_edits.append(nom_edit)
            self.point_edits.append(point_edit)

            grid.addWidget(label_joueur, i, 0)
            grid.addWidget(nom_edit, i, 1)
            grid.addWidget(point_edit, i, 2)

        main_fenetre.addLayout(grid)

        # Résultat
        self.total_label = QLabel("Total des points : 0")
        self.moyenne_label = QLabel("Moyenne : 0")
        self.gagnant_label = QLabel("Gagnant : -")

        stats_grid = QGridLayout()
        stats_grid.addWidget(self.total_label, 0, 0)
        stats_grid.addWidget(self.moyenne_label, 0, 1)
        stats_grid.addWidget(self.gagnant_label, 1, 0)

        main_fenetre.addSpacing(15)
        main_fenetre.addLayout(stats_grid)

        # Buttons
        btn_layout = QHBoxLayout()

        self.btn_charger = QPushButton("Charger résultats")
        self.btn_sauvegarde = QPushButton("Sauvegarder résultats")
        self.btn_analyse = QPushButton("Analyser résultats")

        btn_layout.addWidget(self.btn_charger)
        btn_layout.addWidget(self.btn_sauvegarde)
        btn_layout.addWidget(self.btn_analyse)

        main_fenetre.addSpacing(20)
        main_fenetre.addLayout(btn_layout)

        self.btn_analyse.clicked.connect(self.analyse_resultat)
        self.btn_sauvegarde.clicked.connect(self.sauvegarde_resultat)

        self.setLayout(main_fenetre)


    def analyse_resultat(self):
        totale = 0
        nom_gagnant = "-"
        score_gagnant = -1

        for name_edit, points_edit in zip(self.nom_edits, self.point_edits):
            name = name_edit.text().strip()
            try:
                score = int(points_edit.text())
            except ValueError:
                score = 0

            totale += score

            if score > score_gagnant:
                score_gagnant = score
                nom_gagnant = name

        avg = totale / 4 if totale else 0

        self.total_label.setText(f"Total des points : {totale}")
        self.moyenne_label.setText(f"Moyenne : {avg:.1f}")
        self.gagnant_label.setText(f"Gagnant : {nom_gagnant}")


    def sauvegarde_resultat(self):

        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListeJoueur()
    window.show()
    sys.exit(app.exec())