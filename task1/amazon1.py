import os

# 更安全的路径构建
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
file_name = 'Amazon. popular .html'
file_path = os.path.join(desktop_path, file_name)

# 其余代码保持不变...
from bs4 import BeautifulSoup
import os


def parse_bestseller_categories(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 查找列表容器
    ul = soup.find('ul', {
        'class': 'a-unordered-list a-nostyle a-vertical _p13n-zg-nav-tree-all_style_zg-browse-group__88fbz',
        'role': 'group'
    })

    if not ul:
        return []

    # 提取所有列表项
    categories = []
    for li in ul.find_all('li', class_='_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf'):
        # 查找链接元素
        a_tag = li.find('a')
        if a_tag:
            # 获取文本并清理
            category_name = a_tag.get_text(strip=True)
            if category_name:
                categories.append(category_name)

    return categories


# 文件路径 - 使用原始字符串表示法解决路径问题
file_path = r"C:\Users\赵锐锋\Desktop\Amazon. popular .html"

try:
    # 使用UTF-8编码读取文件
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 解析类目
    categories = parse_bestseller_categories(html_content)

    if not categories:
        print("未找到商品分类数据，请检查HTML文件结构。")
    else:
        print("亚马逊最佳销售商品分类:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

except FileNotFoundError:
    print(f"错误：文件未找到 - {file_path}")
    print("请检查：1. 文件路径是否正确 2. 文件名是否为'Amazon. popular .html'")
except Exception as e:
    print(f"处理文件时出错: {str(e)}")