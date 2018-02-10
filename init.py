# -*- coding: utf-8 -*-

"该脚本用于初始化项目"

import os
import time


def show_log(info):
    "显示日志"

    print time.strftime("%H:%M:%S ") + info


def mkdir_and_mkfile(dir_name, file_name_list):
    "创建指定目录并在目录内添加指定文件"

    if os.path.exists(dir_name):
        show_log('The directory ' + dir_name + ' already exists !')
        return 0
    else:
        os.mkdir('./' + dir_name)      # 创建指定目录
        show_log('Successfully create the directory: ' + dir_name)
        for file_name in file_name_list:
            # 创建指定文件
            text_file = open('./' + dir_name + '/' + file_name, 'w')
            if file_name[len(file_name) - 2:] == 'py':
                # 识别 .py 文件加入 utf-8 声明
                text_file.writelines('# -*- coding: utf-8 -*-')
            elif file_name[len(file_name) - 2:] == 'md':
                # 识别 .md 文件加入标题
                data = '# Example ' + dir_name + '\n' * 2
                data += '## Description' + '\n' * 4
                data += '## Analysis' + '\n' * 4
                data += '## Source' + '\n' * 2
                data += '```python\n\n```\n'
                text_file.writelines(data)
            else:
                pass
            text_file.close()


if __name__ == '__main__':

    os.mkdir('./source')        # 创建 source 目录
    os.chdir('./source')        # 进入 source 目录

    for num in range(1, 101):
        dn = '%03d' % num
        fnl = ('README.md', dn + '.py')
        mkdir_and_mkfile(dn, fnl)

    raw_input('Press any key to continue ...')
