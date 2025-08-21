import PyPDF2
import pdfplumber
import pandas as pd
import re
from typing import Dict, List, Any

class FinancialDataExtractor:
    def __init__(self):
        self.patterns = {
            'order_id': r'Order ID[:\s]+(\d+)',
            'customer_id': r'Customer ID[:\s]+(\w+)',
            'total_price': r'Total[:\s]*Price[:\s]*(\d+\.?\d*)',
            'order_date': r'Order Date[:\s]*(\d{8})',
            'products': {
                'product_id': r'Product ID[:\s]*(\d+)',
                'product_name': r'Product Name[:\s]*([^\n]+)',
                'quantity': r'Quantity[:\s]*(\d+)',
                'unit_price': r'Unit Price[:\s]*(\d+\.?\d*)'
            }
        }

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from PDF using pdfplumber with PyPDF2 fallback"""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = '\n'.join(page.extract_text() for page in pdf.pages)
                return text
        except Exception as e:
            print(f"pdfplumber failed, trying PyPDF2: {e}")
            try:
                with open(pdf_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    text = '\n'.join(page.extract_text() for page in reader.pages)
                    return text
            except Exception as e:
                print(f"Failed to extract text from {pdf_path}: {e}")
                return ""

    def extract_basic_info(self, text: str) -> Dict[str, Any]:
        """Extract basic financial information"""
        info = {}
        for field, pattern in self.patterns.items():
            if field != 'products':
                match = re.search(pattern, text)
                if match:
                    info[field] = match.group(1)
        return info

    def extract_product_details(self, text: str) -> List[Dict[str, Any]]:
        """Extract product details from the text"""
        products = []
        # Find the Products section
        product_section = re.findall(r'Product.*?(?=\n\n|\Z)', text, re.DOTALL)
        
        if product_section:
            # Split into lines and process each product
            lines = product_section[0].split('\n')
            current_product = {}
            
            for line in lines:
                for field, pattern in self.patterns['products'].items():
                    match = re.search(pattern, line)
                    if match:
                        current_product[field] = match.group(1)
                
                # If we have all fields, add to products list
                if len(current_product) == len(self.patterns['products']):
                    products.append(current_product.copy())
                    current_product = {}
                    
        return products

    def process_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """Process a single PDF and extract all financial information"""
        text = self.extract_text_from_pdf(pdf_path)
        if not text:
            return None

        # Extract basic information
        info = self.extract_basic_info(text)
        
        # Extract product details
        info['products'] = self.extract_product_details(text)
        
        return info

    def export_to_excel(self, data: List[Dict[str, Any]], output_path: str):
        """Export the extracted data to Excel"""
        # Create DataFrames for basic info and products
        basic_info_df = pd.DataFrame([{k: v for k, v in d.items() if k != 'products'} for d in data])
        
        # Create products DataFrame
        products_data = []
        for doc in data:
            order_id = doc.get('order_id', '')
            for product in doc.get('products', []):
                product['order_id'] = order_id
                products_data.append(product)
        
        products_df = pd.DataFrame(products_data)

        # Export to Excel with multiple sheets
        with pd.ExcelWriter(output_path) as writer:
            basic_info_df.to_excel(writer, sheet_name='Basic Info', index=False)
            products_df.to_excel(writer, sheet_name='Products', index=False)

def main():
    # Initialize the extractor
    extractor = FinancialDataExtractor()
    
    # List of PDF files to process
    pdf_files = [
        "/path/to/your/invoice_10294.pdf",
        # Add more PDF paths here
    ]
    
    # Process all PDFs
    extracted_data = []
    for pdf_file in pdf_files:
        data = extractor.process_pdf(pdf_file)
        if data:
            extracted_data.append(data)
    
    # Export to Excel
    extractor.export_to_excel(extracted_data, 'financial_data.xlsx')
    
    # Also export to CSV (if needed)
    pd.DataFrame(extracted_data).to_csv('financial_data.csv', index=False)

if __name__ == "__main__":
    main()

# Modify the pdf_files list in main():
pdf_files = [
    "/Users/spandan/Downloads/archive/CompanyDocuments/invoices/invoice_10294.pdf",
    "/Users/spandan/Downloads/archive/CompanyDocuments/PurchaseOrders/purchase_orders_10309.pdf",
    "/Users/spandan/Downloads/archive/CompanyDocuments/Shipping orders/order_10357.pdf"
]
