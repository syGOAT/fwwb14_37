
class JiZhang:
    superclass = None
    subclass = None
    money = ''
    shop = ''
    detailed = ''
    

kind = ['traffic', 'office', 'daily', 'service', 'digital_appliance', 
        'rent_decoration', 'communication', 'lodging', 'post', 
        'medical_treatment', 'repast', 'foodstuff', 'raiment', 
        'vehicle', 'education', 'other']
kind_classify = [('出行', None), ('其他', '办公'), ('购物', '日用'), 
                 (None, None), ('购物', '数码电器'), ('生活', '房租装饰'), 
                 ('生活', '生活缴费'), ('生活', '住宿'), ('生活', '快递'),
                 ('生活', '医疗'), ('饮食', '餐饮'), ('饮食', None), 
                 ('购物', '服饰'), ('出行', '用车'), ('教育', '学习'), 
                 (None, None), ]

type = ['air_transport', 'blockchain_electronic_invoice', 'education_receipt', 
        'general_machine_invoice', 'highway_passenger_invoice', 'machine_printed_invoice', 
        'medical_receipt', 'motor_vehicle_sale_invoice', 'non_tax_income_unified_bill', 
        'parking_invoice', 'passenger_transport_invoice', 'quota_invoice', 
        'shipping_invoice', 'shop_receipt', 'taxi_ticket', 'train_ticket', 
        'travel_transport', 'used_car_purchase_invoice', 'vat_common_invoice', 
        'vat_electronic_invoice', 'vat_electronic_special_invoice', 
        'vat_electronic_toll_invoice', 'vat_electronic_invoice_new', 
        'vat_electronic_special_invoice_new', 'vat_invoice_sales_list', 
        'vat_roll_invoice', 'vat_special_invoice', 'vat_transport_invoice', 
        'vehicle_toll', 'other']

vat_items = ('vat_invoice_price', 'vat_invoice_seller_name', 'vat_invoice_goods_list')
moto_items = ('vehicle_invoice_total_price_digits', 'vehicle_invoice_dealer', None)
usedcar_items = ('vehicle_invoice_total_price_digits', 'vehicle_invoice_seller', 'vehicle_invoice_note')
vatroll_items = ('total_money', 'sold_name', None)
toll_items = ('money', None, None)
quota_items = ('money_small', None, None)
taxi_items = ('sum', None, None)
air_items = ('total', 'issued_by', None)
train_items = ('price', None, None)
general_items = ('money', 'seller', None)
ship_items = ('money', None, None)
passenger_items = ('money', None, None)
parking_items = ('money', None, None)
vatsales_items = ('tax_total', 'seller_name', None)
shop_items = ('money', 'shop', 'sku')
medical_items = ('amount_small', 'medical_institution_type', None)
travel_items = ('total_money', None, None)
income_items = ('TotalAmount', 'ItemUnit', 'Remark')
none_items = (None, None, None)  # education_receipt、vat_transport_invoice 无法结构化识别

type_classify = [('出行', '飞机', air_items), (None, None, vat_items), ('教育', '学习', none_items), 
                 (None, None, general_items), ('出行', '客车', passenger_items), (None, None, vat_items), 
                 ('生活', '医疗', medical_items), ('出行', '用车', moto_items), ('收入', '其他收入', income_items), 
                 ('出行', '停车费', parking_items), ('出行', None, passenger_items), (None, None, quota_items), 
                 ('出行', '船运', ship_items), (None, None, shop_items), ('出行', '打车', taxi_items), 
                 ('出行', '火车', train_items), ('出行', None, travel_items), ('出行', '用车', usedcar_items), 
                 ('税务', '增值税', vat_items), ('税务', '增值税', vat_items), ('税务', '增值税', vat_items), 
                 ('税务', '增值税', vat_items), ('税务', '增值税', vat_items), ('税务', '增值税', vat_items), 
                 ('税务', '增值税',vatsales_items), ('税务', '增值税', vatroll_items), ('税务', '增值税', vat_items), 
                 ('税务', '增值税', none_items), ('出行', '过路费', toll_items), (None, None, none_items), ]

jz = JiZhang()


def first_classify(bill):  
    i = kind.index(bill['kind'])
    jz.superclass = kind_classify[i][0]
    jz.subclass = kind_classify[i][1]

def second_classify(bill):
    i = type.index(bill['type'])
    if jz.superclass == None:
        jz.superclass = type_classify[i][0]
    if jz.subclass == None:
        jz.superclass = type_classify[i][1]
    return i


