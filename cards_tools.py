# 记录所有的名片字典
cards_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)

    # 1.提示用户输入详细的名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3.将名片字典添加到列表中
    cards_list.append(card_dict)
    print(cards_list)
    # 4.提示用户添加成功
    print("添加 %s名片成功" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)

    # 判断是否存在名片记录，如果不存在，提示用户使用新增功能
    if len(cards_list) == 0:
        print("名片列表里面没有记录，请使用新增功能")
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")

    # 打印分割符号
    print("=" * 50)

    # 遍历名片列表依次输出字典信息
    for card_dict in cards_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2.遍历名片列表，查询要搜索的姓名，如果没有，需要提示用户
    for card_dict in cards_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 针对找到的名片进行修改和删除操作
            deal_dict(card_dict)

            break
    else:
        print("抱歉，没有找到%s" % find_name)


# 处理名片
def deal_dict(find_card):
    """
    处理查找到的名片
    :param find_card:查找到的名片
    """
    # print(find_card)
    action_str = input("请选则要执行的操作  1：修改  2：删除  0：返回上级菜单")
    if action_str == "1":
        find_card["name"] = input_card_info(find_card["name"], "请输入姓名[回车不修改]：")
        find_card["phone"] = input_card_info(find_card["phone"],"请输入电话[回车不修改]：")
        find_card["qq"] = input_card_info(find_card["qq"],"请输入qq[回车不修改]：")
        find_card["email"] = input_card_info(find_card["email"],"请输入邮箱[回车不修改]：")
        print("修改名片成功")
    elif action_str == "2":
        cards_list.remove(find_card)
        print("删除名片成功")


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str

    # 3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value
