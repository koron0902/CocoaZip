import codecs
import os
          
class ErrorMessageManager():
    '''
    エラーメッセージを管理するクラス
    '''
    
    MESSAGE = {}
    
    def __init__(self):
        '''
        初期化を行う。
        '''
        self.hasErrors = False
        self.parentCell = None
                        
    def RefreshMessage(self, lang):
        '''
        エラーメッセージファイルからエラーメッセージを読込む
        
        :param path(string): エラーメッセージファイルのパス  
        '''
        f = open(os.path.join(*[os.path.dirname(__file__), "message", lang]), 'r', encoding='utf-8')
        for row in f:
            try:
                row = str(row)
            except:
                row = str(row,errors='ignore')
                    
            errorno, level, msg = row.split(':',2)
            self.MESSAGE[errorno] = (level, msg)
                
    def AppendMessage(self, errorno, **kwargs):
        '''
        エラーメッセージを登録する
        
        :param errorno(string): エラーメッセージ番号
        :param　parameters(list): エラーメッセージのパラメータ
        '''
        level = msg = None
        if str(errorno) in self.MESSAGE:
            level, msg = self.MESSAGE[str(errorno)]
            
            if kwargs:
                msg = msg.format(**kwargs)
            
        if level == '1':
            msg = '[ERROR]:[{}]:{}'.format(errorno, msg)
            self.hasErrors = True
        elif level == '2':
            msg = '[WARNING]:[{}]:{}'.format(errorno, msg)
        else:
            msg = '[{}]:{}'.format(errorno, msg)
            
        print (msg)
        return self

    def HasErrors(self):
        '''
        エラーメッセージが存在するかどうかを返す。
        
        :param errorno(string): エラーメッセージ番号 
        :return: エラーメッセージが存在する場合True,存在しない場合False
        :return　type: boolean
        '''
        return self.hasErrors
    
    def Assert(self, **kwargs):
        '''
        エラーメッセージが存在する場合ツールの実行を終了する
        
        '''
        if self.hasErrors:
            exit("!!!!!! ABORT !!!!!!")