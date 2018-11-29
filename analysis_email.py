import imaplib
import email  #导入两个库

def analysis_email():
    conn = imaplib.IMAP4_SSL(port = '993',host = 'imap.163.com')
    print('已连接服务器')
    conn.login('xq_liu1103@163.com','password')
    print('已登陆')
    conn.select()
    type, data = conet.search(None, 'ALL')
    newlist = data[0].split()
    type, data = conet.fetch(newlist[0], '(RFC822)')
    msg = email.message_from_string(data[0][1].decode('utf-8'))
    sub = msg.get('subject')
    # 用get()获取标题并进行初步的解码。
    subdecode = email.header.decode_header(a)[0][0]
    # 打印标题
    print(subdecode.decode('utf-8'))
    for part in msg.walk():
        # 如果ture的话内容是没用的
        if not part.is_multipart():
            print(part.get_payload(decode=True).decode('utf-8'))
            # 解码出文本内容，直接输出来就可以了。
