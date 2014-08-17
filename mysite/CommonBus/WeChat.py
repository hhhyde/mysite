# coding:utf8
'''
Created on 2013-9-21

@author: Chris
'''
import hashlib, time
import xml.etree.ElementTree as ET
from django.utils.encoding import smart_str, smart_unicode
class WeChat(object):
    toUserName = ''
    fromUserName = ''
    createTime = ''
    msgType = ''
    content = ''
    msgId = ''
    
    def __init__(self, req):
        rawStr = smart_str(req.raw_post_data)
        msg = self.__paraseMsgXml(ET.fromstring(rawStr))
        self.toUserName = msg['ToUserName']
        self.fromUserName = msg['FromUserName']
        self.createTime = msg['CreateTime']
        self.msgType = msg['MsgType']
        self.content = msg['Content']
        self.msgId = msg['MsgId']
    '''
        检查是否是来自微信官方的消息
    '''
    def checkSign(self, req):
        hash_sha1 = hashlib.sha1()
        signature = req.GET['signature']
        timestamp = req.GET['timestamp']
        nonce = req.GET['nonce']
        echostr = req.GET['echostr']
        args = [timestamp, nonce, 'hhhyde']
        args.sort()
        hash_sha1.update(''.join(args))
        hash_value = hash_sha1.hexdigest()
        if hash_value == signature:
            return echostr

    def __paraseMsgXml(self, rootElem):
        msg = {}
        if rootElem.tag == 'xml':
            for child in rootElem:
                msg[child.tag] = smart_str(child.text)
        return msg
    def __getReplyXml(self, msg, replyContent):
        extTpl = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>";
        extTpl = extTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), 'text', replyContent)
        return extTpl
    '''
        接受普通消息,目前只做一个原消息返回
    '''
    def getMsg(self, req):
        print 'getMsg'
        rawStr = smart_str(req.raw_post_data)
        msg = self.__paraseMsgXml(ET.fromstring(rawStr))
        return self.__getReplyXml(msg, msg['Content'])

    def send(self, req, msg):
        print 'sendMsg'
        rawStr = smart_str(req.raw_post_data)
        profile = self.__paraseMsgXml(ET.fromstring(rawStr))
        return self.__getReplyXml(profile, msg)
