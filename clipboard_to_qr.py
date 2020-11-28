import qrcode

import win32clipboard as w
import win32con
import chardet  #八进制转中文

# from PIL import Image

def getText():
    "读取剪切板"
    w.OpenClipboard()
    try:
        byte_str = w.GetClipboardData(win32con.CF_TEXT) #得到剪切板上的八进制数据
    except TypeError:
        byte_str = '格式错误，请确保当前剪切板内容为文本。'
        print(byte_str)
        return byte_str
    finally:
        w.CloseClipboard()

    byte_str_charset = chardet.detect(byte_str)  # 获取字节码编码格式
    byte_str = str(byte_str, byte_str_charset.get('encoding'))  # 将八进制字节转化为字符串
    return byte_str

def generateQr(qrStr):
    "根据字符串生成qr码"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qrStr)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def saveQr(qrImg, saveName='qr_code.png', isShow=True):
    "保存生成的二维码"
    qrImg.save(saveName)
    if isShow:
        # 展示二维码
        qrImg.show()

# def saveQrWithImage(qrImg, imageName, saveName='qr_code.png', isShow=True):
#     "将生成的二维码与一张图片结合并保存"
#     # 添加头像，打开头像照片
#     icon = Image.open(imageName)
#     # 获取图片的宽高
#     img_w, img_h = qrImg.size
#     # 参数设置头像的大小
#     factor = 6
#     size_w = int(img_w / factor)
#     size_h = int(img_h / factor)
#     icon_w, icon_h = icon.size
#     if icon_w > size_w:
#         icon_w = size_w
#     if icon_h > size_h:
#         icon_h = size_h
#     # 设置头像的尺寸
#     icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

#     w = int((img_w - icon_w) / 2)
#     h = int((img_h - icon_h) / 2)
#     # 粘贴头像
#     qrImg.paste(icon, (w, h), mask=None)
#     # 保存img
#     qrImg.save(saveName)
#     if isShow:
#         # 展示二维码
#         qrImg.show()

if __name__ == "__main__":
    data = getText()
    saveQr(generateQr(data))