from django.core.management.base import BaseCommand
from polls.models import Question, Choice

class Command(BaseCommand):
    help = "Questionテーブルのデータをtxtファイルに書き出す"

    def handle(self, *args, **options):
        # 出力ファイル名
        filename = "quesions.txt"

        # 全データ取得
        questions = Question.objects.all()

        # ファイルに書き込み
        with open(filename, "w", encoding="utf-8") as f:
            for q in questions:
                f.write(f"{q.question_text},{q.pub_date}\n")
                for c in q.choice_set.all():
                    f.write(f'  Choice: {c.choice_text} (votes: {c.votes})\n')
                f.write("\n")
        self.stdout.write(self.style.SUCCESS('QuestionsとChoicesを書き出しました -> {}'.format(filename)))
