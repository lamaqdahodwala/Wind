from django.contrib.auth.models import User
import graphene
from graphene_django import DjangoObjectType
from .models import Question, Answer

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'body', 'user', 'answers')

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('user', 'content')

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username','questions')

class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    single_question = graphene.Field(QuestionType, pk=graphene.Int())
    user_by_id = graphene.Field(UserType, id=graphene.Int())
    def resolve_all_questions(root, info):
        return Question.objects.all()

    def resolve_single_question(root, info, pk):
        return Question.objects.get(pk=pk)
    
    def resolve_user_by_id(root, info, id):
        return User.objects.get(pk=id)

schema = graphene.Schema(query=Query)