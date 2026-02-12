import smtplib, ssl, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_visionary_notes():
    # UPDATED IDENTITY
    sender_email = "prxject64@gmail.com"
    receiver_email = "damarieusj@gmail.com" # Keeping target as damarieusj
    
    print("\n--- SOVEREIGN ESTATE EMAIL GATEWAY (PRXJECT64) ---")
    raw_password = getpass.getpass("Paste App Password (rldc alwx hxum ipra): ")
    password = raw_password.replace(" ", "")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Sovereign Estate: ARC & CC Visionary Notes"
    message.attach(MIMEText("Visionary, find your estate data attached.", "plain"))

    filename = "visionary_notes.zip"
    filepath = f"/home/ubuntu/sovereign_estate/{filename}"

    try:
        with open(filepath, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        message.attach(part)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls(context=ssl.create_default_context())
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        
        print(f"\n✅ SUCCESS: Sent from {sender_email} to {receiver_email}")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    send_visionary_notes()