def other_items(bill, i):
    item_list = bill['item_list']
    item_names = type_classify[i][2]
    for item in item_list:
        if item['key'] == item_names[0]:
            jz.money = item['value']
        elif item['key'] == item_names[1]:
            jz.shop = item['value']
        elif item['key'] == item_names[2]:
            jz.detailed = item['value'].replace('\n', ' ')


def jizhang(bill):
    first_classify(bill)
    i = second_classify(bill)
    other_items(bill, i)

    if jz.superclass in [None, '餐饮'] and jz.subclass is None:
        snack = [
            "薯片", "饼干", "君乐宝", "糖", "奶", "茶", "可乐", "果冻", "巧克力", "酥", "蛋糕", "点心", "干脆面", "辣条",
            "锅巴", "仙贝", "虾条", "小馒头", "海苔", "蛋卷", "泡芙", "奶油", "面包", "派", "Q蒂", "沙琪玛", "魔芋", "肉脯", "君乐宝",
            "真果粒", "金典", "特仑苏", "山楂树下", "优酸乳", "AD钙", "营养快线", "发酵乳", "优乐美", "蜜饯", "鱼干", "香肠",
            "罐头", "卤鸡蛋", "元気森林", "牛肉干", "红牛", "脉动", "健力宝", "康师傅", "健力宝", "加多宝", "娃哈哈", "锐澳",
            "王老吉", "伊利", "蒙牛", "东方树叶", "盼盼", "三得利", "旺仔", "雪碧", "雀巢", "李子园", "海河", "喜之郎",
            "旺旺", "芬达", "乐事", "卫龙", "健达", "士力架", "费列罗", "德芙", "脆香米", "花花牛", "统一", "银鹭", "达利园",
            "三只松鼠", "炫迈", "益达", "星巴克", "安慕希", "纯甄", "真巧", "徐福记", "上好佳", "乐吧", "米多奇", "小浣熊",
            "佳龙", "曲奇", "好丽友", "呀土豆", "妙脆角", "浪味仙", "米老头", "笨笨狗", "好多鱼", "可比克", "好有趣", "百草味",
            "溜溜梅", "金丝猴", "大白兔", "奥利奥","阿尔卑斯", "金丝猴", "纳宝帝", "百醇", "格力高", "嘉士利", "美丹", "好吃点",
            "铜锣烧", "蘑古力", "星球杯", "绿箭", "雪饼", "奶酪", "芝士条", "果然多", "谷粒多", "百奇", "百力滋", "麦丽素",
            "洋葱圈", "冰淇淋", "爆米花", "话梅", "葡萄干", "甜甜圈", "甜筒", "猫耳朵", "桃酥", "果丹皮", "千层脆", "趣多多"
        ]
        garden = [
            "苹果", "梨", "香蕉", "菠萝", "草莓", "橙", "橘子", "柠檬", "瓜", "甘蔗", "火龙果", "提子",
            "葡萄", "芒果", "枇杷", "桃", "李子", "樱桃", "石榴", "柿子", "杏", "榴莲", "梅子", "无花果",
            "柚子", "红枣", "荔枝", "龙眼", "桑葚", "板栗", "山竹", "山楂", "椰子", "蓝莓", "百香果", "桂圆",
            "毛红丹", "桔", "大蕉", "青柠", "圣女果", "黄瓜", "牛油果", "番茄", "罗汉果", "豆", "菇", "葱",
            "莲藕", "笋", "山药", "菜", "蒜苗", "水芹", "甘蓝", "姜", "大蒜", "芋头", "红薯", "紫薯",
            "马铃薯", "西红柿", "萝卜", "海带", "芽", "椒", "茄子", "灵芝", "松茸", "竹荪", "木耳", "银耳",
            "葫芦", "芜菁", "牛蒡", "莴苣", "茴香", "芝麻", "花生", "大米", "牛肝菌", "玉米", "西蓝花", "薄荷",
            "秋葵", "上海青", "魔芋", "菊苣", "鱼腥草", "鸡蛋"
        ]
        is_snack = False
        is_garden = False
        for i in snack:
            if i in jz.detailed:
                jz.superclass = '饮食'
                jz.subclass = '零食'
                is_snack = True
                break
        if is_snack is False:
            for i in garden:
                if i in jz.detailed:
                    jz.superclass = '饮食'
                    jz.subclass = '果蔬'
                    is_garden = False
                    break
        if (is_snack or is_garden) is False:
            if '外卖' in jz.detailed:
                jz.superclass = '饮食'
                jz.subclass = '餐饮'

   
    return {
        'superclass': jz.superclass, 
        'subclass': jz.subclass, 
        'money': jz.money, 
        'shop': jz.shop, 
        'detailed': jz.detailed, 
    }



    
