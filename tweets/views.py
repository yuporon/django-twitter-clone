from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .forms import TweetForm
from .models import Tweet


# 投稿画面
class New(CreateView):
    # 使うためテンプレートの指定
    template_name = 'tweets/new.html'
    # 使うformクラスの指定
    form_class = TweetForm
    # 成功時に飛ぶURLの指定
    success_url = reverse_lazy('tweets:index')

    # 入力に問題がない場合現在ログインしているアカウントを投稿者として登録するための処理
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(New, self).form_valid(form)


# 投稿一覧
class Index(ListView):
    model = Tweet
    template_name = 'tweets/index.html'
    #  最大表示件数を設定 (100件)
    paginate_by = 100
    # 投稿日を降順で並べる
    queryset = Tweet.objects.order_by('created_at').reverse()

