import os #import system 用isfile確認有沒有檔案

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue #continue
            name, price = line.strip().split('')
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products): 
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    print(products)

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], 'price is', p[1])

#寫入檔案
def write_file(filename, products):
    with open ('products.csv', 'w', encoding = 'UTF-8') as f:
        f.write('商品, 價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

#main
def main():
    filename = 'product.csv'
    if os.path.isfile(filename):
        print('找到檔案了')
        products = read_file(filename)
    else:
        print('找不到檔案')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()