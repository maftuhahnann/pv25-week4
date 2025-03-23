from PyQt5 import QtCore, QtWidgets

class POSAppUI(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("F1D022135 - Maftuh Ahnan Al-Kautsar")
        MainWindow.resize(700, 600)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.central_widget)

        self.layout_container = QtWidgets.QWidget(self.central_widget)
        self.layout_container.setGeometry(QtCore.QRect(150, 60, 521, 350))
        
        self.form_layout = QtWidgets.QFormLayout(self.layout_container)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        
        self.lbl_product = QtWidgets.QLabel("Produk", self.layout_container)
        self.cmb_product = QtWidgets.QComboBox(self.layout_container)
        self.cmb_product.addItems([
            "Pilih Produk 😊",
            "Bimoli (Rp. 20,000)",
            "Beras 5 Kg (Rp. 75,000)",
            "Kecap ABC (Rp. 7,000)",
            "Saos Saset (Rp. 2,500)"
        ])
        self.form_layout.addRow(self.lbl_product, self.cmb_product)
        
        self.lbl_quantity = QtWidgets.QLabel("Jumlah", self.layout_container)
        self.txt_quantity = QtWidgets.QLineEdit(self.layout_container)
        self.form_layout.addRow(self.lbl_quantity, self.txt_quantity)
        
        self.lbl_discount = QtWidgets.QLabel("Diskon", self.layout_container)
        self.cmb_discount = QtWidgets.QComboBox(self.layout_container)
        self.cmb_discount.addItems(["0%", "5%", "10%", "15%"])
        self.cmb_discount.setFixedWidth(70)
        self.form_layout.addRow(self.lbl_discount, self.cmb_discount)
        
        self.btn_add = QtWidgets.QPushButton("Add to your cart", self.layout_container)
        self.btn_clear = QtWidgets.QPushButton("Clear from cart", self.layout_container)
        self.form_layout.addRow(self.btn_add, self.btn_clear)
        
        self.list_cart = QtWidgets.QListView(self.layout_container)
        self.form_layout.addRow(self.list_cart)
      
        self.lbl_total = QtWidgets.QLabel("Total: Rp 0", self.layout_container)
        self.lbl_total.setStyleSheet("font-weight: bold;")
        self.form_layout.addRow(self.lbl_total)
     
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        MainWindow.setWindowTitle("Aplikasi POS")
