import xml.etree.ElementTree as ET

class XMLReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_xml(self):
        try:
            tree = ET.parse(self.file_path)
            self.data = tree.getroot()
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
        except ET.ParseError:
            print(f"Error: Failed to parse XML file '{self.file_path}'.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def display_data(self):
        if self.data is not None:  
            for product in self.data.findall('product'):
                name = product.find('name')
                price = product.find('price')
                quantity = product.find('quantity')
                name_text = name.text if name is not None else "N/A"
                price_text = price.text if price is not None else "N/A"
                quantity_text = quantity.text if quantity is not None else "N/A"

                print(f"Product: {name_text}, Price: {price_text}, Quantity: {quantity_text}")
        else:
            print("No data to display. Please check the XML file.")

# Sử dụng lớp XMLReader
path = 'D:/17A3KHDL/LAB1/DATA/products.xml'  
reader = XMLReader(path)
reader.read_xml()
reader.display_data()
