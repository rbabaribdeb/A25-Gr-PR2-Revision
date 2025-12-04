import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout,
    QFileDialog
)
from PyQt6.QtCore import Qt


class PlayerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste des joueurs")
        self.setMinimumWidth(600)

        # --- Main layout ---
        main_layout = QVBoxLayout()
        grid = QGridLayout()

        # Title
        title = QLabel("Liste des joueurs")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")

        main_layout.addWidget(title)
        main_layout.addSpacing(20)

        # --- Player fields ---
        self.name_edits = []
        self.points_edits = []

        for i in range(4):
            lbl_player = QLabel(f"Joueur #{i+1}")

            name_edit = QLineEdit()
            name_edit.setPlaceholderText("Nom du joueur")

            points_edit = QLineEdit()
            points_edit.setFixedWidth(80)
            points_edit.setPlaceholderText("0")

            self.name_edits.append(name_edit)
            self.points_edits.append(points_edit)

            grid.addWidget(lbl_player, i, 0)
            grid.addWidget(name_edit, i, 1)
            grid.addWidget(points_edit, i, 2)

        main_layout.addLayout(grid)

        # --- Results section ---
        self.total_label = QLabel("Total des points : 0")
        self.avg_label = QLabel("Moyenne : 0")
        self.winner_label = QLabel("Gagnant : -")

        stats_grid = QGridLayout()
        stats_grid.addWidget(self.total_label, 0, 0)
        stats_grid.addWidget(self.avg_label, 0, 1)
        stats_grid.addWidget(self.winner_label, 1, 0)

        main_layout.addSpacing(15)
        main_layout.addLayout(stats_grid)

        # --- Buttons ---
        btn_layout = QHBoxLayout()

        self.btn_load = QPushButton("Charger résultats")
        self.btn_save = QPushButton("Sauvegarder résultats")
        self.btn_analyze = QPushButton("Analyser résultats")

        btn_layout.addWidget(self.btn_load)
        btn_layout.addWidget(self.btn_save)
        btn_layout.addWidget(self.btn_analyze)

        main_layout.addSpacing(20)
        main_layout.addLayout(btn_layout)

        # Connect buttons
        self.btn_analyze.clicked.connect(self.analyze_results)
        self.btn_save.clicked.connect(self.save_results)

        self.setLayout(main_layout)

    # --- Calculation Logic ---
    def analyze_results(self):
        total = 0
        winner_name = "-"
        winner_score = -1

        for name_edit, points_edit in zip(self.name_edits, self.points_edits):
            name = name_edit.text().strip()
            try:
                score = int(points_edit.text())
            except ValueError:
                score = 0

            total += score

            if score > winner_score:
                winner_score = score
                winner_name = name

        avg = total / 4 if total else 0

        self.total_label.setText(f"Total des points : {total}")
        self.avg_label.setText(f"Moyenne : {avg:.1f}")
        self.winner_label.setText(f"Gagnant : {winner_name}")

    # --- Save to .txt file ---
    def save_results(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Sauvegarder résultats",
            "",
            "Fichier texte (*.txt)"
        )

        if not filename:
            return  # user canceled

        lines = []

        # Player lines
        for i, (name_edit, points_edit) in enumerate(zip(self.name_edits, self.points_edits), start=1):
            name = name_edit.text()
            points = points_edit.text()
            lines.append(f"Joueur #{i} : {name} - {points} points")

        # Stats
        lines.append("")
        lines.append(self.total_label.text())
        lines.append(self.avg_label.text())
        lines.append(self.winner_label.text())

        # Write file
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))


# --- Launch app ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayerGUI()
    window.show()
    sys.exit(app.exec())

