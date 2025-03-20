from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QTabWidget, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize
import sys

class GameTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Tracker")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #121212; color: white;")
        
        # Main Layout
        main_layout = QVBoxLayout(self)
        
        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("QTabBar::tab { font-size: 60px; padding: 0px 40px; height: 20px; padding: 5px; width: 50vw; background: transparent; border: none; width: 50%; text-align: center; }"
                                   "QTabBar::tab:selected { font-weight: bold; border-bottom: 3px solid white; background-color: #333; }"
                                   "QTabWidget::pane { border: none; }")
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
                
        tab_bar_layout = QHBoxLayout()
        tab_bar_layout.addStretch()
        tab_bar_layout.addWidget(self.tabs.tabBar())
        tab_bar_layout.addStretch()
        main_layout.insertLayout(0, tab_bar_layout)
        tab_bar_layout.setContentsMargins(0, 0, 0, 0)
        tab_bar_layout.setSpacing(0)
        self.tabs.tabBar().setStyleSheet("QTabBar { qproperty-alignment: AlignCenter; }")
        self.tabs.setStyleSheet("QTabBar { qproperty-alignment: 'AlignCenter'; }")
        self.pending_tab = QWidget()
        self.completed_tab = QWidget()
        self.tabs.addTab(self.pending_tab, "Pending Games")
        self.tabs.addTab(self.completed_tab, "Completed Games")
        main_layout.addWidget(self.tabs)
        
        # Pending Games Layout
        pending_layout = QVBoxLayout()
        pending_layout.setContentsMargins(0, 0, 0, 0)
        pending_layout.setSpacing(0)
        self.pending_search = QLineEdit()
        self.pending_search.setPlaceholderText("Search Pending Games...")
        self.pending_search.setStyleSheet("background-color: #1E1E1E; border: 2px solid #888; color: white; padding: 8px; font-size: 16px;")
        self.pending_search.textChanged.connect(lambda: self.filter_games(self.pending_games_list, self.pending_search.text()))
        self.pending_games_list = QListWidget()
        self.pending_games_list.setStyleSheet("background-color: #1E1E1E; border: none; color: white;")
        pending_layout.addWidget(self.pending_search)
        pending_layout.addWidget(self.pending_games_list)
        self.pending_tab.setLayout(pending_layout)
        
        # Completed Games Layout
        completed_layout = QVBoxLayout()
        completed_layout.setContentsMargins(0, 0, 0, 0)
        completed_layout.setSpacing(0)
        self.completed_search = QLineEdit()
        self.completed_search.setPlaceholderText("Search Completed Games...")
        self.completed_search.setStyleSheet("background-color: #1E1E1E; border: 2px solid #888; color: white; padding: 8px; font-size: 16px;")
        self.completed_search.textChanged.connect(lambda: self.filter_games(self.completed_games_list, self.completed_search.text()))
        self.completed_games_list = QListWidget()
        self.completed_games_list.setStyleSheet("background-color: #1E1E1E; border: none; color: white;")
        completed_layout.addWidget(self.completed_search)
        completed_layout.addWidget(self.completed_games_list)
        
        self.completed_tab.setLayout(completed_layout)
        
        # Load Games
        self.load_games()
    
    def load_games(self):
        self.pending_games_list.clear()
        self.completed_games_list.clear()
        
        try:
            with open("Prototype/GT/Saves.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                pending_section = False
                completed_section = False
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    if "To Complete" in line:
                        pending_section = True
                        completed_section = False
                        continue
                    elif "Completed" in line:
                        pending_section = False
                        completed_section = True
                        continue
                    
                    if pending_section:
                        self.add_game_tile(self.pending_games_list, line, move_to=self.completed_games_list)
                    elif completed_section:
                        self.add_game_tile(self.completed_games_list, line, move_to=self.pending_games_list)
        except FileNotFoundError:
            print("Games Pending and Completed.txt not found.")

    def filter_games(self, list_widget, search_text):
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            widget = list_widget.itemWidget(item)
            label = widget.layout().itemAt(1).widget()
            item.setHidden(search_text.lower() not in label.text().lower())
    
    def add_game_tile(self, list_widget, game_name, move_to):
        item = QListWidgetItem()
        item.setSizeHint(QSize(300, 80))
        
        widget = QWidget()
        layout = QHBoxLayout()
        
        image_label = QLabel()
        image_label.setFixedSize(60, 60)
        image_label.setStyleSheet("background-color: #333; border: 1px solid #555;")
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        upload_button = QPushButton("+")
        upload_button.setStyleSheet("background-color: transparent; font-size: 24px; border: none;")
        upload_button.clicked.connect(lambda: self.upload_thumbnail(image_label))
        
        image_label.setLayout(QHBoxLayout())
        image_label.layout().addWidget(upload_button)
        
        label = QLabel(game_name)
        move_button = QPushButton("Move to Completed" if list_widget == self.pending_games_list else "Move to Pending")
        move_button.setStyleSheet("background-color: #444; padding: 5px; border-radius: 5px;")
        move_button.clicked.connect(lambda: self.move_game(item, list_widget, move_to))
        
        layout.addWidget(image_label)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addStretch()
        layout.addWidget(move_button, alignment=Qt.AlignmentFlag.AlignRight)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        widget.setLayout(layout)
        
        list_widget.addItem(item)
        list_widget.setItemWidget(item, widget)
    
    def upload_thumbnail(self, image_label):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Thumbnail", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            pixmap = QPixmap(file_path).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            image_label.setPixmap(pixmap)
            image_label.layout().takeAt(0).widget().deleteLater()
    
    def move_game(self, item, from_list, to_list):
        game_name = from_list.itemWidget(item).layout().itemAt(1).widget().text()
        from_list.takeItem(from_list.row(item))
        self.add_game_tile(to_list, game_name, move_to=from_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameTrackerApp()
    window.show()
    sys.exit(app.exec())
