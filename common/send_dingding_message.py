# coding=utf-8
from dingtalkchatbot import chatbot
from common import common_util


class SendDingDindMsg:
    def __init__(self, web_hook, msg):
        self.web_hook = web_hook
        self.msg = msg

    def send_dingding_message(self, message_type="text", is_at_all=False, at_mobiles=None):
        result = None
        ding_robot = chatbot.DingtalkChatbot(self.web_hook)
        if message_type == "text":
            if isinstance(self.msg, str):
                result = ding_robot.send_text(msg=self.msg, is_at_all=is_at_all, at_mobiles=at_mobiles)
        elif message_type == "link":
            # msg={title="测试标题",text="this is 内容",message_url="http://132.232.15.12/jky/#/personnel/employeeinfo"}
            if isinstance(self.msg, dict):
                result = ding_robot.send_link(**self.msg)
            else:
                print("msg数据类型错误")
        elif message_type == "markdown":
            # msg={title="测试标题",text="this is 内容"}
            if isinstance(self.msg, dict):
                title = self.msg['title']
                text = self.msg['text']
                result = ding_robot.send_markdown(title=title, text=text, is_at_all=is_at_all, at_mobiles=at_mobiles)
            else:
                print("msg数据类型错误")
        elif message_type == "send_feed_card":
            if isinstance(self.msg, list):
                links = []
                # title = "测试feedcard",message_url = "http://132.232.15.12/jky/#/personnel/employeeinfo",\
                # pic_url="http://pic18.nipic.com/20120103/8993051_170340691334_2.jpg"
                for m in self.msg:
                    if isinstance(m, dict):
                        link = chatbot.FeedLink(**m)
                        links.append(link)
                    else:
                        print("msg中有类型错误")
                if links:
                    result = ding_robot.send_feed_card(links=links)
            else:
                print("msg数据类型错误")
        elif message_type == "ActionCard":
            if isinstance(self.msg, dict):
                action_card = chatbot.ActionCard(**self.msg)
                result = ding_robot.send_action_card(action_card)
            else:
                print("msg数据类型错误")
        else:
            print("msg_type错误")
        return result


def get_markdown_template() -> str:
    markdown_template = """
    接口测试概要（${host}）
    测试系统:${test_sys}
    测试模块:${test_modules}
    整体结果: ${result_all}
    测试开始时间：${start_time}
    测试结束时间：${end_time}
    持续时间：${duration}
    测试接口总数：${total}
    成功：${success_num} || 失败：${fail_num}
    测试成功率：${success_rate}
    测试失败率：${fail_rate}   
    """
    return markdown_template


def send_result_message(summary: dict, web_hook):
    result = summary["result"]
    result_all = summary["result_all"]
    time = summary["time"]
    message_data = {
        "host": summary["host"],
        "result_all": result_all,
        "total": result["total"],
        "success_num": result["success_num"],
        "fail_num": result["fail_num"],
        "success_rate": result["success_rate"],
        "fail_rate": result["fail_rate"],
        "start_time": time["start_time"],
        "end_time": time["end_time"],
        "duration": time["duration"],
        "test_sys": summary["test_sys"],
        "test_modules": summary["test_modules"]
    }
    markdown_template = get_markdown_template()
    markdown = common_util.replace_string(markdown_template, message_data)
    msg = {
        "title": "接口测试概况",
        "text": markdown
    }
    sddm = SendDingDindMsg(web_hook, msg)
    sddm.send_dingding_message(message_type="markdown")

