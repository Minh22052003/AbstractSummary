import os
import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

data_folder = 'original'

# Kiểm tra xem thư mục có tồn tại không
if not os.path.exists(data_folder):
    print(f"Thư mục {data_folder} không tồn tại.")
else:
    print(f"Thư mục {data_folder} tồn tại.")


def extract_article_data(file_content):
    lines = file_content.split('\n')
    data = {
        'Title': '',
        'Source': '',
        'Link': '',
        'Published Date': '',
        'Author': '',
        'Tags': '',
        'Summary': '',
        'Content': ''
    }

    content_start = False
    content_lines = []
    for line in lines:
        if line.startswith('Title:'):
            data['Title'] = line[len('Title:'):].strip()
        elif line.startswith('Source:'):
            data['Source'] = line[len('Source:'):].strip()
        elif line.startswith('Link:'):
            data['Link'] = line[len('Link:'):].strip()
        elif line.startswith('Published Date:'):
            data['Published Date'] = line[len('Published Date:'):].strip()
        elif line.startswith('Author:'):
            data['Author'] = line[len('Author:'):].strip()
        elif line.startswith('Tags:'):
            data['Tags'] = line[len('Tags:'):].strip()
        elif line.startswith('Summary:'):
            data['Summary'] = line[len('Summary:'):].strip()
        elif line.startswith('Content:'):
            content_start = True  # Nội dung bắt đầu sau Content
        elif content_start:
            content_lines.append(line.strip())

    data['Content'] = ' '.join(content_lines)
    return data

def prepare_dataset_to_csv(data_folder, output_csv):
    check =1
    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Title', 'Source', 'Link', 'Published Date', 'Author', 'Tags', 'Summary', 'Content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for cluster_folder in os.listdir(data_folder):
            cluster_path = os.path.join(data_folder, cluster_folder)

            if os.path.isdir(cluster_path):

                for original_folder in os.listdir(cluster_path):
                    original_path = os.path.join(cluster_path, original_folder)

                    if os.path.isdir(original_path):
                        for file_name in os.listdir(original_path):
                            file_path = os.path.join(original_path, file_name)

                            if os.path.isfile(file_path) and file_name.endswith('.txt'):
                                try:
                                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                        content = f.read()

                                    article_data = extract_article_data(content)
                                    writer.writerow(article_data)
                                except Exception as e:
                                    print(f"Lỗi khi đọc tệp {file_path}: {e}")
                            else:
                                print(f"{file_name} không phải là tệp .txt hoặc không phải là tệp.")
                    else:
                        print(f"{original_folder} không phải là thư mục.")

                



output_csv = 'dataset.csv'

prepare_dataset_to_csv(data_folder, output_csv)
