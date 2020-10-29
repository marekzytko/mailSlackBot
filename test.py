from imap_tools import MailBox, AND
import time
import os
import requests
import logging
from slackeventsapi import SlackEventAdapter
from slack import WebClient
import os
import sys

MAIL = 'kn.whitehats@pwr.edu.pl'
PASSWORD = os.environ["MAIL_PASSWORD"]
IMAP_SERVER = 'mail.pwr.wroc.pl'

SLEEP_TIME = 10

mailbox = MailBox(IMAP_SERVER)

# Create a SlackClient for your bot to use for Web API requests
SLACK_BOT_TOKEN = os.environ["SLACK_TOKEN"]


def sendToSlack(msg: str, token: str):
    slackClient = WebClient(token)
    slackClient.chat_postMessage(channel='G01E0FE3KR7', text=msg)
    

try:
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('logging in...')

    mailbox = MailBox(IMAP_SERVER)
    mailbox.login(MAIL, PASSWORD)

    logging.debug('Mail counting...')

    nCount = len([msg.subject for msg in mailbox.fetch(AND(all=True))])
    print(nCount)
    while True:
        # get list of email subjects from INBOX folder - equivalent verbose version
        mailbox = MailBox(IMAP_SERVER)
        mailbox.login(MAIL, PASSWORD)

        
        temp = mailbox.fetch(AND(all=True))
        mails = []
        for msg in temp:
            mails.append((msg.subject, msg.from_, msg.text[:120]+'...'))
            
        #subjects = [msg.subject for msg in mailbox.fetch(AND(all=True))]
        
        if len(mails) == nCount:
            logging.debug('No new messages')
            
        else:
            logging.debug("New message arrived!")
            logging.debug(f'Subject: {mails[-1][0]}')
            count = len(mails)
            sendToSlack(f'[MAIL]:\nOd: {mails[-1][1]}\nTemat: *{mails[-1][0]}*\n```{mails[-1][2]}```', SLACK_BOT_TOKEN)
        nCount = len(mails)
        logging.debug(len(mails))
        logging.debug(f'sleeping {SLEEP_TIME} seconds...')
        time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
    print('logging out...')
    mailbox.logout()
