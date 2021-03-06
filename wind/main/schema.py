from django.contrib.auth.models import User
import graphene
from graphene_django import DjangoObjectType
from .models import Question, Answer

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'body', 'user', 'answers', 'id')

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('user', 'content', 'question', 'id')

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username','questions', 'id', 'answers')

class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    single_question = graphene.Field(QuestionType, pk=graphene.Int())
    user_by_id = graphene.Field(UserType, id=graphene.Int())
    current_user = graphene.Field(UserType)
    def resolve_all_questions(root, info):
        return Question.objects.all()

    def resolve_single_question(root, info, pk):
        return Question.objects.get(pk=pk)
    
    def resolve_user_by_id(root, info, id):
        return User.objects.get(pk=id)
    
    def resolve_current_user(root, info):
        uid = info.context.user.id
        return User.objects.get(id=uid)

class QuestionMutate(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        body = graphene.String()
        user = graphene.Int()
    
    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, title, body, user):
        question = Question(title=title, body=body, user=User.objects.get(id=user))
        question.save()
        return QuestionMutate(question=question)

class AnswerMutate(graphene.Mutation):
    class Arguments:
        content = graphene.String()
        question = graphene.Int()

    answer = graphene.Field(AnswerType)

    @classmethod
    def mutate(cls, root, info, content, question):
        if info.context.user:
            answer = Answer(content=content, question=Question.objects.get(pk=question), user=User.objects.get(id=info.context.user.id))
            answer.save()
            return AnswerMutate(answer=answer)

class Mutation(graphene.ObjectType):
    create_question = QuestionMutate.Field()
    create_answer = AnswerMutate.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)