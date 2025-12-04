import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout,
    QFileDialog
)
from PyQt6.QtCore import Qt


# ---------- Analyze function ----------
def analyze_results():
    total = 0
    winner_name = "-"
    winner_score = -1

    for name_edit, points_edit in zip(name_edits, points_edits):
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

    total_label.setText(f"Total des points : {total}")
    avg_label.setText(f"Moyenne : {avg:.1f}")
    winner_label.setText(f"Gagnant : {winner_name}")


# ---------- Save function ----------
def save_results():
    filename, _ = QFileDialog.getSaveFileName(
        window,
        "Sauvegarder résultats",
        "",
        "Fichier texte (*.txt)"
    )

    if not filename:
        return

    lines = []

    for i, (name_edit, points_edit) in enumerate(zip(name_edits, points_edits), start=1):
        name = name_edit.text()
        points = points_edit.text()
        lines.append(f"Joueur #{i} : {name} - {points} points")

    lines.append("")
    lines.append(total_label.text())
    lines.append(avg_label.text())
    lines.append(winner_label.text())

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ---------- Create the window ----------
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Liste des joueurs")
window.setMinimumWidth(600)

main_layout = QVBoxLayout()
grid = QGridLayout()

# Title
title = QLabel("Liste des joueurs")
title.setAlignment(Qt.AlignmentFlag.AlignCenter)
title.setStyleSheet("font-size: 22px; font-weight: bold;")
main_layout.addWidget(title)
main_layout.addSpacing(20)

# Player fields
name_edits = []
points_edits = []

for i in range(4):
    lbl = QLabel(f"Joueur #{i+1}")

    name_edit = QLineEdit()
    name_edit.setPlaceholderText("Nom du joueur")

    points_edit = QLineEdit()
    points_edit.setPlaceholderText("0")
    points_edit.setFixedWidth(80)

    name_edits.append(name_edit)
    points_edits.append(points_edit)

    grid.addWidget(lbl, i, 0)
    grid.addWidget(name_edit, i, 1)
    grid.addWidget(points_edit, i, 2)

main_layout.addLayout(grid)

# Results section
total_label = QLabel("Total des points : 0")
avg_label = QLabel("Moyenne : 0")
winner_label = QLabel("Gagnant : -")

stats = QGridLayout()
stats.addWidget(total_label, 0, 0)
stats.addWidget(avg_label, 0, 1)
stats.addWidget(winner_label, 1, 0)

main_layout.addSpacing(15)
main_layout.addLayout(stats)

# Buttons
btn_layout = QHBoxLayout()

btn_load = QPushButton("Charger résultats")
btn_save = QPushButton("Sauvegarder résultats")
btn_analyze = QPushButton("Analyser résultats")

btn_layout.addWidget(btn_load)
btn_layout.addWidget(btn_save)
btn_layout.addWidget(btn_analyze)

main_layout.addSpacing(20)
main_layout.addLayout(btn_layout)

# Button connections
btn_analyze.clicked.connect(analyze_results)
btn_save.clicked.connect(save_results)

window.setLayout(main_layout)
window.show()

sys.exit(app.exec())
