import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("kenuchiha98@gmail.com", "darklight1010")
server.sendmail(
  "fromkencuhiha98@gmail.com", 
  "tokenuchiha98@gmail.com", 
  "this message is from python")
server.quit()