from bs4 import BeautifulSoup
import requests
import sys
import io

# Thiết lập mã hóa cho stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Bước 1: Gửi yêu cầu đến trang web
url = 'https://vov.vn/xa-hoi/gian-nan-nhung-chuyen-xe-0-dong-den-vung-lu-kho-khan-nhat-o-lao-cai-post1123671.vov'
response = requests.get(url)

# Bước 2: Tạo đối tượng Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Bước 3: Trích xuất tóm tắt
summary_div = soup.find('div', class_='article-summary')
summary = summary_div.find('h2').get_text(strip=True) if summary_div else 'Tóm tắt không tìm thấy'

# Bước 4: Trích xuất nội dung
content_div = soup.find('div', class_='article-content')
content_paragraphs = content_div.find_all('p') if content_div else []
content = '\n'.join([p.get_text(strip=True) for p in content_paragraphs])

# In kết quả
print(f'Title: {summary}')  # Bạn có thể thay đổi điều này nếu có tiêu đề khác
print('Content:')
print(content)
