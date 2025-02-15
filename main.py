import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class CyberpunkEconomyAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyberpunk 2077 - Economy & Crafting Analyzer")
        self.setGeometry(100, 100, 900, 700)
        self.initUI()

    def initUI(self):
        pass  # Здесь будет интерфейс

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CyberpunkEconomyAnalyzer()
    window.show()
    sys.exit(app.exec_())
