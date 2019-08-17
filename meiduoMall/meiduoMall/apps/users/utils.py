from django.contrib.auth.backends import ModelBackend

import re

from .models import User


def get_user_by_account(account):
    """
    根据account查询用户
    :param account: 用户名或手机号
    :return: user
    """

    try:
        if re.match('^1[3-9]\d{9}%', account):
            # 手机号
            user = User.objects.get(mobile=account)

        else:

            # 用户名登录

            user = User.objects.get(username=account)

    except User.DoseNotExist:
        return None

    else:

        return user


class UsernameMobileAuthBackend(ModelBackend):
    """自定义用户登录"""

    # 不需要导入此包，在设置页面配置用户认证后端
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        重写登录方法，实现多账号登录
        :param request: 请求对象
        :param username:  用户名
        :param password:  密码
        :param kwargs:  其他参数
        :return: user
        """

        # 根据传入的username获取user对象。username可以是手机号也可以是账号

        user = get_user_by_account(username)

        # 校验user是否存在并校验密码是否正确

        if user and user.check_password(password):
            return user