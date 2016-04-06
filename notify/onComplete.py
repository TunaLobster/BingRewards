#!/usr/bin/env python2

#
#Developed by Charles Johnson (2014)
#for use in Sergey Markelov's BingRewards
#
#In order to use this scprit please put the password for your Live account here
password = 'your_password_here'
#As such this will only work with one account right now
#

import os, smtplib, datetime, urllib, urllib2, argparse, sys

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'pkg')))

#from config import Config, BingRewardsReportItem, AccountKey

parser = argparse.ArgumentParser(description="Sends an email over SMTP with information passed from config.xml")

#Command line arguments passed from main.py
parser.add_argument('input', metavar='%a %p %r %P %l %i', nargs=6, type=str, help='Default options from config. The order is important!')

#Parse all args
args = parser.parse_args()

account = args.input[0]
points = args.input[1]
retries = args.input[2]
totalPoints = args.input[3]
lifeCredits = args.input[4]
ifStatement = args.input[5]
date = str(datetime.datetime.now().date())
type = account[:account.index("_")]
email = account[account.index("_")+1:]

#Check for Live accountType
if type[0] != "L": raise ValueError("Accounts of type %s are not supported" % (type))

#Connects to Live SMTP and sends message
try:
    smtpserver = smtplib.SMTP("smtp.live.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(email, password)
    header = 'To: %s\nFrom: BingRewards Notify Script' % (email)
    msg = header + 'Success!\n\nAccount: %s\nPoints: %s\nRetries: %s\nTotal Points: %s\nLife Credits: %s\nifStatement: %s\n\nDate: %s' % (account, points, retries, totalPoints, lifeCredits, ifStatement, date)
    print msg
    smtpserver.sendmail(email, email, msg)
    print 'Message sent!'
except smtplib.SMTPAuthenticationError:
    print "Could not auth SMTP with %s" % (email)
    print
