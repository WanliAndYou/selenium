# conding: utf-8
# 准备邮箱账号，邮箱服务器地址, 邮箱授权码
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 收发人
sender = "waitforxy@126.com"
# recevier = "2235236875@qq.com"
recevier = "iswanli@163.com"

# 邮箱服务器
mail_server = "smtp.126.com"

# 不用密码发送，使用授权码
auth_code = "xdclass123"

# 主题
subject = "自动化测试报告"
attach_subject = "测试报告主题"

# 读发送内容
f = open(r"./project/2020-05-09 16_11_48_result.html", 'rb')
mail_body = f.read()
f.close()

# msg = MIMEText("<html><h2>我来了，地球人小犬</h2></html>", _subtype="html", _charset="utf-8")
# msg = MIMEText("", _subtype="png", _charset="utf-8")
# msg["Subject"] = subject
# msg["from"] = sender
# msg["to"] = recevier

msg_html = MIMEText(mail_body, _subtype="html", _charset="utf-8")
msg_html["Subject"] = subject
msg_html["from"] = sender
msg_html["to"] = recevier

# 将测试报告放在附件中发送

att1 = MIMEText(mail_body, "base64", 'gb2312')
att1["Content-Type"] = "application/octet-stream"
att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
msg = MIMEMultipart()
msg["Subject"] = attach_subject
msg.attach(msg_html) # 将html附加在msg里
msg.attach(att1) # 新增一个附件



# 连接smtp服务器，并登陆发送用户
smtp = smtplib.SMTP()
smtp.connect(mail_server)
smtp.login(sender, auth_code)

# 发送邮件
smtp.sendmail(sender, recevier, msg.as_string())
smtp.quit()

