def get_value():
    return "newdream"

def setup_test_step():
    print("测试步骤开始")

def teardown_test_step():
    print("测试步骤结束")

def setup_test_case(content):
    print("测试用例[%s]开始"%content)

def teardown_test_case(content):
    print("测试用例[%s]结束"%content)

def get_condition():
    return []

if __name__ == "__main__":
    print(get_value())