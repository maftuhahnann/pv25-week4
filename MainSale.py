import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
from Pos_ui import POSAppUI  


class MainOfSale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = POSAppUI()
        self.ui.setup_ui(self)

        self.product_prices = {
            "Pilih Produk Anda!!": 0,
            "Bimoli (Rp. 20,000)": 20000,
            "Beras 5 Kg (Rp. 75,000)": 75000,
            "Kecap ABC (Rp. 7,000)": 7000,
            "Saos Saset (Rp. 2,500)": 2500,
        }
        
        self.ui.cmb_product.clear()
        self.ui.cmb_product.addItems(self.product_prices.keys())

        self.cart_model = QStringListModel()
        self.ui.list_cart.setModel(self.cart_model)
        self.cart_items = []
        self.total_cost = 0

        self.ui.btn_add.clicked.connect(self.add_to_cart)
        self.ui.btn_clear.clicked.connect(self.clear_cart)

    def add_to_cart(self):
        product_name = self.ui.cmb_product.currentText()
        quantity_text = self.ui.txt_quantity.text()
        discount_text = self.ui.cmb_discount.currentText()

        if product_name == "Pilih Produk Anda!!":
            QMessageBox.warning(self, "Warning", "Silakan pilih produk dulu.")
            return
        if not quantity_text.isdigit():
            QMessageBox.warning(self, "Warning!!", "Jumlah harus angka.")
            return

        quantity = int(quantity_text)
        price = self.product_prices[product_name]
        subtotal = price * quantity

        discount = int(discount_text.replace("%", ""))
        discount_amount = subtotal * discount // 100
        final_price = subtotal - discount_amount

        self.total_cost += final_price

        item_text = f"{product_name} - {quantity} x Rp. {price:,} (diskon {discount}%)"
        self.cart_items.append(item_text)
        self.cart_model.setStringList(self.cart_items)

        self.update_total_label()

    def clear_cart(self):
        """Menghapus semua item dari keranjang belanja."""
        self.cart_items = []
        self.cart_model.setStringList(self.cart_items)
        self.total_cost = 0
        self.update_total_label()

    def update_total_label(self):
        """Memperbarui tampilan total harga."""
        self.ui.lbl_total.setText(f"Total: Rp. {self.total_cost:,}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainOfSale()
    window.setWindowTitle("F1D022135 - Maftuh Ahnan Al-Kautsar")
    window.show()
    sys.exit(app.exec())
