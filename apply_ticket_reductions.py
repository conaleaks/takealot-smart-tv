import os, re

def update_smart_tv():
    folder = '/Users/green/Downloads/Takealot Smart TV - Copia'
    print("Updating Smart TV (Port 3000)...")
    
    # 1. server.js
    sp = os.path.join(folder, 'server.js')
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8') as f:
            c = f.read()
        # 55" was 2599 or 1999 -> 1199. 75" was 4999 or 3999 -> 1499.
        c = re.sub(r'R\s*2[,.]?599', 'R 1,199', c)
        c = re.sub(r'R\s*1[,.]?999', 'R 1,199', c)
        c = re.sub(r'R\s*12[,.]?999', 'R 4,999', c)
        c = re.sub(r'R\s*8[,.]?999', 'R 4,999', c)
        c = re.sub(r'R\s*17[,.]?999', 'R 5,999', c)
        c = re.sub(r'R\s*3[,.]?999', 'R 1,499', c)
        c = re.sub(r'R\s*4[,.]?999', 'R 1,499', c)
        c = re.sub(r'amount:\s*(?:2599|1999)', 'amount: 1199', c)
        c = re.sub(r'total:\s*(?:2599|1999)', 'total: 1199', c)
        c = re.sub(r'amount\s*=\s*(?:2599|1999)', 'amount = 1199', c)
        c = re.sub(r'amount\s*\|\|\s*(?:2599|1999)', 'amount || 1199', c)
        c = re.sub(r'R\s*349', 'R 199', c)
        c = re.sub(r'349\.00', '199.00', c)
        c = re.sub(r'amount\s*=\s*349', 'amount = 199', c)
        c = re.sub(r'amount\s*:\s*349', 'amount: 199', c)
        with open(sp, 'w', encoding='utf-8') as f:
            f.write(c)

    # 2. index.html
    ip = os.path.join(folder, 'index.html')
    if os.path.exists(ip):
        with open(ip, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'id="main-price-display">R\s*[0-9,\s]+<', 'id="main-price-display">R 1,199<', c)
        c = re.sub(r'id="main-old-price">R\s*[0-9,\s]+<', 'id="main-old-price">R 4,999<', c)
        c = re.sub(r'id="footer-price-display">R\s*[0-9,\s]+<', 'id="footer-price-display">R 1,199<', c)
        c = c.replace('R 2,599', 'R 1,199').replace('R 12,999', 'R 4,999')
        c = c.replace('R 1,999', 'R 1,199').replace('R 8,999', 'R 4,999')
        c = c.replace('R 3,999', 'R 1,499').replace('R 17,999', 'R 5,999')
        c = c.replace('10,400', '3,800')
        c = c.replace('7,000', '3,800')
        # update variation dictionary in index.html if present
        c = re.sub(r'price:\s*["\']?(?:2599|1999)["\']?', 'price: 1199', c)
        c = re.sub(r'oldPrice:\s*["\']?R\s*(?:12,999|8,999)["\']?', 'oldPrice: "R 4,999"', c)
        c = re.sub(r'price:\s*["\']?(?:4999|3999)["\']?', 'price: 1499', c)
        c = re.sub(r'oldPrice:\s*["\']?R\s*17,999["\']?', 'oldPrice: "R 5,999"', c)
        with open(ip, 'w', encoding='utf-8') as f:
            f.write(c)

    # 3. checkout.html, cart.html, track.html, obrigado.html
    for fn in ['checkout.html', 'cart.html', 'track.html', 'obrigado.html']:
        fp = os.path.join(folder, fn)
        if os.path.exists(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                c = f.read()
            c = re.sub(r'R\s*2[,.]?599', 'R 1,199', c)
            c = re.sub(r'R\s*1[,.]?999', 'R 1,199', c)
            c = re.sub(r'R\s*12[,.]?999', 'R 4,999', c)
            c = re.sub(r'R\s*8[,.]?999', 'R 4,999', c)
            c = re.sub(r'2599', '1199', c)
            c = re.sub(r'1999', '1199', c)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(c)


def update_washing_machine():
    folder = '/Users/green/Downloads/Takealot Washing Machine'
    print("Updating Washing Machine (Port 3015)...")
    
    # 1. server.js
    sp = os.path.join(folder, 'server.js')
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8') as f:
            c = f.read()
        # Hero was 1899 or 1999 -> 1299. Old was 8999 or 8499 -> 5499.
        c = re.sub(r'R\s*1[,.]?899', 'R 1,299', c)
        c = re.sub(r'R\s*1[,.]?999', 'R 1,299', c)
        c = re.sub(r'R\s*8[,.]?999', 'R 5,499', c)
        c = re.sub(r'R\s*8[,.]?499', 'R 5,499', c)
        c = re.sub(r'amount:\s*(?:1899|1999)', 'amount: 1299', c)
        c = re.sub(r'total:\s*(?:1899|1999)', 'total: 1299', c)
        c = re.sub(r'amount\s*=\s*(?:1899|1999)', 'amount = 1299', c)
        c = re.sub(r'amount\s*\|\|\s*(?:1899|1999)', 'amount || 1299', c)
        c = re.sub(r'R\s*269', 'R 199', c)
        c = re.sub(r'R\s*279', 'R 199', c)
        c = re.sub(r'269\.00', '199.00', c)
        c = re.sub(r'279\.00', '199.00', c)
        c = re.sub(r'amount\s*=\s*(?:269|279)', 'amount = 199', c)
        c = re.sub(r'amount\s*:\s*(?:269|279)', 'amount: 199', c)
        with open(sp, 'w', encoding='utf-8') as f:
            f.write(c)

    # 2. index.html
    ip = os.path.join(folder, 'index.html')
    if os.path.exists(ip):
        with open(ip, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'id="main-price-display">R\s*[0-9,\s]+<', 'id="main-price-display">R 1,299<', c)
        c = re.sub(r'id="main-old-price">R\s*[0-9,\s]+<', 'id="main-old-price">R 5,499<', c)
        c = re.sub(r'id="footer-price-display">R\s*[0-9,\s]+<', 'id="footer-price-display">R 1,299<', c)
        c = c.replace('R 1,899', 'R 1,299').replace('R 8,999', 'R 5,499')
        c = c.replace('R 1,999', 'R 1,299').replace('R 8,499', 'R 5,499')
        c = c.replace('7,100', '4,200')
        c = c.replace('6,500', '4,200')
        # update variation dictionary in index.html
        c = re.sub(r'price:\s*["\']?(?:1899|1999)["\']?', 'price: 1299', c)
        c = re.sub(r'oldPrice:\s*["\']?R\s*(?:8,999|8,499)["\']?', 'oldPrice: "R 5,499"', c)
        with open(ip, 'w', encoding='utf-8') as f:
            f.write(c)

    # 3. checkout.html, cart.html, track.html, obrigado.html
    for fn in ['checkout.html', 'cart.html', 'track.html', 'obrigado.html']:
        fp = os.path.join(folder, fn)
        if os.path.exists(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                c = f.read()
            c = re.sub(r'R\s*1[,.]?899', 'R 1,299', c)
            c = re.sub(r'R\s*1[,.]?999', 'R 1,299', c)
            c = re.sub(r'R\s*8[,.]?999', 'R 5,499', c)
            c = re.sub(r'R\s*8[,.]?499', 'R 5,499', c)
            c = re.sub(r'1899', '1299', c)
            c = re.sub(r'1999', '1299', c)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(c)


def update_refrigerator():
    folder = '/Users/green/Downloads/Takealot Refrigerator'
    print("Updating Refrigerator (Port 3020)...")
    
    # 1. server.js
    sp = os.path.join(folder, 'server.js')
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8') as f:
            c = f.read()
        # Hero was 2199 -> 1299. Old was 9999 or 8999 -> 5499.
        c = re.sub(r'R\s*2[,.]?199', 'R 1,299', c)
        c = re.sub(r'R\s*9[,.]?999', 'R 5,499', c)
        c = re.sub(r'R\s*8[,.]?999', 'R 5,499', c)
        c = re.sub(r'amount:\s*2199', 'amount: 1299', c)
        c = re.sub(r'total:\s*2199', 'total: 1299', c)
        c = re.sub(r'amount\s*=\s*2199', 'amount = 1299', c)
        c = re.sub(r'amount\s*\|\|\s*2199', 'amount || 1299', c)
        c = re.sub(r'R\s*299', 'R 199', c)
        c = re.sub(r'299\.00', '199.00', c)
        c = re.sub(r'amount\s*=\s*299', 'amount = 199', c)
        c = re.sub(r'amount\s*:\s*299', 'amount: 199', c)
        with open(sp, 'w', encoding='utf-8') as f:
            f.write(c)

    # 2. index.html
    ip = os.path.join(folder, 'index.html')
    if os.path.exists(ip):
        with open(ip, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'id="main-price-display">R\s*[0-9,\s]+<', 'id="main-price-display">R 1,299<', c)
        c = re.sub(r'id="main-old-price">R\s*[0-9,\s]+<', 'id="main-old-price">R 5,499<', c)
        c = re.sub(r'id="footer-price-display">R\s*[0-9,\s]+<', 'id="footer-price-display">R 1,299<', c)
        c = c.replace('R 2,199', 'R 1,299').replace('R 9,999', 'R 5,499')
        c = c.replace('R 8,999', 'R 5,499')
        c = c.replace('7,800', '4,200')
        c = re.sub(r'price:\s*["\']?2199["\']?', 'price: 1299', c)
        c = re.sub(r'oldPrice:\s*["\']?R\s*(?:9,999|8,999)["\']?', 'oldPrice: "R 5,499"', c)
        with open(ip, 'w', encoding='utf-8') as f:
            f.write(c)

    # 3. checkout.html, cart.html, track.html, obrigado.html
    for fn in ['checkout.html', 'cart.html', 'track.html', 'obrigado.html']:
        fp = os.path.join(folder, fn)
        if os.path.exists(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                c = f.read()
            c = re.sub(r'R\s*2[,.]?199', 'R 1,299', c)
            c = re.sub(r'R\s*9[,.]?999', 'R 5,499', c)
            c = re.sub(r'R\s*8[,.]?999', 'R 5,499', c)
            c = re.sub(r'2199', '1299', c)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(c)


def update_playstation():
    folder = '/Users/green/Downloads/Takealot PlayStation 5'
    print("Updating PlayStation 5 (Port 3025)...")
    
    # 1. server.js
    sp = os.path.join(folder, 'server.js')
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8') as f:
            c = f.read()
        # Hero was 3299 or 3499 -> 1399. Old was 14999 or 14499 -> 5899.
        c = re.sub(r'R\s*3[,.]?299', 'R 1,399', c)
        c = re.sub(r'R\s*3[,.]?499', 'R 1,399', c)
        c = re.sub(r'R\s*14[,.]?999', 'R 5,899', c)
        c = re.sub(r'R\s*14[,.]?499', 'R 5,899', c)
        c = re.sub(r'amount:\s*(?:3299|3499)', 'amount: 1399', c)
        c = re.sub(r'total:\s*(?:3299|3499)', 'total: 1399', c)
        c = re.sub(r'amount\s*=\s*(?:3299|3499)', 'amount = 1399', c)
        c = re.sub(r'amount\s*\|\|\s*(?:3299|3499)', 'amount || 1399', c)
        c = re.sub(r'R\s*399', 'R 199', c)
        c = re.sub(r'399\.00', '199.00', c)
        c = re.sub(r'amount\s*=\s*399', 'amount = 199', c)
        c = re.sub(r'amount\s*:\s*399', 'amount: 199', c)
        with open(sp, 'w', encoding='utf-8') as f:
            f.write(c)

    # 2. index.html
    ip = os.path.join(folder, 'index.html')
    if os.path.exists(ip):
        with open(ip, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'id="main-price-display">R\s*[0-9,\s]+<', 'id="main-price-display">R 1,399<', c)
        c = re.sub(r'id="main-old-price">R\s*[0-9,\s]+<', 'id="main-old-price">R 5,899<', c)
        c = re.sub(r'id="footer-price-display">R\s*[0-9,\s]+<', 'id="footer-price-display">R 1,399<', c)
        c = c.replace('R 3,299', 'R 1,399').replace('R 14,999', 'R 5,899')
        c = c.replace('R 3,499', 'R 1,399').replace('R 14,499', 'R 5,899')
        c = c.replace('11,700', '4,500')
        c = c.replace('11,000', '4,500')
        c = re.sub(r'price:\s*["\']?(?:3299|3499)["\']?', 'price: 1399', c)
        c = re.sub(r'oldPrice:\s*["\']?R\s*(?:14,999|14,499)["\']?', 'oldPrice: "R 5,899"', c)
        with open(ip, 'w', encoding='utf-8') as f:
            f.write(c)

    # 3. checkout.html, cart.html, track.html, obrigado.html
    for fn in ['checkout.html', 'cart.html', 'track.html', 'obrigado.html']:
        fp = os.path.join(folder, fn)
        if os.path.exists(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                c = f.read()
            c = re.sub(r'R\s*3[,.]?299', 'R 1,399', c)
            c = re.sub(r'R\s*3[,.]?499', 'R 1,399', c)
            c = re.sub(r'R\s*14[,.]?999', 'R 5,899', c)
            c = re.sub(r'R\s*14[,.]?499', 'R 5,899', c)
            c = re.sub(r'3299', '1399', c)
            c = re.sub(r'3499', '1399', c)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(c)


def update_dishwasher():
    folder = '/Users/green/Downloads/Takealot Dishwasher'
    print("Updating Dishwasher (Port 3030)...")
    
    # 1. server.js
    sp = os.path.join(folder, 'server.js')
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8') as f:
            c = f.read()
        # Hero was 1999 -> 1299. Old was 8999 -> 5499.
        c = re.sub(r'R\s*1[,.]?999', 'R 1,299', c)
        c = re.sub(r'R\s*8[,.]?999', 'R 5,499', c)
        c = re.sub(r'amount:\s*1999', 'amount: 1299', c)
        c = re.sub(r'total:\s*1999', 'total: 1299', c)
        c = re.sub(r'amount\s*=\s*1999', 'amount = 1299', c)
        c = re.sub(r'amount\s*\|\|\s*1999', 'amount || 1299', c)
        c = re.sub(r'R\s*279', 'R 199', c)
        c = re.sub(r'279\.00', '199.00', c)
        c = re.sub(r'amount\s*=\s*279', 'amount = 199', c)
        c = re.sub(r'amount\s*:\s*279', 'amount: 199', c)
        with open(sp, 'w', encoding='utf-8') as f:
            f.write(c)

    # 2. index.html
    ip = os.path.join(folder, 'index.html')
    if os.path.exists(ip):
        with open(ip, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'id="main-price-display">R\s*[0-9,\s]+<', 'id="main-price-display">R 1,299<', c)
        c = re.sub(r'id="main-old-price">R\s*[0-9,\s]+<', 'id="main-old-price">R 5,499<', c)
        c = re.sub(r'id="footer-price-display">R\s*[0-9,\s]+<', 'id="footer-price-display">R 1,299<', c)
        c = c.replace('R 1,999', 'R 1,299').replace('R 8,999', 'R 5,499')
        c = c.replace('7,000', '4,200')
        c = re.sub(r'price:\s*["\']?1999["\']?', 'price: 1299', c)
        c = re.sub(r'oldPrice:\s*["\']?R\s*8,999["\']?', 'oldPrice: "R 5,499"', c)
        with open(ip, 'w', encoding='utf-8') as f:
            f.write(c)

    # 3. checkout.html, cart.html, track.html, obrigado.html
    for fn in ['checkout.html', 'cart.html', 'track.html', 'obrigado.html']:
        fp = os.path.join(folder, fn)
        if os.path.exists(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                c = f.read()
            c = re.sub(r'R\s*1[,.]?999', 'R 1,299', c)
            c = re.sub(r'R\s*8[,.]?999', 'R 5,499', c)
            c = re.sub(r'1999', '1299', c)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(c)


if __name__ == '__main__':
    update_smart_tv()
    update_washing_machine()
    update_refrigerator()
    update_playstation()
    update_dishwasher()
    print("\nAll 5 stores have been successfully updated to tickets between R 600 and R 1,500!")
