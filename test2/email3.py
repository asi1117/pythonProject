import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import  Header
#设置域名，发件人邮箱，邮箱授权吗，收件人邮箱
mail_host ="smtp.gmail.com"
mail_sender ="mingd899@gmail.com"
mail_license="jkrhavgnxfeytssk"
mail_recivers =["luy984361@gmail.com","1319816348@qq.com","cwu908666@gmail.com"]
mm =MIMEMultipart('related')
#设置邮件头部内容
subject_content ="test"
mm["From"]="sender_name<jkrhavgnxfeytssk>"
mm["To"] ="receiver_1_name<luy984361@gmail.com>,receiver_2_name<1319816348@qq.com>,receiver_3_name<cwu908666@gmail.com>"
mm["Subject"] =Header(subject_content,'utf-8')
#添加正文文本
body_content ="您好这是测试"
message_text =MIMEText(body_content,"plain","utf-8")
mm.attach(message_text)
#添加图片
image_data =open('data/a.png','rb')
message_image =MIMEImage(image_data.read())
image_data.close()
mm.attach(message_image)
#添加附件(excel)
# atta =MIMEText(open('.xlsx','rb').read(),'base64','utf-8')
# atta["Content-Disposition"]='attachment;filename=.xlsx'
# stp =smtplib.SMTP(mail_host)
#发送邮件
stp =smtplib.SMTP_SSL(mail_host,465)
print(mail_host)
stp.set_debuglevel(1)
stp.login(mail_sender,mail_license)
stp.sendmail(mail_sender,mail_recivers,mm.as_string())
print("发送成功")
stp.quit()