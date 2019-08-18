from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# 导入qq登录模块工具包
from QQLoginTool.QQtool import OAuthQQ
from django.conf import settings
from meiduoMall.utils.response_code import RETCODE
from django.http import HttpResponseForbidden


class QQAuthURLView(View):
    """提供QQ登录页面网址"""

    def get(self, request):
        # next表示从哪个页面进入我的登录页面，将来登录成功后，就自动回到那个页面

        next = request.GET.get('next')

        # 获取QQ登录页面网址
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET,
                        redirect_uri=settings.QQ_REDIRECT_URI, state=True)
        login_url = oauth.get_qq_url()

        return JsonResponse({"code": RETCODE.OK, 'errmsg': 'ok', 'login_url': login_url})


class QQAuthUserView(View):
    """用户扫码登录的回调处理"""

    def get(self, request):
        """Oauth2.0认证"""
        # 接收Authorization Code
        code = request.GET.get('code')

        if not code:
            return HttpResponseForbidden("缺少code")

        pass
