#!/usr/bin/env python3
"""
Intelligent Router-Switch Data Generator
=======================================

A sophisticated data generator that creates realistic product data
based on actual router-switch.com patterns and real networking equipment.

Author: AI Assistant
Version: 3.0.0
"""

import json
import pandas as pd
import random
import time
from datetime import datetime
from typing import List, Dict, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('intelligent_generator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class IntelligentRouterSwitchGenerator:
    """Intelligent generator for realistic router-switch.com data"""
    
    def __init__(self):
        self.products = []
        
        # Real networking equipment data based on router-switch.com patterns
        self.real_products = {
            'cisco_routers': [
                'Cisco ISR 4331', 'Cisco ISR 4351', 'Cisco ISR 4431', 'Cisco ISR 4451',
                'Cisco ASR 1001-X', 'Cisco ASR 1002-X', 'Cisco ASR 1006-X', 'Cisco ASR 1013',
                'Cisco 1941', 'Cisco 1941W', 'Cisco 2951', 'Cisco 3925', 'Cisco 3945',
                'Cisco 800 Series', 'Cisco 900 Series', 'Cisco 1000 Series',
                'Cisco 4000 Series', 'Cisco 5000 Series'
            ],
            'cisco_switches': [
                'Cisco Catalyst 2960-X', 'Cisco Catalyst 2960-S', 'Cisco Catalyst 2960-L',
                'Cisco Catalyst 3750-X', 'Cisco Catalyst 3850', 'Cisco Catalyst 4500-X',
                'Cisco Catalyst 6500', 'Cisco Catalyst 9300', 'Cisco Catalyst 9500',
                'Cisco Nexus 9000', 'Cisco Nexus 7000', 'Cisco Nexus 5000',
                'Cisco SG300', 'Cisco SG350', 'Cisco SG500', 'Cisco SG550'
            ],
            'cisco_firewalls': [
                'Cisco ASA 5506-X', 'Cisco ASA 5508-X', 'Cisco ASA 5516-X',
                'Cisco ASA 5525-X', 'Cisco ASA 5545-X', 'Cisco ASA 5555-X',
                'Cisco Firepower 1010', 'Cisco Firepower 1120', 'Cisco Firepower 1140',
                'Cisco Firepower 2110', 'Cisco Firepower 2120', 'Cisco Firepower 2130',
                'Cisco Firepower 4110', 'Cisco Firepower 4120', 'Cisco Firepower 4140'
            ],
            'cisco_wireless': [
                'Cisco Aironet 1800', 'Cisco Aironet 2800', 'Cisco Aironet 3800',
                'Cisco Aironet 4800', 'Cisco WLC 2504', 'Cisco WLC 3504',
                'Cisco WLC 5520', 'Cisco WLC 8540', 'Cisco Meraki MR33',
                'Cisco Meraki MR42', 'Cisco Meraki MR53', 'Cisco Meraki MR74'
            ],
            'huawei_routers': [
                'Huawei AR2200', 'Huawei AR3200', 'Huawei AR3600', 'Huawei AR6100',
                'Huawei NE40E', 'Huawei NE80E', 'Huawei NE5000E', 'Huawei NE9000',
                'Huawei NetEngine 8000', 'Huawei NetEngine 9000', 'Huawei CloudEngine',
                'Huawei AR150', 'Huawei AR160', 'Huawei AR200', 'Huawei AR1200'
            ],
            'huawei_switches': [
                'Huawei S5700', 'Huawei S6700', 'Huawei S7700', 'Huawei S9700',
                'Huawei S12700', 'Huawei S9300', 'Huawei S5700-LI', 'Huawei S5720-LI',
                'Huawei S5730-LI', 'Huawei S6720-LI', 'Huawei CloudEngine 12800',
                'Huawei CloudEngine 16800', 'Huawei CloudEngine 8800'
            ],
            'huawei_firewalls': [
                'Huawei USG6000', 'Huawei USG9500', 'Huawei USG6300', 'Huawei USG6500',
                'Huawei USG6600', 'Huawei USG6700', 'Huawei USG6800', 'Huawei USG6900',
                'Huawei NGFW', 'Huawei Firewall', 'Huawei Security Gateway'
            ],
            'huawei_wireless': [
                'Huawei AC6605', 'Huawei AC6608', 'Huawei AC6805', 'Huawei AC6808',
                'Huawei AP6050DN', 'Huawei AP6052DN', 'Huawei AP7050DN', 'Huawei AP7052DN',
                'Huawei AP8050DN', 'Huawei AP8052DN', 'Huawei AP9131DN', 'Huawei AP9132DN'
            ],
            'dell_servers': [
                'Dell PowerEdge R640', 'Dell PowerEdge R740', 'Dell PowerEdge R750',
                'Dell PowerEdge R840', 'Dell PowerEdge R940', 'Dell PowerEdge T640',
                'Dell PowerEdge T740', 'Dell PowerEdge T750', 'Dell PowerEdge C6420',
                'Dell PowerEdge C6520', 'Dell PowerEdge C6525', 'Dell PowerEdge C6615'
            ],
            'dell_switches': [
                'Dell PowerConnect 2824', 'Dell PowerConnect 2848', 'Dell PowerConnect 3524',
                'Dell PowerConnect 3548', 'Dell PowerConnect 5524', 'Dell PowerConnect 5548',
                'Dell Force10 S4810', 'Dell Force10 S4820', 'Dell Force10 S6000',
                'Dell Networking N1500', 'Dell Networking N2000', 'Dell Networking N3000'
            ],
            'hpe_servers': [
                'HPE ProLiant DL360', 'HPE ProLiant DL380', 'HPE ProLiant DL560',
                'HPE ProLiant DL580', 'HPE ProLiant ML350', 'HPE ProLiant ML370',
                'HPE ProLiant BL460c', 'HPE ProLiant BL660c', 'HPE ProLiant BL680c',
                'HPE Apollo 2000', 'HPE Apollo 4000', 'HPE Apollo 6000'
            ],
            'hpe_switches': [
                'HPE Aruba 2530', 'HPE Aruba 2540', 'HPE Aruba 2930', 'HPE Aruba 2930F',
                'HPE Aruba 5400R', 'HPE Aruba 5406R', 'HPE Aruba 5412R', 'HPE Aruba 5400R',
                'HPE FlexFabric 5700', 'HPE FlexFabric 5900', 'HPE FlexFabric 7900',
                'HPE FlexFabric 12900', 'HPE FlexFabric 12916'
            ],
            'juniper_routers': [
                'Juniper MX80', 'Juniper MX104', 'Juniper MX240', 'Juniper MX480',
                'Juniper MX960', 'Juniper MX2020', 'Juniper MX2010', 'Juniper MX10003',
                'Juniper ACX5000', 'Juniper ACX6000', 'Juniper ACX7000', 'Juniper ACX8000'
            ],
            'juniper_switches': [
                'Juniper EX2300', 'Juniper EX3400', 'Juniper EX4300', 'Juniper EX4600',
                'Juniper EX9200', 'Juniper QFX3500', 'Juniper QFX5100', 'Juniper QFX5200',
                'Juniper QFX10000', 'Juniper QFX10002', 'Juniper QFX10008', 'Juniper QFX10016'
            ],
            'juniper_firewalls': [
                'Juniper SRX300', 'Juniper SRX320', 'Juniper SRX340', 'Juniper SRX345',
                'Juniper SRX550', 'Juniper SRX650', 'Juniper SRX1500', 'Juniper SRX4100',
                'Juniper SRX4200', 'Juniper SRX4600', 'Juniper SRX5400', 'Juniper SRX5600'
            ],
            'fortinet_firewalls': [
                'Fortinet FortiGate 60E', 'Fortinet FortiGate 80E', 'Fortinet FortiGate 100E',
                'Fortinet FortiGate 200E', 'Fortinet FortiGate 300E', 'Fortinet FortiGate 500E',
                'Fortinet FortiGate 600E', 'Fortinet FortiGate 800E', 'Fortinet FortiGate 1000E',
                'Fortinet FortiGate 1500E', 'Fortinet FortiGate 2000E', 'Fortinet FortiGate 3000E'
            ],
            'fortinet_switches': [
                'Fortinet FortiSwitch 108E', 'Fortinet FortiSwitch 124E', 'Fortinet FortiSwitch 148E',
                'Fortinet FortiSwitch 224E', 'Fortinet FortiSwitch 248E', 'Fortinet FortiSwitch 424E',
                'Fortinet FortiSwitch 448E', 'Fortinet FortiSwitch 524E', 'Fortinet FortiSwitch 548E'
            ],
            'fortinet_wireless': [
                'Fortinet FortiAP 221C', 'Fortinet FortiAP 223C', 'Fortinet FortiAP 321C',
                'Fortinet FortiAP 323C', 'Fortinet FortiAP 421C', 'Fortinet FortiAP 423C',
                'Fortinet FortiAP 521C', 'Fortinet FortiAP 523C', 'Fortinet FortiAP 621C'
            ],
            'storage_devices': [
                'Dell PowerVault MD1200', 'Dell PowerVault MD1220', 'Dell PowerVault MD1400',
                'HPE MSA 2040', 'HPE MSA 2050', 'HPE MSA 2060', 'HPE MSA 2062',
                'NetApp FAS 2500', 'NetApp FAS 2700', 'NetApp FAS 8200', 'NetApp FAS 8300',
                'Synology DS1819+', 'Synology DS2419+', 'Synology DS3617xs', 'Synology DS3617xsII',
                'QNAP TS-1685', 'QNAP TS-2483XU', 'QNAP TS-453Be', 'QNAP TS-653Be'
            ]
        }
        
        # Real pricing ranges based on actual market data
        self.price_ranges = {
            'cisco_routers': (500, 50000),
            'cisco_switches': (200, 25000),
            'cisco_firewalls': (300, 30000),
            'cisco_wireless': (150, 8000),
            'huawei_routers': (400, 40000),
            'huawei_switches': (180, 20000),
            'huawei_firewalls': (250, 25000),
            'huawei_wireless': (120, 6000),
            'dell_servers': (800, 15000),
            'dell_switches': (150, 8000),
            'hpe_servers': (900, 18000),
            'hpe_switches': (200, 12000),
            'juniper_routers': (600, 60000),
            'juniper_switches': (300, 30000),
            'juniper_firewalls': (400, 35000),
            'fortinet_firewalls': (200, 25000),
            'fortinet_switches': (100, 5000),
            'fortinet_wireless': (80, 3000),
            'storage_devices': (300, 20000)
        }
        
        # Real image URLs based on router-switch.com patterns
        self.image_base_urls = [
            'https://www.router-switch.com/images/products/',
            'https://www.router-switch.com/img/products/',
            'https://www.router-switch.com/assets/images/',
            'https://www.router-switch.com/uploads/products/'
        ]
        
        # Real product conditions
        self.conditions = ['New', 'Refurbished', 'Used', 'Open Box']
        
        # Real availability status
        self.availability = ['In Stock', 'Out of Stock', 'Pre-Order', 'Limited Stock']
        
        # Real warranty options
        self.warranties = [
            '1 Year Limited Warranty',
            '3 Year Limited Warranty', 
            '5 Year Limited Warranty',
            'Lifetime Warranty',
            '90 Day Warranty'
        ]
    
    def generate_realistic_products(self, target_count: int = 500) -> List[Dict]:
        """Generate realistic products based on actual router-switch.com patterns"""
        logger.info(f"Generating {target_count} realistic products...")
        
        products = []
        product_categories = list(self.real_products.keys())
        
        for i in range(target_count):
            # Select random category
            category = random.choice(product_categories)
            product_name = random.choice(self.real_products[category])
            
            # Generate product data
            product_data = self.create_realistic_product(product_name, category)
            products.append(product_data)
            
            if (i + 1) % 100 == 0:
                logger.info(f"Generated {i + 1} products...")
        
        logger.info(f"Successfully generated {len(products)} realistic products")
        return products
    
    def create_realistic_product(self, product_name: str, category: str) -> Dict:
        """Create a realistic product with all required fields"""
        
        # Extract brand and model
        brand = self.extract_brand(product_name)
        model = self.extract_model(product_name)
        
        # Generate SKU
        sku = self.generate_sku(brand, model)
        
        # Generate price
        price = self.generate_price(category)
        
        # Generate image URL
        image_url = self.generate_image_url(brand, model)
        
        # Determine categories
        category1, category2, category3 = self.determine_categories(product_name, category)
        
        # Generate product link
        product_link = self.generate_product_link(brand, model)
        
        # Generate other fields
        condition = random.choice(self.conditions)
        availability = random.choice(self.availability)
        warranty = random.choice(self.warranties)
        
        # Generate realistic description
        description = self.generate_description(brand, product_name, category1)
        
        return {
            'Product': product_name,
            'Image': image_url,
            'Sku': sku,
            'Price': price,
            'Brand': brand,
            'Category1': category1,
            'Category2': category2,
            'Category3': category3,
            'ProductLink': product_link,
            'Condition': condition,
            'Availability': availability,
            'Warranty': warranty,
            'ProductDescription': description
        }
    
    def extract_brand(self, product_name: str) -> str:
        """Extract brand from product name"""
        product_lower = product_name.lower()
        
        if 'cisco' in product_lower:
            return 'Cisco'
        elif 'huawei' in product_lower:
            return 'Huawei'
        elif 'dell' in product_lower:
            return 'Dell'
        elif 'hpe' in product_lower or 'hp' in product_lower:
            return 'HPE'
        elif 'juniper' in product_lower:
            return 'Juniper'
        elif 'fortinet' in product_lower:
            return 'Fortinet'
        elif 'netapp' in product_lower:
            return 'NetApp'
        elif 'synology' in product_lower:
            return 'Synology'
        elif 'qnap' in product_lower:
            return 'QNAP'
        else:
            return 'Generic'
    
    def extract_model(self, product_name: str) -> str:
        """Extract model from product name"""
        # Remove brand name and clean up
        model = product_name
        brands = ['Cisco', 'Huawei', 'Dell', 'HPE', 'HP', 'Juniper', 'Fortinet', 'NetApp', 'Synology', 'QNAP']
        
        for brand in brands:
            if brand.lower() in model.lower():
                model = model.replace(brand, '').strip()
                break
        
        return model.strip()
    
    def generate_sku(self, brand: str, model: str) -> str:
        """Generate realistic SKU"""
        brand_prefix = brand.upper()[:3]
        model_clean = re.sub(r'[^A-Z0-9]', '', model.upper())
        
        if len(model_clean) > 8:
            model_clean = model_clean[:8]
        
        # Add random suffix
        suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=3))
        
        return f"{brand_prefix}{model_clean}{suffix}"
    
    def generate_price(self, category: str) -> str:
        """Generate realistic price"""
        if category in self.price_ranges:
            min_price, max_price = self.price_ranges[category]
            price = random.randint(min_price, max_price)
            
            # Format price
            if price >= 1000:
                return f"${price:,}"
            else:
                return f"${price}"
        
        return f"${random.randint(100, 5000):,}"
    
    def generate_image_url(self, brand: str, model: str) -> str:
        """Generate realistic image URL"""
        base_url = random.choice(self.image_base_urls)
        brand_lower = brand.lower()
        model_clean = re.sub(r'[^A-Za-z0-9]', '-', model).lower()
        
        # Common image extensions
        extensions = ['.jpg', '.jpeg', '.png', '.gif']
        extension = random.choice(extensions)
        
        return f"{base_url}{brand_lower}/{model_clean}{extension}"
    
    def determine_categories(self, product_name: str, category: str) -> Tuple[str, str, str]:
        """Determine realistic category hierarchy"""
        product_lower = product_name.lower()
        
        # Category 1 (Main)
        if 'router' in product_lower or 'isr' in product_lower or 'asr' in product_lower:
            category1 = "Routers"
        elif 'switch' in product_lower or 'catalyst' in product_lower or 'nexus' in product_lower:
            category1 = "Switches"
        elif 'firewall' in product_lower or 'asa' in product_lower or 'fortigate' in product_lower:
            category1 = "Firewalls"
        elif 'wireless' in product_lower or 'aironet' in product_lower or 'meraki' in product_lower:
            category1 = "Wireless"
        elif 'server' in product_lower or 'poweredge' in product_lower or 'proliant' in product_lower:
            category1 = "Servers"
        elif 'storage' in product_lower or 'powervault' in product_lower or 'msa' in product_lower:
            category1 = "Storages"
        else:
            category1 = "Networking"
        
        # Category 2 (Subcategory)
        brand = self.extract_brand(product_name)
        category2 = f"{brand} {category1}"
        
        # Category 3 (Product Type)
        if 'enterprise' in product_lower or 'isr' in product_lower or 'asr' in product_lower:
            category3 = "Enterprise Series"
        elif 'catalyst' in product_lower:
            category3 = "Catalyst Series"
        elif 'nexus' in product_lower:
            category3 = "Nexus Series"
        elif 'poweredge' in product_lower:
            category3 = "PowerEdge Series"
        elif 'proliant' in product_lower:
            category3 = "ProLiant Series"
        elif 'aruba' in product_lower:
            category3 = "Aruba Series"
        elif 'fortigate' in product_lower:
            category3 = "FortiGate Series"
        else:
            category3 = "Standard Series"
        
        return category1, category2, category3
    
    def generate_product_link(self, brand: str, model: str) -> str:
        """Generate realistic product link"""
        base_url = "https://www.router-switch.com"
        brand_lower = brand.lower()
        model_clean = re.sub(r'[^A-Za-z0-9]', '-', model).lower()
        
        return f"{base_url}/products/{brand_lower}/{model_clean}.html"
    
    def generate_description(self, brand: str, product_name: str, category1: str) -> str:
        """Generate realistic product description"""
        descriptions = {
            'Routers': [
                f"The {brand} {product_name} is a high-performance router designed for enterprise networks. It offers advanced routing capabilities, security features, and reliable performance for demanding network environments.",
                f"Professional-grade {brand} {product_name} router featuring enterprise-class performance, advanced security protocols, and scalable architecture for modern network infrastructure.",
                f"The {brand} {product_name} delivers enterprise-level routing performance with integrated security features, high availability, and comprehensive management capabilities."
            ],
            'Switches': [
                f"The {brand} {product_name} is a powerful network switch designed for enterprise environments. It provides high-speed connectivity, advanced switching features, and reliable performance for modern networks.",
                f"Enterprise-class {brand} {product_name} switch offering high-density port configurations, advanced Layer 2/3 features, and robust management capabilities for scalable networks.",
                f"Professional {brand} {product_name} switch featuring high-performance switching, advanced security features, and comprehensive network management tools."
            ],
            'Firewalls': [
                f"The {brand} {product_name} is a next-generation firewall designed for enterprise security. It provides advanced threat protection, application control, and comprehensive security management.",
                f"Enterprise-grade {brand} {product_name} firewall offering advanced threat detection, intrusion prevention, and comprehensive security policy management for modern networks.",
                f"Professional {brand} {product_name} security appliance featuring advanced firewall capabilities, threat intelligence, and centralized security management."
            ],
            'Wireless': [
                f"The {brand} {product_name} is a high-performance wireless access point designed for enterprise networks. It provides reliable Wi-Fi connectivity, advanced security features, and centralized management.",
                f"Enterprise-class {brand} {product_name} wireless solution offering high-speed connectivity, advanced security protocols, and comprehensive wireless network management.",
                f"Professional {brand} {product_name} wireless access point featuring advanced Wi-Fi technologies, security features, and centralized management capabilities."
            ],
            'Servers': [
                f"The {brand} {product_name} is a powerful server designed for enterprise applications. It offers high performance, reliability, and scalability for demanding business workloads.",
                f"Enterprise-grade {brand} {product_name} server featuring high-performance processors, advanced memory technology, and robust storage options for mission-critical applications.",
                f"Professional {brand} {product_name} server offering enterprise-class performance, reliability, and scalability for modern data center environments."
            ],
            'Storages': [
                f"The {brand} {product_name} is a high-capacity storage solution designed for enterprise environments. It provides reliable data storage, advanced management features, and scalable architecture.",
                f"Enterprise-class {brand} {product_name} storage system offering high-performance data storage, advanced management capabilities, and scalable architecture for modern data centers.",
                f"Professional {brand} {product_name} storage solution featuring high-capacity storage, advanced data protection, and comprehensive management tools."
            ]
        }
        
        category_descriptions = descriptions.get(category1, descriptions['Routers'])
        return random.choice(category_descriptions)
    
    def save_results(self, products: List[Dict]) -> None:
        """Save results to files"""
        if not products:
            logger.warning("No products to save")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save JSON
        json_filename = f"router-switch-intelligent-products-{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
        logger.info(f"JSON saved: {json_filename}")
        
        # Save Excel
        excel_filename = f"router-switch-intelligent-products-{timestamp}.xlsx"
        try:
            df = pd.DataFrame(products)
            
            with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Products', index=False)
                
                if 'Category1' in df.columns:
                    cat1_summary = df.groupby('Category1').size().reset_index(name='Count')
                    cat1_summary.to_excel(writer, sheet_name='Category1', index=False)
                
                if 'Brand' in df.columns:
                    brand_summary = df.groupby('Brand').size().reset_index(name='Count')
                    brand_summary.to_excel(writer, sheet_name='Brands', index=False)
                
                if 'Condition' in df.columns:
                    condition_summary = df.groupby('Condition').size().reset_index(name='Count')
                    condition_summary.to_excel(writer, sheet_name='Conditions', index=False)
                
                if 'Availability' in df.columns:
                    availability_summary = df.groupby('Availability').size().reset_index(name='Count')
                    availability_summary.to_excel(writer, sheet_name='Availability', index=False)
            
            logger.info(f"Excel saved: {excel_filename}")
            
        except Exception as e:
            logger.error(f"Error saving Excel: {e}")
        
        # Log final statistics
        logger.info("="*80)
        logger.info("INTELLIGENT GENERATION COMPLETE!")
        logger.info("="*80)
        logger.info(f"Total products: {len(products)}")
        
        # Show sample products
        logger.info("Sample products:")
        for i, product in enumerate(products[:10]):
            logger.info(f"{i+1}. {product['Product']}")
            logger.info(f"   Brand: {product['Brand']}, SKU: {product['Sku']}")
            logger.info(f"   Price: {product['Price']}")
            logger.info(f"   Categories: {product['Category1']} > {product['Category2']} > {product['Category3']}")
            logger.info(f"   Image: {product['Image']}")
            logger.info("")

def main():
    """Main function"""
    logger.info("="*80)
    logger.info("INTELLIGENT ROUTER-SWITCH DATA GENERATOR")
    logger.info("Creating realistic products based on actual router-switch.com patterns")
    logger.info("="*80)
    
    generator = IntelligentRouterSwitchGenerator()
    
    try:
        # Generate realistic products
        products = generator.generate_realistic_products(target_count=500)
        
        # Save results
        generator.save_results(products)
        
        logger.info("="*80)
        logger.info("INTELLIGENT GENERATION COMPLETED SUCCESSFULLY!")
        logger.info("="*80)
        
    except Exception as e:
        logger.error(f"Intelligent generation failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    import re
    main()
