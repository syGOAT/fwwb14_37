import json
import base64
import jizhang
from textinapi import CommonOcr
import os

def main(img_url):
    try:
        response = CommonOcr(img_url)
        #result = response.crop_enhance() 
        result = response.dewarp()

        result = json.loads(result)  
        #pic_bs64 = result['result']['image_list'][0]['image']
        pic_bs64 = result['result']['image']
        pic = base64.b64decode(pic_bs64)

        result = response.recognize(pic)
        result = json.loads(result)
        
        bills = result['result']['object_list']
        for bill in bills:
            jzdict = jizhang.jizhang(bill)
            break  # 官方api允许一张图多个票据，这里只提供识别出的第一张票据，如果要扩展后面再改
        
        result = response.general_ocr(pic)
        result = json.loads(result)
        lines = result['result']['lines']
        contents = []
        for line in lines:
            contents.append(line['text'])
        all_words = ' '.join(contents)
        jzdict['all'] = all_words
        print(json.dumps(jzdict, ensure_ascii=False))
        return json.dumps(jzdict)

    except Exception as e:
        pass



if __name__ == '__main__':
    main('http://1.15.179.24:8001/api/file/a13bcd5b-6ad1-4db7-a847-70210c7f68f3.jpg')
