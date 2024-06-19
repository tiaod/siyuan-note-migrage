import dotenv
dotenv.load_dotenv()

import os
import re
input_folder = os.environ.get('INPUT_FOLDER')

# 递归处理input_folder里面的所有.md文件
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.md'): 
            # 打开文件
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                #   则匹配文件里面的img标签，进行替换
                if re.search(r'<img.*?src=\"(.*?)\".*?>', content):
                    print(f'处理文件：{file}')
                    with open(os.path.join(root, file), 'w', encoding='utf-8') as f:
                        # 替换img标签
                        content = re.sub(r'<img.*?src=\"(.*?)\".*?>', r'![](\1)', content)
                        # 写入回文件
                        f.write(content)