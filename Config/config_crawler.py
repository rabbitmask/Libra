#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

file_type_black = ['.css',
                    '.jpg', 'png', 'bmp', '.gif', 'ico', 'svg', 'jpeg',
                    '.zip', '.rar', '.7z','.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.bz2',
                    '.exe','.msi','.dmg','.deb','.rpm','.app','.apk'
                    '.doc', '.xls', '.xlsx', '.pdf','.ppt', '.pptx', '.odt', '.ods', '.odp',
                    '.mp3', '.mp4', '.wmv','.avi', '.mov', '.mkv', '.flv', '.webm', '.m4v', '.3gp','.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a',
                    '.ttf','.tiff', '.tif', '.psd', '.raw', '.cr2', '.nef', '.webp','.otf', '.woff', '.woff2', '.eot',
                    '.db', '.sqlite', '.mdb', '.accdb','.iso', '.bin', '.img', '.vmdk', '.log', '.bak', '.tmp'
                    'mailto', 'javascript', 'data:image',
                   ]  # 文件爬取黑名单，以上内容不爬取