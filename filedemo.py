#coding=utf8
from urllib3 import encode_multipart_formdata
import requests



def sendFile(filename, file_path):
  '''

  :param filename:
  :param file_path:
  :return:
  '''

  #请求的接口地址
  url = "http://192.168.1.6:8666/cloudApi/fileUpload/doUpload"
  with open(file_path, mode="r", encoding="utf-8")as f: # 打开文件
    file = {
    "file": (filename, f.read()),
    "bussCode":"questionBankPic"
    }

  encode_data = encode_multipart_formdata(file)

  file_data = encode_data[0]
  # b'--c0c46a5929c2ce4c935c9cff85bf11d4\r\nContent-Disposition: form-data; name="file"; filename="1.txt"\r\nContent-Type: text/plain\r\n\r\n...........--c0c46a5929c2ce4c935c9cff85bf11d4--\r\n

  headers_from_data = {
  "Content-Type":"application/octet-stream"
  }
  # token是登陆后给的值，如果你的接口中头部不需要上传字段，就不用写，只要前面的就可以
  # 'Content-Type': 'multipart/form-data; boundary=c0c46a5929c2ce4c935c9cff85bf11d4'，这里上传文件用的是form-data,不能用json

  response = requests.post(url=url, headers=headers_from_data, data=file_data).json()
  return response

if __name__ == '__main__':
  # 上传文件

  res = sendFile("zxz图片", r"C:\Users\Admin\PycharmProjects\pythonProject\mg .jpg")  # 调用sendFile方法
  if __name__ == '__main__':

    # python3

    # 以读入文件为例：

    f = open(r"C:\Users\Admin\PycharmProjects\pythonProject\ooo.png", "rb")  # 二进制格式读文件

    while True:

      line = f.readline()

      if not line:

        break

      else:

        try:

          # print(line.decode('utf8'))

          line.decode('utf8')

          # 为了暴露出错误，最好此处不print

        except:

          print(str(line))