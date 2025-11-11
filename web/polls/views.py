from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect ,Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from bokeh.plotting import figure
from bokeh.embed import components



from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        まだ pub_date フィールドの日付が到来していない質問は除外するメソッド
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

 
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.object

        # グラフ作成
        choices = question.choice_set.all()
        x = [choice.choice_text for choice in choices]
        y = [choice.votes for choice in choices]

        p = figure(
            x_range=x,
            title=f"「{question.question_text}」の投票結果",
            x_axis_label = "選択肢",
            y_axis_label = "投票数",
            toolbar_location = None,
            tools=""
        )
        p.vbar(x=x, top=y, width=0.5, color="skyblue")

        # HTML埋め込み用に変換
        script, div = components(p)

        # コンテキストに追加
        context["bokeh_script"] = script
        context["bokeh_div"] = div
        return context


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "投票するには必ず一つ選択してください。",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

